Name: drqueue
Version: 0.64.3
Release: alt2.1.1

Summary: Open Source Distributed Render Queue

Url: https://ssl.drqueue.org/project
License: GPL
Group: Shells

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://drqueue.org/files/%{name}.%version.tar.bz2
Patch: %name.patch

# manually removed: bk rcs cvs
# Automatically added by buildreq on Mon Apr 27 2009
BuildRequires: flex gcc-c++ ghostscript-utils libgtk+2-devel scons swig texlive-latex-base

%description
DrQueue is the Open Source Distributed Render Queue. It is the Open
Source alternative to other propietary products. It has been tested on
renderfarms with more than 200 processors and mixed architectures.

It is a tool under development, though it is being used in production by
many people since it release.

%prep
%setup -q

%build
scons

%install
mkdir -p %buildroot%_libdir/%name/
scons PREFIX=%buildroot%_libdir install
rm -rf %buildroot%_libdir/%name/bin/Turtle*

%files
%doc README* contrib
%dir %_libdir/%name/
%_libdir/%name/bin/
%_libdir/%name/etc/

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.64.3-alt2.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.64.3-alt2.1
- Rebuilt with python 2.6

* Mon Apr 27 2009 Vitaly Lipatov <lav@altlinux.ru> 0.64.3-alt2
- update buildreq

* Sun Jan 25 2009 Vitaly Lipatov <lav@altlinux.ru> 0.64.3-alt1
- new version 0.64.3 (with rpmrb script)
- fix Url

* Sun Dec 31 2006 Vitaly Lipatov <lav@altlinux.ru> 0.64.1-alt0.2
- move examples to doc

* Sat Dec 30 2006 Vitaly Lipatov <lav@altlinux.ru> 0.64.1-alt0.1
- initial build for ALT Linux Sisyphus
