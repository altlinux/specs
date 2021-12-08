%define _unpackaged_files_terminate_build 1
%def_disable check

%define oname altrepo_api

Name: altrepo-api
Version: 1.5.1
Release: alt1

Summary: ALTRepo API is a REST API for the repository database of ALT distribution
License: AGPL-3.0
Group: System/Servers
URL: https://git.altlinux.org/gears/a/altrepo-api.git

BuildArch: noarch

Requires: python3-module-rpm
Requires: python3-module-gunicorn

BuildRequires(pre): rpm-build-python3

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
%python3_build

%install
%python3_install
mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_datadir/%name
mkdir -p examples
install -Dm0644 api.conf.example %buildroot%_sysconfdir/%name/api.conf.example
mv services/uwsgi/uwsgi.ini %buildroot%_datadir/%name/uwsgi.ini
mv services/uwsgi/wsgi.py %buildroot%_datadir/%name/wsgi.py
cp -r services/* examples/
mkdir -p %buildroot%_logdir/altrepo-api

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
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Wed Dec 08 2021 Danil Shein <dshein@altlinux.org> 1.5.1-alt1
- 1.5.0 -> 1.5.1

* Tue Dec 07 2021 Danil Shein <dshein@altlinux.org> 1.5.0-alt1
- initial package build


