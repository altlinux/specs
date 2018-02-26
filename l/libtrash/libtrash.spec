Name: libtrash
Version: 3.1
Release: alt1.1

Summary: %name - a trash can for GNU/Linux
License: GNU GPL
Group: System/Libraries

Url: http://pages.stern.nyu.edu/~marriaga/software/libtrash/
Source: http://pages.stern.nyu.edu/~marriaga/software/libtrash/%name-%version.tgz
Source1: %name.README.ALT
Source2: %name-profile.tar.bz2
Patch0: libtrash-Makefile-2.4.patch
Patch1: libtrash-3.1-python.patch
Packager: Eugene Ostapets <eostapets@altlinux.ru>

BuildPreReq: /proc

# Automatically added by buildreq on Sun Jan 06 2008
BuildRequires: python-base

%description
This is the homepage of libtrash, the shared library which, when preloaded, implements a trash can under GNU/Linux. Through the interception of function calls which might lead to accidental data loss libtrash effectively ensures that your data remains protected from your own mistakes.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
%make
cp %SOURCE1 README.ALT
tar -jxf %SOURCE2
%__subst "s@^INSTLIBDIR=\${DESTDIR}/usr/lib@INSTLIBDIR=\${DESTDIR}%_libdir@g" src/Makefile

%install
mkdir -p %buildroot{%_libdir,%_sysconfdir}
%make DESTDIR=%buildroot install

%files
%doc README.ALT CHANGE.LOG README TODO config.txt libtrash.conf libtrash.sh libtrash.csh cleanTrash
%config(noreplace) %_sysconfdir/%name.conf
%_libdir/%name.*

%changelog
* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libtrash
  * postun_ldconfig for libtrash

* Sun Jan 06 2008 Eugene Ostapets <eostapets@altlinux.ru> 3.1-alt1
- new version

* Sun Jun 17 2007 Eugene Ostapets <eostapets@altlinux.ru> 2.8-alt1
- new version

* Fri Mar 16 2007 Eugene Ostapets <eostapets@altlinux.ru> 2.6-alt1
- new version

* Mon Nov 13 2006 Eugene Ostapets <eostapets@altlinux.ru> 2.5-alt2
- fix x86_64 build

* Sun Nov 12 2006 Eugene Ostapets <eostapets@altlinux.ru> 2.5-alt1
- new version

* Mon Dec 12 2005 Eugene Ostapets <eostapets@altlinux.ru> 2.4-alt1
- first build

