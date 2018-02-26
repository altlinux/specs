Name: python-module-mocker
Version: 1.1
Release: alt1.1
Summary: graceful creation of test doubles (mocks, stubs, fakes and dummies)

Group: Development/Python
License: BSD
Url: http://labix.org/mocker

Source: %name-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildArch: noarch
BuildRequires: python-module-setuptools python-module-distutils-extra intltool

%description
%summary

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/mocker-*.egg-info
%python_sitelibdir/mocker.*
%doc NEWS LICENSE

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.1
- Rebuild with Python-2.7

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt1
- initial build

