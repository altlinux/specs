Name: dissy
Version: 10
Release: alt1

Summary: Graphical frontend to objdump

License: GPL
Group: Development/Other
Url: http://code.google.com/p/dissy/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dissy.googlecode.com/files/%name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildPreReq: rpm-build-compat >= 1.2

%add_python_req_skip wali

%description
Dissy is a disassembler (graphical frontend to objdump) for multiple
architectures. It allows fast navigation through the disassembled code
and easy searching for addresses and symbols. Dissy is written in Python
and available under the GNU GPL.

%prep
%setup
%python_build

%install
%python_install

#%__subst "s,/usr/bin/python,/usr/bin/env python," %buildroot%_bindir/%name
rm -rf %buildroot/%_datadir/doc/

%files
%doc README
%_bindir/%name
%python_sitelibdir/%name/
%python_sitelibdir//dissy-*.egg-info
%_datadir/%name/
%_man1dir/*

%changelog
* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 10-alt1
- new version 10 (with rpmrb script)
- fix url, source url

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 7-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7-alt1.1
- Rebuilt with python 2.6

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 7-alt1
- new version 7 (with rpmrb script)

* Mon Feb 18 2008 Vitaly Lipatov <lav@altlinux.ru> 6-alt3
- cleanup spec, use python_build/python_install macroses
- update buildreqs

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 6-alt2.1
- Rebuilt with python-2.5.

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 6-alt2
- Build as noarch.

* Sun Sep 16 2007 Vitaly Lipatov <lav@altlinux.ru> 6-alt1
- new version 6 (with rpmrb script)
- update Url, Source

* Sun May 28 2006 Vitaly Lipatov <lav@altlinux.ru> 1-alt0.1
- initial build for ALT Linux Sisyphus

