%define oname huey
Name: python3-module-%oname
Version: 2.4.5
Release: alt1

Summary: a little task queue for python

License: MIT
Group: Development/Python
Url: https://github.com/coleifer/huey/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
# for test
BuildRequires: python3-module-setuptools_scm

%py3_use redis-py

%description
huey is:
* a task queue written in python
* clean and simple API
* redis, sqlite, or in-memory storage
* example code.

huey supports:
* multi-process, multi-thread or greenlet task execution models
* schedule tasks to execute at a given time, or after a given delay
* schedule recurring tasks, like a crontab
* automatically retry tasks that fail
* task prioritization
* task result storage
* task locking
* task pipelines and chains

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune
rm -rfv %buildroot%python3_sitelibdir/huey/contrib/

%check
#python3_test

%files
%_bindir/huey_consumer
%_bindir/huey_consumer.py
%python3_sitelibdir/*

%changelog
* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 2.4.5-alt1
- new version 2.4.5 (with rpmrb script)

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt1
- new version 2.4.4 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt1
- new version 2.4.3 (with rpmrb script)

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- new version 2.3.0 (with rpmrb script)

* Fri Apr 10 2020 Eugene Omelyanovich <regatio@etersoft.ru> 2.2.0-alt1
- new version (2.2.0) with rpmgs script

