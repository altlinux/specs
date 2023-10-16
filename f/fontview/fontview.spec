Name: fontview
Version: 0.3.1
Release: alt2.20191205

Summary: Demo app that displays fonts with a free/libre/open-source text rendering stack: FreeType, HarfBuzz and Raqm

License: Apache-2.0
Group: Publishing
Url: https://github.com/googlei18n/fontview

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/googlei18n/fontview/archive/v%version.tar.gz
Source: %name-%version.tar

# manually removed: mariadb-common python-module-google python-module-mwlib python3-dev python3-module-yieldfrom python3-module-zope ruby ruby-stdlibs selinux-policy

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: libfribidi-devel
BuildRequires: libharfbuzz-devel
BuildRequires: libfreetype-devel
BuildRequires: libwxGTK3.2-devel
BuildRequires: %_bindir/python3

BuildRequires: libucdn-devel
BuildRequires: libraqm-devel >= 0.2.0

%description
Demo app that displays fonts with a free/libre/open-source text rendering stack:
FreeType, HarfBuzz and Raqm.

%prep
%setup

%build
%__python3 build.py

%install
%__install -D build/%name %buildroot%_bindir/%name

%files
%doc README.md LICENSE.md
%_bindir/%name
# TODO
#%_desktopdir/%name.desktop

%changelog
* Mon Oct 16 2023 Anton Midyukov <antohami@altlinux.org> 0.3.1-alt2.20191205
- NMU: rebuild with wxGTK3.2

* Thu Jun 04 2020 Anton Midyukov <antohami@altlinux.org> 0.3.1-alt1.20191205
- New version

* Sat Sep 15 2018 Anton Midyukov <antohami@altlinux.org> 0.2.3-alt2
- Rebuilt with compat-libwxGTK3.0-gtk2

* Tue Apr 25 2017 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt1
- initial build for ALT Sisyphus
