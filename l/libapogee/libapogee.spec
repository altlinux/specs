# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/gtkdocize gcc-c++ libaccounts-glib-devel pkgconfig(dbus-1) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) unzip
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name: libapogee
Version: 2.2
Release: alt2_7
Summary: Library for Apogee CCD Cameras

%define majorver 2

Group: Development/C
License: GPLv2+
URL: http://indi.sourceforge.net/index.php

Source0: http://downloads.sourceforge.net/indi/%{name}%{majorver}_%{version}.tar.gz
Patch0: libapogee-suffix.patch
# Patch to build in ppc ppc64
#https://sourceforge.net/tracker2/?func=detail&aid=2215787&group_id=90275&atid=593019
Patch1: libapogee-sysio.patch

# Bug upstream about libapogee calling exit()
# https://sourceforge.net/tracker2/?func=detail&aid=2595732&group_id=90275&atid=593019

# Since curl 7.21.7, curl/types.h has been removed
BuildRequires: ctest cmake libusb-compat-devel libusb-devel libcurl-devel
Source44: import.info

%description
Apogee library is used by applications to control Apogee CCDs.

%package devel
Summary: Libraries, includes, etc. used to develop an application with %{name}
Group: Development/C
Requires: %{name} = %{version}-%{release}
%description devel
These are the header files needed to develop a %{name} application

%prep
%setup -q -n %{name}%{majorver}-%{version}
%patch0 -p1
%patch1 -p1
# curl/types.h is deprecated
# upstream bug https://sourceforge.net/tracker/?func=detail&aid=3462419&group_id=90275&atid=593019
sed -i '/include.*[<"]curl\/types.h[">]/d' \
`egrep -rl 'include.*["<]curl/types.h[">]' .`

%build
%{fedora_cmake}
make VERBOSE=1 %{?_smp_mflags}

%install
rm -fr %{buildroot}
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS ChangeLog README LICENSE
%{_libdir}/*.so.*

%files devel
%doc LICENSE
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_7
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_6
- spec cleanup thanks to ldv@

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_6
- update to new release by fcimport

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_5
- initial import by fcimport

