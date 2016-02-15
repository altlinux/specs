# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen libncurses-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name libnjb
%define version 2.2.7
# SPEC file for libnjb, primary target is the Fedora Extras
# RPM repository.

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		libnjb
Version:	2.2.7
Release:	alt3_12
Summary:	A software library for talking to the Creative Nomad Jukeboxes and Dell DJs
URL:		http://libnjb.sourceforge.net/

Group:		System/Libraries
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
License:	BSD
BuildRequires: libusb-compat-devel libusb-devel
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
BuildRequires:	doxygen
BuildRequires:	systemd
Source44: import.info

%description
This package provides a software library for communicating with the
Creative Nomad Jukebox line of MP3 players.

%package examples
Summary:        Example programs for libnjb
Group:          Sound
Requires:       %{name} = %{version}

%description examples
This package provides example programs for communicating with the
Creative Nomad Jukebox and Dell DJ line of MP3 players.

%package devel
Summary:        Development files for libnjb
Group:          System/Libraries
Requires:       %{name} = %{version}
# doc subpackage removed in newer releases, and included
# in the -devel package.
Provides:	libnjb-doc
Obsoletes:	libnjb-doc <= 2.2-1

%description devel
This package provides development files for the libnjb
library for Creative Nomad/Zen/Jukebox and Dell DJ line of MP3 players.

%prep
%setup -q

%build
%configure --disable-static --program-prefix=njb-
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT pkgdocdir=%{_docdir}/%{name}
# Remove libtool archive remnant
rm -f $RPM_BUILD_ROOT%{_libdir}/libnjb.la
# Install udev rules file.
install -p -D -m0644 libnjb.rules $RPM_BUILD_ROOT%{_udevrulesdir}/60-libnjb.rules
# Copy documentation to a good place
install -p -m 644 AUTHORS ChangeLog ChangeLog-old FAQ \
        INSTALL HACKING $RPM_BUILD_ROOT%{_docdir}/%{name}
# Touch generated files to make them always have the same time stamp.
touch -r configure.ac \
      $RPM_BUILD_ROOT%{_docdir}/%{name}/html/* \
      $RPM_BUILD_ROOT%{_includedir}/*.h \
      $RPM_BUILD_ROOT%{_libdir}/pkgconfig/*.pc
# Remove the Doxygen HTML documentation, this get different
# each time it is generated and thus creates multiarch conflicts.
# I don't want to pre-generate it but will instead wait for upstream
# to find a suitable solution that will always bring the same files,
# or that Doxygen is fixed not to do this.
#rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html

%files
%doc LICENSE
%{_libdir}/*.so.*
%{_udevrulesdir}/*

%files examples
%{_bindir}/*

%files devel
%{_libdir}/*.so
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt3_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt3_11
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt3_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt3_5
- update to new release by fcimport

* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 2.2.7-alt3_4.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * udev-files-in-etc for libnjb

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt3_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt3_3
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt3_2
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt2_1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_1
- initial import by fcimport

