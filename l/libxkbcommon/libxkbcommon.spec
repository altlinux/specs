%global gitdate  20120306

Name:           libxkbcommon
Version:        0.1.0
Release:        alt2_6.20120306
Summary:        X.Org X11 XKB parsing library
License:        MIT
Group:          System/Libraries
URL:            http://www.x.org

%if 0%{?gitdate}
Source0:       %{name}-%{gitdate}.tar.bz2
%else
Source0:        ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%endif
Source1:        make-git-snapshot.sh

BuildRequires:  autoconf automake libtool
BuildRequires:  xorg-util-macros bison flex bison
BuildRequires:  xorg-x11-proto-devel libX11-devel
BuildRequires:  xkeyboard-config-devel
Source44: import.info

%description
%{name} is the X.Org library for compiling XKB maps into formats usable by
the X Server or other display servers.

%package devel
Summary:        X.Org X11 XKB parsing development package
Group:          Development/C
Requires:       libxkbcommon = %{version}-%{release}

%description devel
X.Org X11 XKB parsing development package

%prep
%setup -q -n %{name}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install || exit 1
%configure --disable-static

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/libxkbcommon.so.0.0.0
%{_libdir}/libxkbcommon.so.0

%files devel
%{_libdir}/libxkbcommon.so
%{_includedir}/xkbcommon/xkbcommon.h
%{_libdir}/pkgconfig/xkbcommon.pc

%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_6.20120306
- update to new version

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_4.20111109
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_3.20111109
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_3.20111109
- initial import by fcimport

