Name: libtomcrypt
Version: 1.17
Release: alt1
Summary: A comprehensive, portable cryptographic toolkit
Group: System/Libraries
License: WTFPL
Url: http://libtom.org/
Source0: http://www.libtom.org/files/crypt-%version.tar.bz2

Patch0: libtomcrypt-makefile.patch

BuildRequires: texlive-latex-recommended

# Automatically added by buildreq on Wed Sep 14 2011
# optimized out: fontconfig ghostscript-classic ghostscript-common tex-common texlive-base texlive-base-bin texlive-common texlive-generic-recommended texlive-latex-base texlive-latex-recommended texlive-xetex
BuildRequires: ghostscript-utils libtommath-devel

%description
A comprehensive, modular and portable cryptographic toolkit that
provides developers with a vast array of well known published block
ciphers, one-way hash functions, chaining modes, pseudo-random number
generators, public key cryptography and a plethora of other routines.

Designed from the ground up to be very simple to use. It has a modular
and standard API that allows new ciphers, hashes and PRNGs to be added
or removed without change to the overall end application. It features
easy to use functions and a complete user manual which has many source
snippet examples.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-static
Summary: Static development files for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
The %name-devel-static package contains static libraries files for
developing applications that use %name.

%package doc
Summary: Documentation files for %name
Group: Documentation
Requires: %name = %version-%release

%description doc
The %name-doc package contains documentation for use with %name.

%prep
%setup
%patch0 -p1

%build
# no configure script ships with libtomcrypt.  Its only requirement is
# ANSI C. And libtommath.  Explicitly force it to be built against libtommath
export CFLAGS="$RPM_OPT_FLAGS -DLTM_DESC -I%_includedir/tommath"
%make_build LIBPATH=%_libdir EXTRALIBS="-ltommath" -f makefile.shared
%make_build LIBPATH=%_libdir -f makefile docs

%check
export CFLAGS="$RPM_OPT_FLAGS -DLTM_DESC -DUSE_LTM -I%_includedir/tommath -I testprof"
%make_build LIBPATH=%_libdir EXTRALIBS="-L.libs -Ltestprof/.libs -ltommath" test -f makefile.shared
LD_LIBRARY_PATH=.libs:testprof/.libs ./test

%install
# There is no configure script that ships with libtomcrypt but it does
# have understand DESTDIR and its installs via that and the
# INSTALL_USER and INSTALL_GROUP environment variables.

export INSTALL_USER=$(id -un)
export INSTALL_GROUP=$(id -gn)
export CFLAGS="$RPM_OPT_FLAGS -DLTM_DESC -DUSE_LTM"

make install INCPATH=%_includedir/tomcrypt DESTDIR=%buildroot LIBPATH=%_libdir EXTRALIBS="-ltommath" -f makefile.shared
find %buildroot -name '*.h' -exec chmod 644 {} ';'

# remove unneeded files
find %buildroot -name '*.la' -exec rm -f {} ';'
find %buildroot -name 'libtomcrypt_prof*' -exec rm -f {} ';'

%files
%doc LICENSE
%_libdir/*.so.*

%files devel
%doc LICENSE
%_includedir/tomcrypt
%_libdir/*.so

%files devel-static
%_libdir/*.a

%files doc
%doc LICENSE doc/crypt.pdf

%changelog
* Wed Sep 14 2011 Fr. Br. George <george@altlinux.ru> 1.17-alt1
- Initial build from FC

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.17-9
- Autorebuild for GCC 4.3

* Sun Nov 25 2007 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.17-8
- Resolve multilib conflicts from Bug #342431 by splitting out
  documentation to libtomcrypt-docs subpackage
- fix rpmlint Summary: warning

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.17-7
- Rebuild for selinux ppc32 issue.

* Tue Jul 10 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.17-6
- turn off optimization for ppc64 to work around Bug #239003

* Sat Jun 30 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.17-5
- removed package name from summary
- fixed URL and Source0 links
- really fixed linkage flag this time, added it to the build section not
  just the check.

* Fri Jun 29 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.17-4
- fixed linkage flag with correct tommath name
- added check section
- removed libtomcrypt_prof libraries from package
- remove package name from summary

* Wed Jun 27 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.17-3
- create makefile patch to ensure RPM_OPT_FLAGS is honored
- install headers into _includedir/tomcrypt
- add location of libtommath headers to CFLAGS

* Sat Jun 23 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.17-2
- update build process to pass LIBPATH to make

* Fri Jun 22 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.17-1
- Initial spec file creation
