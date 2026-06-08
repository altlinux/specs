%define _unpackaged_files_terminate_build 1

%define pypi_name pyinstaller
%define mod_name PyInstaller

%def_with check

Name: %pypi_name
Version: 6.20.0
Release: alt1

Summary: Freeze (package) Python programs into stand-alone executables
License: GPL-2.0+
Group: Development/Python3

Url: https://pyinstaller.org
VCS: https://github.com/pyinstaller/pyinstaller

Packager: Andrey Cherepanov <cas@altlinux.org>

Requires: python3-module-pyinstaller-hooks-contrib

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

# mapping of PyPI name to distro name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: zlib-devel
BuildRequires: libcmocka-devel
%pyproject_builddeps_build
%if_with check
# not packaged in Sisyphus
%add_pyproject_deps_check_filter pytest-drop-dup-tests
BuildRequires: /proc
%pyproject_builddeps_check
%pyproject_builddeps_metadata
%endif

%filter_from_requires /python3(macholib.*)/d
%add_python3_req_skip pywintypes pefile pyimod01_archive pyimod02_importers pyimod03_ctypes

%description
PyInstaller bundles a Python application and all its dependencies into a single
package. The user can run the packaged app without installing a Python
interpreter or any modules.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements-base.txt
%endif
# Remove binary files
rm -rf PyInstaller/bootloader/*

%ifarch %e2k
# old waf didn't know of e2k
sed -i "/xtensa/a\    '__e2k__': 'e2k'," bootloader/waflib/Tools/c_config.py
# lcc 1.26 sneezes at pyi_main.c:57
sed -i "s/'-Werror', /&'-Wno-error=unused-but-set-variable', /" \
	bootloader/wscript
%endif

%build
%pyproject_build

%install
%pyproject_install
# Fix path for executable files
if [ "%_libexecdir" != "%_libdir" ]; then
    mv %buildroot%_libexecdir %buildroot%_libdir
fi

%check
# Bootloader built in the RPM environment fails to read its own archive TOC.
%pyproject_run_pytest \
-k "not test_pyz_as_external_file \
and not test_sys_executable[onedir-sideload] \
and not test_sys_executable[onefile-sideload]" \
-n auto tests/unit tests/functional

%files
%doc README.rst
%_bindir/*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jun 08 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 6.20.0-alt1
- New version (6.20.0).

* Fri Jan 16 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 6.18.0-alt1
- New version (6.18.0).
- Enabled check section.
- Updated dependency management.
- Mapped of PyPI name to distro name.

* Sat Nov 04 2023 Andrey Cherepanov <cas@altlinux.org> 6.1.0-alt1
- New version.
- Removed deprecated distutils.

* Tue Apr 04 2023 Michael Shigorin <mike@altlinux.org> 5.6.2-alt2
- E2K: fix build.

* Sun Nov 13 2022 Andrey Cherepanov <cas@altlinux.org> 5.6.2-alt1
- New version.

* Sun Oct 30 2022 Andrey Cherepanov <cas@altlinux.org> 5.6.1-alt1
- New version.

* Sun Sep 18 2022 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt1
- New version.

* Sun Aug 28 2022 Andrey Cherepanov <cas@altlinux.org> 5.3-alt1
- Initial build for Sisyphus.
