Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 3

%bcond_without autoreconf

Name:           readosm
Version:        1.1.0a
%global so_version 1
Release:        alt1_3
Summary:        Library to extract valid data from within an Open Street Map input file

License:        MPLv1.1 or GPLv2+ or LGPLv2+
Source0:        https://www.gaia-gis.it/gaia-sins/readosm-sources/readosm-%{version}.tar.gz
URL:            https://www.gaia-gis.it/fossil/readosm

%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

BuildRequires:  gcc

BuildRequires:  libexpat-devel
BuildRequires:  zlib-devel
Source44: import.info

%description
ReadOSM is a simple library intended for extracting the contents from 
Open Street Map files: both input formats (.osm XML based and .osm.pbf based
on Google's Protocol Buffer serialization) are indifferently supported.

%package devel
Group: Development/Other
Summary:        Development libraries and headers for ReadOSM

Requires:       readosm = %{version}-%{release}

%description devel
The readosm-devel package contains libraries and header files for
developing applications that use ReadOSM.


%prep
%setup -q



%build
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif
%configure --disable-static
%make_build


%install
%makeinstall_std
# Delete undesired libtool archives
find '%{buildroot}' -type f -name '*.la' -print -delete


%check
%make_build check


%files
%doc --no-dereference COPYING
%doc AUTHORS

%{_libdir}/libreadosm.so.%{so_version}
%{_libdir}/libreadosm.so.%{so_version}.*


%files devel
%{_libdir}/pkgconfig/readosm.pc
%{_libdir}/libreadosm.so
%{_includedir}/readosm.h


%changelog
* Wed Feb 09 2022 Igor Vlasenko <viy@altlinux.org> 1.1.0a-alt1_3
- update to new release by fcimport

* Sat Dec 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_5
- fixed self-br in import code

* Thu Jun 20 2019 Michael Shigorin <mike@altlinux.org> 1.1.0-alt2_1
- avoid self-BR

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1
- NMU (for oddity@): new version by fcimport

* Sat Jul 25 2015 Ilya Mashkin <oddity@altlinux.ru> 1.0.0e-alt1
- 1.0.0e

* Tue Mar 10 2015 Ilya Mashkin <oddity@altlinux.ru> 1.0.0d-alt1
- 1.0.0d

* Thu Jan 31 2013 Ilya Mashkin <oddity@altlinux.ru> 1.0.0b-alt1
- Build for Sisyphus

* Sun Dec  2 2012 Volker Frohlich <volker27@gmx.at> - 1.0.0b-1
- New upstream release

* Sun Aug 12 2012 Volker Frohlich <volker27@gmx.at> - 1.0.0a-2
- Disable coverage profiling

* Sun Aug 12 2012 Volker Frohlich <volker27@gmx.at> - 1.0.0a-1
- Inital package for Fedora
