Name: xsnow
Version: 2.0.15
Release: alt1

Summary: An X Window System based dose of Christmas cheer
License: GPL
Group: Toys

Url: https://www.ratrabbit.nl/ratrabbit/content/xsnow/introduction
Source0: xsnow-%version.tar.gz
Packager: Alexei Mezin <alexvm@altlinux.org>

Summary(ru_RU.UTF8):  Немножко новогоднего настроения на рабочий стол

# Automatically added by buildreq on Wed Jan 01 2020
# optimized out: at-spi2-atk fontconfig glib2-devel glibc-kernheaders-generic libX11-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libharfbuzz-devel libpango-devel libwayland-client libwayland-cursor libwayland-egl pkg-config python-modules python2-base python3 python3-base python3-dev sh4 xorg-proto-devel
###BuildRequires: i586-libxcb libXpm-devel libXt-devel libdb4-devel libdbus-devel libgtk+3-devel libxml2-devel python3-module-mpl_toolkits python3-module-yieldfrom selinux-policy
BuildRequires: libXpm-devel libXt-devel libgtk+3-devel libxml2-devel libdbus-devel

###BuildRequires: gccmakedep imake libXext-devel libXpm-devel libXt-devel xorg-cf-files

%description
The Xsnow toy provides a continual gentle snowfall, trees, and Santa
Claus flying his sleigh around the screen.  Xsnow is only for the X
Window System, though; consoles just get coal.

%description -l ru_RU.UTF8
Xsnow добавляет анимированные снежинки и Санту на оленях на рабочий стол.

%prep
%setup

%build
%configure
%make

%install
%makeinstall_std

%files
%doc README
%_gamesbindir/*
%_man6dir/*
%_pixmapsdir/*
%_desktopdir/*

%changelog
* Wed Jan 01 2020 Alexei Mezin <alexvm@altlinux.org> 2.0.15-alt1
- New version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.42-alt4.qa1
- NMU: rebuilt for debuginfo.

* Sun Dec 13 2009 Michael Shigorin <mike@altlinux.org> 1.42-alt4
- an icon is now correctly placed 48x48 one (thx repocop)

* Fri Oct 30 2009 Michael Shigorin <mike@altlinux.org> 1.42-alt3
- buildreq per repocop proposal
- updated an Url:
- minor spec cleanup

* Tue Jun 20 2006 Michael Shigorin <mike@altlinux.org> 1.42-alt2.1
- rebuild (x86_64)

* Mon Feb 28 2005 Victor Forsyuk <force@altlinux.ru> 1.42-alt2
- Updated build deps and patch.

* Thu Dec 26 2002 Michael Shigorin <mike@altlinux.ru> 1.42-alt1
- built for ALT Linux
- based on Red Hat spec; credits:
  Donnie Barnes <djb@redhat.com>
  Erik Troan <ewt@redhat.com>
  Michael Maher <mike@redhat.com>
  Than Ngo <than@redhat.com>
  Tim Powers <timp@redhat.com>
