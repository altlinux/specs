Name: rtlsdr-scanner
Version: 1.3.2
Release: alt3

Summary: A cross platform Python frequency scanning GUI for the OsmoSDR rtl-sdr library
License: GPL-3.0-or-later
Group: Communications
URL: https://github.com/EarToEarOak/RTLSDR-Scanner

Packager: Anton Midyukov <antohami@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar
Source1: rtlsdr-scanner-16x16.png
Source2: rtlsdr-scanner-32x32.png
Source3: rtlsdr-scanner-48x48.png
Source4: rtlsdr-scanner-96x96.png
Source5: rtlsdr_scan.png

# Fedora patchs
Patch0: rtlsdr-scanner-1.3.2-fedora.patch
Patch1: rtlsdr-scanner-1.3.2-python3.patch

# ALT patchs
# See: https://bugzilla.redhat.com/show_bug.cgi?id=1844800
Patch2: rtlsdr-scanner-1.3.2-fix-with-matplotlib-3.3.0.patch
Patch3: rtlsdr-scanner-1.3.2-fix_wx_support.patch
Patch4: rtlsdr-scanner-1.3.2-disable-colourMap.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: desktop-file-utils

Requires: rtl-sdr

%description
%summary

%prep
%setup
%autopatch -p1

find rtlsdr_scanner -name '*.py' | xargs sed -i '1s|^#!.*|#!%{__python3}|'

# rtlsdr_scan_diag.py is not needed in distribution
rm -f rtlsdr_scanner/rtlsdr_scan_diag.py

# fix name of the application
mv rtlsdr_scanner/__main__.py %name

# drop python artefact from resources
rm -f rtlsdr_scanner/res/__init__.py

%build
%python3_build

%install
%python3_install

# rtlsdr-scanner
install -Dpm 0755 ./%name %buildroot%_bindir/%name

# Install resources to correct location
install -Dpm 0644 -t %buildroot%_datadir/%name/res rtlsdr_scanner/res/*

# desktop file
mkdir -p %buildroot%_desktopdir
desktop-file-install --add-category="Development" \
  --dir=%buildroot%_datadir/applications \
  --set-icon=%name \
  %name.desktop

# icon
install -Dpm 0644 %SOURCE1 %buildroot%_iconsdir/hicolor/16x16/apps/%name.png
install -Dpm 0644 %SOURCE2 %buildroot%_iconsdir/hicolor/32x32/apps/%name.png
install -Dpm 0644 %SOURCE3 %buildroot%_iconsdir/hicolor/48x48/apps/%name.png
install -Dpm 0644 %SOURCE4 %buildroot%_iconsdir/hicolor/96x96/apps/%name.png

%files
%doc readme.md COPYING doc/Manual.pdf
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.png
%python3_sitelibdir/rtlsdr_scanner/
%python3_sitelibdir/*.egg-info

%changelog
* Fri Jun 25 2021 Anton Midyukov <antohami@altlinux.org> 1.3.2-alt3
- fix run with python3, python3-module-matplotlib >= 3.3.0 (Closes: 40089)

* Tue Apr 14 2020 Anton Midyukov <antohami@altlinux.org> 1.3.2-alt2
- switch to python3 (Closes: 38255)
- fix license tag

* Tue Dec 25 2018 Anton Midyukov <antohami@altlinux.org> 1.3.2-alt1
- new version 1.3.2

* Sun Mar 18 2018 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus
