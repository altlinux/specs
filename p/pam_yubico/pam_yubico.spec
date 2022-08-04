%define _unpackaged_files_terminate_build 1

%def_without check

%def_with ldap
%def_with mysql

Name: pam_yubico
Version: 2.27
Release: alt3

Summary: Yubico Pluggable Authentication Module (PAM)
License: BSD-2-Clause
Group: System/Base
Url: https://github.com/Yubico/yubico-pam

Source: %name-%version.tar
Patch0: pam_yubico-2.27-alt-fix-pam_strerror-signature.patch

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
%if_with check
BuildRequires: perl-Net-LDAP-Server
%endif
%if_with ldap
BuildRequires: libldap-devel
%endif
%if_with mysql
BuildRequires: libMySQL-devel
%endif
%if %{with mysql} && %{with check}
BuildRequires: /proc
BuildRequires: rpm-build-vm
BuildRequires: MySQL-server
%endif

%description
The Yubico PAM module provides an easy way to integrate the YubiKey
into your existing user authentication infrastructure. PAM is used by
GNU/Linux, Solaris and Mac OS X for user authentication, and by other
specialized applications such as NCSA MyProxy.

%prep
%setup
%patch0 -p1

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

%check
# force run mysql tests
%if_with mysql
sed -i tests/pam_test.c -e '/#define YKVAL_PORT1/i #define RUN_MYSQL_TESTS 1'
%endif

# autotests require running mysqld, so they don't work
vm-run "%make_install check"

%files
%doc README AUTHORS BLURB COPYING NEWS
%_bindir/*
%_pam_modules_dir/*.so
%_man1dir/*
%_man8dir/*

%changelog
* Thu Aug 04 2022 Anton Zhukharev <ancieg@altlinux.org> 2.27-alt3
- build with ldap and mysql support

* Thu Aug 04 2022 Anton Zhukharev <ancieg@altlinux.org> 2.27-alt2
- remove ykpamcfg subpackage

* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 2.27-alt1
- initial build for Sisyphus

