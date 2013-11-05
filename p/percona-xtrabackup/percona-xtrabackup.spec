%define ibx_ver 1.5.1

Summary: XtraBackup online backup for MySQL / InnoDB
Name: percona-xtrabackup
Version: 2.1.5
Release: alt1
Group: Databases
License: GPLv2
Packager: Evgenii Terechkov <evg@altlinux.org>
Url: http://www.percona.com/software/percona-xtrabackup/

Source: %name-%version.tar.gz
Source1: PerconaXtraBackup-2.1.5.pdf

Patch1: percona-xtrabackup-2.1.5-srv_buf_size.patch

BuildRequires: libaio-devel libgcrypt-devel gcc-c++ cmake bzr bison libtool libncurses-devel zlib-devel python-module-sphinx perl-podlators libevent-devel libssl-devel

BuildRequires: /proc

%description
Percona XtraBackup is OpenSource online (non-blockable) backup solution for InnoDB and XtraDB engines.

%prep
%setup
%patch1 -p1

%build
set -ue
export CC=${CC-"gcc"}
export CXX=${CXX-"g++"}
export CFLAGS="-DXTRABACKUP_VERSION=\\\"%version\\\" -DXTRABACKUP_REVISION=\\\"undefined\\\""
export CXXFLAGS="-DXTRABACKUP_VERSION=\\\"%version\\\" -DXTRABACKUP_REVISION=\\\"undefined\\\""
./utils/build.sh xtradb
cp src/xtrabackup .
./utils/build.sh xtradb55
cp src/xtrabackup_55 src/xbstream src/xbcrypt .
./utils/build.sh xtradb56
cp src/xtrabackup_56 .

pushd doc
make man
popd
cp %SOURCE1 .
pod2man innobackupex > innobackupex.1
mv innobackupex innobackupex-%ibx_ver

%install
# install binaries and configs
mkdir -p %buildroot%_bindir %buildroot%_datadir %buildroot%_man1dir
install -m 755 xtrabackup %buildroot%_bindir
install -m 755 xtrabackup_55 %buildroot%_bindir
install -m 755 xtrabackup_56 %buildroot%_bindir
install -m 755 innobackupex-%ibx_ver %buildroot%_bindir
ln -s innobackupex-%ibx_ver %buildroot%_bindir/innobackupex
install -m 755 xbstream %buildroot%_bindir
install -m 755 xbcrypt %buildroot%_bindir

install -m 755 doc/build/man/xtrabackup.1 %buildroot%_man1dir
install -m 755 innobackupex.1 %buildroot%_man1dir

%files
%_bindir/innobackupex
%_bindir/innobackupex-%ibx_ver
%_bindir/xbcrypt
%_bindir/xbstream
%_bindir/xtrabackup
%_bindir/xtrabackup_55
%_bindir/xtrabackup_56
%_man1dir/*.1.*
%doc contrib/backup_mysql_cron.sh PerconaXtraBackup-2.1.5.pdf

%changelog
* Mon Nov  4 2013 Terechkov Evgenii <evg@altlinux.org> 2.1.5-alt1
- Initial build for ALT Linux Sisyphus
