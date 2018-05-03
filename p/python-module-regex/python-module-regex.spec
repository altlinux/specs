%def_without check
%def_with python3

%define modulename regex
Name: python-module-regex
Version: 2017.09.23
Release: alt2.1

Summary: Alternative regular expression module, to replace re

Url: https://pypi.python.org/pypi/regex/
License: Python Software Foundation License
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/r/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
This regex implementation is backwards-compatible with the standard 're' module, but offers additional functionality.


%package -n python3-module-regex
Summary: Alternative regular expression module, to replace re
Group: Development/Python3

%description -n python3-module-regex
This regex implementation is backwards-compatible with the standard 're' module, but offers additional functionality.


%prep
%setup

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

# remove test modules (with module test requires)
rm -rf %buildroot/%python_sitelibdir/test_*
rm -rf %buildroot/%python3_sitelibdir/test_*

%files
%doc README docs/
%python_sitelibdir/*

%if_with python3
%files -n python3-module-regex
%doc README docs/
%python3_sitelibdir/*
%endif


%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2017.09.23-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Oct 02 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.09.23-alt2
- drop python*(test) requires

* Mon Oct 02 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.09.23-alt1
- initial build for ALT Sisyphus

