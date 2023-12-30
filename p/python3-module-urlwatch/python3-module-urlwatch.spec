%define _unpackaged_files_terminate_build 1
%define pypi_name urlwatch

%def_with check

Name: python3-module-%pypi_name
Version: 2.28
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
%pyproject_run_pytest -vra \
    --deselect lib/urlwatch/tests/test_handler.py::test_pep8_conformance

%files
%doc CHANGELOG.md COPYING README.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_datadir/%pypi_name
%_man1dir/%{pypi_name}*.1.xz
%_man5dir/%{pypi_name}*.5.xz
%_man7dir/%{pypi_name}*.7.xz

%changelog
* Sat Dec 30 2023 Anton Zhukharev <ancieg@altlinux.org> 2.28-alt1
- Built for ALT Sisyphus.

