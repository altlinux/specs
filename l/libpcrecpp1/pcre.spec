Name: libpcrecpp1
Version: 8.37
Release: alt2

Summary: Perl-compatible regular expressions C++ wrapper legacy shared library
License: BSD-style
Group: System/Legacy libraries
Url: http://www.pcre.org/

Provides: libpcrecpp = %version
Obsoletes: libpcrecpp < %version

# ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-%version.tar.bz2
Source: pcre-%version.tar
Patch: pcre-%version-%release.patch

%set_gcc_version 4.9
BuildRequires: gcc4.9-c++

%description
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

This package contains PCRE C++ wrapper legacy shared library.

%prep
%setup -n pcre-%version
%patch -p1
rm aclocal.m4 m4/{libtool,lt*}.m4

%build
%autoreconf
%define docdir %_docdir/%name-%version
%configure --includedir=%_includedir/%name \
	--docdir=%docdir \
	--enable-pcre8 \
	--enable-pcre16 \
	--enable-utf \
	--enable-unicode-properties \
	--disable-pcretest-libreadline \
	--enable-cpp \
	--disable-jit \
	#
%make_build

%install
%makeinstall_std

%files
%_libdir/libpcrecpp.so.*

%changelog
* Tue May 26 2015 Dmitry V. Levin <ldv@altlinux.org> 8.37-alt2
- Built libpcrecpp1 legacy library.

* Tue May 26 2015 Dmitry V. Levin <ldv@altlinux.org> 8.37-alt1
- Updated to 8.37 (closes: #24958).

* Thu May 30 2013 Dmitry V. Levin <ldv@altlinux.org> 8.33-alt2
- Disabled JIT compiling support because it pulls in pthread library.

* Wed May 29 2013 Dmitry V. Levin <ldv@altlinux.org> 8.33-alt1
- Updated to 8.33.
- Enabled JIT compiling support.

* Sun Dec 16 2012 Dmitry V. Levin <ldv@altlinux.org> 8.32-alt1
- Updated to 8.32.

* Mon Sep 24 2012 Dmitry V. Levin <ldv@altlinux.org> 8.31-alt2
- libpcre3: reintroduced obsolete pcre_info() API for compatiblity.

* Mon Sep 24 2012 Dmitry V. Levin <ldv@altlinux.org> 8.31-alt1
- Updated to 8.31.
- Enabled and packaged libpcre16.

* Wed Dec 14 2011 Dmitry V. Levin <ldv@altlinux.org> 8.21-alt1
- Updated to 8.21.

* Thu Oct 06 2011 Dmitry V. Levin <ldv@altlinux.org> 8.20-alt0.1
- Updated to 8.20-rc2 (closes: #26422).

* Wed Sep 14 2011 Dmitry V. Levin <ldv@altlinux.org> 8.13-alt1
- Updated to 8.13.

* Sat Feb 05 2011 Dmitry V. Levin <ldv@altlinux.org> 8.12-alt2
- Packaged pcretest separately from -devel (closes: #24980).

* Sun Jan 23 2011 Dmitry V. Levin <ldv@altlinux.org> 8.12-alt1
- Updated to 8.12 (closes: #24958).

* Fri Oct 08 2010 Dmitry V. Levin <ldv@altlinux.org> 8.10-alt1
- Updated to 8.10.

* Mon Jun 21 2010 Dmitry V. Levin <ldv@altlinux.org> 8.02-alt1
- Updated to 8.02.
- Synced with Debian 8.02-1.
- Packaged html docs.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 7.9-alt3
- Moved "make check" to %%check section.

* Wed May 27 2009 Dmitry V. Levin <ldv@altlinux.org> 7.9-alt2
- Moved pcrecpp manpage to lib%{name}cpp-devel subpackage.

* Wed May 27 2009 Dmitry V. Levin <ldv@altlinux.org> 7.9-alt1
- Updated to 7.9.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 7.8-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Fri Sep 26 2008 Dmitry V. Levin <ldv@altlinux.org> 7.8-alt1
- Updated to 7.8.

* Thu Sep 11 2008 Alexey Tourbin <at@altlinux.ru> 7.7-alt3
- enable unicode properties (required for glib2)
- provide pcre-config(utf8) and pcre-config(unicode-properties)

* Tue Jul 01 2008 Dmitry V. Levin <ldv@altlinux.org> 7.7-alt2
- pcre_compile: Fix potential heap buffer overflow
  (by Tavis Ormandy, closes: CVE-2008-2371).

* Sat May 31 2008 Dmitry V. Levin <ldv@altlinux.org> 7.7-alt1
- Updated to 7.7.

* Tue Feb 12 2008 Dmitry V. Levin <ldv@altlinux.org> 7.6-alt1
- Updated to 7.6 (CVE-2008-0674).

* Tue Jan 15 2008 Dmitry V. Levin <ldv@altlinux.org> 7.5-alt1
- Updated to 7.5.

* Fri Sep 21 2007 Dmitry V. Levin <ldv@altlinux.org> 7.4-alt1
- Updated to 7.4.

* Tue Sep 18 2007 Dmitry V. Levin <ldv@altlinux.org> 7.3-alt1
- Updated to 7.3.

* Sun Jan 14 2007 Dmitry V. Levin <ldv@altlinux.org> 7.0-alt2
- Bump libpcrecpp soname version number to reflect API change.
- Package %_pkgconfigdir/libpcrecpp.pc in libpcrecpp-devel.

* Sat Jan 13 2007 Dmitry V. Levin <ldv@altlinux.org> 7.0-alt1
- Updated to 7.0.

* Sun Sep 24 2006 Dmitry V. Levin <ldv@altlinux.org> 6.7-alt1
- Updated to 6.7.

* Sat Dec 03 2005 Dmitry V. Levin <ldv@altlinux.org> 6.4-alt2
- Relocated shared libraries from %_libdir/ to /%_lib/.
- Merged grep subpackage into devel subpackage.
- Moved pcregrep to grep package.

* Tue Oct 04 2005 Dmitry V. Levin <ldv@altlinux.org> 6.4-alt1
- Updated to 6.4.

* Tue Sep 13 2005 Dmitry V. Levin <ldv@altlinux.org> 6.3-alt1
- Updated to 6.3.
- Updated Debian patches.
- Dropped unused bootstage logic.
- Packaged pcredemo.c (#7720).
- Packaged zpcregrep.
- Packaged C++ bindings in separate subpackages.

* Sun Apr  3 2005 Ilya Evseev <evseev@altlinux.org> 5.0-alt2
- enabled UTF-8 support by default, see bugreport #2030
- added optional bootstage support package, see bugreport #3851

* Tue Mar  8 2005 Ilya Evseev <evseev@altlinux.org> 5.0-alt1
- 5.0
- specfile: added russian summaries/descriptions

* Thu Dec 11 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5-alt1
- Updated to 4.5.
- Removed alt-makefile patch (merged upstream).

* Mon Nov 03 2003 Dmitry V. Levin <ldv@altlinux.org> 4.4-alt1
- Updated to 4.4.
- Changed API, soname and renamed library subpackage to libpcre3.
- Implemented backwards compatibility build mode.
- Reverted back library relocation introduced in 3.4-ipl3mdk.
- Added pcre-config(1) manpage (deb).
- Do not package .la files.
- Updated package descriptions.
- Fixed SMP build.

* Tue Sep 10 2002 Dmitry V. Levin <ldv@altlinux.org> 3.9-alt3
- Fixed lib%name.la

* Sun Sep 01 2002 Dmitry V. Levin <ldv@altlinux.org> 3.9-alt2
- Updated %post/%postun scripts.
- Fixed library symlinks generation.
- Relocated documentation.
- Updated devel-static requirements.

* Mon Jan 14 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.9-alt1
- 3.9

* Mon Nov 19 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.7-alt1
- 3.7
- Created subdirectory for include files.

* Mon Aug 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.5-alt1
- 3.5
- Moved static libraries to devel-static subpackage.
- Corrected requires.
- Corrected license info.
- Added pcretest utility to grep subpackage.

* Thu Feb 08 2001 Dmitry V. Levin <ldv@fandra.org> 3.4-ipl4mdk
- Fixed group tag in %name-grep subpackage.
- Libification.

* Wed Dec 13 2000 Dmitry V. Levin <ldv@fandra.org> 3.4-ipl3mdk
- Moved shared libraries from %_libdir to /lib.

* Wed Oct 11 2000 Dmitry V. Levin <ldv@fandra.org> 3.4-ipl2mdk
- Automatically added BuildRequires.

* Thu Aug 24 2000 Dmitry V. Levin <ldv@fandra.org> 3.4-ipl1mdk
- 3.4

* Thu Aug  3 2000 Dmitry V. Levin <ldv@fandra.org> 3.3-ipl1mdk
- 3.3
- Renamed subpackage pgrep --> pcre-grep.

* Wed Jun 28 2000 Dmitry V. Levin <ldv@fandra.org> 3.2-ipl1mdk
- Use FHS-compatible macros.

* Wed May 17 2000 Dmitry V. Levin <ldv@fandra.org>
- 3.2

* Thu Feb 10 2000 Dmitry V. Levin <ldv@fandra.org>
- 3.1

* Thu Dec 12 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Fri Nov 05 1999 Arne Coucheron <arneco@online.no>
  [2.08-1]
- using name and version macros
- changed Group to comply with RH 6.x
- using make install
- using install -d instead of mkdir -p
- removing RPM_BUILD_ROOT before installing
- some changes in the files section

* Fri May 28 1999 Damien Miller <dmiller@ilogic.com.au>
- Built RPMs
