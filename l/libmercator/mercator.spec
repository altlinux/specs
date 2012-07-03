# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(wfmath-0.3)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname mercator
Name:           libmercator
Version:        0.3.0
Release:        alt2_5
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
Requires: mercator = %{version}-%{release}
Provides: mercator-devel = %{version}-%{release}


%description devel
Development libraries and headers for linking against the mercator library.


%prep
%setup -q -n %{oldname}-%{version}


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
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2_5
- update to new release by fcimport

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2_2
- rebuild with new libwfmath

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_2
- initial release by fcimport

