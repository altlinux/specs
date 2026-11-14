%define _unpackaged_files_terminate_build 1
%define pypi_name hypothesis-crosshair
%define mod_name hypothesis_crosshair_provider

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.32
Release: alt1.1.gdb16513

Summary: Level-up your Hypothesis tests with CrossHair
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hypothesis-crosshair/
Vcs: https://github.com/pschanely/hypothesis-crosshair

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0

%description
Add the power of solver-based symbolic execution to your Hypothesis
tests with CrossHair.

%prep
%setup
%autopatch -p1
%pyproject_setup_deps
# Findability checks are not meaningful for symbolic providers.
sed -i '/_realize_objects=_realize_objects,/a\        check_findability=False,' \
       hypothesis_crosshair_provider/crosshair_provider_test.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Nov 15 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.32-alt1.1.gdb16513
- Updated to 0.0.32.

* Wed Aug 26 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.30-alt1
- Updated to 0.0.30.

* Tue Jul 07 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.28-alt1
- Updated to 0.0.28.

* Wed Mar 18 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.27-alt1
- Updated to 0.0.27.

* Fri Jul 04 2025 Anton Zhukharev <ancieg@altlinux.org> 0.0.24-alt1
- Packaged for ALT Sisyphus.
