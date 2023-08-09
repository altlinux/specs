%define _name cchardet
%define pypi_name faust-%_name
%def_enable check

Name: python3-module-%pypi_name
Version: 2.1.19
Release: alt1

Summary: cChardet is high speed universal character encoding detector
Group: Development/Python3
License: GPL-2.0 and LGPL-2.1 and MPL-1.1
Url: https://pypi.org/project/%pypi_name

Vcs: https://github.com/faust-streaming/cChardet.git
Source: https://pypi.io/packages/source/f/%pypi_name/%pypi_name-%version.tar.gz

Obsoletes: python3-module-%_name < %version
Provides: python3-module-%_name = %EVR

Requires: uchardet

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ python3-devel python3-module-Cython
BuildRequires: python3-module-setuptools python3-module-wheel
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-chardet}

%description
cChardet is high speed universal character encoding detector - binding to
uchardet.

This is a fork of the https://github.com/PyYoshi/cChardet since the
original project is no longer maintained.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd src
%__python3 tests/%{_name}_test.py
#%__python3 tests/bench.py
popd

%files
%_bindir/cchardetect
%python3_sitelibdir/%_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc CHANGES* README*

%changelog
* Wed Aug 09 2023 Yuri N. Sedunov <aris@altlinux.org> 2.1.19-alt1
- 2.1.19

* Fri Apr 07 2023 Yuri N. Sedunov <aris@altlinux.org> 2.1.18-alt1
- first build for Sisyphus (obsoletes/provides python3-module-cchardet)



