%define _unpackaged_files_terminate_build 1
%define pypi_name ftfy
%define mod_name ftfy

%def_with check

Name: python3-module-%pypi_name
Version: 6.3.1
Release: alt1

Summary: Fixes mojibake and other glitches in Unicode text, after the fact
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/ftfy
Vcs: https://github.com/rspeer/python-ftfy

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-sphinx
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build
%make -C docs man

%install
%pyproject_install
ln -s %_licensedir/Apache-2.0 LICENSE
install -pDv -m644 docs/_build/man/%pypi_name.1 %buildroot%_man1dir/%pypi_name.1

%check
%pyproject_run_pytest

%files
%doc LICENSE.txt README.md
%doc --no-dereference LICENSE
%_man1dir/%pypi_name.1*
%_bindir/%mod_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Feb 03 2026 Dmitry Mihalchenko <tascad@altlinux.org> 6.3.1-alt1
- Initial build for ALT Sisyphus.
