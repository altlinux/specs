Name: wmctrl
Version: 1.07
Release: alt6

Summary: Tool to interact with an EWMH/NetWM compatible X Window Manager
License: GPLv2
Group: System/X11

Url: http://tomas.styblo.name/wmctrl/
Source0: %name-%version.tar.gz
Patch0: 01_64-bit-data.patch
Patch1: 02_manpage-fixes.patch
Patch2: wmctrl-sticky-workspace.patch
Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sat Sep 21 2013
BuildRequires: glib2-devel imake libXmu-devel xorg-cf-files

Summary(ru_RU.UTF-8): Утилита для взаимодействия с EWMH/NetWM-совместимым оконным менеджером

%description
A command line tool to interact with an EWMH/NetWM compatible
X Window Manager.

%description -l ru_RU.UTF-8
Утилита коммандной строки для взаимодействия с оконным менеджером,
соответствующим стандартам EWMH/NetWM.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README
%_bindir/*
%_man1dir/*

%changelog
* Fri May 26 2017 Michael Shigorin <mike@altlinux.org> 1.07-alt6
- add fedora patch to allow stick to all workspaces (rhbz#524023)
- actually apply both of the other patches

* Sat Sep 21 2013 Igor Zubkov <icesik@altlinux.org> 1.07-alt5
- Sync with wmctrl_1.07-7.debian
- Update Url
- Add man page

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.07-alt4.qa1
- NMU: rebuilt for debuginfo.

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


