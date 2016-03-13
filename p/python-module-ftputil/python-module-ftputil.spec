%define oname ftputil

%def_with python3

Name: python-module-%oname
Version: 3.1
Release: alt1.1

Summary: high-level interface to the ftplib module

License: GPL
Group: Development/Python
Url: http://ftputil.sschwarzer.net/trac

Packager: Vitaly Lipatov <lav@altlinux.ru>
Source: http://ftputil.sschwarzer.net/trac/attachment/wiki/Download/%oname-%version.tar.bz2

BuildArch: noarch

%setup_python_module %oname

# Automatically added by buildreq on Wed Oct 24 2007
BuildRequires: python-devel python-modules-compiler

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
The ftputil Python library is a high-level interface to the ftplib
module. The FTPHost objects generated with ftputil allow many operations
similar to those of os  and os.path

%package -n python3-module-%oname
Summary: high-level interface to the ftplib module
Group: Development/Python3

%description -n python3-module-%oname
The ftputil Python library is a high-level interface to the ftplib
module. The FTPHost objects generated with ftputil allow many operations
similar to those of os  and os.path

%prep
%setup -n %oname-%version

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

%files
%doc doc/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc doc/*
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Aug 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1
- Version 3.1
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.3-alt2.1.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.3-alt2.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.2.3-alt1.1
- Rebuilt with python-2.5.

* Wed Oct 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt1
- initial build for ALT Linux Sisyphus
