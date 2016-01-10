%define modulename cffi

%def_with python3

Name: python-module-cffi
Version: 1.4.2
Release: alt1

Summary: Foreign Function Interface for Python calling C code

Group: Development/Python
License: LGPLv2+
Url: http://pypi.python.org/pypi/%modulename/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/c/%modulename/%modulename-%version.tar
Patch: cffi-0.8.6-alt-link.patch

%setup_python_module %modulename

BuildRequires: python-devel libffi-devel python-module-setuptools
Requires: python-module-pycparser

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Foreign Function Interface for Python calling C code.

%package -n python3-module-cffi
Summary: Foreign Function Interface for Python calling C code
Group: Development/Python3

Requires: python3-module-pycparser

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
* Sun Jan 10 2016 Vladimir Didenko <cow@altlinux.ru> 1.4.2-alt1
- Version 1.4.2

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Mon Aug 04 2014 Lenar Shakirov <snejok@altlinux.ru> 0.8.6-alt2
- python{3,}-module-pycparser added to Requires
- Because find-requires script /usr/lib/rpm/python3.req.py says:
  * cffi/cparser.py: line=2 possible relative import from ., UNIMPLEMENTED

* Fri Jul 11 2014 Vitaly Lipatov <lav@altlinux.ru> 0.8.6-alt1
- new version 0.8.6 (with rpmrb script) (ALT bug #30174)

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt3
- Added module for Python3

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt2
- fix packing

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- initial build for ALT Linux Sisyphus
