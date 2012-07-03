Name: CVector
Version: 1.0.3.1
Release: alt2

Summary: ANSI C API for Dynamic Arrays
License: LGPLv2+
Group: System/Libraries

Url: http://cvector.sourceforge.net
Source: http://downloads.sourceforge.net/project/cvector/cvector/CVector-%version/CVector-%version.tar.gz
# to fix /-dynamic/-rdynamic/ issue, reported to upstream
Patch0: CVector-1.0.3.1-dynamic.patch
# to fix libdir for lib64 architecture
Patch1: CVector-1.0.3-lib64.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++

%description
CVector is an ANSI C implementation of dynamic arrays to provide
a crude approximation to the C++ vector class.

%package -n lib%name
Summary: Shared library for CVector
Group: System/Libraries

%description -n lib%name
This package includes the shared library files
for running applications that use CVector.

%package -n lib%name-devel
Summary: Development tools for compiling programs using CVector
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package includes the header and library files
for developing applications that use CVector.

%prep
%setup
%patch0 -p1 -b .dynamic
%if %_lib == lib64
%patch1 -p1 -b .lib64
%endif
sed -i -r 's,(--mode=(compile|link)),--tag=CC \1,' Makefile

%build
%make_build

%install
%make_install install INSTALL_PREFIX="%buildroot%prefix"
find %buildroot -name '*.la' -exec rm -f {} ';'
find %buildroot -name '*.a' -exec rm -f {} ';'

%check
make tests

%files -n lib%name
%doc README_CVector.html README_CVector.txt lgpl.txt
%_libdir/libCVector-*.so.*

%files -n lib%name-devel
%_includedir/CVector.h
%_libdir/libCVector.so

%changelog
* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 1.0.3.1-alt2
- drop empty package

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 1.0.3.1-alt1
- initial build for ALT Linux Sisyphus (based on F15 package)
- libtool band-aid
- spec cleanup
- libification

* Sat Apr  9 2011 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3.1-3
- use %%{_lib} detection to fix

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3.1-1
- update to 1.0.3.1
- use "make all" instead of "make"
- add %%check

* Tue Sep  1 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-1.5Aug09
- initial release

* Tue Sep  1 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-0.7.5Aug09
- use "-rdynamic" instead of "-shared"

* Tue Sep  1 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-0.6.5Aug09
- initial import for Fedora (#545046)

* Mon Aug 30 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-0.5.5Aug09
- change release versioning scheme
- provide 64 bit libdir fix as a patch
- remove useless s/dynamic/rsynamic/g

* Wed Dec  9 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-4.20090805
- remove static library

* Wed Dec  9 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-3.20090805
- apply changes mentioned in rhbz #545046 comment #4

* Tue Dec  8 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-2.20090805
- fit to Fedora Packaging Guidelines

* Tue Aug 25 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-1.20090805
- update to 1.0.3-5Aug09

* Wed Jul 29 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-1
- initial build
