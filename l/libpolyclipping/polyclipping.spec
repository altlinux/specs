%define oldname polyclipping

Name: libpolyclipping
Version: 6.4.2
Release: alt2
%global so_version 22
Summary: Polygon clipping library
Group: System/Libraries

# The entire source is BSL-1.0, except:
# - The contents of Documentation/Scripts/SyntaxHighlighter/ are a.'Dual licensed
#   under the MIT and GPL licensesa.'. These sources do not contribute to the
#   binary RPMs and are removed in %%prep.
License: BSL-1.0
URL: https://sourceforge.net/projects/polyclipping
# Source-url: https://downloads.sourceforge.net/%{oldname}/clipper_ver%{version}.zip
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: dos2unix
Provides: polyclipping = %EVR

%description
This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

%package devel
Group: Development/Other
Summary: Development files for %oldname
Requires: %name = %EVR
Provides: polyclipping-devel = %EVR

%description    devel
The %oldname-devel package contains libraries and header files for
developing applications that use %oldname.


%prep
%setup

# Delete binaries
find . \( -name "*.exe" -o -name "*.dll" \) -delete

# Delete bundled(js-syntaxhighlighter),
# https://github.com/syntaxhighlighter/syntaxhighlighter.
rm -rvf Documentation/Scripts/SyntaxHighlighter

# Correct line ends and encodings
find . -type f -exec dos2unix -k {} \;

for filename in "Third Party/perl/perl_readme.txt" README; do
  iconv -f iso8859-1 -t utf-8 "${filename}" > "${filename}".conv && \
    touch -r "${filename}" "${filename}".conv && \
    mv "${filename}".conv "${filename}"
done


%build
%add_optflags %optflags_shared
pushd cpp
%cmake
%cmake_build
popd


%install
pushd cpp
%cmake_install

# Install agg header with corrected include statement
  sed -e 's/\.\.\/clipper\.hpp/clipper.hpp/' < cpp_agg/agg_conv_clipper.h > %buildroot%_includedir/%oldname/agg_conv_clipper.h
popd

# viy hack
sed -i -e 's/^Version: $/Version: %version/' %buildroot%_datadir/pkgconfig/%oldname.pc


%files
%doc --no-dereference License.txt
%doc README
%_libdir/lib%oldname.so.%so_version
%_libdir/lib%oldname.so.%so_version.*

%files devel
%doc Third\ Party
%_datadir/pkgconfig/%oldname.pc
%_includedir/%oldname/
%_libdir/lib%oldname.so

%changelog
* Sat Jul 12 2025 Anton Midyukov <antohami@altlinux.org> 6.4.2-alt2
- fix ftbfs
- cleanup spec

* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 6.4.2-alt1_17
- update to new release by fcimport

* Fri Dec 17 2021 Igor Vlasenko <viy@altlinux.org> 6.4.2-alt1_13
- update to new release by fcimport

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 6.4.2-alt1_6
- fc update

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

