%define oname huey
Name: python3-module-%oname
Version: 3.2.1
Release: alt1

Summary: a little task queue for python

License: MIT
Group: Development/Python
Url: https://github.com/coleifer/huey/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro

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
%python3_sitelibdir/*

%changelog
* Fri Jul 17 2026 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt1
- new version 3.2.1
- drop huey_consumer.py (entry-point only since 3.x)
- drop setuptools_scm BR (version is now static __version__ attr)

* Sun Mar 08 2026 Vitaly Lipatov <lav@altlinux.ru> 2.6.0-alt1
- new version 2.6.0

* Tue Mar 18 2025 Vitaly Lipatov <lav@altlinux.ru> 2.5.2-alt1
- new version 2.5.2 (with rpmrb script)

* Sun Feb 18 2024 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version 2.5.0 (with rpmrb script)

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

