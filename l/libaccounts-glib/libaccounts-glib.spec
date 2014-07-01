# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize /usr/bin/xmllint /usr/bin/xsltproc docbook-dtds pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) python-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libaccounts-glib
Version:	1.16
Release:	alt1_2
Group:		System/Libraries
Summary:	Accounts framework for Linux and POSIX based platforms
License:	LGPLv2
URL:		https://code.google.com/p/accounts-sso/
Source0:	https://accounts-sso.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		libaccounts-glib-1.16-build-with-werror.patch
BuildRequires:	libdbus-glib-devel
BuildRequires:	libxml2-devel
BuildRequires:	libsqlite3-devel
BuildRequires:	libcheck-devel
BuildRequires:	gobject-introspection-devel
# no needed for final release tarball
BuildRequires:	libtool
BuildRequires:	gtk-doc
Source44: import.info

%description
%{summary}.

%package devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package docs
Group: System/Libraries
Summary:	Documentation for %{name}
BuildArch:	noarch

%description docs
The %{name}-docs package contains documentation for %{name}.

%prep
%setup -q

%patch0	-p1 -b .werror

%build
gtkdocize
autoreconf -i --force

%configure --disable-static \
	--disable-gtk-doc

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la

# add docs manuall to %%doc instead
rm -rf %{buildroot}%{_prefix}/doc/reference

# remove tests for now
rm -f %{buildroot}%{_bindir}/*test*
rm -rf %{buildroot}%{_datadir}/libaccounts-glib0-test

%files
%doc COPYING AUTHORS INSTALL ChangeLog README NEWS
%{_bindir}/ag-backup
%{_bindir}/ag-tool
%{_mandir}/man1/ag-backup.1*
%{_mandir}/man1/ag-tool.1*
%dir %{_datadir}/backup-framework
%dir %{_datadir}/backup-framework/applications
%{_datadir}/backup-framework/applications/*.conf
%{_libdir}/%{name}.so.*
%{_libdir}/girepository-1.0/Accounts-1.0.typelib
%dir %{_datadir}/xml/
%dir %{_datadir}/xml/accounts/
%dir %{_datadir}/xml/accounts/schema/
%dir %{_datadir}/xml/accounts/schema/dtd
%{_datadir}/xml/accounts/schema/dtd/accounts-*.dtd

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_datadir}/gir-1.0/Accounts-1.0.gir
%{_libdir}/libaccounts-glib
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/libaccounts-glib
%{_datadir}/vala/vapi/libaccounts-glib.deps
%{_datadir}/vala/vapi/libaccounts-glib.vapi

%files docs
%doc %{_datadir}/gtk-doc/html/libaccounts-glib/

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_2
- update to new release by fcimport

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_2
- update to new release by fcimport

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_1
- new fc release

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.45-alt3_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.45-alt3_4
- update to new release by fcimport

* Wed Jun 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.45-alt3_3
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.45-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.45-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1_2
- initial import by fcimport

