%define _unpackaged_files_terminate_build 1
%define pypi_name pkgconfig

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.5
Release: alt2

Summary: Interface Python with pkg-config
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pkgconfig/
BuildArch: noarch

# https://github.com/matze/pkgconfig.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(poetry-core)

%if_with check
BuildRequires: /usr/bin/pkg-config
# cat data/fake-openssl.pc | grep Requires
BuildRequires: libssl-devel

BuildRequires: python3(pytest)
%endif

%description
%pypi_name is a Python module to interface with the pkg-config command line tool
for Python.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/pkgconfig/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 1.5.5-alt2
- Modernized packaging (fixes FTBFS due to poetry-core 1.1.0).

* Fri Mar 25 2022 Stanislav Levin <slev@altlinux.org> 1.5.5-alt1
- 1.2.2 -> 1.5.5.

* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2.2-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.git20141212.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20141212
- Initial build for Sisyphus

