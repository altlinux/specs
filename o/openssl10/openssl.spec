Name: openssl10
Version: 1.0.0j
Release: alt1

Summary: OpenSSL - Secure Sockets Layer and cryptography shared libraries and tools
License: BSD-style
Group: System/Base
Url: http://www.openssl.org

Source: ftp://ftp.openssl.org/source/openssl-%version.tar
Source1: openssl-config
Source2: Makefile.certificate
Source3: make-dummy-cert

Patch01: openssl-1.0.0b-owl-alt-issetugid.patch
Patch02: openssl-1.0.0b-alt-krb5.patch
Patch03: openssl-1.0.0f-alt-config.patch
Patch04: openssl-1.0.0b-gosta-pkcs12-fix.patch
Patch05: openssl-1.0.0j-rh-alt-soversion.patch
Patch06: openssl-1.0.0b-rh-enginesdir.patch
Patch07: openssl-1.0.0b-rh-rpath.patch
Patch08: openssl-1.0.0b-rh-test-use-localhost.patch
Patch09: openssl-1.0.0b-rh-default-paths.patch
Patch11: openssl-1.0.0i-rh-man.patch
Patch12: openssl-1.0.0b-rh-ia64-asm.patch
Patch13: openssl-1.0.0b-rh-x509.patch
Patch14: openssl-1.0.0b-rh-version-engines.patch
Patch16: openssl-1.0.0b-rh-alt-ipv6-apps.patch
Patch17: openssl-1.0.0b-rh-env-nozlib.patch
Patch18: openssl-1.0.0b-rh-aesni.patch
Patch22: openssl-1.0.0d-rh-apps-dgst.patch
Patch23: openssl-1.0.0d-rh-xmpp-starttls.patch
Patch24: openssl-1.0.0d-rh-padlock64.patch

%define shlib_soversion 10
%define compat_shlib_versions 1.0.0 1.0.0a
%if "%_lib" == "lib64"
%define lib_suffix ()(64bit)
%else
%define lib_suffix %nil
%endif
%define openssldir /var/lib/ssl
%define old_openssldir %_libdir/ssl
%def_enable compat
%def_with krb

BuildRequires: /usr/bin/pod2man bc zlib-devel

%package -n libcrypto%shlib_soversion
Summary: OpenSSL libcrypto shared library
Group: System/Libraries
Provides: libcrypto = %version-%release
# due to openssl.cnf
Conflicts: libcrypto7 < 0.9.8o-alt3, libssl7 < 0.9.8o-alt3, libssl6 < 0.9.8d-alt6
# due to openssldir migration
Conflicts: openssl < 0:0.9.8d-alt1
Requires: ca-certificates
# Backwards compatibility with alien libssl packages.
Provides: %(for i in %compat_shlib_versions; do echo -n "libcrypto.so.$i%lib_suffix "; done)

%package -n libssl%shlib_soversion
Summary: OpenSSL libssl shared library
Group: System/Libraries
Provides: libssl = %version
%{?_with_krb:Provides: openssl-krb = %version-%release}
Requires: libcrypto%shlib_soversion = %version-%release
Provides: libssl8 = %version-%release
# Backwards compatibility with alien libssl packages.
Provides: %(for i in %compat_shlib_versions; do echo -n "libssl.so.$i%lib_suffix "; done)

%package -n libssl-devel
Summary: OpenSSL include files and development libraries
Group: Development/C
Provides: openssl-devel = %version
Obsoletes: openssl-devel < %version
Requires: libssl%shlib_soversion = %version-%release
%{?_with_krb:Requires: libkrb5-devel}
# due to /usr/bin/openssl-config
Conflicts: openssl < %version-%release, openssl > %version-%release
# manpage clash: crypto(3).
Conflicts: erlang <= 0:R9C.0-alt2
%{?_with_krb:Provides: openssl-krb-devel = %version-%release}

%package -n libssl-devel-static
Summary: OpenSSL static libraries
Group: Development/C
Provides: openssl-devel-static = %version
Obsoletes: openssl-devel-static < %version
Requires: libssl-devel = %version-%release
%{?_with_krb:Provides: openssl-krb-devel-static = %version-%release}

%package -n openssl
Summary: OpenSSL tools
Group: System/Base
Provides: %openssldir
# due to /usr/bin/openssl-config
Conflicts: libssl-devel < %version-%release, libssl-devel > %version-%release
Requires: libssl%shlib_soversion = %version-%release
%{?_with_krb:BuildRequires: libkrb5-devel}

%package -n openssl-doc
Summary: OpenSSL documentation and demos
Group: Development/C
Requires: openssl = %version-%release
BuildArch: noarch

%package -n openssl-engines
Summary: OpenSSL ENGINE interface modules
Group: System/Libraries
Requires: libssl%shlib_soversion = %version-%release

%package -n tsget
Summary: Time Stamping HTTP/HTTPS client
Group: Security/Networking 
BuildArch: noarch
Requires: libssl%shlib_soversion = %version-%release
BuildRequires: perl-WWW-Curl

%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

%description -n libcrypto%shlib_soversion
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains the OpenSSL libcrypto shared library.

%description -n libssl%shlib_soversion
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains the OpenSSL libssl shared library.

%description -n libssl-devel
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains the OpenSSL include files and development libraries
required when building OpenSSL-based applications.

%description -n libssl-devel-static
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains static libraries required when developing
OpenSSL-based statically linked applications.

%description -n openssl
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains the base OpenSSL cryptography and SSL/TLS tools.

%description -n openssl-doc
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains the OpenSSL cryptography and SSL/TLS extra
documentation and demos required when developing applications.

%description -n openssl-engines
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

With OpenSSL 0.9.6, a new component was added to support alternative
cryptography implementations, most commonly for interfacing with external
crypto devices (eg. accelerator cards).  This component is called ENGINE,
and its presence in OpenSSL 0.9.6 (and subsequent bug-fix releases) caused
a little confusion as 0.9.6** releases were rolled in two versions,
a "standard" and an "engine" version.  In development for 0.9.7, the
ENGINE code has been merged into the main branch and is present in
the standard releases from 0.9.7 forwards.

There are currently following built-in ENGINE implementations:
- 4758cca: IBM 4758 CCA hardware support;
- aep: Aep hardware support;
- atalla: Atalla hardware support;
- chil: CHIL hardware support;
- cswift: CryptoSwift hardware support;
- gost: GOST (Russian cryptography standard) implementation;
- nuron: Nuron hardware support;
- padlock: VIA PadLock ACE support;
- sureware: SureWare hardware support;
- ubsec: UBSEC hardware support.

In addition, dynamic binding to external ENGINE implementations is
provided by a special ENGINE called "dynamic".

%description -n tsget
The tsget command can be used for sending a time stamp request, as
specified in RFC 3161, to a time stamp server over HTTP or HTTPS and
storing the time stamp response in a file.  This tool cannot be used for
creating the requests and verifying responses, you can use the OpenSSL
ts(1) command to do that.  tsget can send several requests to the server
without closing the TCP connection if more than one requests are specified
on the command line.

%prep
%setup -n openssl-%version

%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch04 -p1
%patch05 -p1
%patch06 -p1
%patch07 -p1
%patch08 -p1
%patch09 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1

find -type f -name \*.orig -delete

# Correct shared library name.
subst 's/\\\$(SHLIB_MAJOR)\.\\\$(SHLIB_MINOR)/\\$(VERSION)/g' Configure
subst 's/\$(SHLIB_MAJOR)\.\$(SHLIB_MINOR)/\$(VERSION)/g' Makefile.org

# Correct compilation options.
%add_optflags -fno-strict-aliasing -Wa,--noexecstack
subst 's/-O\([0-9s]\>\)\?\( -fomit-frame-pointer\)\?\( -m.86\)\?/\\\$(RPM_OPT_FLAGS)/' \
	Configure

# Be more verbose.
subst -p 's/^\([[:space:]]\+\)@/\1/' Makefile*

%build
ADD_ARGS=%_os-%_arch
%ifarch %ix86
	ADD_ARGS=linux-elf
%ifarch i386
	ADD_ARGS="$ADD_ARGS 386"
%endif
%endif
%ifarch %arm
ADD_ARGS=linux-generic32
%endif

./Configure shared -DSSL_ALLOW_ADH \
	--prefix=%prefix \
	--libdir=%_lib \
	--openssldir=%openssldir \
	--enginesdir=%_libdir/openssl/engines \
%if_with krb
	--with-krb5-flavor=MIT \
	--with-krb5-dir=%prefix \
%endif
	enable-gost enable-md2 enable-rfc3779 enable-tlsext zlib \
	$ADD_ARGS

# SMP-incompatible build.
make SHLIB_SOVERSION=%shlib_soversion

# Make soname symlinks.
/sbin/ldconfig -nv .

# Save library timestamps for later check.
touch -r libcrypto.so.%version libcrypto-stamp
touch -r libssl.so.%version libssl-stamp

LD_LIBRARY_PATH=`pwd` make rehash
LD_LIBRARY_PATH=`pwd` make test

%install
# The make_install macro doesn't work here.
make install \
	INSTALL_PREFIX=%buildroot \
	MANDIR=%_mandir

# Fail if one of shared libraries was rebuit.
if [ libcrypto.so.%version -nt libcrypto-stamp -o \
     libssl.so.%version -nt libssl-stamp ]; then
	echo 'Shared library was rebuilt by "make install".'
	exit 1
fi

# Fail if the openssl binary is statically linked against OpenSSL at this
# stage (which could happen if "make install" caused anything to rebuild).
LD_LIBRARY_PATH=`pwd` ldd %buildroot%_bindir/openssl |tee openssl.libs
grep -qw libssl openssl.libs
grep -qw libcrypto openssl.libs

# Install openssl-config script.
install -pDm755 %_sourcedir/openssl-config %buildroot%_bindir/openssl-config
subst -p 's,%%version,%version,g;s,%%openssldir,%openssldir,g' \
	%buildroot%_bindir/openssl-config

# Relocate shared libraries from %_libdir/ to /lib/.
mkdir -p %buildroot{/%_lib,%_libdir/openssl,%_sbindir}
for f in %buildroot%_libdir/*.so; do
	t=$(readlink "$f") || continue
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

# Add extra symlinks for compatibility with alien libssl packages.
for i in %compat_shlib_versions; do
	for n in crypto ssl; do
		[ -f %buildroot/%_lib/libcrypto.so.$i ] ||
			ln -s ../../%_lib/lib$n.so.%version %buildroot%_libdir/lib$n.so.$i
	done
done

mv %buildroot%_libdir/engines %buildroot%_libdir/openssl/

# Relocate openssl.cnf from %%openssldir/ to %_sysconfdir/openssl/.
mkdir -p %buildroot%_sysconfdir/openssl
mv %buildroot%openssldir/openssl.cnf %buildroot%_sysconfdir/openssl/
ln -s `relative %_sysconfdir/openssl/openssl.cnf %openssldir/openssl.cnf` %buildroot%openssldir/

# Rename some man pages, fix references.
for f in passwd.1 err.3 rand.3 threads.3 config.5; do
	name="${f%%.*}"
	sect="${f##*.}"
	NAME=`printf %%s "$name" |tr '[:lower:]' '[:upper:]'`
	subst "s/\\<$NAME $sect\\>/SSL&/" %buildroot%_mandir/man"$sect/$f"
	mv -v %buildroot%_mandir/man"$sect"/{,ssl}"$f"
	find %buildroot%_mandir -type f -print0 |
		xargs -r0 grep -FZl "\\fI$name\\fR\\|($sect)" -- |
		xargs -r0 subst -p "s/\\\\fI$name\\\\fR\\\\|($sect)/\\\\fIssl$name\\\\fR\\\\|($sect)/" --
	find %buildroot%_mandir -type l |while read link; do
		[ "$(readlink -n "$link")" = "$f" ] || continue
		ln -sfv "ssl$f" "$link"
	done
done
ln -s sslconfig.5 %buildroot%_mandir/man5/openssl.cnf.5

# Make backwards-compatibility symlink to ssleay.
ln -snf openssl %buildroot%_bindir/ssleay

# Install a makefile for generating keys and self-signed certs,
# and a script for generating them on the fly.
install -pDm644 %_sourcedir/Makefile.certificate \
	%buildroot%openssldir/certs/Makefile
install -pDm644 %_sourcedir/make-dummy-cert \
	%buildroot%openssldir/certs/make-dummy-cert

# Install standard root certificates.
ln -s ../../..%_datadir/ca-certificates/ca-bundle.crt \
	%buildroot%openssldir/cert.pem

mv %buildroot%openssldir/misc/CA{.sh,}
rm %buildroot%openssldir/misc/CA.pl

mv %buildroot%openssldir/misc/tsget %buildroot%_sbindir/

%define docdir %_docdir/openssl-%version
mkdir -p %buildroot%docdir
install -pm644 CHANGES* LICENSE NEWS README* engines/ccgost/README.gost \
	%buildroot%docdir/
bzip2 -9 %buildroot%docdir/CHANGES*
cp -a demos doc %buildroot%docdir/
rm -rf %buildroot%docdir/doc/{apps,crypto,ssl}

%if_enabled compat
%pre -n openssl
[ $1 -gt 1 ] || exit 0
if [ ! -e %_sysconfdir/openssl -a ! -L %_sysconfdir/openssl -a -e %old_openssldir/openssl.cnf ]; then
	mkdir -p %_sysconfdir/openssl &&
	cp -a %old_openssldir/openssl.cnf %_sysconfdir/openssl/
fi
if [ ! -e %openssldir -a ! -L %openssldir -a -d %old_openssldir ]; then
	cp -a %old_openssldir %openssldir
fi
%endif #compat

%files -n libcrypto%shlib_soversion
/%_lib/libcrypto*
%_libdir/libcrypto*.so.*
%config(noreplace) %_sysconfdir/openssl
%dir %openssldir
%openssldir/*.cnf
%openssldir/*.pem
%dir %docdir
%docdir/[A-Z]*

%files -n libssl%shlib_soversion
/%_lib/libssl*
%_libdir/libssl*.so.*

%files -n libssl-devel
%_bindir/openssl-config
%_libdir/*.so
%_libdir/pkgconfig/*
%_includedir/*

%files -n libssl-devel-static
%_libdir/*.a

%files -n openssl
%_bindir/*
%dir %openssldir
%openssldir/misc
%openssldir/certs
%dir %attr(700,root,root) %openssldir/private
%_mandir/man[157]/*
%exclude %_man1dir/tsget.*

%files -n openssl-doc
%dir %docdir
%docdir/[a-z]*
%_man3dir/*

%files -n openssl-engines
%_libdir/openssl

%files -n tsget
%_sbindir/tsget
%_man1dir/tsget.*

%changelog
* Sat May 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.0j-alt1
- Updated to 1.0.0j (fixes CVE-2012-2333).

* Thu Apr 19 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.0i-alt1
- Updated to 1.0.0i (fixes CVE-2012-2110).

* Fri Mar 23 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.0h-alt1
- Updated to 1.0.0h (fixes CVE-2012-0050, CVE-2012-0884 and other bugs).

* Fri Jan 13 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.0f-alt1
- Updated to 1.0.0f (fixes multiple CVEs).

* Mon Sep 12 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0.0e-alt1
- Updated to 1.0.0e (fixes CVE-2011-3207).

* Tue Mar 15 2011 Alexey Tourbin <at@altlinux.ru> 1.0.0d-alt2
- In pkgconfig files, moved -ldl -lz to Libs.private.

* Wed Feb 09 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0.0d-alt1
- Updated to 1.0.0d (fixes CVE-2011-0014).

* Tue Feb 01 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0.0c-alt1
- Updated to 1.0.0c (fixes CVE-2010-4180).

* Tue Nov 16 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.0b-alt1
- Updated to 1.0.0b (fixes CVE-2010-2939 and CVE-2010-3864).

* Sat Oct 02 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.0a-alt2
- Hardened conflict with incompatible libssl6 (closes: #24195).

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.0a-alt1
- Updated to 1.0.0a.
- Merged with FC openssl-1.0.0a-3.

* Thu Sep 30 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.8o-alt2
- openssl.cnf: Updated from openssl-1.0.0a, merged with FC.

* Wed Sep 29 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.8o-alt1
- Updated to 0.9.8o (fixes CVE-2010-0742).
- Fixed ssl/dtls1.h ABI breakage introduced in 0.9.8m.
- Fixed 0.9.8m build regression on architectures where %%_lib != lib.

* Thu Mar 25 2010 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8n-alt1
- Updated to 0.9.8n (fixes CVE-2010-0740 and CVE-2010-0433).

* Fri Feb 26 2010 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8m-alt1
- Updated to 0.9.8m with security fixes and improvements, including:
  + CVE-2009-3245, CVE-2008-1678
  + CVE-2009-1377, CVE-2009-1378, CVE-2009-1379
  + CVE-2009-1387 (closes: #20280)
  + CVE-2009-4355 (closes: #22817, #23037)
  + patch for Cisco VPN client DTLS

* Fri Jan 15 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.8l-alt6
- Relocated backwards compatibility symlinks from /%_lib to %_libdir.
- Fixed backwards compatibility Provides on x86-64.

* Fri Jan 15 2010 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8l-alt5
- Added extra symlinks and Provides for backwards compatibility
  with Mandriva's openssl.

* Fri Jan 08 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.8l-alt4
- Built for target linux-generic32 on ARM.
- Applied upstream crypto/{md5,sha1} build fixes (by Evgeny Sinelnikov
  and Kirill A. Shutemov).
- Applied upstream compatibility patch for Cisco VPN client DTLS
  (closes: #22615).

* Sat Nov 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8l-alt1
- Updated to 0.9.8l with security fixes and improvements.
- Includes CVE-2009-3555

* Wed May 27 2009 Dmitry V. Levin <ldv@altlinux.org> 0.9.8k-alt4
- Relocated %_sysconfdir/openssl and %openssldir from
  libssl7 subpackage to libcrypto7 subpackage.

* Wed May 27 2009 Dmitry V. Levin <ldv@altlinux.org> 0.9.8k-alt3
- Packaged libcrypto shared library into separate subpackage
  to break dependency loop (closes: #20175).
- Packaged doc subpackage as noarch.
- Fixed backwards compatibility symlink added in previous build.

* Thu May 21 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8k-alt2
- Added extra symlinks for backwards compatibility with Fedora's libssl8.
- Backported security updates from 0.9.8l:
  CVE-2009-1377, CVE-2009-1378, CVE-2009-1379

* Wed Mar 25 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8k-alt1
- Updated to new 0.9.8k includes security fixes and improvements
- Includes CVE-2009-0789, CVE-2009-0591, CVE-2009-0590

* Thu Jan 08 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8j-alt1
- Updated to 0.9.8j includes properly check EVP_VerifyFinal() and
  similar return values (CVE-2008-5077)

* Tue Dec 09 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8i-alt3
- Added patch with pkcs12 fix for '-name' option

* Wed Nov 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8i-alt2
- Rebuilt without obsolete %post/%postun calls

* Wed Nov 05 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8i-alt1
- Updated to 0.9.8i

* Wed Nov 05 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8h-alt4
- Fixed KRB5 cipher crash for FQDN not equal SPN's FQDN at keytab.
  Resolved with fixing checks at kssl_keytab_is_available()

* Sun Aug 10 2008 Dmitry V. Levin <ldv@altlinux.org> 0.9.8h-alt3
- Updated dependencies (Alexey Tourbin).
- Added workaround for krb5.h inclusion.

* Sat Aug 09 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8h-alt2
- Fixed patches
+ At openssl-0.9.8g-rh-alt-soversion.patch SHLIB_SOVERSION set to 7
+ openssl-0.9.8g-rh-shlib-version.patch changed to openssl-0.9.8h-alt-shlib-version.patch

* Fri Aug 01 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8h-alt1
- Updated to new release
- Removed old fixes

* Fri Aug 01 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8g-alt1
- Prepared to Sisyphus release

* Tue Jun 24 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8g-alt0.eter3
- Added openssl-krb providing

* Fri Jun 13 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8g-alt0.eter2
- Changed soname
+ Renamed libssl6 to libssl7

* Thu Jun 12 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8g-alt0.eter1
- Updated to 0.9.8g
- Removed old patches and got new from Fedora

* Wed Mar 26 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8d-alt4.test2
- Add rfc2712 support with MIT Kerberos.

* Wed Oct 10 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8d-alt4
- Backported upstream fix for off-by-one bug in the
  SSL_get_shared_ciphers() function (CVE-2007-5135).

* Tue Aug 07 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8d-alt3
- Fixed side-channel attack on private keys
  (CVE-2007-3108, RH#245732, http://cvs.openssl.org/chngview?cn=16275).
- Mitigated branch prediction attacks
  (RH#250573, http://cvs.openssl.org/chngview?cn=16077).
- Changed SSL/TLS server implementation to be stricter about session ID
  context matching (RH#233599, http://cvs.openssl.org/chngview?cn=16006).

* Tue Feb 06 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8d-alt2
- Moved a bundle of X.509 certificates of public Certificate
  Authorities (CA) from openssl package to separate ca-certificates
  package.
- Moved %openssldir/{openssl.cnf,cert.pem} from openssl subpackage
  to libssl6 subpackage.

* Sun Nov 05 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.8d-alt1
- openssl: Updated to 0.9.8d.
- TSA patch: Updated to 20060923 (still not applied by default).
- Asymm patch: Updated to 20061110 (still not applied by default).
- Packaged engine and tsget in separate subpackages.
- Makefile.certificate, ca-bundle.crt: Updated from FC.
- Updated FC specific patches from 0.9.8b-12.
- Renamed subpackage according to soname change: libssl4 -> libssl6.

* Thu Nov 02 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.7g-alt6
- Updated upstream bss_conn.c fix.
- Renamed srpm: openssl -> openssl097.
- Renamed subpackage: libssl -> libssl4.

* Wed Sep 27 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.7g-alt5
- Applied upstream fixes for DoS bugs in ASN1 parser
  (CVE-2006-2937, CVE-2006-2940).
- Applied fix for buffer overflow in SSL_get_shared_ciphers(),
  discovery and patch from Tavis Ormandy and Will Drewry of the
  Google Security Team (CVE-2006-3738).
- Applied fix for possible DoS in the sslv2 client code,
  discovery and patch from Tavis Ormandy and Will Drewry of the
  Google Security Team (CVE-2006-4343).
- Build this package without optimizations based on strict aliasing rules.

* Wed Sep 06 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.7g-alt4
- Applied upstream patch to avoid RSA signature forgery (CVE-2006-4339).

* Tue Oct 11 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.7g-alt3
- Applied upstream fix for potential SSL 2.0 rollback
  during SSL handshake (CAN-2005-2969).

* Fri Jun 24 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.7g-alt2
- Minor package cleanup.

* Fri Jun 17 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.7g-alt1
- Removed those of RH patches which I do not like.
- Rediffed patches and renamed them accourding to the packaging policy.
- Relocated development manpages from libssl-devel subpackage to
  openssl-doc subpackage.

* Tue Jun 07 2005 Anton D. Kachalov <mouse@altlinux.org> 0.9.7g-alt0.4
- Added multilib support

* Fri Jun 03 2005 LAKostis <lakostis at altlinux.org> 0.9.7g-alt0.3
- Incorporated patches from Fedora.
- Changed certs dir to be more useful.
- Added provides/requires for tsa (for future use).

* Fri Jun 03 2005 LAKostis <lakostis at altlinux.org> 0.9.7g-alt0.2
- Updated to 0.9.7g.
- Made split build (with/without tsa patch).

* Wed Nov 16 2004 LAKostis <lakostis at altlinux.org> 0.9.7e-alt0.1.ts
- Test build with 0.9.7e.

* Thu Oct 26 2004 LAKostis <lakostis at altlinux.org> 0.9.7d-alt1.ts
- Added timestamping support patch.

* Sat May 08 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.7d-alt1
- Updated to 0.9.7d.
- Reviewed patches.
- Applied RH's soname convention.

* Wed Mar 17 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.6m-alt1
- Updated to 0.9.6m.

* Wed Mar 17 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.6l-alt2
- Fixed null-pointer assignment during SSL handshake
  (CAN-2004-0079).

* Fri Nov 07 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.6l-alt1
- Updated to 0.9.6l.
- For non-i386 ix86 platforms, relaxed textrel check.

* Tue Sep 30 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.6k-alt1
- Updated to 0.9.6k:
  + Fix various ASN1 parsing bugs.
  + SSL/TLS protocol fix for unrequested client certificates.

* Thu Aug 28 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.6j-alt2
- Fixed linux-elf-arm architecture support (sbolshakov@, #2804).
- Shared %_bindir/openssl-config between openssl and
  libssl-devel subpackages (fixes #2806).

* Sat Apr 12 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.6j-alt1
- Updated to 0.9.6j.

* Thu Mar 20 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.6i-alt3
- Applied patch against Klima-Pokorny-Rosa attack.

* Tue Mar 18 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.6i-alt2
- Applied blinding patch from OpenSSL team,
  to defend against timing attack on RSA keys.

* Wed Feb 19 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.6i-alt1
- Updated to 0.9.6i.

* Thu Dec 12 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.6h-alt1
- Updated to 0.9.6h.
- Merged Owl changes:
  * Fri Nov 15 2002 Solar Designer <solar@owl.openwall.com>
  - Dropped the patch removing -Wl,-Bsymbolic which is no longer needed with
    0.9.6g and/or after dropping the explicit "make build-shared".
  - Dropped RSAref stuff.

* Sun Sep 29 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.6g-alt3
- Fixed glibc/crypto compatibility patch.

* Sat Sep 21 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.6g-alt2
- Fixed libssl linkage:
  Don't do an explicit "make build-shared", it's not needed and
  could only cause harm (link libssl against libcrypto statically).
- FHS fixes (#0000915):
  + changed %%openssldir from %_libdir/ssl to /var/lib/ssl;
  + moved openssl.cnf from %%openssldir/ to %_sysconfdir/openssl/;
  + on upgrade, copy old %%openssldir to new location;
  + added openssl-config script to provide current %%openssldir location.
- Renamed openssl-devel subpackage to libssl-devel.
- Renamed openssl-devel-static subpackage to libssl-devel-static.

* Mon Aug 19 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.6g-alt1
- 0.9.6g; asn1_lib patch merged upstream.

* Mon Aug 05 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.6e-alt1
- Updated to 0.9.6e, recent security patch merged upstream.
- Added two post-0.9.6e changes from the CVS which correct the recent ASN.1
  parsing vulnerability fixes (Owl).

* Wed Jul 31 2002 Solar Designer <solar@owl.openwall.com>
- Updated to 0.9.6e, dropping the shared-on-SPARC and the official
  security patches (both are now included).

* Mon Jul 29 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.6d-alt2
- Various security fixes (see CHANGES).

* Mon May 13 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.9.6d-alt1
- Updated to 0.9.6d.
- Added a patch by Ben Laurie for "openssl dgst" to behave on read errors.
- Properly restrict the instruction set in assembly code when building for i386 (Owl).

* Wed Apr 10 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.9.6c-alt3
- Fixed %_bindir/openssl linkage.
- Relocate shared libs to /lib/.

* Thu Mar 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.9.6c-alt2
- libssl: Conflicts: %%name < %%version-%%release.

* Tue Jan 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.9.6c-alt1
- 0.9.6c
- Relocated docs.

* Wed Jul 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.6b-alt1
- 0.9.6b

* Fri Jun 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.6a-alt2
- Changed two memcpy() calls to memmove() (nalin).
- Added a script for creating dummy certificates (nalin).

* Mon May 14 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.6a-alt1
- 0.9.6a
- Keep standard soname scheme.
- Do not provide crypt symbol (solar).
- Use __libc_enable_secure variable (solar).
- Link %_bindir/openssl dinamically with shared libraries from libssl subpackage (solar).

* Wed Apr 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.6-ipl2mdk
- Moved shared libraries to libssl subpackage.
- Moved static libraries to devel-static subpackage.

* Thu Sep 28 2000 Dmitry V. Levin <ldv@fandra.org> 0.9.6-ipl1mdk
- 0.9.6

* Wed May 31 2000 Dmitry V. Levin <ldv@fandra.org>
- 0.9.5a

* Fri Apr 28 2000 Dmitry V. Levin <ldv@fandra.org>
- separate openssl-doc package
- 0.9.5

* Sun Dec  5 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Sun Nov 28 1999 Arne Coucheron <arneco@online.no>
  [0.9.4-3]
- config file moved to /var/ssl due to problems when it stays in /etc

* Tue Aug 17 1999 Arne Coucheron <arneco@online.no>
  [0.9.4-2]
- the source rpm was corrupt, so this is just a rerelase

* Wed Aug 11 1999 Arne Coucheron <arneco@online.no>
  [0.9.4-1]

* Sun Jun 20 1999 Arne Coucheron <arneco@online.no>
  [0.9.3a-1]
- several changes
