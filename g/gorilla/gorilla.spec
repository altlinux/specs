BuildRequires: desktop-file-utils
# -*- mode: rpm-spec; coding: utf-8 -*-
%define _tcl_lib_path %_datadir/%name

Name: gorilla
Version: 1.5.3.3
Release: alt1.qa1

Summary: Password gorilla is simple but powerful password manager writen in tcl/tk
License: GPL2
Group: Databases
Url: http://github.com/zdia/gorilla
BuildArch: noarch

Requires: bwidget tcl-incrtcl tcllib
Packager: Evgenii Terechkov <evg@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildPreReq: rpm-build-tcl
BuildRequires: tk

%description
Password gorilla is simple but powerful password manager writen in tcl/tk

%prep
%setup
%patch -p1

%build

%install
chmod ugo-x sources/blowfish/* sources/pwsafe/* sources/sha1/* sources/twofish/* sources/*.tcl sources/*.txt

mkdir -p %buildroot%_desktopdir
cp -v %name.desktop %buildroot%_desktopdir

mkdir -p %buildroot%_bindir
perl -i -walpe's@"LICENSE.txt"@"%_defaultdocdir/%name-%version/LICENSE.txt"@;s@ReadHelpFiles \$::gorillaDir@ReadHelpFiles %_defaultdocdir/%name-%version@' sources/%name.tcl
install sources/%name.tcl %buildroot%_bindir/%name

mkdir -p %buildroot%_datadir/%name
install sources/isaac.tcl %buildroot%_datadir/%name
install sources/viewhelp.tcl %buildroot%_datadir/%name

cp -vr sources/sha1 %buildroot%_datadir/%name
cp -vr sources/blowfish %buildroot%_datadir/%name
cp -vr sources/twofish %buildroot%_datadir/%name
cp -vr sources/pwsafe %buildroot%_datadir/%name
cp -vr sources/msgs %buildroot%_datadir/%name

mkdir -p %buildroot%_niconsdir
mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_liconsdir

install sources/pics/%name-32x32.gif %buildroot%_niconsdir/%name.gif
install sources/pics/%name-16x16.gif %buildroot%_miconsdir/%name.gif
install sources/pics/%name-48x48.gif %buildroot%_liconsdir/%name.gif
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=Security \
	%buildroot%_desktopdir/gorilla.desktop

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_niconsdir/%name.gif
%_miconsdir/%name.gif
%_liconsdir/%name.gif

%doc README sources/*.txt

%changelog
* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.5.3.3-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gorilla

* Sat Oct 30 2010 Terechkov Evgenii <evg@altlinux.org> 1.5.3.3-alt1
- 1.5.3.3
- Reverted back upstream braindead binary blobhellmess

* Sat Jul 31 2010 Terechkov Evgenii <evg@altlinux.ru> 1.5.3.2-alt1
- 1.5.3.2

* Fri Jul 16 2010 Terechkov Evgenii <evg@altlinux.ru> 1.5.3.1-alt1
- 1.5.3.1

* Sat May  8 2010 Terechkov Evgenii <evg@altlinux.ru> 1.5.2.8-alt1
- 1.5.28

* Sun Nov 16 2008 Terechkov Evgenii <evg@altlinux.ru> 1.4-alt7
- Update spec to new filetriggers system

* Fri Jan  4 2008 Terechkov Evgenii <evg@altlinux.ru> 1.4-alt6
- Russian translation removed from spec (Specpo)
- s/wish8.4/wish/;s/tclsh84/tclsh/ to work with system versions of wish and tclsh
- Licence changed to gpl2

* Mon May 21 2007 Terechkov Evgenii <evg@altlinux.ru> 1.4-alt5
- Encoding for Russian Description and Summary fixed
- Spec changed to provide included packages
- Spell-check spec

* Thu Jan 25 2007 Terechkov Evgenii <evg@altlinux.ru> 1.4-alt4
- Patch1 updated to fix adding logins
- Spec converted in utf-8 + small sleanups

* Thu Jan  4 2007 Terechkov Evgenii <evg@altlinux.ru> 1.4-alt3
- Patch1 added. It fixes some Xresources-fonts ignoring.

* Sat Dec  2 2006 Terechkov Evgenii <evg@altlinux.ru> 1.4-alt2
- Spec changed according menu packaging policy (icons)

* Sat Sep 23 2006 Terechkov Evgenii <evg@altlinux.ru> 1.4-alt1
- Build for Sisyphus

* Mon Aug 21 2006 Terechkov Evgenii <evg@altlinux.ru> 1.4-alt0.C30.1
- Initial build for C30

* Sun Jul  9 2006 Evgenii Terechkov <evg@altlinux.ru> 1.4-alt0.M24.1
- 1.4
- Arg parsing patch removed (fixed in upstream)

* Thu May 25 2006 Evgenii Terechkov <evg@altlinux.ru> 1.3-alt0.M24.2
- Bugs with about and help dialogs fixed
- Small spec cleanups for Sisyphus

* Sun May 21 2006 Evgenii Terechkov <evg@altlinux.ru> 1.3-alt0.M24.1
- Initial build for ALT
