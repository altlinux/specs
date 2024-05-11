# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: aide
Version: 0.18.8
Release: alt1
Summary: Intrusion Detection Environment
License: GPL-2.0-or-later
Group: System/Base
Url: https://aide.github.io/
Vcs: https://github.com/aide/aide

Source: %name-%version.tar

BuildRequires: autoconf-archive
BuildRequires: flex
BuildRequires: libacl-devel
BuildRequires: libattr-devel
BuildRequires: libaudit-devel
BuildRequires: libcap-devel
BuildRequires: libcheck-devel
BuildRequires: libcurl-devel
BuildRequires: libe2fs-devel
BuildRequires: libgcrypt-devel
BuildRequires: libpcre2-devel
BuildRequires: libselinux-devel
BuildRequires: zlib-devel
%description
AIDE is an intrusion detection system for checking the integrity of files.

%prep
%setup

# Remove garbage algorithms
sed -i \
    -e 's/GCRY_MD_MD5/-1/' \
    -e 's/GCRY_MD_SHA1/-1/' \
    -e 's/GCRY_MD_RMD160/-1/' \
    -e 's/GCRY_MD_TIGER/-1/' \
    -e 's/GCRY_MD_WHIRLPOOL/-1/' src/hashsum.c
# Replace md5 in 'R' with sha256
sed -i 's/attr_md5/attr_sha256/' src/aide.c

%build
echo "m4_define([AIDE_VERSION], [%version])" > version.m4
%autoreconf
%add_optflags %(getconf LFS_CFLAGS)
%configure \
	--disable-static \
	--with-audit \
	--with-capabilities \
	--with-config_file=%_sysconfdir/aide.conf \
	--with-curl \
	--with-e2fsattrs \
	--with-extra-includes=-I%_includedir/pcre \
	--with-gcrypt \
	--with-posix-acl \
	--with-selinux \
	--with-xattr \
	--with-zlib \
	%nil
%make_build

%install
%makeinstall_std bindir=%_sbindir
install -dm700 %buildroot%_localstatedir/%name
install -dm700 %buildroot%_logdir/%name
# Example config
install -Dpm600 .gear/aide.conf -t %buildroot%_sysconfdir
# Running AIDE locally is not completely meaningful (as the database could be
# modified under root) so user is free to configure it themselves.

%define _customdocdir %_docdir/%name

%check
./aide --version
make check
.gear/test.sh %buildroot

%files
%doc AUTHORS COPYING ChangeLog README NEWS contrib SECURITY.md
%config(noreplace) %attr(0600,root,root) %_sysconfdir/aide.conf
%_sbindir/aide
%dir %attr(0700,root,root) %_localstatedir/%name
%dir %attr(0700,root,root) %_logdir/%name
%_man1dir/*.1*
%_man5dir/*.5*

%changelog
* Sat May 11 2024 Vitaly Chikunov <vt@altlinux.org> 0.18.8-alt1
- Update to v0.18.8 (2024-05-09).

* Mon May 06 2024 Vitaly Chikunov <vt@altlinux.org> 0.18.7-alt1
- Update to v0.18.7 (2024-05-04).

* Thu Aug 03 2023 Vitaly Chikunov <vt@altlinux.org> 0.18.6-alt1
- Update to v0.18.6 (2023-08-01).

* Wed Jul 12 2023 Vitaly Chikunov <vt@altlinux.org> 0.18.5-alt1
- Update to v0.18.5 (2023-06-30).

* Thu Jun 15 2023 Vitaly Chikunov <vt@altlinux.org> 0.18.4-alt1
- Update to v0.18.4 (2023-06-13).

* Sat May 20 2023 Vitaly Chikunov <vt@altlinux.org> 0.18.3-alt1
- Update to v0.18.3 (2023-05-16).

* Sat Apr 08 2023 Vitaly Chikunov <vt@altlinux.org> 0.18.2-alt1
- Update to v0.18.2 (2023-04-07).

* Fri Feb 03 2023 Vitaly Chikunov <vt@altlinux.org> 0.17.4-alt1
- First import v0.17.4 (2022-01-19).
