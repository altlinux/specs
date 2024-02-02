%define _unpackaged_files_terminate_build 1
%define oname dictdiffer

%def_with check

Name: python3-module-%oname
Version: 0.8.1
Release: alt2

Summary: Dictdiffer is a module that helps you to diff and patch dictionaries
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/dictdiffer/

BuildArch: noarch

# https://github.com/inveniosoftware/dictdiffer.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%description
Dictdiffer is a library that helps you to diff and patch dictionaries.

%prep
%setup
%autopatch -p1

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%tox_check_pyproject

%files
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Fri Feb 02 2024 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt2
- Moved on modern pyptoject macros.

* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- 0.7.0 -> 0.8.1.

* Thu Apr 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7.0-alt2
- Build for python2 disabled.

* Tue Mar 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt1
- Initial build for ALT.
