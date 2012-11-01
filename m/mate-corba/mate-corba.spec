# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize
# END SourceDeps(oneline)
Group: System/Servers
%define _libexecdir %_prefix/libexec
Name:	mate-corba
Summary:	CORBA Object Request Broker for MATE Desktop
Version:	1.4.0
Release:	alt1_10
License:	LGPLv2+ and GPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

Provides: MateCORBA-2.0

BuildRequires:	mate-common glib2-devel libIDL-devel libtool autoconf automake gtk-doc
Source44: import.info
Patch33: mate-corba-2.14.3-ref-leaks.patch

%description
MateCORBA is a fork of GNOME's Orbit

%package devel
Summary: Development libraries, header files and utilities for mate-corba
Group: Development/C
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: indent
%description devel
This package contains the header files for MATE CORBA, libraries and utilities
necessary to write programs that use CORBA technology.

%prep
%setup -q -n %{name}-%{version}
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1

%build
%configure --enable-gtk-doc-html --enable-purify --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

rm -fv $RPM_BUILD_ROOT%{_libdir}/libMateCORBA-2.la
rm -fv $RPM_BUILD_ROOT%{_libdir}/libMateCORBA-imodule-2.la
rm -fv $RPM_BUILD_ROOT%{_libdir}/libMateCORBACosNaming-2.la
rm -fv $RPM_BUILD_ROOT%{_libdir}/matecorba-2.0/Everything_module.la


%files
%doc AUTHORS COPYING README TODO
%{_bindir}/matecorba-idl-2
%{_bindir}/matecorba-ior-decode-2
%{_bindir}/matecorba-linc-cleanup-sockets
%{_bindir}/matecorba-typelib-dump
%{_libdir}/libMateCORBA-2.so.0*
%{_libdir}/libMateCORBA-imodule-2.so.0*
%{_libdir}/libMateCORBACosNaming-2.so.0*
%{_libdir}/matecorba-2.0/

%files devel
%{_bindir}/matecorba2-config
%{_libdir}/libMateCORBA-2.so
%{_libdir}/libMateCORBACosNaming-2.so
%{_libdir}/libMateCORBA-imodule-2.so
%{_includedir}/matecorba-2.0/
%{_libdir}/libname-matecorba-server-2.a
%{_libdir}/pkgconfig/MateCORBA*-2.0.pc
%{_bindir}/matecorba-idl-2
%{_bindir}/matecorba-typelib-dump
%{_bindir}/matecorba-ior-decode-2
%{_datadir}/aclocal/MateCORBA2.m4
%{_datadir}/idl/matecorba-2.0/
%{_bindir}/matecorba-linc-cleanup-sockets
%{_datadir}/gtk-doc/

%changelog
* Thu Nov 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_10
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_1
- converted by srpmconvert script

