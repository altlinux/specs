%define modulename cffi

%def_with python3

Name: python-module-cffi
Version: 0.6
Release: alt3

Summary: Foreign Function Interface for Python calling C code

Group: Development/Python
License: LGPLv2+
Url: http://pypi.python.org/pypi/%modulename/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/c/%modulename/%modulename-%version.tar
Patch: cffi-0.6-alt-link.patch

%setup_python_module %modulename

BuildRequires: python-devel libffi-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Foreign Function Interface for Python calling C code.

%package -n python3-module-cffi
Summary: Foreign Function Interface for Python calling C code
Group: Development/Python3

%description -n python3-module-cffi
Foreign Function Interface for Python calling C code.

%prep
%setup -n %modulename-%version
%patch -p2

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
%python_sitelibdir/_cffi_backend.so
%python_sitelibdir/%modulename/
%python_sitelibdir/%modulename-%version-*.egg-info

%if_with python3
%files -n python3-module-cffi
%python3_sitelibdir/*
%endif

%changelog
* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt3
- Added module for Python3

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt2
- fix packing

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- initial build for ALT Linux Sisyphus
