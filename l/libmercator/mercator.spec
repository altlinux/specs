# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(wfmath-1.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname mercator
Name:           libmercator
Version:        0.3.3
Release:        alt1_7
Summary:        Terrain library for WorldForge client/server

Group:          Development/C++
License:        GPL+
URL:            http://worldforge.org/dev/eng/libraries/mercator
Source0:        http://downloads.sourceforge.net/worldforge/%{oldname}-%{version}.tar.bz2

BuildRequires:  wfmath-devel >= 0.3.2
BuildRequires:  doxygen
Source44: import.info
Provides: mercator = %{version}-%{release}

%description
Mercator is primarily aimed at terrain for multiplayer online games and forms
one of the WorldForge core libraries. It is intended to be used as a terrain
library on the client, while a subset of features are useful on the server.


%package devel
Summary: Development files for mercator library
Group:   Development/C++
Requires: %{name} = %{version} pkgconfig
Provides: mercator-devel = %{version}-%{release}


%description devel
Development libraries and headers for linking against the mercator library.


%prep
%setup -n %{oldname}-%{version} -q


%build
%configure
make %{?_smp_mflags}
make docs

# Remove timestamps from the generated documentation to avoid
# multiarch conflicts

for file in doc/html/*.html ; do
    sed -i -e 's/Generated on .* for Mercator by/Generated for Mercator by/' $file
done

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{oldname}-*.la

%check
# Run tests in debug mode so asserts won't be skipped
sed -i -e 's/-DNDEBUG/-DDEBUG/' tests/Makefile
make %{?_smp_mflags} check

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_libdir}/lib%{oldname}-*.so.*


%files devel
%doc doc/html/*
%{_includedir}/Mercator-*
%{_libdir}/lib%{oldname}-*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt1_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt1_6
- update to new release by fcimport

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.3-alt1_4.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt1_4
- update to new release by fcimport

* Thu Sep 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1
- Version 0.3.3

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_2
- update to new release by fcimport

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_1
- new release

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2_6
- update to new release by fcimport

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2_5
- update to new release by fcimport

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2_2
- rebuild with new libwfmath

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_2
- initial release by fcimport

