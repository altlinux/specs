%define up_name	DisplayCAL

Name: displaycal
Version: 3.9.10
Release: alt1

Summary: A graphical user interface for the Argyll CMS display calibration utilities

Group: Graphics
License: GPL-3.0
Url: https://github.com/eoyilmaz/displaycal-py3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/eoyilmaz/displaycal-py3/releases/download/%version/DisplayCAL-%version.tar.gz
Source: %name-%version.tar
Patch: displaycal-3.9.3-udev-dir.patch
Patch1: displaycal-skip-update-check.patch
Patch2: displaycal-3.9.8-fix-autostart-location.patch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-module-wheel

#BuildRequires: python3dist(setuptools-scm)
#BuildRequires: python3dist(setuptools-scm[toml])
#BuildRequires: python3dist(wheel)
#BuildRequires: python3dist(pip)
#BuildRequires: python3dist(wxpython)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(python3)
BuildRequires: xdg-user-dirs
#BuildRequires: locales-fr

Requires: argyllcms
#Requires: python3dist(setuptools)
#Requires: python3dist(pygobject)
#Requires: python3dist(numpy)
#Requires: python3dist(wxpython)
#Requires: python3dist(send2trash)
#Requires: python3dist(distro)

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
%autopatch -p1

# drop prebuilt modules
find . -name '*.so' -print -delete

# fix paths
%if "%_lib" == "lib"
ln -s ./lib64 DisplayCAL/lib32
%__subst 's/DisplayCAL\.lib64/DisplayCAL\.lib32/g' DisplayCAL/RealDisplaySizeMM.py
%endif

%build
#export LC_ALL=fr_FR.UTF-8
%pyproject_build

%install
#export LC_ALL=fr_FR.UTF-8
%pyproject_install
mkdir -p %buildroot%_sysconfdir/xdg/autostart/
mv %buildroot%_datadir/DisplayCAL/z-displaycal-apply-profiles.desktop %buildroot%_sysconfdir/xdg/autostart/

%files
%docdir %_docdir/%up_name-%version/
%doc %_docdir/%up_name-%version/*
%_sysconfdir/xdg/autostart/z-displaycal-apply-profiles.desktop
%_bindir/*
%_datadir/%up_name/
%_iconsdir/hicolor/*/apps/%{name}*.png
%_desktopdir/*.desktop
%_metainfodir/net.displaycal.%up_name.appdata.xml
%python3_sitelibdir/%up_name/
%python3_sitelibdir/%up_name-%version.dist-info
%_man1dir/*


%changelog
* Thu Apr 20 2023 Vitaly Lipatov <lav@altlinux.ru> 3.9.10-alt1
- initial build for ALT Sisyphus
