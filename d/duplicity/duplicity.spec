Name: duplicity
Version: 0.7.16
Release: alt1

Summary: Untrusted/encrypted backup using rsync algorithm

Group: Archiving/Backup
Url: https://launchpad.net/duplicity
License: GPL

Source: https://launchpad.net/duplicity/0.7-series/%version/+download/duplicity-%version.tar

# Automatically added by buildreq on Sat Nov 03 2007
BuildRequires: librsync-devel python-devel python-modules-compiler python-module-setuptools
BuildPreReq: rpm-build-compat >= 1.2

# No required by default
%add_python_req_skip dropbox
# No required by default (OpenStack)
%add_python_req_skip pyrax

%description
Duplicity incrementally backs up files and directory by encrypting
tar-format volumes with GnuPG and uploading them to a remote (or
local) file server.  In theory many remote backends are possible;
right now local, ssh/scp, ftp, and rsync backends are written.
Because duplicity uses librsync, the incremental archives are space
efficient and only record the parts of files that have changed since
the last backup.  Currently duplicity supports deleted files, full
unix permissions, directories, symbolic links, fifos, etc., but not
hard links.

%prep
%setup

%build
%python_build

%install
%python_install

%find_lang %name

%files -f %name.lang
%doc CHANGELOG README
%_bindir/rdiffdir
%_bindir/duplicity
%_man1dir/*
%python_sitelibdir/%name/
%python_sitelibdir/duplicity-*.egg-info

%changelog
* Wed Feb 07 2018 Vitaly Lipatov <lav@altlinux.ru> 0.7.16-alt1
- new version 0.7.16 (with rpmrb script)

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.7.15-alt1
- new version 0.7.15 (with rpmrb script)

* Sat Oct 07 2017 Vitaly Lipatov <lav@altlinux.ru> 0.7.14-alt1
- new version 0.7.14 (with rpmrb script)

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.7.13.1-alt1
- new version 0.7.13.1 (with rpmrb script)

* Fri Jun 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.7.13-alt1
- new version 0.7.13 (with rpmrb script)

* Tue May 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.7.12-alt1
- new version 0.7.12 (with rpmrb script)

* Sun Jan 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.7.11-alt1
- new version 0.7.11 (with rpmrb script)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 0.7.10-alt1
- new version 0.7.10 (with rpmrb script)

* Fri Aug 05 2016 Vitaly Lipatov <lav@altlinux.ru> 0.7.09-alt1
- new version 0.7.09 (with rpmrb script)

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 0.7.08-alt1
- new version 0.7.08 (with rpmrb script)

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 0.7.07.1-alt1
- new version 0.7.07.1 (with rpmrb script)

* Sat Jan 02 2016 Vitaly Lipatov <lav@altlinux.ru> 0.7.06-alt1
- new version 0.7.06 (with rpmrb script)

* Sat Oct 17 2015 Vitaly Lipatov <lav@altlinux.ru> 0.7.05-alt1
- new version (0.7.05) with rpmgs script

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 0.7.04-alt1
- new version 0.7.04 (with rpmrb script)

* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 0.6.24-alt1
- new version 0.6.24 (with rpmrb script)

* Sat Oct 12 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6.22-alt1
- new version 0.6.22 (with rpmrb script) (ALT bug #28842)

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6.21-alt1
- new version 0.6.21 (with rpmrb script)

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.17-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 02 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.6.17-alt1
- 0.6.17

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.13-alt1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.6.13-alt1
- 0.6.13

* Fri Mar 19 2010 Denis Klimov <zver@altlinux.org> 0.6.08b-alt1
- new version
- added async download volumes patch

* Fri Jan 29 2010 Denis Klimov <zver@altlinux.org> 0.6.06-alt1
- new version

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.05-alt1.1
- Rebuilt with python 2.6

* Sat Sep 19 2009 Denis Klimov <zver@altlinux.org> 0.6.05-alt1
- new version
- remove needless -q param for setup macros
- use find_lang macros

* Mon Jul 07 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.11-alt1
- new version 0.4.11 (with rpmrb script)
- add rpm-build-compat >= 2 buildreq

* Tue Apr 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.10-alt1
- new version 0.4.10 (with rpmrb script)

* Tue Jan 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.9-alt1
- new version 0.4.9
- fix lib files packing
- remove COPYING, fix build/install commmands

* Fri Dec 21 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.8-alt1
- new version 0.4.8 (with rpmrb script)

* Sat Nov 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.3-alt1
- change mantainer, cleanup spec
- new version 0.4.3 (with rpmrb script)

* Wed May 17 2006 Alex V. Myltsev <avm@altlinux.ru> 0.4.2-alt0.1
- Initial build for Sisyphus

* Sat Aug 09 2003 Ben Escoto <bescoto@stanford.edu>
- Repackaging for Fedora
- autodetect python version
- require librsync >=0.9.6
* Sun Aug 30 2002 Ben Escoto <bescoto@stanford.edu>
- Initial RPM

