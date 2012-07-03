%define version 1.0.0a13
%define release alt3
%setup_python_module starpy

Name: %packagename
Version: %version
Release: %release.1

Summary: Twisted Protocols for interaction with the Asterisk PBX
Group: Development/Python
License: BSD
URL: http://starpy.sourceforge.net
Packager: Sergey Alembekov <rt@altlinux.ru>

BuildArch: noarch
Source0: %modulename-%version.tar.gz
BuildRequires: python-dev

%description
Twisted Protocols for interaction with Asterisk PBX

Provides Asterisk AMI and Asterisk FastAGI protocols under Twisted,
allowing for fairly extensive customisation of Asterisk operations
from a Twisted process.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0a13-alt3.1
- Rebuild with Python-2.7

* Thu Mar 25 2010 Denis Klimov <zver@altlinux.org> 1.0.0a13-alt3
- change BuildRequires to python-dev

* Thu Mar 25 2010 Denis Klimov <zver@altlinux.org> 1.0.0a13-alt2
- patch for check not standart HANGUP200 status from
  Asterisk 1.6.2
- add BuildRequires: python-devel

* Thu Mar 25 2010 Denis Klimov <zver@altlinux.org> 1.0.0a13-alt1
- new version
- using rpm-build-python macros
- remove needless -q param from setup macro

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0a12-alt1.1
- Rebuilt with python 2.6

* Wed Oct 22 2008 Sergey Alembekov <rt@altlinux.ru> 1.0.0a12-alt1
- Initial build for ALTLinux

