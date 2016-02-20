#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, render_template, request, redirect, url_for
from flask.ext.login import login_required
from .forms import AddHostForm
from .models import Host
from ..extensions import db
from ..decorators import admin_required

host = Blueprint('host', __name__, url_prefix='/hosts')

@host.route('/', methods=['GET', 'POST'])
@login_required
@admin_required
def index():
    if request.method == 'GET':
        form = AddHostForm()
        host_list = Host.query.filter().all()
        return render_template("host/index.html", form=form, host_list=host_list)

    else:
        form = AddHostForm(request.form)
        if form.validate_on_submit():
            host_instance = Host()
            form.populate_obj(host_instance)
            db.session.add(host_instance)
            db.session.commit()
        return redirect(url_for('host.index'))


@host.route('/<int:host_id>/delete', methods=['GET'])
@login_required
@admin_required
def delete_host(host_id):
    host_instance = Host.query.filter(Host.id==host_id).first()
    if host_instance:
        db.session.delete(host_instance)
        db.session.commit()
    return redirect(url_for('host.index'))
