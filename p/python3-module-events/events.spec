%define _unpackaged_files_terminate_build 1
%define pypi_name Events
%define pypi_nname events
%define mod_name %pypi_nname

%def_with check

Name: python3-module-%pypi_nname
Version: 0.5
Release: alt1.2

Summary: Bringing the elegance of C# EventHanlder to Python
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/Events/
Vcs: https://github.com/pyeve/events
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%description
The C# language provides a handy way to declare, subscribe to and fire
events. Technically, an event is a "slot" where callback functions
(event handlers) can be attached to - a process referred to as
subscribing to an event. Here is a handy package that encapsulates the
core to event subscription and event firing and feels like a "natural"
part of the language.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest -v

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%mod_name/tests

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.5-alt1.2
- Demodernized packaging.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 0.5-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Thu Oct 10 2024 Stanislav Levin <slev@altlinux.org> 0.5-alt1
- 0.2.1 -> 0.5.

* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1.git20140515.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20140515.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20140515
- Initial build for Sisyphus

