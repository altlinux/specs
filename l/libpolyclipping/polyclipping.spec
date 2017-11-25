# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname polyclipping
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# The Clipper C++ crystallographic library already uses the name "clipper".
# The developer is fine with the choosen name.

# API monitoring
# http://upstream-tracker.org/versions/clipper.html

Name:           libpolyclipping
Version:        6.4.2
Release:        alt1_1
Summary:        Polygon clipping library

Group:          System/Libraries
License:        Boost
URL:            http://sourceforge.net/projects/polyclipping
Source0:        http://downloads.sourceforge.net/%{oldname}/clipper_ver%{version}.zip

BuildRequires:  ctest cmake
BuildRequires:  dos2unix
Source44: import.info
Provides: polyclipping = %{version}-%{release}

%description
This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

%package        devel
Summary:        Development files for %{oldname}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Provides: polyclipping-devel = %{version}-%{release}

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.


%prep
%setup -n %{oldname}-%{version} -qc

# Delete binaries
find . \( -name "*.exe" -o -name "*.dll" \) -delete

# Correct line ends and encodings
find . -type f -exec dos2unix -k {} \;

for filename in perl/perl_readme.txt README; do
  iconv -f iso8859-1 -t utf-8 "${filename}" > "${filename}".conv && \
    touch -r "${filename}" "${filename}".conv && \
    mv "${filename}".conv "${filename}"
done

# Enable use_lines
sed -i 's|^//#define use_lines$|#define use_lines|' cpp/clipper.hpp


%build
pushd cpp
  %{fedora_cmake}
%make_build
popd


%install
pushd cpp
  make install DESTDIR=%{buildroot}

# Install agg header with corrected include statement
  sed -e 's/\.\.\/clipper\.hpp/clipper.hpp/' < cpp_agg/agg_conv_clipper.h > %{buildroot}/%{_includedir}/%{oldname}/agg_conv_clipper.h
popd

# viy hack
sed -i -e 's/^Version: $/Version: %version/' %buildroot%{_datadir}/pkgconfig/%{oldname}.pc

%files
%doc License.txt README
%doc Third\ Party/Haskell Third\ Party/perl Third\ Party/ruby Third\ Party/python Documentation
%{_libdir}/lib%{oldname}.so.*

%files devel
%{_datadir}/pkgconfig/%{oldname}.pc
%{_includedir}/%{oldname}/
%{_libdir}/lib%{oldname}.so

%changelog
* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 6.4.2-alt1_1
- new version

* Sat Jun 07 2014 Igor Vlasenko <viy@altlinux.ru> 6.1.3a-alt1_2
- converted for ALT Linux by srpmconvert tools

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 5.1.6-alt1_3
- update to new release by fcimport

* Mon Jul 08 2013 Igor Vlasenko <viy@altlinux.ru> 5.1.6-alt1_2
- update to new release by fcimport

* Sun Apr 28 2013 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_1
- initial fc import

