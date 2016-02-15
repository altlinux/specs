# BEGIN SourceDeps(oneline):
BuildRequires: libsocket pkgconfig(dbus-1) pkgconfig(dbus-glib-1)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define fedora 23
Name:           libsynce
Version:        0.15.1
Release:        alt2_10
Summary:        Connection library for Pocket PC devices

Group:          System/Libraries
License:        MIT
URL:            http://www.synce.org
Source0:        http://download.sf.net/synce/libsynce-%{version}.tar.gz

BuildRequires:  libdbus-glib-devel
BuildRequires:  libudev-devel
%if 0%{?fedora} < 16
BuildRequires:  hal-devel
%endif

# Provide an upgrade path from the monilithic synce package
Provides:       synce = %{version}-%{release}
Obsoletes:      synce <= 0.9.1-10
Source44: import.info

%description
The purpose of the SynCE project is to provide a means of
communication with a Windows CE device from a computer running Linux,
FreeBSD or a similar operating system.

%package devel
Summary: Development libraries and header files for SynCE
Group: Development/C
Requires: %{name} = %{version}
Requires: pkgconfig

%description devel
This package contains the header files and link libraries for SynCE
application development. SynCE provides support for communication
between a Windows CE device (PDA, smart phone) and a Linux machine.

For more details on the SynCE project, please refer to the project's
homepage at http://www.synce.org

%prep
%setup -q 

%build
%configure \
--disable-static --disable-rpath \
%if 0%{?fedora} >= 16
--disable-hal-support \
%endif
--enable-udev-support

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%files
%doc README TODO ChangeLog
%{_libdir}/libsynce.so.0*
%{_mandir}/man7/synce.*

%files devel
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_mandir}/man3/*
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.15.1-alt2_10
- update to new release by fcimport

* Tue Nov 17 2015 Igor Vlasenko <viy@altlinux.ru> 0.15.1-alt2_9
- rebuild

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.15.1-alt2
- resurrected

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.1-alt1
- 0.15.1
- build withouth hal support
- disable versioning

* Tue Nov 23 2010 Denis Smirnov <mithraen@altlinux.ru> 0.15-alt1.1
- rebuild (with the help of girar-nmu utility)

* Mon May 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt1
- 0.15

* Fri Aug 21 2009 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt1
- 0.14
- add versioning

* Sun Mar 01 2009 Alexey Shabalin <shaba@altlinux.ru> 0.13-alt1
- 0.13
- removed pre/post scripts

* Sat Oct 04 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12-alt1
- 0.12

* Mon Jun 30 2008 Grigory Milev <week@altlinux.ru> 0.11.1-alt2
- add devel static package
- fix Sisyphus requires

* Thu Apr 17 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11.1-alt1
- 0.11.1
- update buildreq

* Thu Jan 31 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11-alt2
- add %%post and %%postun spec sections

* Wed Jan 09 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11-alt1
- 0.11

* Thu Jan 03 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt3
- update to SVN 20080102 version

* Fri Dec 07 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt2
- update to SVN 20071207 version

* Mon May 14 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Fri Jan 12 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Sun Jul 24 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt1
- 0.9.1
- spec clean-up (gcc3.2 dependency removed)

* Wed Sep 01 2004 Michael Shigorin <mike@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Sun Apr 25 2004 Michael Shigorin <mike@altlinux.ru> 0.8.9-alt1
- 0.8.9
- using gcc3.2 for now (can't patch "type punning" in trivial way)

* Fri Nov 28 2003 Michael Shigorin <mike@altlinux.ru> 0.8.1-alt2
- removed *.la and devel-static subpackage

* Fri Nov 07 2003 Michael Shigorin <mike@altlinux.ru> 0.8.1-alt1
- built for ALT Linux

