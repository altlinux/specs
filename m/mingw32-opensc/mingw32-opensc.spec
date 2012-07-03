Name: mingw32-opensc
Version: 0.11.8
Release: alt1
Summary: MingGW Windows OpenSC library

Group: System/Libraries
License: LGPLv2+
Url: http://www.opensc-project.org/opensc/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://www.opensc-project.org/files/opensc/opensc-%version.tar.gz
Patch1: opensc-0.11.7-develconfig.patch

BuildArch: noarch

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-iconv
BuildRequires: mingw32-libltdl
BuildRequires: mingw32-openssl
BuildRequires: mingw32-readline

Requires: pkgconfig

%description
OpenSC is a package for for accessing smart card devices.  Basic
functionality (e.g. SELECT FILE, READ BINARY) should work on any ISO
7816-4 compatible smart card.  Encryption and decryption using private
keys on the smart card is possible with PKCS #15 compatible cards,
such as the FINEID (Finnish Electronic IDentity) card.  Swedish Posten
eID cards have also been confirmed to work.

This is the MinGW cross-compiled Windows library.

%prep
%setup -q -n opensc-%version
%patch1 -p1 -b .config

%__subst 's|"/lib /usr/lib\b|"%_mingw32_libdir|' configure # lib64 rpaths
cp -p src/pkcs15init/README ./README.pkcs15init
cp -p src/scconf/README.scconf .
# No %_mingw32_libdir here to avoid multilib conflicts; it's just an example
%__subst 's|/usr/local/towitoko/lib/|%_libdir/ctapi/|' etc/opensc.conf.in

%build
%_mingw32_configure  --disable-static \
  --enable-pcsc \
  --enable-iconv
%make_build

%install
%makeinstall_std
install -Dpm 644 etc/opensc.conf %buildroot%_mingw32_sysconfdir/opensc.conf

mv -T %buildroot%_mingw32_datadir/doc/opensc docdir

# Remove a wrapper shell script
rm -f %buildroot%_mingw32_bindir/cardos-info

%files
%doc COPYING NEWS README*
%doc docdir/*
%config(noreplace) %_mingw32_sysconfdir/opensc.conf

%_mingw32_bindir/cardos-info.bat
%_mingw32_bindir/cardos-tool.exe
%_mingw32_bindir/cryptoflex-tool.exe
%_mingw32_bindir/eidenv.exe
%_mingw32_bindir/netkey-tool.exe
%_mingw32_bindir/opensc-config
%_mingw32_bindir/opensc-explorer.exe
%_mingw32_bindir/opensc-tool.exe
%_mingw32_bindir/piv-tool.exe
%_mingw32_bindir/pkcs11-tool.exe
%_mingw32_bindir/pkcs15-crypt.exe
%_mingw32_bindir/pkcs15-init.exe
%_mingw32_bindir/pkcs15-tool.exe
%_mingw32_bindir/rutoken-tool.exe

%_mingw32_bindir/libopensc-2.dll
%_mingw32_bindir/libpkcs15init-2.dll
%_mingw32_bindir/libscconf-2.dll
%_mingw32_bindir/onepin-opensc-pkcs11.dll
%_mingw32_bindir/opensc-pkcs11.dll
%_mingw32_bindir/pkcs11-spy.dll

%_mingw32_libdir/libopensc-2.dll.def
%_mingw32_libdir/libopensc.dll.a
%_mingw32_libdir/libopensc.la
%_mingw32_libdir/libpkcs15init-2.dll.def
%_mingw32_libdir/libpkcs15init.dll.a
%_mingw32_libdir/libpkcs15init.la
%_mingw32_libdir/libscconf.dll.a
%_mingw32_libdir/libscconf.la
%_mingw32_libdir/onepin-opensc-pkcs11.dll.a
%_mingw32_libdir/onepin-opensc-pkcs11.la
%_mingw32_libdir/opensc-pkcs11.dll.a
%_mingw32_libdir/opensc-pkcs11.la
%_mingw32_libdir/pkcs11-spy.dll.a
%_mingw32_libdir/pkcs11-spy.la

%_mingw32_includedir/opensc/
%_mingw32_libdir/pkgconfig/lib*.pc
%_mingw32_datadir/opensc/
%_mingw32_sbindir/opensc-install.bat

%changelog
* Sat Sep 19 2009 Boris Savelev <boris@altlinux.org> 0.11.8-alt1
- initial build for Sisyphus

* Sun Aug 30 2009 Kalev Lember <kalev@smartlink.ee> - 0.11.8-4
- Rebuilt with new mingw32-openssl

* Sun Aug 23 2009 Kalev Lember <kalev@smartlink.ee> - 0.11.8-3
- Automatically generate debuginfo subpackage

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 13 2009 Kalev Lember <kalev@smartlink.ee> - 0.11.8-1
- Update to 0.11.8, fixes a security issue.
- Remove iconv detection patch that was applied upstream.

* Fri Apr 17 2009 Kalev Lember <kalev@smartlink.ee> - 0.11.7-3
- Replace %%define with %%global.

* Mon Mar 23 2009 Kalev Lember <kalev@smartlink.ee> - 0.11.7-2
- Include *.la files in the rpm.
- Patch configure.ac to fix iconv detection.

* Mon Mar 23 2009 Kalev Lember <kalev@smartlink.ee> - 0.11.7-1
- Initial RPM release.
