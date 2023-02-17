%define _unpackaged_files_terminate_build 1
%define pypi_name sphinxext-opengraph
%define mod_name opengraph

%def_with check

Name: python3-module-%pypi_name
Version: 0.8.0
Release: alt1
Summary: Sphinx extension to generate unique OpenGraph metadata
License: BSD-3-Clause
Group: Development/Python3
Url: https://sphinxext-opengraph.readthedocs.io
VCS: https://github.com/wpilibsuite/sphinxext-opengraph

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
# dependencies
BuildRequires: python3(sphinx)
BuildRequires: python3(matplotlib)

BuildRequires: python3(pytest)
BuildRequires: python3(sphinx.testing)
BuildRequires: python3(bs4)
%endif

%description
Sphinx extension to generate OpenGraph metadata

%prep
%setup

# if build from git source tree
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM. These files will be packaged unless filtered by MANIFEST.in.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.md
%python3_sitelibdir/sphinxext/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Feb 08 2023 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.6.3 -> 0.8.0.

* Fri Apr 15 2022 Egor Ignatov <egori@altlinux.org> 0.6.3-alt1
- new version 0.6.3

* Mon Jan 10 2022 Egor Ignatov <egori@altlinux.org> 0.5.1-alt1
- 0.5.1

* Wed Dec 01 2021 Egor Ignatov <egori@altlinux.org> 0.5.0-alt1
- 0.5.0

* Wed Sep 01 2021 Egor Ignatov <egori@altlinux.org> 0.4.2-alt1
- Initial build for ALT
