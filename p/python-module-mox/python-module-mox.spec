%define packagename python-module-mox
%define origname mox

Summary: mock object framework for Python
Name: %packagename
Version: 0.5.0
Release: alt2.1.1
Source0: %origname-%version.tar.gz
License: Apache License 2.0
Group: Development/Python
URL: http://code.google.com/p/pymox/
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Sat Apr 05 2008
BuildRequires: python-devel

%description
Mox is a mock object framework for Python. Mox is based on EasyMock, a Java mock object framework.
Mox will make mock objects for you, so you don't have to create your own!
It mocks the public/protected interfaces of Python objects.
You set up your mock objects expected behavior using a domain specific language (DSL), which makes it easy to use, understand, and refactor!


%prep
%setup  -q -n %origname-%version

%build
%python_build

%install
%python_install

%files
%doc COPYING README
%python_sitelibdir/*
%python_sitelibdir/mox-*.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt2.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2.1
- Rebuilt with python 2.6

* Mon Sep 28 2009 Mikhail Pokidko <pma@altlinux.org> 0.5.0-alt2
- Fixed packaging errors

* Tue Nov 18 2008 Mikhail Pokidko <pma@altlinux.org> 0.5.0-alt1
- Initial ALT build


