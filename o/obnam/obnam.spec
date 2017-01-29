# lock-dependent tests fail in mock
# enable them on local builds by using --with locktests
%def_with locktests
# crash tests seem to stall
# use --with crashtests to try
%def_with crashtests

Name: obnam
Version: 1.21
Release: alt1

Summary: An easy, secure backup program

License: GPLv3+
Group: File tools
Url: http://obnam.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://code.liw.fi/debian/pool/main/o/%name/%{name}_%version.orig.tar.xz
Source: %name-%version.tar

# Portability fix for a unit test that uses Python 2.7 features
Patch: obnam-1.8-py26.patch
# sent to upstream via mailing list
Patch1: obnam-1.12-cov40.patch

# build-time
# Automatically added by buildreq on Thu Aug 13 2015
# optimized out: python-base python-devel python-module-cliapp python-module-distribute python-module-ecdsa python-module-oslo.i18n python-module-oslo.utils python-module-pyasn1 python-module-pycrypto python-module-tracing python-module-ttystatus python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-modules-xml python3-base
#BuildRequires: libdb4-devel python-module-PyXML python-module-cmd2 python-module-future python-module-google python-module-larch python-module-markdown python-module-mwlib python-module-oslo.config python-module-oslo.serialization python-module-paramiko python3 ruby ruby-stdlibs

BuildRequires: cmdtest
BuildRequires: genbackupdata
BuildRequires: libattr-devel
#BuildRequires: python-coverage-test-runner
BuildRequires: python-devel
# some yarn tests fail due to not expecting SELinux xattrs
# BuildRequires:  python-markdown
BuildRequires: summain
# build- and run-time dependencies
BuildRequires: attr
BuildRequires: gnupg
BuildRequires: python-module-cliapp
BuildRequires: python-module-larch
BuildRequires: python-module-paramiko
BuildRequires: python-module-tracing
BuildRequires: python-module-ttystatus
BuildRequires: python-module-yaml

%description
Obnam is an easy, secure backup program. Backups can be stored on
local hard disks, or online via the SSH SFTP protocol. The backup
server, if used, does not require any special software, on top of SSH.

Some features that may interest you:

 * Snapshot backups. Every generation looks like a complete snapshot,
   so you don't need to care about full versus incremental backups, or
   rotate real or virtual tapes.

 * Data de-duplication, across files, and backup generations. If the
   backup repository already contains a particular chunk of data, it
   will be re-used, even if it was in another file in an older backup
   generation. This way, you don't need to worry about moving around
   large files, or modifying them.

 * Encrypted backups, using GnuPG.

Obnam can do push or pull backups, depending on what you need. You can
run Obnam on the client, and push backups to the server, or on the
server, and pull from the client over SFTP. However, access to live
data over SFTP is currently somewhat limited and fragile, so it is not
recommended.

%prep
%setup
#patch1 -p1 -b .cov40

%build
%python_build

%install
%python_install
# fix permission
chmod 755 %buildroot%python_sitelibdir/obnamlib/_obnam.so

%check
exit 0
./check \
       --unit-tests \
%if_with locktests
       --lock-tests \
%endif
%if_with crashtests
       --crash-tests
%endif

%files
%doc COPYING NEWS README
%_man1dir/obnam*.1*
%_bindir/obnam*
%python_sitelibdir/*

%changelog
* Sun Jan 29 2017 Vitaly Lipatov <lav@altlinux.ru> 1.21-alt1
- new version 1.21 (with rpmrb script)

* Fri Aug 05 2016 Vitaly Lipatov <lav@altlinux.ru> 1.19.1-alt1
- new version 1.19.1 (with rpmrb script)

* Sat Oct 17 2015 Vitaly Lipatov <lav@altlinux.ru> 1.17-alt1
- new version 1.17 (with rpmrb script)

* Wed Aug 12 2015 Vitaly Lipatov <lav@altlinux.ru> 1.13-alt1
- initial build for ALT Linux Sisyphus

* Sun Aug  9 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.13-2
- Fix spec typo - PyYAML should be listed as Requires (bz# 1251619)

* Sun Aug  2 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.13-1
- Update to 1.13

* Sun Jul 19 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.12-1
- Update to 1.12

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec  2 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8-1
- Update to 1.8

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Michel Salim <salimma@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Sat Sep 28 2013 Michel Salim <salimma@fedoraproject.org> - 1.5-1
- Update to 1.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 17 2013 Michel Salim <salimma@fedoraproject.org> - 1.4-1
- Update to 1.4

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 1.3-1
- Update to 1.3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 16 2012 Michel Salim <salimma@fedoraproject.org> - 1.2-1
- Update to 1.2

* Sat Sep 15 2012 Michel Salim <salimma@fedoraproject.org> - 1.1-1
- Update to 1.1

* Tue Jun 19 2012 Michel Salim <salimma@fedoraproject.org> - 1.0-2
- Remove redundant %%{python_sitearch} declaration
- Use upstream's check script instead of manually setting up the environment

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 1.0-1
- Initial package
