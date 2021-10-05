Name: python3-module-ciso8601
Version: 2.2.0
Release: alt1

Summary: ISO8601/RFC3339 date time strings converter
License: MIT
Group: Development/Python
Url: https://pypi.org/project/ciso8601/

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-python3 python3-module-setuptools
BuildRequires: python3(pytz)

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%python3_sitelibdir/ciso8601
%python3_sitelibdir/ciso8601.*.so
%python3_sitelibdir/ciso8601-%version-*-info

%changelog
* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- 2.2.0 released

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.3-alt1
- initial
