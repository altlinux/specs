%define modulename qserve

Name: python-module-qserve
Version: 0.1.1
Release: alt1.1

Summary: job queue server used in mwlib

Group: Development/Python

License: BSD
Url: https://github.com/pediapress/qserve

Source: %name-%version.tar

BuildPreReq: rpm-build-python

BuildArch: noarch

%setup_python_module %modulename

%description
job queue server used in mwlib

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/qs*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 18 2011 Michael A. Kangin <prividen@altlinux.org> 0.1.1-alt1
- initial build for ALT Linux Sisyphus

