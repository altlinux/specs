Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/xmllint /usr/bin/xsltproc docbook-dtds pkgconfig(pygobject-3.0) python-devel
# END SourceDeps(oneline)
%filter_from_requires /dbus-test-runner/d
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.23

%global commit0 8d14b10652b2fe6c25d8ad8334e2d5023d254313
%global gittag0 VERSION_%{version}
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global snap0 20160216

Name:		libaccounts-glib
Version:	1.23
Release:	alt1_8
Summary:	Accounts framework for Linux and POSIX based platforms
License:	LGPLv2
URL:        https://gitlab.com/accounts-sso/libaccounts-glib

Source0:    https://gitlab.com/accounts-sso/%{name}/repository/archive.tar.gz?ref=%{gittag0}#/%{name}-%{version}.tar.gz

BuildRequires:	libdbus-glib-devel
BuildRequires:	libxml2-devel
BuildRequires:	libsqlite3-devel
BuildRequires:	libcheck-devel
BuildRequires:	gobject-introspection-devel
# no needed for final release tarball
BuildRequires:	libtool
BuildRequires:	gtk-doc gtk-doc-mkpdf
Source44: import.info

%description
%{summary}.

%package devel
Group: Development/C
Summary:	Development files for %{name}
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
%setup -q -n %{name}-%{gittag0}-%{commit0}

sed -i s,-Werror,, `find . -name Makefile'*'`


%build
test -x configure || \
NOCONFIGURE=1 \
./autogen.sh

%configure \
  --disable-static \
  --enable-gtk-doc

%make_build


%install
make install DESTDIR=%{buildroot}

rm -fv %{buildroot}%{_libdir}/lib*.la

# create/own data dirs
mkdir -p %{buildroot}%{_datadir}/accounts/{applications,providers,services,service_types}

# add docs manuall to %%doc instead
rm -rfv %{buildroot}%{_prefix}/doc/reference

%check
# advisory and non-fatal for now
make check || cat tests/test-suite.log ||:




%files
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog README NEWS
%{_bindir}/ag-backup
%{_bindir}/ag-tool
%{_mandir}/man1/ag-backup.1*
%{_mandir}/man1/ag-tool.1*
%dir %{_datadir}/backup-framework
%dir %{_datadir}/backup-framework/applications
%{_datadir}/backup-framework/applications/*.conf
%{_libdir}/libaccounts-glib.so.0*
%{_libdir}/girepository-1.0/Accounts-1.0.typelib
%dir %{_datadir}/xml/
%dir %{_datadir}/xml/accounts/
%dir %{_datadir}/xml/accounts/schema/
%dir %{_datadir}/xml/accounts/schema/dtd
%{_datadir}/xml/accounts/schema/dtd/accounts-*.dtd
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/applications/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%dir %{_datadir}/accounts/service_types/

%files devel
%{_libdir}/libaccounts-glib.so
%{_libdir}/pkgconfig/libaccounts-glib.pc
%{_includedir}/libaccounts-glib
%{_datadir}/gir-1.0/Accounts-1.0.gir
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/vala/vapi/libaccounts-glib.deps
%{_datadir}/vala/vapi/libaccounts-glib.vapi
## testing bits
%{_datadir}/libaccounts-glib/
%{_libdir}/libaccounts-glib/

%files docs
%doc %{_datadir}/gtk-doc/html/libaccounts-glib/


%changelog
* Sat Dec 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_8
- fixed build

* Thu Oct 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_6
- dropped req: dbus-test-runner

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_1
- update to new release by fcimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_1
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1_2
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_4
- update to new release by fcimport

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

