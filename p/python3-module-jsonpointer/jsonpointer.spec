%global pypi_name jsonpointer

Name:       python3-module-%pypi_name
Version:    3.0.0
Release:    alt1

Summary:    Resolve JSON Pointers in Python

Group:      Development/Python3
License:    BSD-3-Clause
URL:        https://pypi.org/project/jsonpointer
VCS:        https://github.com/stefankoegl/python-json-pointer

Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch:  noarch

%description
Library to resolve JSON Pointers according to RFC 6901.

%prep
%setup

%build
%pyproject_build

%install
export LC_ALL=en_US.UTF-8
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc LICENSE.txt README.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Sat Feb 07 2026 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Build new version.

* Sat Oct 18 2025 Grigory Ustinov <grenka@altlinux.org> 2.0-alt3
- Fixed FTBFS.

* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.0-alt2
- Build for python2 disabled.

* Tue Jan 15 2019 Alexey Shabalin <shaba@altlinux.org> 2.0-alt1
- 2.0

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6-alt1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Version 1.6

* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0-alt1
- First build for ALT (based on Fedora 1.0-5.fc21.src)

