# For the curious:
# 0.9.5a soversion = 0
# 0.9.6  soversion = 1
# 0.9.6a soversion = 2
# 0.9.6c soversion = 3
# 0.9.7a soversion = 4
# 0.9.7ef soversion = 5
# 0.9.8ab soversion = 6
# 0.9.8g soversion = 7
# 0.9.8jk + EAP-FAST soversion = 8
# 1.0.0 soversion = 10
%global soversion 10

# Enable the tests.
# These only work some of the time, but fail randomly at other times
# (although I have had them complete a few times, so I don't think
# there is any actual problem with the binaries).
%global run_tests 0

# Number of threads to spawn when testing some threading fixes.
%global thread_test_threads %{?threads:%threads}%{!?threads:1}

Name: mingw32-openssl
Version: 1.0.0a
Release: alt1
Summary: MinGW port of the OpenSSL toolkit

License: OpenSSL
Group: System/Libraries
Url: http://www.openssl.org/

Packager: Boris Savelev <boris@altlinux.org>

# We remove certain patented algorithms from the openssl source tarball
# with the hobble-openssl script which is included below.
Source: openssl-%version-usa.tar.bz2

Source1: hobble-openssl
Source2: Makefile.certificate
Source6: make-dummy-cert
Source8: openssl-thread-test.c
Source9: opensslconf-new.h
Source10: opensslconf-new-warning.h

# Patches from Fedora native package.
# Build changes
Patch: openssl-1.0.0-beta4-redhat.patch
Patch1: openssl-1.0.0-beta3-defaults.patch
Patch3: openssl-1.0.0-beta3-soversion.patch
Patch4: openssl-1.0.0-beta5-enginesdir.patch
Patch5: openssl-0.9.8a-no-rpath.patch
Patch6: openssl-0.9.8b-test-use-localhost.patch
Patch7: openssl-1.0.0-timezone.patch
# Bug fixes
Patch23: openssl-1.0.0-beta4-default-paths.patch
Patch24: openssl-0.9.8j-bad-mime.patch
# Functionality changes
Patch32: openssl-0.9.8g-ia64.patch
Patch33: openssl-1.0.0-beta4-ca-dir.patch
Patch34: openssl-0.9.6-x509.patch
Patch35: openssl-0.9.8j-version-add-engines.patch
Patch38: openssl-1.0.0-beta5-cipher-change.patch
# Disabled this because it uses getaddrinfo which is lacking on Windows.
#Patch39:        openssl-1.0.0-beta5-ipv6-apps.patch
Patch40: openssl-1.0.0a-fips.patch
Patch41: openssl-1.0.0-beta3-fipscheck.patch
Patch43: openssl-1.0.0a-fipsmode.patch
Patch44: openssl-1.0.0-beta3-fipsrng.patch
Patch45: openssl-0.9.8j-env-nozlib.patch
Patch47: openssl-1.0.0-beta5-readme-warning.patch
Patch49: openssl-1.0.0-beta4-algo-doc.patch
Patch50: openssl-1.0.0-beta4-dtls1-abi.patch
Patch51: openssl-1.0.0a-version.patch
Patch52: openssl-1.0.0-beta4-aesni.patch
Patch53: openssl-1.0.0-name-hash.patch
# Backported fixes including security fixes

# MinGW-specific patches.
# Rename *eay32.dll to lib*.dll
Patch101: mingw32-openssl-1.0.0-beta3-libversion.patch
# Fix engines/ install target after lib rename
Patch102: mingw32-openssl-1.0.0a-sfx.patch

BuildArch: noarch

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils

BuildRequires: mingw32-zlib
BuildRequires: mingw32-pthreads
BuildRequires: mingw32-dlfcn

#BuildRequires:  krb5-devel
BuildRequires: perl-devel perl-WWW-Curl perl4-compat

# XXX Not really sure about this one.  The build script uses
# %_bindir/makedepend which comes from imake.
BuildRequires: imake

%if %run_tests
# Required both to build, and to run the tests.
# XXX This needs to be fixed - cross-compilation should not
# require running executables.
BuildRequires: %_bindir/wine

# Required to run the tests.
BuildRequires: xorg-xvfb
%endif

#Requires:       ca-certificates >= 2008-5
Requires: pkgconfig

%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains Windows (MinGW) libraries and development tools.

%package static
Summary: Static version of the MinGW port of the OpenSSL toolkit
Group: System/Libraries
Requires: %name = %version-%release

%description static
Static version of the MinGW port of the OpenSSL toolkit.

%prep
%setup -n openssl-%version

%SOURCE1 > /dev/null
%patch0 -p1 -b .redhat
%patch1 -p1 -b .defaults
%patch3 -p1 -b .soversion
%patch4 -p1 -b .enginesdir
%patch5 -p1 -b .no-rpath
%patch6 -p1 -b .use-localhost
%patch7 -p1 -b .timezone

%patch23 -p1 -b .default-paths
%patch24 -p1 -b .bad-mime

%patch32 -p1 -b .ia64
#patch33 is applied after make test
%patch34 -p1 -b .x509
%patch35 -p1 -b .version-add-engines
%patch38 -p1 -b .cipher-change
#%patch39 -p1 -b .ipv6-apps
%patch40 -p1 -b .fips
%patch41 -p1 -b .fipscheck
%patch43 -p1 -b .fipsmode
%patch44 -p1 -b .fipsrng
%patch45 -p1 -b .env-nozlib
%patch47 -p1 -b .warning
%patch49 -p1 -b .algo-doc
%patch50 -p1 -b .dtls1-abi
%patch51 -p1 -b .version
%patch52 -p1 -b .aesni
%patch53 -p1 -b .name-hash

%patch101 -p1 -b .mingw-libversion
%patch102 -p1 -b .mingw-sfx

# Use _mingw32_cflags instead of hardcoded ones
%__subst '/^"mingw"/ s/-fomit-frame-pointer -O3 -march=i486 -Wall/%_mingw32_cflags/' Configure

# Modify the various perl scripts to reference perl in the right location.
perl util/perlpath.pl `dirname %__perl`

# Generate a table with the compile settings for my perusal.
touch Makefile
make TABLE PERL=%__perl

%build
# NB: 'no-hw' is vital.  MinGW cannot build the hardware drivers
# and if you don't have this you'll get an obscure link error.
export MINGW32_CFLAGS="%_mingw32_cflags"; \
./Configure \
  --prefix=%_mingw32_prefix \
  --openssldir=%_mingw32_sysconfdir/pki/tls \
  zlib enable-camellia enable-seed enable-tlsext enable-rfc3779 \
  enable-cms enable-md2 no-idea no-mdc2 no-rc5 no-ec no-ecdh no-ecdsa \
  no-capieng \
  no-hw --cross-compile-prefix=%_mingw32_target- \
  --enginesdir=%_mingw32_libdir/openssl/engines \
  shared mingw
#  --with-krb5-flavor=MIT
#  -I%_mingw32_prefix/kerberos/include -L%_mingw32_prefix/kerberos/%_lib

# Regenerate def files as we disabled some algorithms above
perl util/mkdef.pl crypto ssl update

make depend
make all build-shared

# Generate hashes for the included certs.
make rehash build-shared

%if %run_tests
#----------------------------------------------------------------------
# Run some tests.  I don't know why this isn't in a %-check section
# but this is how it is in the native RPM.

# This is a bit of a hack, but the test scripts look for 'openssl'
# by name.
pushd apps
ln -s openssl.exe openssl
popd

# This is useful for diagnosing Wine problems.
WINEDEBUG=+loaddll
export WINEDEBUG

# Make sure we can find the installed DLLs.
WINEDLLPATH=%_mingw32_bindir
export WINEDLLPATH

# The tests run Wine and require an X server (but don't really use
# it).  Therefore we create a virtual framebuffer for the duration of
# the tests.
# XXX There is no good way to choose a random, unused display.
# XXX Setting depth to 24 bits avoids bug 458219.
unset DISPLAY
display=:21
Xvfb $display -screen 0 1024x768x24 -ac -noreset & xpid=$!
trap "kill -TERM $xpid ||:" EXIT
sleep 3
DISPLAY=$display
export DISPLAY

make LDCMD=%_mingw32_cc -C test apps tests

# Disable this thread test, because we don't have pthread on Windows.
%_mingw32_cc -o openssl-thread-test \
  -I./include \
%-{_mingw32_cflags} \
%-{SOURCE8} \
  -L. \
  -lssl -lcrypto \
  -lpthread -lz -ldl

## `krb5-config --cflags`
## `krb5-config --libs`
#
./openssl-thread-test --threads %thread_test_threads

#----------------------------------------------------------------------
%endif

# Patch33 must be patched after tests otherwise they will fail
patch -p1 -b -z .ca-dir < %PATCH33

# Add generation of HMAC checksum of the final stripped library
#%define __spec_install_post \
#    %{?__debug_package:%__debug_install_post} \
#    arch_install_post \
#    %__os_install_post \
#    fips/fips_standalone_sha1 %buildroot%_lib/libcrypto.so.%version >%buildroot%_lib/.libcrypto.so.%version.hmac \
#    ln -sf .libcrypto.so.%version.hmac %buildroot%_lib/.libcrypto.so.%soversion.hmac \
#%nil

if ! iconv -f UTF-8 -t ASCII//TRANSLIT CHANGES >/dev/null 2>&1 ; then
  iconv -f ISO-8859-1 -t UTF-8 -o CHANGES.utf8 CHANGES && \
    mv -f CHANGES.utf8 CHANGES
fi

%install
mkdir -p %buildroot%_mingw32_libdir
mkdir -p %buildroot%_mingw32_libdir/openssl
mkdir -p %buildroot%_mingw32_bindir
mkdir -p %buildroot%_mingw32_includedir
mkdir -p %buildroot%_mingw32_mandir
make INSTALL_PREFIX=%buildroot install build-shared

# Install the file applink.c (#499934)
install -m644 ms/applink.c %buildroot%_mingw32_includedir/openssl/applink.c

# I have no idea why it installs the manpages in /etc, but
# we remove them anyway.
rm -r %buildroot%_mingw32_sysconfdir/pki/tls/man

# Set permissions on lib*.dll.a so that strip works.
chmod 0755 %buildroot%_mingw32_libdir/libcrypto.dll.a
chmod 0755 %buildroot%_mingw32_libdir/libssl.dll.a

# Install a makefile for generating keys and self-signed certs, and a script
# for generating them on the fly.
mkdir -p %buildroot%_mingw32_sysconfdir/pki/tls/certs
install -m644 %SOURCE2 %buildroot%_mingw32_sysconfdir/pki/tls/certs/Makefile
install -m755 %SOURCE6 %buildroot%_mingw32_sysconfdir/pki/tls/certs/make-dummy-cert

# Pick a CA script.
pushd  %buildroot%_mingw32_sysconfdir/pki/tls/misc
mv CA.sh CA
popd

mkdir -m700 %buildroot%_mingw32_sysconfdir/pki/CA
mkdir -m700 %buildroot%_mingw32_sysconfdir/pki/CA/private

%__subst "s|/usr/local/bin/perl|%_bindir/perl|g" \
%buildroot%_mingw32_sysconfdir/pki/tls/misc/CA.pl \
%buildroot%_mingw32_bindir/c_rehash

%files
%doc LICENSE
%_mingw32_bindir/openssl.exe
%_mingw32_bindir/c_rehash
%_mingw32_bindir/libcrypto-%soversion.dll
%_mingw32_bindir/libssl-%soversion.dll
#{_mingw32_bindir}/.libcrypto*.hmac
%_mingw32_libdir/libcrypto.dll.a
%_mingw32_libdir/libssl.dll.a
%_mingw32_libdir/engines
%_mingw32_libdir/pkgconfig/*.pc
%_mingw32_includedir/openssl
%config(noreplace) %_mingw32_sysconfdir/pki

%files static
%_mingw32_libdir/libcrypto.a
%_mingw32_libdir/libssl.a

%changelog
* Wed Dec 29 2010 Boris Savelev <boris@altlinux.org> 1.0.0a-alt1
- new version from Fedora

* Sat Jun 19 2010 Kalev Lember <kalev@smartlink.ee> - 1.0.0a-1
- Updated to openssl 1.0.0a
- Synced patches with Fedora native openssl-1.0.0a-1
- Use sed to fix up cflags instead of unmaintainable patch
- Rebased mingw32 specific patches
- Disabled capieng to fix build
- Properly regenerate def files with mkdef.pl and drop linker-fix.patch

* Thu Nov 26 2009 Kalev Lember <kalev@smartlink.ee> - 1.0.0-0.6.beta4
- Merged patches from native Fedora openssl (up to 1.0.0-0.16.beta4)
- Dropped the patch to fix non-fips mingw build,
  as it's now merged into fips patch from native openssl

* Sun Nov 22 2009 Kalev Lember <kalev@smartlink.ee> - 1.0.0-0.5.beta4
- Updated to version 1.0.0 beta 4
- Merged patches from native Fedora openssl (up to 1.0.0-0.15.beta4)
- Added patch to fix build with fips disabled

* Fri Sep 18 2009 Kalev Lember <kalev@smartlink.ee> - 1.0.0-0.4.beta3
- Rebuilt to fix debuginfo

* Sun Aug 30 2009 Kalev Lember <kalev@smartlink.ee> - 1.0.0-0.3.beta3
- Simplified the lib renaming patch

* Sun Aug 30 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.0-0.2.beta3
- Fixed invalid RPM Provides

* Fri Aug 28 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.0-0.1.beta3
- Update to version 1.0.0 beta 3
- Use %%global instead of %%define
- Automatically generate debuginfo subpackage
- Merged various changes from the native Fedora package (up to 1.0.0-0.5.beta3)
- Don't use the %%{_mingw32_make} macro anymore as it's ugly and causes side-effects
- Added missing BuildRequires mingw32-dlfcn (Kalev Lember)
- Reworked patches to rename *eay32.dll to lib*.dll (Kalev Lember)
- Patch Configure script to use %%{_mingw32_cflags} (Kalev Lember)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8j-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.8j-6
- Add the file include/openssl/applink.c to the package (BZ #499934)

* Tue Apr 14 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.8j-5
- Fixed %%defattr line
- Added -static subpackage

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8j-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.8j-3
- Rebuild for mingw32-gcc 4.4

* Mon Feb  2 2009 Levente Farkas <lfarkas@lfarkas.org> - 0.9.8j-2
- Various build fixes.

* Wed Jan 28 2009 Levente Farkas <lfarkas@lfarkas.org> - 0.9.8j-1
- update to new upstream version.

* Mon Dec 29 2008 Levente Farkas <lfarkas@lfarkas.org> - 0.9.8g-2
- minor cleanup.

* Tue Sep 30 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9.8g-1
- Initial RPM release.
