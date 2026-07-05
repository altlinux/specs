%define _unpackaged_files_terminate_build 1

%def_with check

Name: wiredpanda
Version: 5.1.3
Release: alt1

Summary: Logic circuits simulator
License: GPL-3.0-or-later
Group: Education
Url: https://github.com/GIBIS-UNIFESP/wiRedPanda

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(nlohmann_json)
BuildRequires: libjson-schema-validator-devel

%if_with check
BuildRequires: ctest
BuildRequires: xvfb-run
%endif

%description
WiRed Panda is designed to help students to learn about logic circuits
and simulate them in an easy and friendly way.

The main features of the software are:

* Real time logic simulation;
* User-friendly interface;
* It's intuitive and easy to use;
* Export your work as an image or a PDF.

%prep
%setup

sed -i "s|Exec=wiredpanda %%F|Exec=/usr/bin/wiredpanda %%f|" App/Resources/Freedesktop/wiredpanda.desktop
sed -i "s|Categories=.*|Categories=Education;Electronics;|" App/Resources/Freedesktop/wiredpanda.desktop

%build
%ifarch riscv64
%add_optflags -Wno-error=cast-align
%endif
%cmake \
       -DWIREDPANDA_USE_SYSTEM_JSON=ON
%cmake_build

%install
%cmake_install

install -Dm644 App/Resources/Assets/Logos/wpanda.svg %buildroot%_iconsdir/hicolor/scalable/apps/wpanda.svg
install -Dm644 App/Resources/Freedesktop/wiredpanda-mime.xml %buildroot%_datadir/mime/packages/wiredpanda-mime.xml

for sz in 32x32 64x64 26x26 48x48 128x128 ;
do
  install -Dm644 App/Resources/Assets/Icons/${sz}/wpanda-file.png  %buildroot%_iconsdir/hicolor/${sz}/apps/wpanda-file.png
done

%find_lang %name --with-qt --all-name

%check
xvfb-run -a %ctest -E TestLanguageManager

%files -f %{name}.lang
%doc README.md Examples
%_bindir/wiredpanda
%_desktopdir/wiredpanda.desktop
%_iconsdir/hicolor/*/apps/wpanda.png
%_iconsdir/hicolor/*/apps/wpanda-file.png
%_iconsdir/hicolor/scalable/apps/wpanda.svg
%_datadir/mime/packages/wiredpanda-mime.xml

%changelog
* Sat Jul 04 2026 Nikolay Strelkov <snk@altlinux.org> 5.1.3-alt1
- Initial build for Sisyphus
