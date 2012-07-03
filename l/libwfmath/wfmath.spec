# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(atlascpp-0.6)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname wfmath
Name:           libwfmath
Version:        0.3.12
Release:        alt2_1
Summary:        WorldForge client math libraries

Group:          Development/C++
License:        GPLv2+
URL:            http://worldforge.org/dev/eng/libraries/wfmath
Source0:        http://downloads.sourceforge.net/sourceforge/worldforge/%{oldname}-%{version}.tar.bz2

BuildRequires:  doxygen
Source44: import.info
Provides: wfmath = %{version}-%{release}

%description
WFMath provides mathematical functions for WorldForge clients.  The primary
focus of WFMath is geometric objects. Thus, it includes several shapes (boxes,
balls, lines), in addition to the basic math objects that are used to build
these shapes (points, vectors, matrices). WFMath provides a means for other
system compenents to pass geometric information around in a common format.


%package        devel
Summary:        Development files for wfmath
Group:          Development/C++
Requires:       libwfmath = %{version}-%{release}
Provides: wfmath-devel = %{version}-%{release}


%description    devel
Libraries and header files for developing applications that use wfmath.


%prep
%setup -q -n %{oldname}-%{version}


%build
# tests fail when build with -O2 on these arches
%ifarch s390 s390x
CXXFLAGS="%{optflags} -O0" \
%endif
%configure --disable-static
make %{?_smp_mflags}

make docs
# Rename a messed-up man page
mv doc/man/man3/WFMath_Polygon_* doc/man/man3/WFMath_Polygon_2.3
# Delete a messed-up man page that sometimes appears
rm -f doc/man/man3/*_.3

# Remove timestamps from the generated documentation to avoid
# multiarch conflicts

for file in doc/html/*.html ; do
    sed -i -e 's/Generated on .* for WFMath by/Generated for WFMath by/' $file
done

%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3/
install -p -m0644 doc/man/man3/*.3 $RPM_BUILD_ROOT%{_mandir}/man3/

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
# Run tests in debug mode so asserts won't be skipped
sed -i -e 's/-DNDEBUG/-DDEBUG/' wfmath/Makefile
make %{?_smp_mflags} check

%files
%doc AUTHORS COPYING README TODO ChangeLog
%{_libdir}/lib%{oldname}-0.3.so.*


%files devel
%doc doc/CLASS_LAYOUT doc/html/
%{_includedir}/%{oldname}-0.3
%{_libdir}/lib%{oldname}-0.3.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.*


%changelog
* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.12-alt2_1
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.12-alt1_1
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.11-alt1_2
- initial release by fcimport

