Name:    codelite
Version: 17.7.0
Release: alt1

Summary: CodeLite is a powerful open-source, cross platform code editor for C/C++

License: GPLv2+
Group:   Development/Tools
URL:     https://codelite.org/
VCS:     https://github.com/eranif/codelite

Source:  %name-%version.tar
Source1: %name-%version-cc-wrapper.tar
Source2: %name-%version-cc-wrapper-tinyjson.tar
Source3: %name-%version-ctags.tar
Source4: %name-%version-dtl.tar
Source5: %name-%version-wx-config-msys2.tar
Source6: %name-%version-wxdap.tar
Source7: %name-%version-yaml-cpp.tar

Requires: libedit-devel

BuildRequires: rpm-build-python3
BuildRequires: cmake gcc-c++ libssh-devel libedit-devel libgtk+3-devel
BuildRequires: libsqlite3-devel libwxGTK3.2-devel libatk-devel libpango-devel
BuildRequires: libffi-devel libfribidi-devel libtiff-devel
BuildRequires: libmount-devel libpixman-devel libblkid-devel libuuid-devel
BuildRequires: libselinux-devel bzlib-devel libexpat-devel libXdmcp-devel
BuildRequires: libXdamage-devel libXxf86vm-devel libdrm-devel libXinerama-devel
BuildRequires: libXi-devel libXrandr-devel libXcursor-devel libXcomposite-devel
BuildRequires: wayland-protocols libxkbcommon-devel libwayland-cursor-devel
BuildRequires: libwayland-egl-devel libepoxy-devel libhunspell-devel
BuildRequires: libXtst-devel at-spi2-atk-devel libat-spi2-core-devel
BuildRequires: glibc-devel-static
BuildRequires: libpcre2-devel

%add_python_req_skip gdb

%description
CodeLite is a free, open source, cross platform IDE specialized in C, C++,
PHP and JavaScript (mainly for backend developers using Node.js)
programming languages, which runs best on all major platforms
(Windows, macOS and Linux).

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7

%build
cmake . -G "Unix Makefiles" \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_BUILD_RPATH=TRUE \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE

%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_datadir/mime/packages/
cp -p %name.xml %buildroot%_datadir/mime/packages/
rm -f %buildroot%_bindir/codelite_open_helper.py
mkdir -p %buildroot%_datadir/man/man1/
cp -p %buildroot%_datadir/%name/man/man1/%{name}* %buildroot%_datadir/man/man1/

%find_lang %name

%files -f %name.lang
%doc AUTHORS LICENSE COPYING
%_bindir/*
%_datadir/%name
%_datadir/applications/%name.desktop
%_datadir/mime/packages/%name.xml
%_datadir/icons/hicolor/*/apps/%name.png
%_libexecdir/%name
%_man1dir/%{name}*

%changelog
* Wed Jan 24 2024 Grigory Ustinov <grenka@altlinux.org> 17.7.0-alt1
- new version 17.7.0.

* Sat Feb 04 2023 Anton Vyatkin <toni@altlinux.org> 17.0.0-alt1
- new version 17.0.0.

* Tue Dec 20 2022 Anton Vyatkin <toni@altlinux.org> 16.7.0-alt1
- new version 16.7.0.

* Wed Sep 21 2022 Anton Midyukov <antohami@altlinux.org> 16.0.0-alt2
- NMU: build with wxGTK3.2

* Thu Apr 28 2022 Grigory Ustinov <grenka@altlinux.org> 16.0.0-alt1
- Automatically updated to 16.0.0.

* Fri Mar 11 2022 Grigory Ustinov <grenka@altlinux.org> 15.0.11-alt1
- Automatically updated to 15.0.11.

* Wed Nov 17 2021 Grigory Ustinov <grenka@altlinux.org> 15.0.7-alt1
- Automatically updated to 15.0.7.

* Wed Aug 11 2021 Grigory Ustinov <grenka@altlinux.org> 15.0.6-alt1
- Automatically updated to 15.0.6.

* Fri Jul 02 2021 Grigory Ustinov <grenka@altlinux.org> 15.0.3-alt2
- Fixed FTBFS.

* Wed May 12 2021 Grigory Ustinov <grenka@altlinux.org> 15.0.3-alt1
- Automatically updated to 15.0.3.

* Wed Oct 14 2020 Anton Midyukov <antohami@altlinux.org> 14.0-alt2
- Fix BuildRequires

* Mon Apr 27 2020 Grigory Ustinov <grenka@altlinux.org> 14.0-alt1
- Automatically updated to 14.0.

* Tue Aug 20 2019 Anton Midyukov <antohami@altlinux.org> 13.0-alt2
- add_optflags (pkg-config --cflags pango) (Fix FTBFS)

* Wed Jun 19 2019 Grigory Ustinov <grenka@altlinux.org> 13.0-alt1
- Initial build for Sisyphus.
