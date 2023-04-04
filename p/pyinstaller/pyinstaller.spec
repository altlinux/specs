Name:    pyinstaller
Version: 5.6.2
Release: alt2

Summary: Freeze (package) Python programs into stand-alone executables
License: GPL-2.0+
Group:   Development/Python3

URL: https://pyinstaller.org
VCS: https://github.com/pyinstaller/pyinstaller

Packager: Andrey Cherepanov <cas@altlinux.org>

Requires: python3-module-pyinstaller-hooks-contrib

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: zlib-devel
BuildRequires: libcmocka-devel

%filter_from_requires /python3(macholib.*)/d
%filter_from_requires /python3(pywintypes)/d
%filter_from_requires /python3(pefile)/d
%filter_from_requires /python3(win32com.*)/d

%add_python3_req_skip pyimod01_archive pyimod02_importers pyimod03_ctypes

%description
PyInstaller bundles a Python application and all its dependencies into a single
package. The user can run the packaged app without installing a Python
interpreter or any modules.

%prep
%setup
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
%python3_build_debug

%install
%python3_install
# Fix path for executable files
if [ "%_libexecdir" != "%_libdir" ]; then
    mv %buildroot%_libexecdir %buildroot%_libdir
fi

%files
%doc README.rst
%_bindir/*
%python3_sitelibdir/PyInstaller
%python3_sitelibdir/*.egg-info

%changelog
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
