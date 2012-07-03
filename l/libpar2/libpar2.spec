# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name: libpar2
Version: 0.2       
Release: alt2_12
Summary: Library for performing comman tasks related to PAR recovery sets
     
Group: System/Libraries
License: GPLv2+        
URL: http://parchive.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/sourceforge/parchive/%{name}-%{version}.tar.gz
  
BuildRequires: libsigc++2-devel
BuildRequires: sed
Source44: import.info

%description
LibPar2 allows for the generation, modification, verification,
and repair of PAR v1.0 and PAR v2.0(PAR2) recovery sets.
It contains the basic functions needed for working with these
sets and is the basis for GUI applications such as GPar2.


%package devel
Summary: Development files for %{name}
Group: Development/C
Requires: libpar2 = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
#fix source files
chmod -x *.cpp *.h ChangeLog
touch tmpfile -r README 
sed -i 's/\r//' README
touch -r tmpfile README
touch tmpfile -r ROADMAP 
sed -i 's/\r//' ROADMAP
touch -r tmpfile ROADMAP
touch tmpfile -r AUTHORS
sed -i 's/\r//' AUTHORS
touch -r tmpfile AUTHORS

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%{_libdir}/*.so.*
%doc COPYING README ChangeLog AUTHORS ROADMAP

%files devel
%{_includedir}/*
%{_libdir}/*.so
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/include/

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_12
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_11
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_10
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_10
- initial import by fcimport

