# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(x11)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libXcm
Version:        0.5.0
Release:        alt1_2
Summary:        X Color Management Library

Group:          System/Libraries
License:        MIT
URL:            http://www.oyranos.org
Source0:        http://downloads.sourceforge.net/oyranos/libXcm-%{version}.tar.bz2

BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libXfixes-devel
BuildRequires:  libXmu-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-xtrans-devel
Source44: import.info


%description
The libXcm library is a reference implementation of the net-color spec.
It allows to attach color regions to X windows to communicate with color
servers.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       libXcm = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
CFLAGS="$RPM_OPT_FLAGS -fPIC"

%configure --disable-static --enable-shared
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.*

%files devel
%doc docs/*.txt
%dir %{_includedir}/X11/Xcm
%{_includedir}/X11/Xcm/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/xcm.pc
%{_mandir}/man3/*.3.*


%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_2
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_1
- initial import by fcimport

