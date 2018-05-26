# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# define these if using CVS version
%global cvs_date 2007.04.28
%global cvs_ver +cvs.%cvs_date

Name:           zipios++
Version:        0.1.5.9
Release:        alt2_20
License:        LGPLv2+
Summary:        C++ library for reading and writing Zip files
Summary(pl.UTF-8): Biblioteka C++ do odczytu i zapisu plików Zip
Group:          System/Libraries
URL:            http://zipios.sourceforge.net/
# Upstream is dead. Using updated Debian source as they are fixing FTBFS issues.
Source0:        ftp://ftp.debian.org/debian/pool/main/z/%{name}/%{name}_%{version}%{cvs_ver}.orig.tar.gz

# Patches extracted from debian diff
# ftp://ftp.debian.org/debian/pool/main/z/zipios++
Patch0:         zipios++-cstdlib.patch
Patch1:         zipios++-amd64_fix.patch
Patch2:         zipios++-fc16-ptrdiff_t.patch
Patch3:         zipios++-zipinputstreambuff.patch
Patch4:         0001-cppunit-config-no-longer-exists-use-pkg-config.patch
Patch10:        zipios++-zipheadio-size0.patch


BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  graphviz libgraphviz
BuildRequires:  ImageMagick-tools
BuildRequires:  doxygen
Source44: import.info


%description
Zipios++ is a java.util.zip-like C++ library for reading and writing
Zip files. Access to individual entries is provided through standard
C++ iostreams. A simple read-only virtual file system that mounts
regular directories and zip files is also provided.

%description -l pl.UTF-8
Zipios++ jest jak java.util.zip biblioteką C++ do odczytywania oraz
zapisywania plików Zip. Dostęp do pojedyńczych wpisów jest możliwy
poprzez standardowe strumienie we/wy C++. Prosty wirtualny system
plików (tylko do odczytu) montujący regularne katalogi oraz pliki zip
również jest dostarczany.


%package devel
Summary:        Header files for zipios++
Summary(pl.UTF-8): Pliki nagłówkowe zipios++
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description devel
The header files are only needed for development of programs using the
zipios++.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe, przeznaczone dla
programistów używających bibliotek zipios++.


%prep
%setup -q -n %{name}-%{version}%{cvs_ver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch10 -p1

chmod 0644 COPYING


%build
autoreconf -if
%configure
%make_build
make V=1 doc


%install
%makeinstall_std

# Remove static libs
rm -f %{buildroot}%{_libdir}/*.{a,la}





%files
%doc AUTHORS NEWS README
%doc --no-dereference COPYING
%{_libdir}/*.so.*

%files devel
%doc doc/html
%{_libdir}/*.so
%{_includedir}/zipios++


%changelog
* Sat May 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.5.9-alt2_20
- fc update

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.5.9-alt2_5
- moved to Sisyphus for enigma

* Mon Oct 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.5.9-alt1_18
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.5.9-alt1_16
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.5.9-alt1_15
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.1.5.9-alt1_14
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.5.9-alt1_12
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.5.9-alt1_11
- update to new release by fcimport

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.5.9-alt1_10
- update to new release by fcimport

* Thu Mar 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.5.9-alt1_9
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.5.9-alt1_8
- update to new release by fcimport

* Tue May 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.5.9-alt1_6
generated with R::S::Convert 0.46

