# TODO: fix getDaboLocaleDir()
%define module dabo

%def_without python3

Name: python-module-dabo
Version: 0.9.14
Release: alt1

Summary: true 3-tier desktop application framework

License: BSD like
Url: http://dabodev.com/
Group: Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://dabodev.com/dabo/%module-%version.tar.bz2
Patch: %name-locale.patch

BuildArch: noarch

# manually removed: python-module-Rabbyt 
# Automatically added by buildreq on Mon Dec 31 2007
BuildRequires: libuuid python-module-MySQLdb python-module-PyXML python-module-Pyrex python-module-ctypes python-module-pysqlite2 python-module-setuptools

BuildPreReq: python-modules-json

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-MySQLdb
BuildPreReq: python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Dabo is a Python module that provides a true 3-tier desktop application
framework. It separates the three main parts of a desktop app: database
access, user interface and business logic. You would typically use Dabo
to develop graphical, data-aware desktop applications.

%package tests
Summary: Tests for %module
Group: Development/Python
Requires: %name = %EVR

%description tests
Dabo is a Python module that provides a true 3-tier desktop application
framework. It separates the three main parts of a desktop app: database
access, user interface and business logic. You would typically use Dabo
to develop graphical, data-aware desktop applications.

This package contains tests for %module.

%package -n python3-module-%module
Summary: true 3-tier desktop application framework
Group: Development/Python3

%description -n python3-module-%module
Dabo is a Python module that provides a true 3-tier desktop application
framework. It separates the three main parts of a desktop app: database
access, user interface and business logic. You would typically use Dabo
to develop graphical, data-aware desktop applications.

%package -n python3-module-%module-tests
Summary: Tests for %module
Group: Development/Python3
Requires: python3-module-%module = %EVR

%description -n python3-module-%module-tests
Dabo is a Python module that provides a true 3-tier desktop application
framework. It separates the three main parts of a desktop app: database
access, user interface and business logic. You would typically use Dabo
to develop graphical, data-aware desktop applications.

This package contains tests for %module.

%prep
%setup -n %module
#patch

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
export LC_ALL=en_US.UTF-8

mkdir -p %buildroot%_datadir/
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

mv %buildroot%_prefix/dabo/locale %buildroot%_datadir
%find_lang %module

%files -f %module.lang
%doc AUTHORS README.md RELEASENOTES.md dabo/LICENSE.TXT
%doc demo
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/*/test.py*

%files tests
%python_sitelibdir/*/*/*/test.py*

%if_with python3
%files -n python3-module-%module -f %module.lang
%doc AUTHORS README.md RELEASENOTES.md dabo/LICENSE.TXT
%doc demo
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/*/test.py*
%exclude %python3_sitelibdir/*/*/*/*/test.*

%files -n python3-module-%module-tests
%python3_sitelibdir/*/*/*/test.py*
%python3_sitelibdir/*/*/*/*/test.*
%endif

%changelog
* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.14-alt1
- Version 0.9.14

* Thu Dec 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.13-alt1
- Version 0.9.13

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.4-alt2.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt2
- Rebuilt with python 2.6

* Thu Jul 31 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.4-alt1
- new version 0.8.4 (with rpmrb script)
- disable locale hack

* Mon Dec 31 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.3-alt1
- initial build for ALT Linux Sisyphus

