%define oname PyCClass

%def_with python3

Name: python-module-pysces
Version: 0.5.2
Release: alt4.1

Summary: Making object oriented python bindings to an object oriented C API

License: GPL
Group: Development/Python
Url: http://www.nongnu.org/pysces/

Packager: Vitaly Lipatov <lav@altlinux.ru>
Source: http://download.savannah.nongnu.org/releases/pysces/%oname-%version.tar.bz2

BuildArch: noarch

%setup_python_module pysces

# Automatically added by buildreq on Tue Mar 20 2007
BuildRequires: python-devel python-modules-encodings

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
%endif

%description
PyCClass is a library to aid in the task of making object
oriented python bindings to an object oriented C API.

%package -n python3-module-pysces
Summary: Making object oriented python bindings to an object oriented C API
Group: Development/Python3

%description -n python3-module-pysces
PyCClass is a library to aid in the task of making object
oriented python bindings to an object oriented C API.

%prep
%setup -n %oname-%version

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-pysces
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.2-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt4
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.2-alt3.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt3
- Rebuilt with python 2.6

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 0.5.2-alt2.1
- Rebuilt with python-2.5.

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 0.5.2-alt2
- Build as noarch.

* Tue Mar 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- initial build for ALT Linux Sisyphus
