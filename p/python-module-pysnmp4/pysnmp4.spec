%def_with python3

Summary: SNMP v1/v2c/v3 engine
Name: python-module-pysnmp4
Version: 4.3.1
Release: alt1
%setup_python_module pysnmp
Url: http://pysnmp.sourceforge.net/
Source0: %modulename-%version.tar
License: BSD
Group: Development/Python
BuildArch: noarch
Conflicts: python-module-pysnmp

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
This is an alpha-quality revision of pure-Python, open source and free
implementation of v1/v2c/v3 SNMP engine.

%package -n python3-module-pysnmp4
Summary: SNMP v1/v2c/v3 engine
Group: Development/Python3

%description -n python3-module-pysnmp4
This is an alpha-quality revision of pure-Python, open source and free
implementation of v1/v2c/v3 SNMP engine.

%prep
%setup -n %modulename-%version

%if_with python3
cp -fR . ../python3
#sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
#	../python3/tools/libsmi2pysnmp
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
%doc docs/*

%if_with python3
%files -n python3-module-pysnmp4
#%doc CHANGES README THANKS TODO docs/*
%doc docs/*
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 29 2016 Sergey Alembekov <rt@altlinux.ru> 4.3.1-alt1
- Build version 4.3.1

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.6-alt1.rc1
- Version 4.2.6rc1

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.5-alt1
- Version 4.2.5
- Added module for Python 3

* Mon Sep 09 2013 Alexey Shabalin <shaba@altlinux.ru> 4.2.4-alt1
- 4.2.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.14a-alt3.1
- Rebuild with Python-2.7

* Wed Aug 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.14a-alt3
- Added explicit conflict with python-module-pysnmp

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.14a-alt2
- Added url

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.14a-alt1
- Version 4.1.14a

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.8a-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 4.1.8a-alt1.1
- Rebuilt with python-2.5.

* Tue Oct 16 2007 Peter V. Saveliev <peet@altlinux.org> 4.1.8a-alt1
- initial build

