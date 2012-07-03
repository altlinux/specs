%add_optflags %optflags_shared
Name:           libuninameslist
Version:        20091231
Release:        alt3_3

Summary:        A library providing Unicode character names and annotations

Group:          System/Libraries
License:        BSD
URL:            http://libuninameslist.sourceforge.net
Source0:        http://downloads.sourceforge.net/libuninameslist/libuninameslist-%{version}.tar.bz2
Source44: import.info

%description
libuninameslist provides applications with access to Unicode name and
annotation data from the official Unicode Character Database.

%package        devel
Summary:        Header files and static libraries for %{name}
Group:          Development/C
Requires:       libuninameslist = %{version}-%{release}

%description    devel
This package contains header files and static libraries for %{name}.


%prep
%setup -q -n libuninameslist


%build
%configure --disable-static
make %{?_smp_mflags}


%install
%makeinstall incdir=$RPM_BUILD_ROOT%{_includedir}
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%files
%doc LICENSE
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/*


%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 20091231-alt3_3
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 20091231-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 20091231-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 20091231-alt1_2
- initial import by fcimport

