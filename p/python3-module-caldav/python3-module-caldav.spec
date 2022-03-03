%define oname caldav

Name: python3-module-%oname
Version: 0.8.0
Release: alt1

Summary: A CalDAV (RFC4791) client library for Python

License: GPL-3.0-only
Group: Development/Python
Url: https://github.com/python-caldav/caldav/

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
A CalDAV (RFC4791) client library for Python.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*

%changelog
* Thu Mar 3 2022 Vladimir Didenko <cow@altlinux.org> 0.8.0-alt1
- initial build for Sisyphus
