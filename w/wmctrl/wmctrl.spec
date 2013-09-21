Name: wmctrl
Version: 1.07
Release: alt5

Summary: Tool to interact with an EWMH/NetWM compatible X Window Manager
Summary(ru_RU.UTF-8): Утилита для взаимодействия с оконными менеджерами, соответствующими стандартам EWMH/NetWM
License: GPLv2
Group: System/X11
Url: http://tomas.styblo.name/wmctrl/

Packager: Igor Zubkov <icesik@altlinux.org>

Source0: %name-%version.tar.gz

Patch0: 01_64-bit-data.patch
Patch1: 02_manpage-fixes.patch

# Automatically added by buildreq on Sat Sep 21 2013
BuildRequires: glib2-devel imake libXmu-devel xorg-cf-files

%description
A command line tool to interact with an EWMH/NetWM compatible
X Window Manager.

%description -l ru_RU.UTF-8
Утилита коммандной строки для взаимодействия с оконными менеджерами,
соответствующими стандартам EWMH/NetWM.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog README
%_bindir/*
%_man1dir/*

%changelog
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


