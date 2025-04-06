%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define oname stack_data

%def_with check

Name: python3-module-stack-data
Version: 0.6.3
Release: alt2
Summary: Library that extracts data from stack frames and tracebacks
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/stack-data
VCS: https://github.com/alexmojaki/stack_data

BuildArch: noarch

Source: %name-%version.tar
Patch: stack-data-0.6.3-pygments.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-Cython
BuildRequires: python3-module-typeguard
BuildRequires: python3-module-pygments
BuildRequires: python3-module-executing
BuildRequires: python3-module-asttokens
BuildRequires: python3-module-pure-eval
BuildRequires: python3-module-littleutils
%endif

%description
This is a library that extracts data from stack frames and tracebacks,
particularly to display more useful tracebacks than the default.

%prep
%setup
%patch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
# failed due to new pygments
%pyproject_run_pytest \
	--deselect "tests/test_serializer.py::test_example" \
	--deselect "tests/test_core.py::test_pygments_example"

%files
%doc LICENSE.txt README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sun Apr 06 2025 Anton Vyatkin <toni@altlinux.org> 0.6.3-alt2
- Fixed FTBFS.

* Sun May 19 2024 Grigory Ustinov <grenka@altlinux.org> 0.6.3-alt1
- Automatically updated to 0.6.3.

* Tue Jan 18 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.4-alt1
- Initial build for ALT.
