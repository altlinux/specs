%def_without check
%def_with python3
%def_without python2

%define modulename pyperf
Name: python-module-pyperf
Version: 1.7.0
Release: alt1

Summary: Python module to run and analyze benchmarks

Url: https://github.com/vstinner/pyperf
License: the libpyperf bsd 2-clause and gpl, and own bsd 3-clause
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/vstinner/pyperf/archive/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

%if_with python2
BuildRequires: python-dev python-module-setuptools
%endif

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
The Python pyperf module is a toolkit to write, run and analyze benchmarks.

%package -n python3-module-pyperf
Summary: Python module to run and analyze benchmarks
Group: Development/Python3

%description -n python3-module-pyperf
The Python pyperf module is a toolkit to write, run and analyze benchmarks.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
rm -rfv %buildroot%python3_sitelibdir/pyperf/tests/
popd
%endif

%if_with python2
%files
%doc README.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-pyperf
%_bindir/pyperf
%doc README.rst
%python3_sitelibdir/*
%endif


%changelog
* Mon Jan 27 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- initial build for ALT Sisyphus

