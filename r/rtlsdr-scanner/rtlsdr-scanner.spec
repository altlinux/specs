Name: rtlsdr-scanner
Version: 1.3.0
Release: alt1

Summary: A cross platform Python frequency scanning GUI for the OsmoSDR rtl-sdr library
License: GPL-3.0
Group: Communications
URL: https://github.com/EarToEarOak/RTLSDR-Scanner

Packager: Anton Midyukov <antohami@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar
Source1: rtlsdr-scanner-16x16.png
Source2: rtlsdr-scanner-32x32.png
Source3: rtlsdr-scanner-48x48.png
Source4: rtlsdr-scanner-96x96.png

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
BuildRequires: desktop-file-utils

Requires: rtl-sdr
Requires: wxPython >= 3.0
%py_requires matplotlib.backends.backend_wx

%description
%summary

%prep
%setup

%build
%python_build

%install
%python_install

# rtlsdr-scanner
cat>%name<<END
#!/bin/sh
%_bindir/python2 %python_sitelibdir/rtlsdr_scanner
END

mkdir -p %buildroot%_bindir
install -m 755 %name %buildroot%_bindir/%name

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
%_iconsdir/hicolor/*/apps/%name.png
%python_sitelibdir/rtlsdr_scanner/
%python_sitelibdir/*.egg-info

%changelog
* Sun Mar 18 2018 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus
