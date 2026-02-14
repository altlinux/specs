%define _unpackaged_files_terminate_build 1

Name: ipe
Version: 7.2.30
Release: alt1

Summary: Ipe extensible drawing editor
License: GPL-3.0-or-later
Group: Publishing
Url: https://ipe.otfried.org
Vcs: https://github.com/otfried/ipe

Source: %name-%version.tar

BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(lua5.4)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(libspiro)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(cairo)
BuildRequires: qt6-base-devel

Requires: texlive
Requires: texlive-dist

%filter_from_requires /lua5.4(.*)/d

%description
Ipe is the extensible drawing editor. Ipe allows you to create
figures in PDF format, for inclusion into LaTeX (or plain TeX)
documents as well as stand-alone PDF documents, for instance to print
transparencies or for on-line presentations.

%package devel
Summary: Development files and documentation for designing Ipelets
Group: Development/Other
Requires: %name = %{version}-%{release}
Requires: qt6-base-devel

%description devel
This packages contains the files necessary to develop Ipelets, which are
plugins for the Ipe editor.

%prep
%setup

%build
pushd src
%make_build \
            LUA_CFLAGS="`pkg-config --cflags lua`" \
            LUA_LIBS="`pkg-config --libs lua`" \
            IPEPREFIX="%_prefix" \
            MOC="%_libdir/qt6/libexec/moc" \
            IPELETDIR="%_libdir/%name/%version/ipelets" \
            IPECURL=1 \
            IPEGSL=1
popd

%install
pushd src
%makeinstall_std \
                 INSTALL_ROOT=%buildroot \
                 IPEPREFIX="%_prefix" \
                 IPELIBDIR="%_libdir" \
                 IPELETDIR="%_libdir/%name/%version/ipelets"
popd

# prepare desktop file
mkdir -p %buildroot%_desktopdir
cat <<EOF > %buildroot%_desktopdir/ipe.desktop
[Desktop Entry]
Name=Ipe
Comment=The Ipe extensible drawing editor
Exec=ipe
Icon=ipe
Type=Application
Encoding=UTF-8
Categories=Qt;Office;Publishing;
EOF

# install icons
install -Dm644 artwork/ipe.iconset/icon_16x16.png %buildroot%_iconsdir/hicolor/16x16/apps/ipe.png
install -Dm644 artwork/ipe.iconset/icon_32x32.png %buildroot%_iconsdir/hicolor/32x32/apps/ipe.png
install -Dm644 artwork/ipe.iconset/icon_64x64.png %buildroot%_iconsdir/hicolor/64x64/apps/ipe.png
install -Dm644 artwork/ipe.iconset/icon_128x128.png %buildroot%_iconsdir/hicolor/128x128/apps/ipe.png
install -Dm644 artwork/ipe.iconset/icon_256x256.png %buildroot%_iconsdir/hicolor/256x256/apps/ipe.png
install -Dm644 artwork/ipe.iconset/icon_512x512.png %buildroot%_iconsdir/hicolor/512x512/apps/ipe.png

%files
%doc README.md doc/gpl.txt
%_bindir/ipe
%_bindir/ipe6upgrade
%_bindir/ipecurl
%_bindir/ipeextract
%_bindir/iperender
%_bindir/iperender-par
%_bindir/ipescript
%_bindir/ipetoipe
%_bindir/ipepresenter
%_libdir/libipe.so.%{version}
%_libdir/libipeui.so.%{version}
%_libdir/libipecairo.so.%{version}
%_libdir/libipecanvas.so.%{version}
%_libdir/libipelua.so.%{version}
%dir %_libdir/%name
%dir %_libdir/%name/%version
%dir %_libdir/%name/%version/ipelets
%_libdir/%name/%version/ipelets/*
%dir %_datadir/%name
%dir %_datadir/%name/%version
%_datadir/%name/%version/icons
%_datadir/%name/%version/lua
%_datadir/%name/%version/scripts
%_datadir/%name/%version/styles
%_desktopdir/ipe.desktop
%_iconsdir/hicolor/*/apps/ipe.png
%_man1dir/ipe.1.*
%_man1dir/ipe6upgrade.1.*
%_man1dir/ipeextract.1.*
%_man1dir/iperender.1.*
%_man1dir/ipescript.1.*
%_man1dir/ipetoipe.1.*

%files devel
%_includedir/*.h
%_libdir/libipe.so
%_libdir/libipeui.so
%_libdir/libipecairo.so
%_libdir/libipecanvas.so
%_libdir/libipelua.so

%changelog
* Sat Feb 14 2026 Nikolay Strelkov <snk@altlinux.org> 7.2.30-alt1
- Initial build for Sisyphus
