# BEGIN SourceDeps(oneline):
BuildRequires: glib2-devel pkgconfig(gio-2.0)
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		libfep
Version:	0.1.0
Release:	alt3_20
Summary:	Library to implement FEP (front end processor) on ANSI terminals

License:	BSD and GPLv3+
URL:		http://github.com/ueno/libfep
Source0:	https://github.com/ueno/libfep/releases/download/%{version}/%{name}-%{version}.tar.gz

# FIXME switch to libgee-0.8 once this package is ready for the new libgee API
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	gobject-introspection-devel
BuildRequires:	vala vala-tools valadoc-devel
Source44: import.info

%description
The libfep project aims to provide a server and a library to implement
input method FEP (front end processor), running on ANSI compliant
terminals.


%package	devel
Group: System/Libraries
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
# needed to regenerate GIR
GIO_LIBS=`pkg-config gio-2.0 gmodule-2.0 --libs`
export GIO_LIBS
%configure --disable-static
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f '{}' ';'
cp -p fep/README README.fep





%files
%doc README README.fep COPYING fep/COPYING.BSD ChangeLog
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/Fep*.typelib
%{_bindir}/fep*
%{_mandir}/man1/fep*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Fep*.gir
%{_datadir}/vala/vapi/*


%changelog
* Wed Sep 28 2022 Igor Vlasenko <viy@altlinux.org> 0.1.0-alt3_20
- to Sisyphus for fcitx5-*

* Sun Aug 07 2022 Igor Vlasenko <viy@altlinux.org> 0.1.0-alt2_20
- update to new release by fcimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 0.1.0-alt2_19
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.1.0-alt2_18
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.1.0-alt2_17
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_16
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_16
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_15
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_14
- update to new release by fcimport

* Thu Feb 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_13
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_11
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_10
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_9
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_7
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_6
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_5
- update to new release by fcimport

* Tue Jan 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.9-alt1_1
- initial fc import

