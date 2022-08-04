%define _unpackaged_files_terminate_build 1

%def_without ldap
%def_without mysql

Name: pam_yubico
Version: 2.27
Release: alt2

Summary: Yubico Pluggable Authentication Module (PAM)
License: BSD-2-Clause
Group: System/Base
Url: https://github.com/Yubico/yubico-pam

Source: %name-%version.tar

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: asciidoc
BuildRequires: asciidoc-a2x
BuildRequires: xsltproc
BuildRequires: docbook-style-xsl
BuildRequires: libykclient-devel
BuildRequires: libyubikey-devel
BuildRequires: libykpers-1-devel
BuildRequires: libpam-devel

%description
The Yubico PAM module provides an easy way to integrate the YubiKey
into your existing user authentication infrastructure. PAM is used by
GNU/Linux, Solaris and Mac OS X for user authentication, and by other
specialized applications such as NCSA MyProxy.

%prep
%setup

%build
%autoreconf
%configure %{subst_with ldap} \
           %{subst_with mysql} \
           --with-pam-dir=%_pam_modules_dir
%make_build
cp -r README AUTHORS BLURB COPYING NEWS %_builddir/

%install
%makeinstall_std
rm -f %buildroot%_pam_modules_dir/*.la

%files
%doc README AUTHORS BLURB COPYING NEWS
%_bindir/*
%_pam_modules_dir/*.so
%_man1dir/*
%_man8dir/*

%changelog
* Thu Aug 04 2022 Anton Zhukharev <ancieg@altlinux.org> 2.27-alt2
- remove ykpamcfg subpackage

* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 2.27-alt1
- initial build for Sisyphus

