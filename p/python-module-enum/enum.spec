%define module_name enum

%def_with python3

Name: python-module-%module_name
Version: 0.4.4
Release: alt1.1

Summary: This package provides a module for robust enumerations in Python

License: GPL/Python
Group: Development/Python
Url: https://pypi.python.org/pypi/enum/

Packager: Dmitry M. Maslennikov <rlz at altlinux.org>
Source: %module_name-%version.tar
Patch: enum-0.4.4-alt-python3.patch

BuildArch: noarch

%setup_python_module %module_name

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
This package provides a module for robust enumerations in Python.

%package -n python3-module-%module_name
Summary: This package provides a module for robust enumerations in Python
Group: Development/Python3

%description -n python3-module-%module_name
This package provides a module for robust enumerations in Python.

%prep
%setup -n %module_name-%version
%patch -p2

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
%files -n python3-module-%module_name
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1
- Version 0.4.4
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.3-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.1
- Rebuilt with python 2.6

* Tue Dec 02 2008 Dmitry M. Maslennikov <rlz at altlinux.org> 0.4.3-alt1
- Initial build for ALTLinux Sisyphus

