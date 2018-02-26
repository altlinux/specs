Name: alterator-mkbootflash
Version: 0.2
Release: alt4

Summary: Create bootable usb storage for installing system or using as live, rescue etc.
License: GPL
Group: System/Configuration/Other

Source: %name-%version.tar
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
BuildArch: noarch

Requires: mkbootflash >= 0.11
Requires: gettext
Requires: alterator >= 2.9
BuildPreReq: alterator >= 3.5
Conflicts: alterator-fbi < 0.15-alt1

%description
%summary

%prep
%setup -q

%build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_datadir/alterator/help/ru_RU/*
/usr/lib/alterator/backend3/*

%changelog
* Tue Jan 25 2011 Lenar Shakirov <snejok@altlinux.ru> 0.2-alt4
- Ask a question before apply (ALT #22243)

* Tue Jan 25 2011 Lenar Shakirov <snejok@altlinux.ru> 0.2-alt3
- Splash message added (ALT #22249)

* Tue Jan 25 2011 Lenar Shakirov <snejok@altlinux.ru> 0.2-alt2
- BuildPreReq: alterator >= 3.5 (ALT #17165)

* Wed Apr 01 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- translations from cas@ 

* Thu Sep 25 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt5
- added -M key to mkbootflash 

* Thu Sep 18 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt4
- fixed disablin when no IMG_DIR found 

* Fri Sep 12 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt3
- fixed targert device detection
- translated to russian
- help added

* Wed Aug 27 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2
- build fixed 

* Thu Jul 17 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build 

