%define _unpackaged_files_terminate_build 1
%define xdg_name io.github.lawstorant.boxflat

%filter_from_requires /^python3(gi.repository.Gio)/d

Name: boxflat
Version: 1.36.1
Release: alt1

Summary: Boxflat for Moza Racing. Control your Moza gear settings!

License: GPLv3
Group: Games/Other
Url: https://github.com/Lawstorant/boxflat

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

Requires: python3-module-%name
Requires: libgtk4-gir libadwaita-gir

BuildArch: noarch

%description
%summary

%package -n python3-module-%name
Summary: Python 3 module for boxflat
Group: Development/Python3
%description -n python3-module-%name
%summary

%prep
%setup
sed -i "s|/etc/udev/rules.d|%_udevrulesdir|g" install.sh
sed -i "s|/etc/udev/rules.d|%_udevrulesdir|g" boxflat/app.py

%build

%install
./install.sh add-prefix %buildroot no-udev
mkdir -p %buildroot%python3_sitelibdir
mv -v %buildroot%_datadir/%name/%name %buildroot%python3_sitelibdir/

%files
%doc *.md LICENSE
%_bindir/%name
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_datadir/metainfo/%xdg_name.metainfo.xml
%_iconsdir/hicolor/scalable/apps/%xdg_name.svg
%_udevrulesdir/99-%name.rules

%files -n python3-module-%name
%python3_sitelibdir/%name/

%changelog
* Tue Jun 16 2026 Mikhail Tergoev <fidel@altlinux.org> 1.36.1-alt1
- 1.36.1

* Mon Feb 09 2026 Mikhail Tergoev <fidel@altlinux.org> 1.36.0-alt1
- 1.36.0

* Mon Aug 25 2025 Mikhail Tergoev <fidel@altlinux.org> 1.34.4-alt1
- 1.34.4

* Thu Jul 24 2025 Mikhail Tergoev <fidel@altlinux.org> 1.34.2-alt1
- 1.34.2

* Tue Jun 10 2025 Mikhail Tergoev <fidel@altlinux.org> 1.32.1-alt1
- 1.32.1

* Fri May 23 2025 Mikhail Tergoev <fidel@altlinux.org> 1.31.0-alt1
- 1.31.0

* Mon May 12 2025 Mikhail Tergoev <fidel@altlinux.org> 1.30.1-alt1
- 1.30.1

* Mon Apr 07 2025 Mikhail Tergoev <fidel@altlinux.org> 1.29.1-alt1
- 1.29.1

* Thu Mar 27 2025 Mikhail Tergoev <fidel@altlinux.org> 1.28.4-alt1
- 1.28.4

* Tue Mar 04 2025 Mikhail Tergoev <fidel@altlinux.org> 1.28.3-alt1
- 1.28.3

* Tue Feb 25 2025 Mikhail Tergoev <fidel@altlinux.org> 1.28.2-alt1
- 1.28.2

* Sat Feb 15 2025 Mikhail Tergoev <fidel@altlinux.org> 1.27.4-alt1
- initial build for ALT Sisyphus
