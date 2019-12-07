Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           readosm
Version:        1.1.0
Release:        alt2_5
Summary:        Library to extract data from Open Streetmap input files

License:        MPLv1.1 or GPLv2+ or LGPLv2+
Source0:        http://www.gaia-gis.it/gaia-sins/%{name}-%{version}.tar.gz
URL:            https://www.gaia-gis.it/fossil/readosm

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
Summary:  Development libraries and headers for %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static

%make_build


%install
make install DESTDIR=%{buildroot}

# Delete undesired libtool archives
rm -f %{buildroot}%{_libdir}/lib%{name}.la


%check
make check





%files
%doc AUTHORS COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h

%changelog
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
