Name: moneymanagerex
Version: 1.6.3
Release: alt3

Summary: Simple to use financial management software
License: GPLv2
Group: Office

URL: http://www.moneymanagerex.org/

# Note: pack submodules to .gear/@name@-postsubmodules (as in .gear/rules)

## Source-url: https://github.com/moneymanagerex/moneymanagerex/archive/v%version.tar.gz
# Source-git: https://github.com/moneymanagerex/moneymanagerex.git
Source: %name-%version.tar
Patch: fix_compile_flag.patch

ExcludeArch: %arm %ix86

AutoReq:yes,nomingw32

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: git-core
BuildRequires: libcurl-devel
BuildRequires: lsb-release
BuildRequires: gcc-c++ libdb4-devel
BuildRequires: libwxGTK3.2-devel
BuildRequires: rapidjson
BuildRequires: liblua-devel

%description
Simple to use financial management software
Money Manager Ex (MMEX) is a free, open-source,
cross-platform, easy-to-use personal finance software.
It primarily helps organize one's finances and keeps
track of where, when and how the money goes.
MMEX includes all the basic features that 90 percents of users
would want to see in a personal finance application.
The design goals are to concentrate on simplicity
and user friendliness - something one can use everyday.

%prep
%setup
%ifnarch x86_64
%patch -p1
%endif

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %name

%files -f %name.lang
%doc README.TXT README.md
%_bindir/mmex
%_desktopdir/mmex.desktop
#_man1dir/*
%_iconsdir/hicolor/scalable/apps/mmex.svg
%_docdir/mmex/
%_datadir/mmex/

%changelog
* Sat Mar 18 2023 Anton Midyukov <antohami@altlinux.org> 1.6.3-alt3
- fix BuildRequires (liblua5.4-devel -> liblua-devel)

* Thu Mar 16 2023 Anton Midyukov <antohami@altlinux.org> 1.6.3-alt2
- update BuildRequires
- unbuilt-in rapidjson, lua
- Fix build on non-x86_64
- ExcludeArch: %%arm %%ix86

* Thu Mar 09 2023 Anton Midyukov <antohami@altlinux.org> 1.6.3-alt1
- new version 1.6.3 (with rpmrb script)

* Mon Mar 06 2023 Anton Midyukov <antohami@altlinux.org> 1.3.3-alt3
- rebuilt with libwxGTK3.2

* Sat Sep 15 2018 Anton Midyukov <antohami@altlinux.org> 1.3.3-alt2.1
- rebuilt with libwxGTK3.0
- fix place locale

* Sat May 26 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt2
- rebuild with libwxGTK3.1-sqlite3 4.0.3

* Mon Mar 13 2017 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- new version 1.3.3 (with rpmrb script)

* Sun Oct 04 2015 Anton Midyukov <antohami at altlinux.org> 1.2.2-alt2
- Rebuilt for new gcc5 C++11 ABI.

* Thu Aug 13 2015 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- initial build for ALT Linux Sisyphus
