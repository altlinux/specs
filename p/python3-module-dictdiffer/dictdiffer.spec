%define oname dictdiffer

%def_with check

Name: python3-module-%oname
Version: 0.9.0
Release: alt1

Summary: Dictdiffer is a module that helps you to diff and patch dictionaries

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/dictdiffer
VCS: https://github.com/inveniosoftware/dictdiffer

BuildArch: noarch

Source: %name-%version.tar

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
rm -v pytest.ini
%pyproject_run_pytest

%files
%doc LICENSE *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu May 16 2024 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt1
- Automatically updated to 0.9.0.

* Fri Feb 02 2024 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt2
- Moved on modern pyptoject macros.

* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- 0.7.0 -> 0.8.1.

* Thu Apr 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7.0-alt2
- Build for python2 disabled.

* Tue Mar 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt1
- Initial build for ALT.
