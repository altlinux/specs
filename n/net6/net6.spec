# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define api    1.3
%define major  0
%define libname libnet6-%{api}_%{major}
%define libname_devel libnet6-%{api}-devel

Summary:    A library to ease the development of network-based applications
Name:       net6
Version:    1.3.14
Release:    alt2_11
URL:        http://gobby.0x539.de/
License:    GPLv2+
Source0:    http://releases.0x539.de/%{name}/%{name}-%{version}.tar.gz
Patch0:	    net6-1.3.14-drop-deprecated-gnutls-call.patch
Group:      System/Libraries
BuildRequires: pkgconfig(sigc++-2.0)
BuildRequires: pkgconfig(gnutls)
BuildRequires: gettext-tools libasprintf-devel
Source44: import.info
Conflicts: libnet6 < 1.4.3-alt1_3

%description
net6 is a library which eases the development of network-based applications
as it provides a TCP protocol abstraction for C++. It is portable to both
the Windows and Unix-like platforms.

%package -n %libname
Summary:    A library to ease the development of network-based applications
Group:      System/Libraries
Requires:   %{name} >= %{version}
Obsoletes:  libnet6_1.3
Conflicts: libnet6 < 1.4.3-alt1_3
Obsoletes: libnet6 < 1.4.3-alt1_3

%description -n %libname
net6 is a library which eases the development of network-based applications
as it provides a TCP protocol abstraction for C++. It is portable to both
the Windows and Unix-like platforms.

%package -n %libname_devel
Summary:    Development files for %libname
Group:      System/Libraries
Provides:   lib%{name}-devel = %version-%release
Obsoletes:  libnet6_1.3-devel
Requires:   %libname = %version

%description -n %libname_devel
Development files, header and includes for %libname.

net6 is a library which eases the development of network-based applications
as it provides a TCP protocol abstraction for C++. It is portable to both
the Windows and Unix-like platforms.

%prep
%setup -q
%patch0 -p1


# make autoreconf more happy
sed -i -e 's,^\(AM_INIT_AUTOMAKE\)(\(.*\)).*,\1(\[\2 subdir-objects\]),' configure.ac

%build
# fix build on aarch64
autoreconf -vfi

%configure --disable-static
%make_build

%install
%makeinstall_std

rm -f %buildroot%_libdir/*.la

%find_lang %name

%files -f %name.lang

%files -n %libname
%doc ChangeLog README NEWS AUTHORS
%_libdir/*%{api}.so.%{major}*

%files -n %libname_devel
%_includedir/%name/
%_libdir/*.so
%_libdir/pkgconfig/*


%changelog
* Fri Oct 27 2023 Igor Vlasenko <viy@altlinux.org> 1.3.14-alt2_11
- mageia re-import
- switched to shared libs policy

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_12
- update to new release by fcimport

* Sun Nov 08 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_11
- new version

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_8
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_5
- update to new release by fcimport

* Sat Apr 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_4
- initial fc import

