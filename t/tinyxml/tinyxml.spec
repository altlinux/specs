%define underscore_version 2_5_3

Name: tinyxml
Version: 2.6.1
Release: alt1
Summary: A simple, small, C++ XML parser
Group: System/Libraries
License: zlib
Url: http://www.grinninglizard.com/tinyxml/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
BuildRequires: gcc-c++
Source: http://downloads.sourceforge.net/%name/%{name}_%underscore_version.tar.gz
Patch0: tinyxml-2.5.3-stl.patch

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

%build
# Not really designed to be build as lib, DYI
for i in tinyxml.cpp tinystr.cpp tinyxmlerror.cpp tinyxmlparser.cpp; do
  g++ $RPM_OPT_FLAGS -fPIC -o $i.o -c $i
done
g++ $RPM_OPT_FLAGS -shared -o lib%name.so.0.%version \
   -Wl,-soname,lib%name.so.0 *.cpp.o

%install
# Not really designed to be build as lib, DYI
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir
install -m 755 lib%name.so.0.%version %buildroot%_libdir
ln -s lib%name.so.0.%version %buildroot%_libdir/lib%name.so.0
ln -s lib%name.so.0.%version %buildroot%_libdir/lib%name.so
install -p -m 644 %name.h %buildroot%_includedir

%files
%_libdir/*.so.*
%doc changes.txt readme.txt

%files devel
%doc docs/*
%_includedir/*
%_libdir/*.so

%changelog
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
