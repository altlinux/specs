# BEGIN SourceDeps(oneline):
BuildRequires: bzlib-devel gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname atlascpp
Name:           libatlascpp
Version:        0.6.2
Release:        alt1_3
Summary:        WorldForge message protocol library

Group:          Development/C++
License:        LGPLv2+
URL:            http://worldforge.org/dev/eng/libraries/atlas_cpp
Source0:        http://downloads.sourceforge.net/sourceforge/worldforge/Atlas-C++-%{version}.tar.bz2
Patch1:         atlascpp-0.6.1-gcc44.patch
Patch2:         atlascpp-0.6.2-Werror.patch

BuildRequires:  doxygen zlib-devel bzip2-devel
# Provide the other name that this package is commonly known by
Provides:       Atlas-C++
Source44: import.info
Provides: atlascpp = %{version}-%{release}


%description
Atlas-C++ is the perhaps the most important library in the entire WorldForge
project, since nearly every other module requires it. Atlas-C++ provides a
native implementation of the entire Atlas specification including negotiation,
message encode and decode and the overlying Objects layer.


%package devel
Summary:        Development files for Atlas-C++
Group:   Development/C++
Requires: libatlascpp = %{version}-%{release}
Provides: atlascpp-devel = %{version}-%{release}
# Atlas-C++ includes simple tutorial that uses skstream


%description devel
Libraries and header files for developing applications that use Atlas-C++

%prep
%setup -q -n Atlas-C++-%{version}
%patch1 -p1
%patch2 -p0


%build
%configure

# simple hack to remove -Werror from the test suite, which causes
# it to fail.
sed -i -e 's#-Werror##' benchmark/Makefile
sed -i -e 's#-Werror##' tests/Objects/Makefile

make %{?_smp_mflags}
make docs


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libAtlas*-0.6.la

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3
install -p -m 0644 doc/man/man3/Atlas*.3 $RPM_BUILD_ROOT%{_mandir}/man3/

%check
# Run tests in debug mode so asserts won't be skipped
sed -i -e 's/-DNDEBUG/-DDEBUG/' tests/Makefile
make %{?_smp_mflags} check


%files
%doc AUTHORS COPYING ChangeLog README ROADMAP THANKS TODO
%{_libdir}/libAtlas*-0.6.so.*


%files devel
%doc HACKING doc/html/
%{_bindir}/atlas_convert
%{_includedir}/Atlas-C++-0.6
%{_libdir}/libAtlas*-0.6.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/Atlas*

%changelog
* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1_3
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1_2
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1_1
- initial release by fcimport

