%define up_name DisplayCAL

Name: displaycal
Version: 3.9.11
Release: alt4

Summary: A graphical user interface for the Argyll CMS display calibration utilities

Group: Graphics
License: GPL-3.0
Url: https://github.com/eoyilmaz/displaycal-py3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/eoyilmaz/displaycal-py3/releases/download/%version/DisplayCAL-%version.tar.gz
Source: %name-%version.tar

Patch1: displaycal-3.9.11-udev-dir.patch
Patch2: displaycal-skip-update-check.patch
Patch3: displaycal-3.9.8-fix-autostart-location.patch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(python3)
BuildRequires: xdg-user-dirs

Requires: argyllcms

AutoProv: no

Provides: %up_name = %version-%release
Provides: dispcalGUI = %version-%release

%add_python3_req_skip pywintypes win32api win32com.shell win32con win32gui win32process winerror winreg comtypes comtypes.client comtypes.gen.TaskbarLib
# internal
%add_python3_req_skip demjson_compat

#  displaycal: Требует: argyllcms но пакет не может быть установлен
#              Требует: python3(comtypes.client) (< 0) но пакет не может быть установлен
#              Требует: python3(comtypes.gen.TaskbarLib) (< 0) но пакет не может быть установлен
#              Требует: python3(demjson_compat) (< 0) но пакет не может быть установлен


%description
A graphical user interface for the Argyll CMS display calibration utilities.

#--------------------------------------------------------------------

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

# hack to force creating dist/net.displaycal... (missed due pyproject)
subst "s|create_appdata = |create_appdata = True or |" setup.py

# drop prebuilt modules
find . -name '*.so' -print -delete

# fix paths
%if "%_lib" == "lib"
ln -s ./lib64 DisplayCAL/lib32
%__subst 's/DisplayCAL\.lib64/DisplayCAL\.lib32/g' DisplayCAL/RealDisplaySizeMM.py
%endif

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%_sysconfdir/xdg/autostart/
mv -v %buildroot%_datadir/DisplayCAL/z-displaycal-apply-profiles.desktop %buildroot%_sysconfdir/xdg/autostart/
rm -v %buildroot%python3_sitelibdir/%up_name/{setup.py,postinstall.py}

%files
%_docdir/%up_name-%version/
%_sysconfdir/xdg/autostart/z-displaycal-apply-profiles.desktop
%_bindir/%name
%_bindir/%name-*
%_datadir/%up_name/
%_iconsdir/hicolor/*/apps/%{name}*.png
%_desktopdir/*.desktop
%_metainfodir/net.displaycal.%up_name.appdata.xml
%python3_sitelibdir/%up_name/
%python3_sitelibdir/%up_name-%version.dist-info
%_man1dir/*


%changelog
* Sun Oct 22 2023 Vitaly Lipatov <lav@altlinux.ru> 3.9.11-alt4
- remove setup.py designed for uninstall only

* Fri Aug 04 2023 Vitaly Lipatov <lav@altlinux.ru> 3.9.11-alt3
- AutoProv: no

* Fri Aug 04 2023 Vitaly Lipatov <lav@altlinux.ru> 3.9.11-alt2
- cleanup spec

* Mon Jun 12 2023 Vitaly Lipatov <lav@altlinux.ru> 3.9.11-alt1
- new version 3.9.11 (with rpmrb script)

* Thu Apr 20 2023 Vitaly Lipatov <lav@altlinux.ru> 3.9.10-alt1
- initial build for ALT Sisyphus
