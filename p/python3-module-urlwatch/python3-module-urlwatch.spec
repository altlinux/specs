%define _unpackaged_files_terminate_build 1
%define pypi_name urlwatch
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.29
Release: alt1

Summary: urlwatch monitors webpages for you
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/urlwatch/
Vcs: https://github.com/thp/urlwatch

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-docutils
BuildRequires: python3-module-pycodestyle
%endif

%description
urlwatch is intended to help you watch changes in webpages and get notified
(via e-mail, in your terminal or through various third party services) of any
changes. The change notification will include the URL that has changed and a
unified diff of what has changed.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc CHANGELOG.md COPYING README.md
%_bindir/urlwatch
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_datadir/%pypi_name/
%_man1dir/%pypi_name.1.*
%_man5dir/%pypi_name-*.5.*
%_man7dir/%pypi_name-*.7.*

%changelog
* Wed Nov 13 2024 Anton Zhukharev <ancieg@altlinux.org> 2.29-alt1
- Updated to 2.29.

* Sat Dec 30 2023 Anton Zhukharev <ancieg@altlinux.org> 2.28-alt1
- Built for ALT Sisyphus.

