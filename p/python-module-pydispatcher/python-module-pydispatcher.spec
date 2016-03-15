%define oname PyDispatcher
%define sname pydispatcher

%def_with python3

Name: python-module-%sname
Version: 2.0.5
Release: alt1.bzr20150114.1

Summary: Multi-producer-multi-consumer signal dispatching mechanism

Group: Development/Python
License: BSD-like, see license.txt
Url: http://pydispatcher.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# bzr branch lp:pydispatcher
Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %oname

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %sname

%description
The dispatcher provides loosely-coupled message passing between
Python objects (signal senders and receivers). It began as one of the
highest-rated recipes on the Python Cookbook website.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The dispatcher provides loosely-coupled message passing between
Python objects (signal senders and receivers). It began as one of the
highest-rated recipes on the Python Cookbook website.

This package contains documentation for %oname.

%package -n python3-module-%sname
Summary: Multi-producer-multi-consumer signal dispatching mechanism
Group: Development/Python3
%py3_provides %sname

%description -n python3-module-%sname
The dispatcher provides loosely-coupled message passing between
Python objects (signal senders and receivers). It began as one of the
highest-rated recipes on the Python Cookbook website.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs/pydoc
./builddocs.py
popd

%files
%doc license.txt
%python_sitelibdir/pydispatch/
%python_sitelibdir/*egg-info

%files docs
%doc docs/*

%if_with python3
%files -n python3-module-%sname
%doc license.txt
%python3_sitelibdir/pydispatch/
%python3_sitelibdir/*egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.5-alt1.bzr20150114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt1.bzr20150114
- Version 2.0.5

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.bzr20150101
- Version 2.0.4

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.bzr20130112
- Version 2.0.3
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt2.1.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt2.1
- Rebuilt with python 2.6

* Fri Feb 20 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt2
- build as noarch

* Mon Dec 01 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- initial build for ALT Linux Sisyphus
