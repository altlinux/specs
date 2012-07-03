%define _unpackaged_files_terminate_build 1

Name: kdvdcreator
Version: 0.3.2
Release: alt1

Summary: Easy to use application to create video DVDs and CDs
License: GPLv2+
Group: Video

Url: http://sourceforge.net/projects/kdvdcreator/
Packager: Andrey Cherepanov <cas@altlinux.org> 

Source: %name-%version.tar.bz2
Patch: %name-fix-build.patch

BuildPreReq: gcc-c++ kde4libs-devel

%description
Easy to use, user friendly and first of all smart, application to create
video VCD, SVCD or DVD, suitables for home players, from any number of
video files, in any of the formats supported by Mplayer/Mencoder.

%prep
%setup
%patch -p2

%build
%K4cmake -DKDE4_ENABLE_FINAL:BOOL=1
%K4make

%install
%K4install

%files
%doc README
%_bindir/*
%_desktopdir/kde4/*.desktop
%_K4apps/KDVDCreator
%_K4cfg/*.kcfg

%changelog
* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- New version 0.3.2

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2.1
- NMU (by repocop): the following fixes applied:
  * desktop-mime-entry for kdvdcreator
  * update_menus for kdvdcreator

* Sat Aug 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.3.1-alt2
- enable KDE4_ENABLE_FINAL

* Sun Mar 30 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.3.1-alt1
- initial build
