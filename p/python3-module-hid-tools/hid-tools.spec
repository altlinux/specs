%define _unpackaged_files_terminate_build 1
%define pypi_name hid-tools
%def_with check

Name: python3-module-%pypi_name
Version: 0.8
Release: alt1

Summary: Python scripts to manipulate HID data
License: GPLv2
Group: Development/Python3
Url: https://pypi.org/project/hid-tools
Vcs: https://gitlab.freedesktop.org/libevdev/hid-tools
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
Provides: %pypi_name = %EVR

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pytest-retry
%pyproject_builddeps_check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra uhid
BuildRequires: libevdev
BuildRequires: rpm-build-vm
BuildRequires: /proc
%endif

%description
Hid-tools is a set of tools to interact with the kernel's HID subsystem.

%prep
%setup
%autopatch -p1

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_hatch pyproject.toml test

%build
%pyproject_build

%install
%pyproject_install

%check
# kernel tests not included because they check the kernel HID subsystem
vm-run --sbin --udevd --modules="uhid" '%pyproject_run_pytest -vra tests'

%files
%doc README.md COPYING
%_bindir/hid-decode
%_bindir/hid-feature
%_bindir/hid-recorder
%_bindir/hid-replay
%_man1dir/hid-*.1.xz
%python3_sitelibdir_noarch/hidtools/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Aug 01 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.8-alt1
- New version.

* Sat Feb 24 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.7-alt1
- First build for ALT.
