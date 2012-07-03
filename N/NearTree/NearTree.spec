Name: NearTree
Version: 3.1.1
Release: alt1

Summary: An API for finding nearest neighbors
License: LGPLv2+
Group: System/Libraries

Url: http://neartree.sourceforge.net
Source: http://downloads.sourceforge.net/project/neartree/neartree/NearTree-%version/NearTree-%version.tar.gz
# library should not have version number in their name.
# Sent to upstream but upstream cannot accept.
Patch: NearTree-3.1-fedora.patch
# to fix libdir for lib64 architecture
Patch1: NearTree-3.1-lib64.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Apr 22 2012
# optimized out: libstdc++-devel
BuildRequires: gcc-c++ libCVector-devel

%description
This is a release of an API for finding nearest neighbors among
points in spaces of arbitrary dimensions. This release provides
a C++ template, TNear.h, and a C library, CNearTree.c, with
example/test programs.

%package -n lib%name
Summary: A shared library for finding nearest neighbors
Group: System/Libraries

%description -n lib%name
This package includes the shared library files
for running applications that use NearTree.

%package -n lib%name-devel
Summary: Development tools for compiling programs using NearTree
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
The NearTree-devel package includes the header and library files
for developing applications that use NearTree.

%prep
%setup
%patch0 -p1 -b .fedora
%if %_lib == lib64
%patch1 -p1 -b .lib64
%endif
sed -i 's,\(--mode=\(compile\|link\)\) \$(\(CC\|CXX\)),--tag=\3 &,' Makefile

# convert end of line code from CRFL to LF
mv README_NearTree.txt README_NearTree.txt.orig
tr -d \\r < README_NearTree.txt.orig > README_NearTree.txt

%build
%make_build all CFLAGS="%optflags -ansi -pedantic -DCNEARTREE_SAFE_TRIANG=1"

%install
%make_install install \
	CFLAGS="%optflags -ansi -pedantic -DCNEARTREE_SAFE_TRIANG=1" \
	INSTALL_PREFIX="%buildroot%prefix"
find %buildroot -name '*.la' -exec rm -f {} ';'
find %buildroot -name '*.a' -exec rm -f {} ';'

%check
if [ "`gcc -dumpversion | cut -d \. -f 1-2`" = "4.4" ] ; then
  # gcc-4.4.x may have a bug in -fcaller-saves
  make tests \
  	CFLAGS="%optflags -fno-caller-saves -ansi -pedantic -DCNEARTREE_SAFE_TRIANG=1"
else
  make tests \
  	CFLAGS="%optflags -ansi -pedantic -DCNEARTREE_SAFE_TRIANG=1"
fi

%files -n lib%name
%doc README_NearTree.html README_NearTree.txt lgpl.txt
%_libdir/libCNearTree.so.*

%files -n lib%name-devel
%_includedir/CNearTree.h
%_includedir/TNear.h
%_includedir/rhrand.h
%_includedir/triple.h
%_libdir/libCNearTree.so

%changelog
* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 3.1.1-alt1
- 3.1.1

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 3.1-alt2
- drop empty package

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 3.1-alt1
- initial build for ALT Linux Sisyphus (based on F15 package)
- libtool band-aid (typical for this particular stack, sigh)
- spec cleanup
- libification

* Wed Jun  8 2011 Takanori MATSUURA <t.matsuu@gmail.com> - 3.1-1
- update to 3.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 2.4-1
- update to 2.4

* Tue Dec 14 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 2.3.2-2
- add "-fno-caller-saves" option for gcc-4.4.x

* Thu Nov 11 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 2.3.2-1
-  update to 2.3.2

* Fri Oct 22 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 2.3.1-1
- initial import (#545047)

* Mon Oct 18 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 2.3.1-0.1
- use "make all" instead of "make"
- add %%check

* Tue Oct 12 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 2.3.1-0
- update to 2.3.1

* Wed Dec  9 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 2.1.4-3
- remove static library

* Tue Dec  8 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 2.1.4-2
- fit to Fedora Packaging Guidelines

* Fri Dec  3 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 2.1.4-1
- update to 2.1.4

* Wed Jul 29 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 2.1.3-1
- initial build
