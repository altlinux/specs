%define origname xmms-wma

Name: xmms-in-wma
Version: 1.0.5
Release: alt2

Summary: xmms input plugin: wma format support
License: GPL
Group: Sound

Url: http://mcmcc.bat.ru/xmms-wma
Packager: Michael Shigorin <mike@altlinux.org>
Source: %origname-%version.tar.bz2

# Automatically added by buildreq on Sun Jan 24 2010
BuildRequires: libxmms-devel

%description
XMMS input plugin for support WMA format

%prep
%setup -n %origname-%version

%build
%make

%install
install -pDm644 libwma.so %buildroot%xmms_inputdir/libwma.so

%files
%doc readme.* COPYING
%xmms_inputdir/libwma.so

%changelog
* Sun Jan 24 2010 Michael Shigorin <mike@altlinux.org> 1.0.5-alt2
- rebuilt for Sisyphus
- spec cleanup
- buildreq

* Tue Sep 06 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Mon Nov 29 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Mon Sep 06 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Fri May 21 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- initial release
