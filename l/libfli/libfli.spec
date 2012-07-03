# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/bison /usr/bin/docbook-to-man /usr/bin/docbook2html /usr/bin/doxygen /usr/bin/gtkdocize /usr/bin/guile /usr/bin/guile-config /usr/bin/indent /usr/bin/pkg-config /usr/bin/valgrind cppunit-devel gcc-c++ gcc-fortran glib2-devel guile18-devel imlib2-devel libGL-devel libX11-devel libXext-devel libaccounts-glib-devel libexpat-devel libflac-devel libfreetype-devel liboggz-devel libreadline-devel libspeex-devel libuuid-devel libvorbis-devel pkgconfig(dbus-1) pkgconfig(freetype2) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) python-devel unzip zlib-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name: libfli
Version: 1.7
Release: alt2_8
Summary: Library for FLI CCD Camera & Filter Wheels

%define majorver 1

Group: Development/C
# Code and LICENSE.LIB have different versions of the BSD license
# https://sourceforge.net/tracker2/?func=detail&aid=2568511&group_id=90275&atid=593019
License: BSD
URL: http://indi.sourceforge.net/index.php

Source0: http://downloads.sourceforge.net/indi/%{name}%{majorver}_%{version}.tar.gz
Patch0: libfli-suffix.patch

BuildRequires: ctest cmake
Source44: import.info
Patch33: libfli1_1.7-alt-link-libm.patch

%description
Finger Lakes Instrument library is used by applications to control FLI 
line of CCDs and Filter wheels

%package devel
Summary: Libraries, includes, etc. used to develop an application with %{name}
Group: Development/C
Requires: %{name} = %{version}-%{release}
%description devel
These are the header files needed to develop a %{name} application

%prep
%setup -q -n %{name}%{majorver}-%{version}
%patch0 -p1
%patch33 -p1

%build
%{fedora_cmake}
make VERBOSE=1 %{?_smp_mflags}

%install
rm -fr %{buildroot}
make install DESTDIR=%{buildroot}

%files
%doc LICENSE.BSD
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_8
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_7
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_7
- initial import by fcimport

