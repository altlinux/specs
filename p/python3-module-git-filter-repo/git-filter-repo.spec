%define _unpackaged_files_terminate_build 1
%define pypi_name git-filter-repo
%define mod_name git_filter_repo

%def_with check

Name: python3-module-%pypi_name
Version: 2.47.0
Release: alt1

Summary: Quickly rewrite git repository history (filter-branch replacement)
License: GPL-2.0-or-later OR MIT OR CC0-1.0
Group: Development/Tools
Url: https://pypi.org/project/git-filter-repo
Vcs: https://github.com/newren/git-filter-repo

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm

%description
git filter-repo is a versatile tool for rewriting history.
It roughly falls into the same space of tool as
git filter-branch but without the capitulation-inducing
poor performance, with far more capabilities, and with a design
that scales usability-wise beyond trivial rewriting cases

%prep
%setup
%pyproject_scm_init

%build
%pyproject_build

%install
%pyproject_install

%check
./t/run_tests

%files
%doc Documentation/* README.md COPYING COPYING.gpl COPYING.mit
%_bindir/%pypi_name
%python3_sitelibdir_noarch/%mod_name.py
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%python3_sitelibdir_noarch/__pycache__/%mod_name.*

%changelog
* Tue Feb 03 2026 Dmitry Mihalchenko <tascad@altlinux.org> 2.47.0-alt1
- Initial build for ALT Sisyphus.
