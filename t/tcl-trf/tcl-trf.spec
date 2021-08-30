%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: tcl-trf
Version: 2.1.4
Release: alt4

Summary: A tcl extension called Tcl Data transformations
License: TCL
Group: Development/Tcl
Url: http://tcltrf.sourceforge.net/

# CVS import tcltrf.cvs.sourceforge.net:/cvsroot/tcltrf module trf
# git://git.altlinux.org/gears/t/tcl-trf.git
Source: %name-%version-%release.tar

Requires: tcl >= 8.6.7-alt2
BuildRequires: bzlib-devel zlib-devel libssl-devel tcl-devel >= 8.6.7-alt2 tcl-memchan rpm-build-tcl >= 0.5.2-alt1

%description
%name is a collection of data transformation:
- generation of message digests (hash values, checksums)
  MD2, MD5, SHA/SHS, SHA-1, HAVAL, RIPEMD-128, -160,
  CRC (polynomial used by PGP),  ADLER (based upon zlib)
- conversion from and to various data encodings:
  dual, octal, hexadecimal representation, uuencoding,
  base64-encoding, ASCII85-encoding
- a reed-solomon error correcting coder
- (de)compression based on zlib and bzlib

%prep
%setup -n %name-%version-%release
%tea_patch

%build
%autoreconf
%add_optflags -DSSL_STATIC_BUILD=1 -D_XOPEN_SOURCE
export no_zlibtcl=true
export CFLAGS="%optflags"
export SHLIB_SUFFIX=.so
%configure \
		--enable-static-bzlib \
		--enable-static-zlib \
		--enable-static-md5 \
		--with-bz2-include-dir=%_includedir \
		--with-zlib-include-dir=%_includedir \
		--with-ssl-include-dir=%_includedir/openssl \
		--with-bz2-lib-dir=%_libdir \
		--with-zlib-lib-dir=%_libdir \
		--with-ssl-lib-dir=%_libdir \
		--enable-threads
%make_build LIBS="-lz -lbz2 -lcrypt -lcrypto"

%install
%makeinstall

%check
cat <<EOF >test.tcl
#!/usr/bin/tclsh
package require Trf
EOF

chmod +x test.tcl
TCLLIBPATH=%buildroot%_tcllibdir ./test.tcl

%files
%doc ChangeLog README doc/license.terms
%_tcllibdir/Trf%version/libTrf%version.so
%_tcllibdir/Trf%version/pkgIndex.tcl

%changelog
* Mon Aug 30 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.1.4-alt4
- Fixed built with LTO.
- Do no pack stub.

* Mon Jul 05 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.1.4-alt3
- Built with %%tea_patch.
- Fixed license field.

* Sun Nov 03 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.1.4-alt2
- Replaced aclocal and autoconf calls with %%autoreconf in the %%build
  (fixed FTBFS).

* Tue May 07 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.1.4-alt1
- Updated to 2.1.4.
- Applied Debian patches.
- Removed non-free files.
- Added simple test to check extension loading.
- Packaged %%_tcllibdir/Trf%%version (fix post-install unowned files).

* Mon Oct 02 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.1-alt8
- adapted for new Tcl/Tk extenstion packaging policy
- rebuilt without shared libcrypt and fixed bugs in static md5

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.1-alt7.qa1
- NMU: rebuilt for debuginfo.

* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt7
- updated from CVS @20060124
- fixed build on x86_64

* Tue Jan 10 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt6
- updated from CVS @ 20051006

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt5
- rebuilt against new shiny reqprov finder

* Sat May 15 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt4
- updated from CVS @ 200402018
- dynamically linked with zlib, bzlib, libcrypt instead of dlopen()

* Sat Mar  8 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 2.1-alt3
- bzlib bindings fixed

* Wed Sep 25 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1-alt2
- rebuilt in new env

* Tue Aug  6 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1-alt1
- first build for %distribution
