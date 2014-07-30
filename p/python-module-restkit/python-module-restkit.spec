%define sname restkit

%def_with python3

Summary: Restkit is an HTTP resource kit for Python
Name: python-module-%sname
Version: 2.3.1
Release: alt1.2
Source0: %name-%version.tar
#Source0: http://pypi.python.org/packages/source/r/%sname/%sname-%version.tar.gz
License: BSD
Group: Development/Python
URL: http://pypi.python.org/pypi/restkit
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

#add_python_req_skip eventlet

# Automatically added by buildreq on Thu Jul 10 2008
BuildRequires: python-devel
BuildRequires: python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Restkit is an HTTP resource kit for Python. 
It allows you to easily access to HTTP resource and build objects around it. 
It's the base of couchdbkit a Python CouchDB framework.

%package -n python3-module-%sname
Summary: Restkit is an HTTP resource kit for Python
Group: Development/Python3

%description -n python3-module-%sname
Restkit is an HTTP resource kit for Python. 
It allows you to easily access to HTTP resource and build objects around it. 
It's the base of couchdbkit a Python CouchDB framework.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%files
%doc README.rst THANKS LICENSE NOTICE examples/* doc/*
%_bindir/restcli
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/%sname
%python_sitelibdir/%sname-%version-py*.egg-info

%if_with python3
%files -n python3-module-%sname
%doc README.rst THANKS LICENSE NOTICE examples/* doc/*
%_bindir/*.py3
%python3_sitelibdir/%sname
%python3_sitelibdir/%sname-%version-py*.egg-info
%endif

%changelog
* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.1-alt1.1
- Rebuild with Python-2.7

* Tue Nov 30 2010 Mikhail Pokidko <pma@altlinux.org> 2.3.1-alt1
- v2.3.1

* Mon Sep 20 2010 Mikhail Pokidko <pma@altlinux.org> 2.2.1-alt1
- Version up.

* Wed Aug 04 2010 Mikhail Pokidko <pma@altlinux.org> 2.1.0-alt1
- initial build


