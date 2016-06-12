%define underscore_version 2_6_2
%def_with check

Name: tinyxml
Version: 2.6.2
Release: alt1.2
Summary: A simple, small, C++ XML parser
Group: System/Libraries
License: zlib
Url: http://www.grinninglizard.com/tinyxml/
BuildRequires: gcc-c++
Source: http://downloads.sourceforge.net/%name/%{name}_%underscore_version.tar.gz
Source1:        tinyxml.pc.in
Patch0: tinyxml-2.5.3-stl.patch
# http://sourceforge.net/p/tinyxml/patches/51/
Patch1: tinyxml-2.6.2-entity.patch
Patch2: tinyxml-2.6.2-alt-fix-tests.patch

%description
TinyXML is a simple, small, C++ XML parser that can be easily integrating
into other programs. Have you ever found yourself writing a text file parser
every time you needed to save human readable data or serialize objects?
TinyXML solves the text I/O file once and for all.
(Or, as a friend said, ends the Just Another Text File Parser problem.)

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q -n %name
%patch0 -p1 -b .stl
touch -r tinyxml.h.stl tinyxml.h
%patch1 -p0
%patch2 -p2

%build
# Not really designed to be build as lib, DYI
for i in tinyxml.cpp tinystr.cpp tinyxmlerror.cpp tinyxmlparser.cpp; do
  g++ %optflags -fPIC -o $i.o -c $i
done
g++ %optflags -shared -o lib%name.so.0.%version \
   -Wl,-soname,lib%name.so.0 *.cpp.o

%if_with check
ln -s lib%name.so.0.%version lib%name.so.0
ln -s lib%name.so.0.%version lib%name.so
g++ -I. -L. xmltest.cpp -ltinyxml -o xmltest
%endif

%install
# Not really designed to be build as lib, DYI
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir
install -m 755 lib%name.so.0.%version %buildroot%_libdir
ln -s lib%name.so.0.%version %buildroot%_libdir/lib%name.so.0
ln -s lib%name.so.0.%version %buildroot%_libdir/lib%name.so
install -p -m 644 %name.h %buildroot%_includedir

mkdir -p %{buildroot}%{_libdir}/pkgconfig
sed -e 's![@]prefix[@]!%{_prefix}!g' \
 -e 's![@]exec_prefix[@]!%{_exec_prefix}!g' \
 -e 's![@]libdir[@]!%{_libdir}!g' \
 -e 's![@]includedir[@]!%{_includedir}!g' \
 -e 's![@]version[@]!%{version}!g' \
 %{SOURCE1} > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%check
LD_LIBRARY_PATH=$PWD${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH} ./xmltest

%files
%_libdir/*.so.*
%doc changes.txt readme.txt

%files devel
%doc docs/*
%_includedir/*
%_libdir/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.2-alt1.2
- NMU: added pc file

* Tue Jun 09 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.2-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Sep 25 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.2-alt1
- New version.
- Fixed Incorrect entity encoding (ALT#25562).
- Enabled testsuite.

* Wed May 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.6.1-alt1
- 2.6.1 (ALT #25562)

* Wed Mar 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.3-alt4
- rebuild for debuginfo

* Tue Dec 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.3-alt3
- rebuild for soname set-version

* Mon Nov 09 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.3-alt2
- remove %%post_ldconfig

* Mon May 26 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.3-alt1
- Initial for ALT

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.5.3-3
- Autorebuild for GCC 4.3

* Fri Dec 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.5.3-2
- Various improvements from review (bz 407571)

* Fri Nov 30 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.5.3-1
- Initial Fedora Package
