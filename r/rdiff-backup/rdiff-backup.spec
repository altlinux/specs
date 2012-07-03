Name: rdiff-backup
Version: 1.2.8
Release: alt1.1.1

Summary: Backup software

License: GPL
Group: File tools
Url: http://www.nongnu.org/rdiff-backup/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://savannah.nongnu.org/download/%name/%name-%version.tar

BuildPreReq: rpm-build-python

# Automatically added by buildreq on Thu Mar 29 2007
BuildRequires: librsync-devel python-devel python-modules-compiler

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

%build
%python_build

%install
%python_install

%files
%doc CHANGELOG README FAQ.html examples.html
%_bindir/rdiff-backup
%_bindir/rdiff-backup-statistics
%_man1dir/rdiff-backup.1*
%_man1dir/rdiff-backup-statistics.1*
%python_sitelibdir/rdiff_backup/
%python_sitelibdir/*.egg-info

%changelog
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

