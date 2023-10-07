Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:      freexl
Version:   2.0.0
Release:   alt1
Summary:   Library to extract data from within an Excel spreadsheet 
License:   MPLv1.1 or GPLv2+ or LGPLv2+
URL:       https://www.gaia-gis.it/fossil/freexl
Source0:   http://www.gaia-gis.it/gaia-sins/%{name}-sources/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: doxygen libminizip-devel libminizip-devel libexpat-devel
Source44: import.info
Patch33: freexl-1.0.0d-alt-linkage.patch

%description
FreeXL is a library to extract valid data
from within an Excel spreadsheet (.xls)

Design goals:
    * simple and lightweight
    * stable, robust and efficient
    * easily and universally portable
    * completely ignore any GUI-related oddity

%package devel
Group: Development/Other
Summary:  Development Libraries for FreeXL
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch33 -p1


%build
autoreconf -fisv
%configure --enable-gcov=no --disable-static
%make_build

# Mailed the author on Dec 5th 2011
# Preserve date of header file
sed -i 's/^INSTALL_HEADER = \$(INSTALL_DATA)/& -p/' headers/Makefile.in

# Generate HTML documentation and clean unused installdox script
doxygen
rm -f html/installdox


%check
make check

# Clean up
pushd examples
  make clean
popd


%install
make install DESTDIR=%{buildroot}

# Delete undesired libtool archives
rm -f %{buildroot}%{_libdir}/lib%{name}.la





%files 
%doc COPYING AUTHORS README
%{_libdir}/lib%{name}.so.*

%files devel
%doc examples html
%{_includedir}/freexl.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/freexl.pc


%changelog
* Sat Oct 07 2023 Ilya Mashkin <oddity@altlinux.ru> 2.0.0-alt1
- 2.0.0
- Update Url

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt1_1
- update to new release by fcimport

* Thu Aug 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_4
- fixed self-BR (thanks to rider@)

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_1
- update to new release by fcimport

* Fri Nov 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_1
- update to new version by fcimport

* Sat Jul 25 2015 Ilya Mashkin <oddity@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Mar 26 2015 Ilya Mashkin <oddity@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Tue Mar 10 2015 Ilya Mashkin <oddity@altlinux.ru> 1.0.0i-alt1
- 1.0.0i

* Thu Feb 27 2014 Ilya Mashkin <oddity@altlinux.ru> 1.0.0g-alt1
- 1.0.0g

* Tue Jan 29 2013 Ilya Mashkin <oddity@altlinux.ru> 1.0.0d-alt2
- build for Sisyphus

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0d-alt1_2
- initial fc import

