%define _unpackaged_files_terminate_build 1
%define pypi_name pathspec

%def_with check

Name: python3-module-%pypi_name
Version: 0.11.0
Release: alt1
Summary: Utility library for gitignore style pattern matching of file paths
License: MPL-2.0-no-copyleft-exception
Group: Development/Python
Url: https://pypi.org/project/pathspec/
VCS: https://github.com/cpburnz/python-pathspec.git

BuildArch: noarch

Source: %name-%version.tar

BuildRequires: rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit_core)

%description
%pypi_name is a utility library for pattern matching of file paths. So
far this only includes Git's wildmatch pattern matching which itself
is derived from Rsync's wildmatch. Git uses wildmatch for its
gitignore files.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest -v

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jan 25 2023 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1
- 0.10.3 -> 0.11.0.

* Mon Dec 12 2022 Stanislav Levin <slev@altlinux.org> 0.10.3-alt1
- 0.10.2 -> 0.10.3.

* Fri Nov 18 2022 Stanislav Levin <slev@altlinux.org> 0.10.2-alt1
- 0.10.1 -> 0.10.2.

* Mon Sep 12 2022 Stanislav Levin <slev@altlinux.org> 0.10.1-alt1
- 0.9.0 -> 0.10.1.

* Tue Sep 07 2021 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- 0.8.1 -> 0.9.0.

* Tue May 11 2021 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- 0.8.0 -> 0.8.1.

* Mon Sep 14 2020 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.5.9 -> 0.8.0.

* Wed Sep 25 2019 Terechkov Evgenii <evg@altlinux.org> 0.5.9-alt1
- Initial build for ALT Linux Sisyphus
