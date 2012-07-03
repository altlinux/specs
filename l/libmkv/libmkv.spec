%add_optflags %optflags_shared
Name:      libmkv
Version:   0.6.5.1
Release:   alt2_1
Summary:   An alternative to the official libmatroska library

Group:     System/Libraries
License:   GPLv2+
URL:       https://github.com/saintdev/libmkv
# https://github.com/saintdev/libmkv/tarball/0.6.5.1
Source0:   %{name}-%{version}.tar.gz

BuildRequires: autoconf automake libtool
Source44: import.info

%description
This library is meant to be an alternative to the official libmatroska library.
It is writen in plain C, and is intended to be very portable.

%prep
%setup -q -n saintdev-libmkv-d2906c0


%build
# bug in autotools requires missing m4 directory
mkdir m4
autoreconf --verbose --force --install
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%{_libdir}/libmkv.so.*
%doc AUTHORS COPYING README

%package devel
Summary:   An alternative to the official libmatroska library - devel files
Group:     Development/C
Requires:  libmkv = %{version}-%{release}

%description devel
This library is meant to be an alternative to the official libmatroska library.
It is writen in plain C, and is intended to be very portable.  These are the
development files.

%files devel
%{_includedir}/libmkv.h
%{_libdir}/libmkv.so

%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.5.1-alt2_1
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.5.1-alt1_1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.4.1-alt2_1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.4.1-alt1_1
- initial import by fcimport

