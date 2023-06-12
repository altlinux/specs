Name: rdiff-backup
Version: 2.2.5
Release: alt1

Summary: Backup software

License: GPL
Group: File tools
Url: http://www.nongnu.org/rdiff-backup/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/rdiff-backup/rdiff-backup/archive/v%version.tar.gz
Source: %name-%version.tar

# from http://wiki.rdiff-backup.org/wiki/index.php/BashCompletion
Source1: rdiff-backup.bash_completion

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools_scm
BuildRequires: librsync-devel >= 0.9.6
# for man
BuildRequires: /usr/bin/asciidoctor

%description
rdiff-backup is a script, written in Python, that backs up one
directory to another and is intended to be run periodically (nightly
from cron for instance). The target directory ends up a copy of the
source directory, but extra reverse diffs are stored in the target
directory, so you can still recover files lost some time ago. The idea
is to combine the best features of a mirror and an incremental backup.
rdiff-backup can also operate in a bandwidth efficient manner over a
pipe, like rsync. Thus you can use rdiff-backup and SSH to securely
back a hard drive up to a remote location, and only the differences
from the previous backup will be transmitted.

%prep
%setup
#patch1 -p1
#patch2 -p1
#patch3 -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install
rm -rfv %_docdir/%name/Windows-*.md

%files
%_docdir/%name/
%_bindir/rdiff-backup
%_bindir/rdiff-backup-statistics
%_bindir/rdiff-backup-delete
%_man1dir/rdiff-backup*
%python3_sitelibdir/rdiffbackup/
%python3_sitelibdir/rdiff_backup/
%python3_sitelibdir/*.egg-info
%_datadir/bash-completion/completions/%name

%changelog
* Mon Jun 12 2023 Vitaly Lipatov <lav@altlinux.ru> 2.2.5-alt1
- new version 2.2.5 (with rpmrb script)

* Sat Feb 27 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- build 2.0.5 (network incompatible with 1.x.x, see migration.md)
- switch to python3

* Fri Aug 14 2015 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- new version 1.3.3 (with rpmrb script)
- add patches from Fedora and ROSA
- add bash completion

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.8-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.8-alt1.1
- Rebuild with Python-2.7

* Tue Feb 16 2010 Vitaly Lipatov <lav@altlinux.ru> 1.2.8-alt1
- new version 1.2.8 (with rpmrb script)

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.1
- Rebuilt with python 2.6

* Fri Dec 12 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Thu Mar 29 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- new version (1.0.5)

