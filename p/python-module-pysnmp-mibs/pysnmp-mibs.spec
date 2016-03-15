%def_with python3

Summary: Pre-compiled MIB modules for PySNMP
Name: python-module-pysnmp-mibs
Version: 0.1.4
Release: alt1.1
%setup_python_module pysnmp-mibs
Url: http://pysnmp.sourceforge.net/
Source0: %modulename-%version.tar.gz
License: BSD
Group: Development/Python
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
%endif

%description
This is a set of pre-compiled MIB files for the PySNMP framework.

%package -n python3-module-%modulename
Summary: Pre-compiled MIB modules for PySNMP
Group: Development/Python3

%description -n python3-module-%modulename
This is a set of pre-compiled MIB files for the PySNMP framework.

%prep
%setup -n %modulename-%version

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
%python_install --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%doc CHANGES README

%if_with python3
%files -n python3-module-%modulename
%doc CHANGES README
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1
- Version 0.1.4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.9a-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.9a-alt1
- Version 0.0.9a

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5a-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.0.5a-alt1.1
- Rebuilt with python-2.5.

* Tue Oct 16 2007 Peter V. Saveliev <peet@altlinux.org> 0.0.5a-alt1
- initial build

