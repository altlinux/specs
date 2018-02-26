# vim:set ft=spec: -*- rpm-spec -*- 
Name: wmctrl
Version: 1.07
Release: alt4

Summary: Tool to interact with an EWMH/NetWM compatible X Window Manager.
Summary(ru_RU.KOI8-R): Утилита для взаимодействия с оконными менеджерами, соответствующими стандартам EWMH/NetWM
License: GPL
Group: System/XFree86
Url: http://sweb.cz/tripie/utils/wmctrl/
Packager: Gleb Stiblo <ulfr@altlinux.ru>

Source: %name-%version.tar.gz

# Automatically added by buildreq on Thu Sep 04 2008
BuildRequires: glib2-devel imake libXmu-devel xorg-cf-files

#BuildRequires: XFree86-devel glib2-devel

%description
A command line tool to interact with an EWMH/NetWM compatible
X Window Manager.

%description -l ru_RU.KOI8-R
Утилита коммандной строки для взаимодействия с оконными менеджерами,
соответствующими стандартам EWMH/NetWM


%prep
%setup -q

%build
%configure 
%make_build

%install
install -p -m755 -D %name %buildroot/%_x11bindir/%name

%files
%_x11bindir/*
%doc README AUTHORS ChangeLog COPYING 

%changelog
* Thu Sep 04 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.07-alt4
- buildreq fixed

* Tue May 23 2006 Gleb Stiblo <ulfR@altlinux.ru> 1.07-alt3
- typo fixed

* Fri Jan 06 2006 Gleb Stiblo <ulfR@altlinux.ru> 1.07-alt2
- fixed typo in summary (#8654)

* Sat May 14 2005 Gleb Stiblo <ulfR@altlinux.ru> 1.07-alt1
- fixed a formatting bug that made the window list 
  unintelligible for desktop_ids == -1 or desktop_ids > 9

* Thu Jan 06 2005 Gleb Stiblo <ulfR@altlinux.ru> 1.06-alt1
- new version

* Wed Feb 11 2004 Gleb Stiblo <ulfr@altlinux.ru> 1.05-alt1
- initial release


