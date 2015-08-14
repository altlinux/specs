Name: rdiff-backup
Version: 1.3.3
Release: alt1

Summary: Backup software

License: GPL
Group: File tools
Url: http://www.nongnu.org/rdiff-backup/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://savannah.nongnu.org/download/%name/%name-%version.tar

# from http://wiki.rdiff-backup.org/wiki/index.php/BashCompletion
Source1: rdiff-backup.bash_completion

# docs are already installed by doc macro
Patch1: rdiff-backup-1.2.0-dont-install-docs.patch

# Workaround to build with librsync >= 1.0.0
Patch2: rdiff-backup-1.2.8-librsync-1.0.0.patch

# Upstream bug: https://savannah.nongnu.org/bugs/?26064
#
Patch3: http://dev.sgu.ru/rpm/rdiff-backup--popen2.patch


BuildPreReq: rpm-build-python

# Automatically added by buildreq on Thu Mar 29 2007
BuildRequires: python-devel python-modules-compiler
BuildRequires: librsync-devel >= 0.9.6

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
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%python_build

%install
%python_install
# install bash_completion
mkdir -p -m 0755 %buildroot/%_sysconfdir/bash_completion.d
install -m 0644 %SOURCE1 %buildroot/%_sysconfdir/bash_completion.d/%name

%files
%doc CHANGELOG README FAQ.html examples.html
%_bindir/rdiff-backup
%_bindir/rdiff-backup-statistics
%_man1dir/rdiff-backup.1*
%_man1dir/rdiff-backup-statistics.1*
%python_sitelibdir/rdiff_backup/
%python_sitelibdir/*.egg-info
%config(noreplace) %_sysconfdir/bash_completion.d/%name

%changelog
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

