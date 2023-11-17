# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/fep /usr/bin/valadoc pkgconfig(gio-2.0)
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		libskk
Version:	1.0.4
Release:	alt3_11
Summary:	Library to deal with Japanese kana-to-kanji conversion method

License:	GPLv3+
URL:		http://github.com/ueno/libskk
Source0:	https://bitbucket.org/libskk/libskk/downloads/%{name}-%{version}.tar.xz

BuildRequires(pre): rpm-macros-valgrind
BuildRequires:	vala vala-tools valadoc-devel
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	libjson-glib libjson-glib-devel libjson-glib-gir-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gettext-tools libasprintf-devel
%ifarch %valgrind_arches
BuildRequires: /usr/bin/valgrind
%endif
Source44: import.info

%description
The libskk project aims to provide GObject-based interface of Japanese
input methods.  Currently it supports SKK (Simple Kana Kanji) with
various typing rules including romaji-to-kana, AZIK, ACT, TUT-Code,
T-Code, and NICOLA.


%package	devel
Group: Development/Other
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Group: Development/Tools
Summary:	Tools for %{name}
BuildRequires:	libfep-devel
Requires:	%{name} = %{version}-%{release}

%description	tools
The %{name}-tools package contains tools for developing applications
that use %{name}.


%prep
%setup -q


%build
%configure --disable-static --enable-fep
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name}





%files -f %{name}.lang
%doc README rules/README.rules COPYING
%{_libdir}/*.so.*
%{_datadir}/libskk
%{_libdir}/girepository-1.0/Skk*.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Skk*.gir
%{_datadir}/vala/vapi/*

%files tools
%{_bindir}/skk*
%{_libexecdir}/skk*
%{_mandir}/man1/skk*


%changelog
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

