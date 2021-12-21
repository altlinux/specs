%define _name iniparser
# .so.0 is for version 3.x, .so.1 is 4.x
%define sover 1

Name: lib%_name
Version: 4.1
Release: alt1

Group: Development/C
Summary: Simple C library for parsing "INI-style" files
License: MIT
Url: http://ndevilla.free.fr/iniparser/

Vcs: https://github.com/ndevilla/iniparser.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
iniParser is an ANSI C library to parse "INI-style" files,
often used to hold application configuration information.

%package -n %name%sover
Summary: Simple C library for parsing "INI-style" files
Group: System/Libraries
Provides: %name = %EVR

%description -n %name%sover
iniParser is an ANSI C library to parse "INI-style" files,
often used to hold application configuration information.

%package devel
Summary: Development files for %_name
Group: Development/C
Requires: %name%sover = %EVR

%description devel
This package contains the header files, development files and
documentation for %_name library.

%prep
%setup
%patch -p1
# fix pc-file
sed -i 's|\/lib|/%_lib|
        s|\(-I${includedir}\)|\1/%_name|' %_name.pc

%build
%make_build CFLAGS='%optflags %optflags_shared %(getconf LFS_CFLAGS)' libiniparser.so.%sover

%install
%define docdir %_docdir/%name-%version
mkdir -p %buildroot{%_libdir,%_includedir/%_name,%_pkgconfigdir,%docdir}
install -pm644 %name.so.%sover %buildroot%_libdir/
ln -s %name.so.%sover %buildroot%_libdir/%name.so
install -pm644 src/*.h  %buildroot%_includedir/%_name/
install -pm644 %_name.pc  %buildroot%_pkgconfigdir/
install -pm644 LICENSE html/* %buildroot%docdir/

%files -n %name%sover
%_libdir/%name.so.%sover
%dir %docdir
%docdir/LICENSE

%files devel
%_libdir/%name.so
%_includedir/%_name/
%_pkgconfigdir/%_name.pc
%dir %docdir
%docdir/*.*

%changelog
* Tue Dec 21 2021 Yuri N. Sedunov <aris@altlinux.org> 4.1-alt1
- updated to v4.1-11-gdeb85ad (bumped soname)
- moved headers to %%_includedir/iniparser
- added .pc file

* Thu Apr 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.1-alt2
- great spec cleanup thanks to ldv@

* Wed Apr 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.1-alt1
- initial build

