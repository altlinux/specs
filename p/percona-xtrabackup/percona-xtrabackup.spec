%define ROOT %_localstatedir/mysql
%add_findreq_skiplist %_datadir/xtrabackup-test/run.sh

Summary: XtraBackup online backup for MySQL / InnoDB
Name: percona-xtrabackup
Version: 2.3.3
Release: alt1
Group: Databases
License: GPLv2
Packager: Evgenii Terechkov <evg@altlinux.org>
Url: https://github.com/percona/percona-xtrabackup.git

Source: %name-%version.tar

BuildRequires: libaio-devel libgcrypt-devel gcc-c++ cmake bzr bison libtool libncurses-devel zlib-devel python-module-sphinx perl-podlators libev-devel libssl-devel libcurl-devel xxd texlive-latex-base texlive-latex-recommended

BuildRequires: /proc

Requires: perl-podlators rsync

%description
Percona XtraBackup is OpenSource online (non-blockable) backup solution for InnoDB and XtraDB engines.

%package tests
Summary: XtraBackup online backup for MySQL / InnoDB (testsuite)
License: GPLv2
Group: Databases

%description tests
Percona XtraBackup is OpenSource online (non-blockable) backup solution for InnoDB and XtraDB engines.

This subpackage contains testsuite.

%prep
%setup

%build
cmake \
      -DBUILD_CONFIG=xtrabackup_release \
      -DCMAKE_INSTALL_PREFIX=%_prefix \
      -DCMAKE_VERBOSE_MAKEFILE=ON \
      -DMYSQL_DATADIR="%ROOT" \
      -DSYSCONFDIR="%ROOT" \
      -DINSTALL_LAYOUT=RPM \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DWITH_PDF_DOCS=ON \
      -DFEATURE_SET="community"

%make_build

pushd storage/innobase/xtrabackup/doc/source
make man
popd

%install
mkdir -p %buildroot%_bindir %buildroot%_datadir %buildroot%_man1dir
%makeinstall_std

install -m 644 storage/innobase/xtrabackup/doc/source/build/man/xtrabackup.1 %buildroot%_man1dir
install -m 644 storage/innobase/xtrabackup/doc/source/build/man/xbcrypt.1 %buildroot%_man1dir
install -m 644 storage/innobase/xtrabackup/doc/source/build/man/xbstream.1 %buildroot%_man1dir
install -m 644 storage/innobase/xtrabackup/doc/source/build/man/innobackupex.1 %buildroot%_man1dir

%files
%_bindir/innobackupex
%_bindir/xbcrypt
%_bindir/xbstream
%_bindir/xtrabackup
%_bindir/xbcloud
%_bindir/xbcloud_osenv
%_man1dir/*.1.*
%doc storage/innobase/xtrabackup/contrib/backup_mysql_cron.sh storage/innobase/xtrabackup/doc/source/build/latex/PerconaXtraBackup-2.3.pdf

%files tests
%_datadir/xtrabackup-test

%changelog
* Sun Dec 20 2015 Terechkov Evgenii <evg@altlinux.org> 2.3.3-alt1
- 2.3.3

* Wed Dec 16 2015 Terechkov Evgenii <evg@altlinux.org> 2.3.2-alt3
- Build from upstream git repo

* Wed Dec 16 2015 Terechkov Evgenii <evg@altlinux.org> 2.3.2-alt2
- Build pdf manual from source

* Wed Dec  2 2015 Terechkov Evgenii <evg@altlinux.org> 2.3.2-alt1
- 2.3.2

* Thu Dec 11 2014 Terechkov Evgenii <evg@altlinux.org> 2.2.7-alt1
- 2.2.7
- N.B.: xtrabackup >= 2.2.6 will not work with "chroot" option in my.cnf (see relnotes)!

* Sat Aug  9 2014 Terechkov Evgenii <evg@altlinux.org> 2.2.3-alt1
- 2.2.3

* Mon Feb 10 2014 Evgenii Terechkov <evg@altlinux.org> 2.1.7-alt1
- 2.1.7

* Wed Dec 18 2013 Terechkov Evgenii <evg@altlinux.org> 2.1.6-alt1
- 2.1.6

* Mon Dec 16 2013 Terechkov Evgenii <evg@altlinux.org> 2.1.5-alt2
- perl-podlators required for innobackupex

* Mon Nov  4 2013 Terechkov Evgenii <evg@altlinux.org> 2.1.5-alt1
- Initial build for ALT Linux Sisyphus
