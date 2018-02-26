%define oname PyDispatcher

Name: python-module-pydispatcher
Version: 2.0.1
Release: alt2.1.1

Summary: Multi-producer-multi-consumer signal dispatching mechanism

Group: Development/Python
License: BSD-like, see license.txt
Url: http://pydispatcher.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://downloads.sourceforge.net/pydispatcher/%oname-%version.tar.bz2

BuildArch: noarch

%setup_python_module %oname

BuildPreReq: rpm-build-compat >= 1.2

# Automatically added by buildreq on Mon Dec 01 2008
BuildRequires: python-devel python-module-setuptools

%description
The dispatcher provides loosely-coupled message passing between
Python objects (signal senders and receivers). It began as one of the
highest-rated recipes on the Python Cookbook website.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc license.txt
%python_sitelibdir/pydispatch/
%python_sitelibdir/*egg-info

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt2.1.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt2.1
- Rebuilt with python 2.6

* Fri Feb 20 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt2
- build as noarch

* Mon Dec 01 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- initial build for ALT Linux Sisyphus
