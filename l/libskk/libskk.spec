%define _unpackaged_files_terminate_build 1
%add_optflags %optflags_shared
%define soname 0

Name: libskk
Version: 1.1.1
Release: alt1

Summary: Library to deal with Japanese kana-to-kanji conversion method
License: GPLv3+
Group: System/Libraries

Url: http://github.com/ueno/libskk
Vcs: http://github.com/ueno/libskk

Source: %name-%version.tar.xz

Obsoletes: %name-tools <= 1.0.4-alt3_11

BuildRequires(pre): rpm-macros-valgrind
BuildRequires: /usr/bin/fep
BuildRequires: /usr/bin/valadoc
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: vala
BuildRequires: vala-tools
BuildRequires: valadoc-devel
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: libjson-glib
BuildRequires: libjson-glib-devel
BuildRequires: libjson-glib-gir-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gettext-tools
BuildRequires: libasprintf-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libfep-devel
%ifarch %valgrind_arches
BuildRequires: /usr/bin/valgrind
%endif

%description
The libskk project aims to provide GObject-based interface of Japanese
input methods.  Currently it supports SKK (Simple Kana Kanji) with
various typing rules including romaji-to-kana, AZIK, ACT, TUT-Code,
T-Code, and NICOLA.

%package devel
Group: Development/Other
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package %name%soname
Group: System/Libraries
Summary: %name library
%description %name%soname
%name library.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %EVR
%description gir
GObject introspection data for the %name

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR
%description gir-devel
GObject introspection devel data for the %name

%prep
%setup

%build
%autoreconf
%configure --disable-static --enable-fep
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang --all-name %name

%files -f %name.lang
%doc README.md COPYING
%_bindir/skk*
%_libexecdir/skk*
%_mandir/man1/skk*
%_datadir/%name

%files devel
%_includedir/%name
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc
%_datadir/vala/vapi/*

%files %name%soname
%_libdir/%name.so.%soname
%_libdir/%name.so.%{soname}.*

%files gir
%_libdir/girepository-1.0/Skk*.typelib

%files gir-devel
%_datadir/gir-1.0/Skk*.gir

%changelog
* Tue Oct 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.1.1-alt1
- 1.0.4 -> 1.1.1

* Fri Nov 17 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.0.4-alt3_11
- NMU: fixed FTBFS on LoongArch (no valgrind here yet)

* Wed Sep 28 2022 Igor Vlasenko <viy@altlinux.org> 1.0.4-alt3_10
- to Sisyphus for fcitx5-skk

* Sun Aug 07 2022 Igor Vlasenko <viy@altlinux.org> 1.0.4-alt2_10
- update to new release by fcimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 1.0.4-alt2_9
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 1.0.4-alt2_8
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 1.0.4-alt2_7
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_6
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_6
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_5
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_4
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_2
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_1
- update to new release by fcimport

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_6
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_4
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2
- update to new release by fcimport

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_1
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_5
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2
- update to new release by fcimport

* Wed Apr 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1
- update to new release by fcimport

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.13-alt1_3
- update to new release by fcimport

* Tue Jan 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.13-alt1_2
- initial fc import

