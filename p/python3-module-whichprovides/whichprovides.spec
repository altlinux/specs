#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define modulename whichprovides
%def_with check

Name: python3-module-%modulename
Version: 0.4.0
Release: alt1
Summary: A python library which maps a file back to its providing package
Group: Development/Python3
License: MIT

URL: https://pypi.org/project/whichprovides/
VCS: https://github.com/sethmlarson/whichprovides/

Source: %name-%version.tar
BuildArch: noarch

Buildrequires(pre): rpm-macros-python3
Buildrequires: rpm-build-python3
Buildrequires: python3-module-hatchling

%description
whichprovides is a package manager agnostic support for "yum whichprovides"
which maps a file back to its providing package.
This is useful for generating a package URL (PURL) identifier.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests/

%files
%doc LICENSE *.md
%python3_sitelibdir_noarch/%modulename
%python3_sitelibdir_noarch/%modulename-%version.dist-info

%changelog
* Wed Sep 16 2026 Polina Poidenko <polipoki@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.
