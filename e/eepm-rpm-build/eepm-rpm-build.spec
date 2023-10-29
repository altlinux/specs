%define rpmhome %_libexecdir/eepm-rpm
%define rpmlibdir %_libdir/eepm-rpm

%define major 4.18
%define verbase %major.x
%global soversion 9
%define default_payload w2T.xzdio

Name: eepm-rpm-build
Version: %major.1
Release: alt2

Summary: Simplified RPM rpmbuild used in epm repack

License: GPLv2+
Group: System/Configuration/Packaging
Url: http://www.rpm.org/

# Source-url: http://ftp.rpm.org/releases/rpm-%verbase/rpm-%version.tar.bz2
Source: %name-%version.tar

BuildRequires: gawk
#BuildRequires: elfutils-devel >= 0.112
#BuildRequires: elfutils-libelf-devel
BuildRequires: libreadline-devel
BuildRequires: popt-devel
#BuildRequires: file-devel
#BuildRequires: gettext-devel
#BuildRequires: libncurses-devel

BuildRequires: zlib-devel
BuildRequires: bzlib-devel >= 0.9.0c-2
BuildRequires: liblzma-devel >= 4.999.8
BuildRequires: libzstd-devel

BuildRequires: liblua5-devel >= 5.1
BuildRequires: libcap-devel
BuildRequires: libacl-devel

#BuildRequires: libssl-devel
BuildRequires: libgcrypt-devel
BuildRequires: libmagic-devel
BuildRequires: libarchive-devel

%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages.

The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.

This rpmbuild built in distro agnostic way to support epm repack.

%prep
%setup
%__subst 's|/lib/rpm|/lib/eepm-rpm|' configure.ac Makefile.am rpm.am
%__subst "s|#%%_source_payload.*|%%_source_payload	%default_payload|" macros.in
%__subst "s|#%%_binary_payload.*|%%_binary_payload	%default_payload|" macros.in

%build
%configure \
	--with-vendor=EEPM \
	--disable-ndb \
	--disable-plugins \
	--disable-sqlite \
	--enable-zstd \
	--with-cap \
	--with-acl \
	--libdir=%rpmlibdir \
	--localstatedir=/var \
	#

%make_build

%install
%makeinstall_std

mv %buildroot%_bindir/rpmbuild %buildroot%_bindir/eepm-rpmbuild
%__subst 's|%_libexecdir/rpm/rpmdeps|%rpmhome/rpmdeps|' %buildroot%rpmhome/{find-provides,find-requires}
# pass compression tools
echo "exit 0" > %buildroot%rpmhome/brp-compress

rm %buildroot%_bindir/rpm*
rm %buildroot%_bindir/gendiff
rm -r %buildroot%_includedir/

rm %buildroot%rpmhome/mkinstalldirs
rm %buildroot%rpmhome/rpm.daily
rm %buildroot%rpmhome/rpm.log
rm %buildroot%rpmhome/rpm2cpio.sh
rm %buildroot%rpmhome/rpmdb_*
rm %buildroot%rpmhome/tgpg

rm %buildroot%rpmlibdir/librpm*.so
rm %buildroot%rpmlibdir/librpmsign.so.*
rm %buildroot%rpmlibdir/librpm*.la

rm -r %buildroot%rpmlibdir/pkgconfig/
rm -rf %buildroot%_datadir/locale/
rm -rf %buildroot%_mandir/

%files
%attr(0755, root, root) %dir %rpmhome
%rpmhome/macros
%rpmhome/macros.d
%rpmhome/lua
%rpmhome/rpmpopt*
%rpmhome/rpmrc

#rpmhome/rpmdb_*
%rpmhome/rpm.supp
#rpmhome/rpm2cpio.sh
#rpmhome/tgpg

%rpmhome/platform

%dir %rpmhome/fileattrs

%dir %rpmlibdir/
%rpmlibdir/librpmio.so.%soversion
%rpmlibdir/librpm.so.%soversion
%rpmlibdir/librpmio.so.%soversion.*
%rpmlibdir/librpm.so.%soversion.*
%rpmlibdir/librpmbuild.so.%soversion
%rpmlibdir/librpmbuild.so.%soversion.*
#%_libdir/librpmsign.so.%soversion
#%_libdir/librpmsign.so.%soversion.*

%_bindir/eepm-rpmbuild

%rpmhome/brp-*
%rpmhome/check-*
%rpmhome/find-lang.sh
%rpmhome/*provides*
%rpmhome/*requires*
%rpmhome/*deps*
%rpmhome/*.prov
%rpmhome/*.req
%rpmhome/fileattrs/*
%rpmhome/rpmuncompress

%changelog
* Sun Oct 29 2023 Vitaly Lipatov <lav@altlinux.ru> 4.18.1-alt2
- use major macro in the spec
- set correct localstatedir /var

* Mon Jul 31 2023 Vitaly Lipatov <lav@altlinux.ru> 4.18.1-alt1
- initial build for ALT Sisyphus
