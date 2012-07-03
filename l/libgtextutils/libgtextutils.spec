# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libgtextutils
Version:	0.6
Release:	alt2_7
Summary:	Assaf Gordon text utilities    

Group:		System/Libraries
License:	AGPLv3+
URL:		http://hannonlab.cshl.edu/fastx_toolkit/
Source0:	http://hannonlab.cshl.edu/fastx_toolkit/%{name}-%{version}.tar.bz2
Source44: import.info


%description
Text utilities library used by the fastx_toolkit, from the Hannon Lab

%package       devel
Summary:       Development files for %{name}
Group:	       Development/C
Requires:      libgtextutils = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
#fix for unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc AUTHORS COPYING README THANKS NEWS
%{_libdir}/libgtextutils-*.so.*


%files devel
%{_includedir}/gtextutils
%{_libdir}/libgtextutils*.so
%{_libdir}/pkgconfig/gtextutils.pc

%changelog
* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_7
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_6
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_5
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_5
- initial import by fcimport

