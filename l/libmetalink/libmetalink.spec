# BEGIN SourceDeps(oneline):
BuildRequires: CUnit-devel libxml2-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libmetalink
Version:        0.0.3
Release:        alt3_7
Summary:        A Metalink C library
Group:          System/Libraries
License:        MIT
URL:            https://launchpad.net/libmetalink
Source0:        http://launchpad.net/libmetalink/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
BuildRequires:  libexpat-devel
Source44: import.info

%description
libmetalink is a Metalink C library. It adds Metalink functionality such as
parsing Metalink XML files to programs written in C.

%package       devel
Summary:       A Metalink C library devel package
Group:         Development/C
Requires:      %{name} = %{version}-%{release}

%description   devel
Files needed for building applications with libmetalink.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name *.la -exec rm {} \;

%files
%doc COPYING README 
%doc %{_docdir}/libmetalink/sample.c 
%doc %{_docdir}/libmetalink/ubuntu-7_10-server-i386_iso.metalink
%{_libdir}/libmetalink.so.*
%{_mandir}/man3/*


%files devel
%{_includedir}/metalink/
%{_includedir}/metalink/metalink*.h
%{_libdir}/libmetalink.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Wed Jun 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt3_7
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt2_7
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt2_6
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1_6
- initial import by fcimport

