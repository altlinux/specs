%define oname TaskCoach
Name: taskcoach
Version: 1.4.3
Release: alt1

Summary: Your friendly task manager

License: GPL
Group: Text tools
Url: http://taskcoach.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%oname-%version.tar

BuildArch: noarch

# manually removed: eric
# Automatically added by buildreq on Fri Sep 21 2012
# optimized out: python-base python-devel  python-module-zope python-modules python-modules-compiler python-modules-email python-modules-encodings
BuildRequires: python-module-distribute libwxGTK3.1-devel

BuildPreReq: rpm-build-intro

Requires: lsb-release xprop

Requires: python-module-twisted-core-gui-wx libXScrnSaver

AutoProv: no
# wait for correct build python-module-pysyncml
%add_python_req_skip _pysyncml _growl _powermgt
%add_python_req_skip _winreg pywintypes win32api win32com win32con win32gui win32event win32file

%description
Task Coach is a simple open source todo manager to manage personal
tasks and todo lists. It grew out of my frustration that well-known
task managers, such as those provided with Outlook or Lotus Notes,
do not provide facilities for composite tasks. Often, tasks and other
things todo consist of several activities. Task Coach is designed to
deal with composite tasks.

%prep
%setup -n %oname-%version
# disable version checking
%__subst "s|^ *wxversion|#wxversion|g" taskcoach.py
%__subst "s|current_dist =.*|current_dist = ['debian']|g" setup.py

%build
%python_build

%install
%python_install
%__subst "s|/usr/bin/python|%_bindir/env python|" %buildroot/%_bindir/%name.py
ln -s %name.py %buildroot/%_bindir/%name
rm -rf %buildroot%python_sitelibdir/buildlib/

%find_lang %name

%files -f %name.lang
%doc CHANGES.txt PUBLICITY.txt README.txt
%_bindir/%name
%_bindir/%name.py
%_desktopdir/*
%_pixmapsdir/*
%python_sitelibdir/taskcoachlib/
%python_sitelibdir/*.egg-info

%changelog
* Thu Apr 21 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.3-alt1
- new version 1.4.3 (with rpmrb script)

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- new version 1.4.2 (with rpmrb script)

* Thu Sep 25 2014 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- new version 1.4.1 (with rpmrb script)

* Wed Apr 02 2014 Vitaly Lipatov <lav@altlinux.ru> 1.3.36-alt1
- new version 1.3.36 (with rpmrb script)

* Tue Aug 27 2013 Vitaly Lipatov <lav@altlinux.ru> 1.3.30-alt1
- new version 1.3.30 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.3.23-alt1
- new version 1.3.23 (with rpmrb script)

* Fri Sep 21 2012 Vitaly Lipatov <lav@altlinux.ru> 1.3.18-alt1
- new version 1.3.18 (with rpmrb script)

* Thu Aug 16 2012 Vitaly Lipatov <lav@altlinux.ru> 1.3.17-alt1
- new version 1.3.17 (with rpmrb script) (ALT bug #27633)

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.71.5-alt1.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.71.5-alt1.1
- Rebuilt with python 2.6

* Tue Jan 06 2009 Vitaly Lipatov <lav@altlinux.ru> 0.71.5-alt1
- new version 0.71.5 (with rpmrb script)
- cleanup spec, update buildreq

* Tue Sep 25 2007 Vitaly Lipatov <lav@altlinux.ru> 0.65.1-alt1
- new version 0.65.1 (with rpmrb script)

* Sat Jul 28 2007 Vitaly Lipatov <lav@altlinux.ru> 0.64.2-alt2
- fix requires (thanks Alexey Rusakov <ktirf@>)
- use cElementTree instead xml.etree.ElementTree from python 2.5

* Tue Jul 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.64.2-alt1
- new version 0.64.2 (with rpmrb script)

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.61.3-alt0.1
- new version 0.61.3 (with rpmrb script)

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 0.59-alt0.1
- new version 0.59 (with rpmrb script)

* Mon May 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.57-alt0.2
- fix binary name, disable any provides, fix python-strict
- fix requires (#9415)

* Mon Apr 17 2006 Vitaly Lipatov <lav@altlinux.ru> 0.57-alt0.1
- new version 0.57 (with rpmrb script)

* Wed Jan 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.53-alt0.2
- remove fantom requires

* Thu Jan 05 2006 Vitaly Lipatov <lav@altlinux.ru> 0.53-alt0.1
- initial build for ALT Linux Sisyphus

