%define _unpackaged_files_terminate_build 1
%define modulename pythontk

%def_with check

Name:    python3-module-%modulename
Version: 0.9.12
Release: alt1

Summary: A collection of backend utilities for Python
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/pythontk/
Vcs:     https://github.com/m3trik/pythontk.git

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools 
BuildRequires: python3-module-wheel
BuildRequires: python3-module-numpy
BuildRequires: python3-module-Pillow

%if_with check
BuildRequires: python3-modules-tkinter
%endif
BuildArch: noarch

Source: %name-%version.tar

Patch: python3-module-pythontk-0.9.12-alt-pkgutil-get-loade.patch

%description
A collection of Python utility functions for file operations,
text processing, and basic image/video manipulation.
Provides helper classes and convenience functions for common programming tasks.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
# Exclude tests relying on Windows-specific or platform-dependent behavior
# that is not applicable in the Linux build environment.
%pyproject_run_pytest \
    --ignore=test/test_app_installer.py \
    --deselect=test/test_execution_monitor.py::TestExecutionMonitorPythonExecutable \
    -k "not (windows or \
        test_the_staging_sibling_keeps_the_extension_and_is_promoted or \
        test_get_dir_contents_inc_files or \
        test_get_dir_contents_dirpath or \
        test_reveal_in_file_manager or \
        test_format_annotation_without_name or \
        test_channels_round_trip or \
        test_k1_shape)"

%files
%doc LICENSE docs/*.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}/

%changelog
* Wed Aug 12 2026 Nikita Shmatko <nash@altlinux.org> 0.9.12-alt1
- Updated version to 0.9.12.
- Fixed compatibility with python3.14 by replacing removed pkgutil.get_loader().

* Tue Jan 20 2026 Nikita Shmatko <nash@altlinux.org> 0.7.54-alt1
- Updated version to 0.7.54.

* Thu Oct 30 2025 Nikita Shmatko <nash@altlinux.org> 0.7.30-alt1
- Initial build for Sisyphus.
