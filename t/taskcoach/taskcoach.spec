%define oname TaskCoach
Name: taskcoach
Version: 0.71.5
Release: alt1.1.1

Summary: Your friendly task manager

License: GPL
Group: Text tools
Url: http://taskcoach.niessink.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%oname-%version.tar.bz2
Patch: %name.patch

BuildArch: noarch

# manually removed: eric
# Automatically added by buildreq on Tue Jan 06 2009
BuildRequires: libcurl python-module-PyXML python-module-wx

BuildPreReq: rpm-build-compat >= 1.2

AutoProv: no
# wait for correct build python-module-pysyncml
%add_python_req_skip _pysyncml

%description
Task Coach is a simple open source todo manager to manage personal
tasks and todo lists. It grew out of my frustration that well-known
task managers, such as those provided with Outlook or Lotus Notes,
do not provide facilities for composite tasks. Often, tasks and other
things todo consist of several activities. Task Coach is designed to
deal with composite tasks.

%prep
%setup -q -n %oname-%version
%patch

%build
%python_build

%install
%python_install
%__subst "s|/usr/bin/python|%_bindir/env python|" %buildroot/%_bindir/%name.py
ln -s %name.py %buildroot/%_bindir/%name

%find_lang %name

%files -f %name.lang
%doc CHANGES.txt PUBLICITY.txt README.txt
%_bindir/%name
%_bindir/%name.py
%_desktopdir/*
%_pixmapsdir/*
%python_sitelibdir/taskcoachlib/

%changelog
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

