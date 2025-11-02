%define _unpackaged_files_terminate_build 1

%define pypi_name frog

%def_with check

Name: frog-ocr
Version: 1.6.0
Release: alt1

Summary: Intuitive text extraction tool (OCR) for GNOME
License: MIT
Group: Graphical desktop/GNOME
URL: https://github.com/tenderowl/frog

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: meson
BuildRequires: cmake
BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: /usr/bin/blueprint-compiler
BuildRequires: pkgconfig(gio-2.0)

Requires: python3(nanoid)
Requires: python3(pyzbar.pyzbar)
Requires: /usr/bin/tesseract

BuildArch: noarch

Source: %name-%version.tar

# Completely disabled PostHog telemetry
# to prevent https://github.com/TenderOwl/Frog/issues/249
Patch: %name-%version-%release.patch

%description
Quickly extract text from almost any source: youtube, screencasts,
PDFs, webpages, photos, etc. Grab the image and get the text.

The Frog could help you to deal with QR codes helping you to
get them decoded!

%prep
%setup
sed -i 's|/app/share/|/usr/share/|g' frog/language_manager.py
sed -i 's|^Categories=.*|Categories=Graphics;OCR;Scanning;|' data/com.github.tenderowl.frog.desktop.in
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %pypi_name

%check
%meson_test

%files -f %pypi_name.lang
%doc COPYING LICENSE README.md
%_bindir/%pypi_name
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/*.svg
%python3_sitelibdir_noarch/%pypi_name/
%_datadir/appdata/*.appdata.xml
%_datadir/appdata/eng.traineddata
%dir %_datadir/frog
%_datadir/frog/*.gresource
%_datadir/glib-2.0/schemas/*.gschema.xml
%exclude %_datadir/locale/be_Latn/LC_MESSAGES/frog.mo
%exclude %_datadir/locale/zh_Hans/LC_MESSAGES/frog.mo

%changelog
* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 1.6.0-alt1
- Initial build for Sisyphus
