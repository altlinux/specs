# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen libncurses-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
# SPEC file for libnjb, primary target is the Fedora Extras
# RPM repository.

Name:		libnjb
Version:	2.2.7
Release:	alt3_2
Summary:	A software library for talking to the Creative Nomad Jukeboxes and Dell DJs
URL:		http://libnjb.sourceforge.net/

Group:		System/Libraries
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
License:	BSD
Requires:	udev
BuildRequires:	libusb-compat-devel libusb-devel
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
BuildRequires:	doxygen
Source44: import.info

%description
This package provides a software library for communicating with the
Creative Nomad Jukebox line of MP3 players.

%package examples
Summary:        Example programs for libnjb
Group:          Sound
Requires:       libnjb = %{version}-%{release}

%description examples
This package provides example programs for communicating with the
Creative Nomad Jukebox and Dell DJ line of MP3 players.

%package devel
Summary:        Development files for libnjb
Group:          System/Libraries
Requires:       libnjb = %{version}-%{release}
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
%makeinstall
# Remove libtool archive remnant
rm -f $RPM_BUILD_ROOT%{_libdir}/libnjb.la
# Install udev rules file.
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d
install -p -m 644 libnjb.rules $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/60-libnjb.rules
# Copy documentation to a good place
install -p -m 644 AUTHORS ChangeLog ChangeLog-old FAQ \
INSTALL LICENSE HACKING $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
# Touch generated files to make them always have the same time stamp.
touch -r configure.ac \
      $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html/* \
      $RPM_BUILD_ROOT%{_includedir}/*.h \
      $RPM_BUILD_ROOT%{_libdir}/pkgconfig/*.pc
# Remove the Doxygen HTML documentation, this get different
# each time it is generated and thus creates multiarch conflicts.
# I don't want to pre-generate it but will instead wait for upstream
# to find a suitable solution that will always bring the same files,
# or that Doxygen is fixed not to do this.
#rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html

%files
%{_libdir}/*.so.*
%config(noreplace) %{_sysconfdir}/udev/rules.d/*
%files examples
%{_bindir}/*

%files devel
%{_libdir}/*.so
%dir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/*
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}


%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt3_2
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt2_1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_1
- initial import by fcimport

