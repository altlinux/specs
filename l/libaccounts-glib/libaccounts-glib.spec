# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize pkgconfig(dbus-1) pkgconfig(glib-2.0) pkgconfig(gobject-2.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libaccounts-glib
Version:	0.45
Release:	alt3_3
Group:		System/Libraries
Summary:	Nokia Maemo Accounts base library
License:	LGPLv2
URL:		http://gitorious.org/accounts-sso/accounts-glib
# extracted from http://repo.meego.com/MeeGo/builds/trunk/daily/core/repos/source/libaccounts-glib-0.45-1.1.src.rpm
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	libdbus-glib-devel
BuildRequires:	libxml2-devel
BuildRequires:	libsqlite3-devel
BuildRequires:	libcheck-devel
# no needed for final release tarball
BuildRequires:	libtool
BuildRequires:	gtk-doc
Source44: import.info
Patch33: libaccounts-glib-0.45-alt-gcc47.patch

%description
%{summary}.

%package devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	libaccounts-glib = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch33 -p1

%build
gtkdocize
autoreconf -i --force

%configure --disable-static \
	--disable-gtk-doc

sed -i 's/-Werror//g' libaccounts-glib/Makefile
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
%doc COPYING AUTHORS
%dir %{_datadir}/backup-framework
%dir %{_datadir}/backup-framework/applications
%{_datadir}/backup-framework/applications/*.conf
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}

%changelog
* Wed Jun 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.45-alt3_3
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.45-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.45-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1_2
- initial import by fcimport

