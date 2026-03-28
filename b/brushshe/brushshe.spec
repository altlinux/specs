%define _unpackaged_files_terminate_build 1

Name: brushshe
Version: 2.5.0
Release: alt1

Summary: Painting app, written in Python, CustomTkinter and PIL
License: MPL-2.0 AND CC0-1.0 AND (MPL-2.0 OR CC-BY-4.0) AND OFL-1.1-no-RFN AND OFL-1.1-RFN
Group: Graphics
URL: https://github.com/limafresh/Brushshe

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: python3(tkinter)
Requires: python3(customtkinter)
Requires: python3(PIL)

BuildArch: noarch

Source: %name-%version.tar
Source1: brushshe.desktop

%description
Brushshe is a simple and user-friendly raster graphics editor.

%prep
%setup
sed -i "s|https://raw.githubusercontent.com/limafresh/Brushshe/main/||" README.md
sed -i "s|https://raw.githubusercontent.com/limafresh/Brushshe/main/Brushshe/assets/icons/logo.svg|/usr/share/icons/hicolor/scalable/apps/brushshe.svg|" README.md

%build
# nothing to build here

%install
# program files
mkdir -pv %buildroot/%_datadir/
cp -rv Brushshe %buildroot/%_datadir

# executable, FIXME
mkdir -pv %buildroot/%_bindir
cat <<EOF > %buildroot/%_bindir/%name
#!/bin/sh
python3 %_datadir/Brushshe/main.py "\$@"
EOF
chmod a+x %buildroot/%_bindir/%name

# icon
mkdir -pv %buildroot/%_iconsdir/hicolor/scalable/apps/
cp -v Brushshe/assets/icons/logo.svg %buildroot/%_iconsdir/hicolor/scalable/apps/%name.svg

# desktop-file
install -Dpm0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%doc LICENSE LICENSE-CC0 README.md screenshot.png
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%dir %_datadir/Brushshe
%_datadir/Brushshe/*

%changelog
* Sat Mar 28 2026 Nikolay Strelkov <snk@altlinux.org> 2.5.0-alt1
- New version 2.5.0.

* Wed Dec 31 2025 Nikolay Strelkov <snk@altlinux.org> 2.4.0-alt1
- New version 2.4.0.

* Sun Nov 02 2025 Nikolay Strelkov <snk@altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus
