%define _unpackaged_files_terminate_build 1

%def_enable check

%define oname altrepo_api

Name: altrepo-api
Version: 1.9.4
Release: alt1

Summary: ALTRepo API is a REST API for the repository database of ALT distribution
License: AGPL-3.0
Group: System/Servers
URL: https://git.altlinux.org/gears/a/altrepo-api.git
VCS: https://git.altlinux.org/people/dshein/packages/altrepo-api.git

BuildArch: noarch

Requires: librpm7
Requires: python3-module-gunicorn

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_enabled check
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mmh3
BuildRequires: python3-module-gunicorn
BuildRequires: python3-module-flask-restx
BuildRequires: python3-module-clickhouse-driver
%endif

Source0: %name-%version.tar
Patch1: %name-%version-%release.patch

%description
ALTRepo API is a REST API for the repository database of ALT
distribution. ALTRepo API allows users to get the necessary information 
regards to the repository by GET requests.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_datadir/%name
mkdir -p examples
install -Dm0644 api.conf.example %buildroot%_sysconfdir/%name/api.conf.example
mv services/uwsgi/uwsgi.ini %buildroot%_datadir/%name/uwsgi.ini
mv services/uwsgi/wsgi.py %buildroot%_datadir/%name/wsgi.py
cp -r services/* examples/
mkdir -p %buildroot%_logdir/altrepo-api

%check
%tox_create_default_config
%tox_check_pyproject -- -vra tests/unit

%pre
%_sbindir/groupadd -r -f _altrepo_api 2> /dev/null ||:
%_sbindir/useradd -r -g _altrepo_api -s /dev/null -c "ALTRepo API User" _altrepo_api 2> /dev/null ||:

%preun
%preun_service altrepo-api

%files
%dir %_datadir/%name
%dir %_sysconfdir/%name
%dir %attr(0750,_altrepo_api,_altrepo_api) %_logdir/altrepo-api
%doc LICENSE.txt README.* AUTHORS.txt CHANGELOG.* examples
%_datadir/%name/*
%_bindir/altrepo-api
%_sysconfdir/%name/api.conf.example
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Wed Mar 22 2023 Danil Shein <dshein@altlinux.org> 1.9.4-alt1
 - 1.8.11 -> 1.9.4

* Mon Mar 06 2023 Danil Shein <dshein@altlinux.org> 1.9.3-alt1
 - new version 1.9.3

* Mon Dec 12 2022 Danil Shein <dshein@altlinux.org> 1.9.0-alt1
 - new version 1.9.0

* Tue Nov 22 2022 Danil Shein <dshein@altlinux.org> 1.8.11-alt1
 - 1.8.8 -> 1.8.11
   + enable unit tests

* Thu Nov 03 2022 Danil Shein <dshein@altlinux.org> 1.8.8-alt1
 - 1.8.0 -> 1.8.8
   + migrate to pyproject

* Wed Jul 13 2022 Danil Shein <dshein@altlinux.org> 1.8.0-alt1
 - 1.7.0 -> 1.8.0

* Thu Apr 14 2022 Danil Shein <dshein@altlinux.org> 1.7.0-alt1
 - 1.6.0 -> 1.7.0

* Mon Feb 14 2022 Danil Shein <dshein@altlinux.org> 1.6.0-alt1
 - 1.5.4 -> 1.6.0

* Mon Jan 10 2022 Danil Shein <dshein@altlinux.org> 1.5.4-alt1
 - 1.5.1 -> 1.5.4

* Wed Dec 08 2021 Danil Shein <dshein@altlinux.org> 1.5.1-alt1
 - 1.5.0 -> 1.5.1

* Tue Dec 07 2021 Danil Shein <dshein@altlinux.org> 1.5.0-alt1
 - initial package build


