# Generated by Django 4.0.4 on 2022-05-26 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('river', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='onapprovedhook',
            name='callback_function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_hooks', to='river.function', verbose_name='Function'),
        ),
        migrations.AlterField(
            model_name='onapprovedhook',
            name='hook_type',
            field=models.CharField(choices=[('BEFORE', 'Before'), ('AFTER', 'After')], max_length=50, verbose_name='When?'),
        ),
        migrations.AlterField(
            model_name='onapprovedhook',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='onapprovedhook',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_hooks', to='river.workflow', verbose_name='Workflow'),
        ),
        migrations.AlterField(
            model_name='oncompletehook',
            name='callback_function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_hooks', to='river.function', verbose_name='Function'),
        ),
        migrations.AlterField(
            model_name='oncompletehook',
            name='hook_type',
            field=models.CharField(choices=[('BEFORE', 'Before'), ('AFTER', 'After')], max_length=50, verbose_name='When?'),
        ),
        migrations.AlterField(
            model_name='oncompletehook',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='oncompletehook',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_hooks', to='river.workflow', verbose_name='Workflow'),
        ),
        migrations.AlterField(
            model_name='ontransithook',
            name='callback_function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_hooks', to='river.function', verbose_name='Function'),
        ),
        migrations.AlterField(
            model_name='ontransithook',
            name='hook_type',
            field=models.CharField(choices=[('BEFORE', 'Before'), ('AFTER', 'After')], max_length=50, verbose_name='When?'),
        ),
        migrations.AlterField(
            model_name='ontransithook',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ontransithook',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_hooks', to='river.workflow', verbose_name='Workflow'),
        ),
        migrations.AlterField(
            model_name='state',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='transition',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='transition',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('cancelled', 'Cancelled'), ('done', 'Done'), ('jumped', 'Jumped')], default='pending', max_length=100, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='transitionapproval',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='transitionapproval',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('cancelled', 'Cancelled'), ('jumped', 'Jumped')], default='pending', max_length=100, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='transitionapprovalmeta',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='transitionmeta',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
