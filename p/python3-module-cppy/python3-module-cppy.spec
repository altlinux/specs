%define  modulename cppy

Name:    python3-module-%modulename
Version: 1.3.0
Release: alt1

Summary: A collection of C++ headers which make it easier to write Python C extension modules
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/nucleic/cppy

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

BuildArch: noarch

Source:  %modulename-%version.tar

%description
A small C++ header library which makes it easier to write Python
extension modules. The primary feature is a PyObject smart pointer which
automatically handles reference counting and provides convenience
methods for performing common object operations.

%prep
%setup -n %modulename-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Wed Dec 25 2024 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version.
- Migrate to pyproject macroses.

* Thu Apr 07 2022 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- New version.

* Sat Mar 12 2022 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version.

* Fri Mar 27 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
