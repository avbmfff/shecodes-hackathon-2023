# Generated by Django 4.2.7 on 2023-11-25 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accompanying',
            fields=[
                ('accompanying_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('mobile_phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('ratimg', models.IntegerField()),
                ('status', models.CharField(max_length=45)),
                ('price_per_hour', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BillAccomp',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_date', models.DateTimeField()),
                ('advance_amount', models.FloatField()),
                ('discount_amount', models.FloatField()),
                ('total_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BillDetails',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_date', models.DateField()),
                ('advance_amount', models.FloatField()),
                ('discount_amount', models.FloatField()),
                ('total_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BillEntertainment',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_date', models.DateField()),
                ('advance_amount', models.FloatField()),
                ('discount_amount', models.FloatField()),
                ('total_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BillOrder',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_date', models.DateField()),
                ('advance_amount', models.FloatField()),
                ('discount_amount', models.FloatField()),
                ('total_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BillTaxi',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_date', models.DateField()),
                ('advance_amount', models.FloatField()),
                ('discount_amount', models.FloatField()),
                ('total_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Disabilities',
            fields=[
                ('disabilities_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_phone', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('gender_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('service_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('taxi_id', models.AutoField(primary_key=True, serialize=False)),
                ('registration_number', models.IntegerField()),
                ('model', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('taxi_type_id', models.IntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.driver')),
            ],
        ),
        migrations.CreateModel(
            name='TaxiStatuses',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('home_address', models.CharField(max_length=100)),
                ('diseases', models.ManyToManyField(blank=True, to='taxi_project.disabilities')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.gender')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TripDetails',
            fields=[
                ('trip_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('start_address', models.CharField(max_length=100)),
                ('end_address', models.CharField(max_length=100)),
                ('service_type_id', models.IntegerField()),
                ('customer', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.driver')),
                ('taxi', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.taxi')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('trip_id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.FloatField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('start_address', models.CharField(max_length=100)),
                ('end_address', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.driver')),
                ('taxi', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.taxi')),
            ],
        ),
        migrations.AddField(
            model_name='taxi',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.taxistatuses'),
        ),
        migrations.CreateModel(
            name='ServiceAccompany',
            fields=[
                ('srv_accomp_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('details', models.CharField(max_length=100, null=True)),
                ('total', models.FloatField()),
                ('accomp', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.accompanying')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('category_id', models.IntegerField()),
                ('price', models.FloatField()),
                ('vendor_id', models.IntegerField()),
                ('disability', models.ForeignKey(db_column='disability_id', on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.disabilities')),
            ],
        ),
        migrations.CreateModel(
            name='OwnerTaxi',
            fields=[
                ('owner_id', models.AutoField(primary_key=True, serialize=False)),
                ('taxi', models.OneToOneField(db_column='taxi-d', on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.taxi')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatuses',
            fields=[
                ('status_id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.IntegerField()),
                ('products', models.ManyToManyField(to='taxi_project.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi_project.user')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.FloatField()),
                ('datetime', models.DateTimeField()),
                ('customer', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.orderstatuses')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('order', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.products')),
            ],
        ),
        migrations.CreateModel(
            name='GroupEntertainment',
            fields=[
                ('gr_enter_id', models.AutoField(primary_key=True, serialize=False)),
                ('people_amount', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('total', models.CharField(max_length=45)),
                ('start_address', models.CharField(max_length=45)),
                ('end_address', models.CharField(max_length=45)),
                ('accomp', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.accompanying')),
                ('taxi', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.taxi')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackTaxi',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=45)),
                ('bill_taxi', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.billtaxi')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.trip')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackProduct',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=45)),
                ('rating', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.products')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackOrder',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('bill_order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.billorder')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.orders')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackEnter',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=45)),
                ('rating', models.IntegerField()),
                ('bill_entertainment', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.billentertainment')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user')),
                ('group_entertainment', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.groupentertainment')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackAccompany',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=45)),
                ('rating', models.IntegerField()),
                ('bill_accomp', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.billaccomp')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user')),
                ('srv_accomp', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.serviceaccompany')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=45)),
                ('bill', models.ForeignKey(db_column='bill_id', on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.billdetails')),
                ('customer', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='gender',
            field=models.ForeignKey(db_column='gender_id', on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.gender'),
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.AutoField(primary_key=True, serialize=False)),
                ('price_for_delivery', models.FloatField()),
                ('end_address', models.CharField(max_length=100)),
                ('start_address', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.CharField(max_length=45)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.orders')),
            ],
        ),
        migrations.AddField(
            model_name='billtaxi',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user'),
        ),
        migrations.AddField(
            model_name='billtaxi',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.trip'),
        ),
        migrations.AddField(
            model_name='billorder',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user'),
        ),
        migrations.AddField(
            model_name='billorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.orders'),
        ),
        migrations.AddField(
            model_name='billentertainment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user'),
        ),
        migrations.AddField(
            model_name='billentertainment',
            name='group_entertainment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.groupentertainment'),
        ),
        migrations.AddField(
            model_name='billdetails',
            name='customer',
            field=models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user'),
        ),
        migrations.AddField(
            model_name='billdetails',
            name='trip',
            field=models.ForeignKey(db_column='trip_id', on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.tripdetails'),
        ),
        migrations.AddField(
            model_name='billaccomp',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user'),
        ),
        migrations.AddField(
            model_name='billaccomp',
            name='srv_accomp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.serviceaccompany'),
        ),
        migrations.CreateModel(
            name='Additionalls',
            fields=[
                ('additionals_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=100)),
                ('price_per_hour', models.FloatField()),
                ('main_dis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.disabilities')),
            ],
        ),
        migrations.AddField(
            model_name='accompanying',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.gender'),
        ),
        migrations.CreateModel(
            name='UserDisabilities',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, primary_key=True, serialize=False, to='taxi_project.user')),
                ('disabilities', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.disabilities')),
            ],
        ),
        migrations.CreateModel(
            name='TaxiDisabilities',
            fields=[
                ('taxi', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, primary_key=True, serialize=False, to='taxi_project.taxi')),
                ('disabilities', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.disabilities')),
            ],
        ),
        migrations.CreateModel(
            name='GroupEntertainmentDetails',
            fields=[
                ('gr_enter_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='taxi_project.groupentertainment')),
                ('pickup_address', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('additionals', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.additionalls')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.user')),
            ],
        ),
        migrations.CreateModel(
            name='AccompDisabilities',
            fields=[
                ('accomp', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, primary_key=True, serialize=False, to='taxi_project.accompanying')),
                ('disabilities', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taxi_project.disabilities')),
            ],
        ),
    ]
