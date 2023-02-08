%define oname pyee

%def_with check

Name: python3-module-%oname
Version: 9.0.4
Release: alt1

Summary: A port of node.js's EventEmitter to python

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyee

# https://github.com/jesusabdullah/pyee.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-flake8
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-mock
BuildRequires: python3-module-twisted-core
BuildRequires: python3-module-pytest-trio
%endif

%py3_provides %oname

BuildArch: noarch

%description
pyee supplies an event_emitter object that acts similar to the
EventEmitter that comes with node.js.

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
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Mon Sep 19 2022 Grigory Ustinov <grenka@altlinux.org> 9.0.4-alt1
- Automatically updated to 9.0.4 (Closes: #44638).

* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 6.0.0-alt1
- Version updated to 6.0.0
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.8-alt1.git20130806.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt1.git20130806
- Initial build for Sisyphus

