Name: gpa
Version: 0.9.0
Release: alt4.r1025

Summary: The GNU Privacy Assistant
License: GPLv3+
Group: File tools

URL: http://www.gnupg.org/related_software/gpa/
#Source0: http://wald.intevation.org/frs/download.php/603/gpa-%version.tar.bz2
Source0: gpa-0.9.0+r1025.tar.bz2
# Downsized icons made from original icon by 'convert -resize'
Source1: gpa16.png
Source2: gpa32.png
Patch1: gpa-0.9.0-desktop.patch

Requires: gnupg

# Automatically added by buildreq on Wed Mar 09 2011
BuildRequires: gnupg libassuan-devel libgtk+2-devel subversion zlib-devel

# libgpgme-devel removed from buildreq'ed line and added with version req:
BuildRequires: libgpgme-devel >= 1.2.0

%description
The GNU Privacy Assistant is a graphical user interface for the GNU Privacy
Guard (GnuPG). GnuPG is a system that provides you with privacy by encrypting
emails or other documents and with authentication of received files by signature
management.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std icondir=%_liconsdir
install -pD -m644 %_sourcedir/gpa16.png %buildroot%_miconsdir/gpa.png
install -pD -m644 %_sourcedir/gpa32.png %buildroot%_niconsdir/gpa.png

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/gpa
%_desktopdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_man1dir/*

%changelog
* Wed Mar 09 2011 Victor Forsiuk <force@altlinux.org> 0.9.0-alt4.r1025
- Refresh BuildRequires.

* Wed Aug 25 2010 Victor Forsiuk <force@altlinux.org> 0.9.0-alt3.r1025
- Build post-0.9.0 svn revision 1025. Upgrade to this release is a must if
  libassuan2 installed in your system. Closes ALT bug 23406.

* Sun Feb 07 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.0-alt2.1
- Rebuilt with libassuan0.so.0.

* Thu Feb 04 2010 Victor Forsiuk <force@altlinux.org> 0.9.0-alt2
- Rebuild with static libassuan 1.0.5.

* Wed Jul 01 2009 Victor Forsyuk <force@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Dec 31 2008 Victor Forsyuk <force@altlinux.org> 0.8.0-alt2
- Remove obsolete desktop menu updating.

* Fri Nov 07 2008 Victor Forsyuk <force@altlinux.org> 0.8.0-alt1
- 0.8.0

* Mon Jun 04 2007 Victor Forsyuk <force@altlinux.org> 0.7.6-alt1
- 0.7.6

* Mon Mar 19 2007 Victor Forsyuk <force@altlinux.org> 0.7.5-alt1
- 0.7.5

* Tue Sep 26 2006 Victor Forsyuk <force@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Thu Apr 13 2006 Victor Forsyuk <force@altlinux.ru> 0.7.3-alt1
- 0.7.3
- Refresh build requirements.

* Fri Mar 25 2005 Victor Forsyuk <force@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Wed Oct 23 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.3-alt2
- rebuild with gcc3

* Wed May 01 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.4.3-alt1
- 0.4.3

* Thu Dec 06 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.4.2-alt1
- 0.4.2

* Wed Aug 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Sun Jan 21 2001 Dmitry V. Levin <ldv@fandra.org> 0.3.1-ipl6mdk
- RE adaptions (lenny sux).

* Mon Oct 02 2000 Daouda Lo <daouda@mandrakesoft.com> 0.3.1-6mdk
- add icons to menuentry

* Wed Sep 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-5mdk
- fix menu entry

* Fri Sep 01 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-4mdk
- added %%lang

* Wed Aug 02 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-3mdk
- add menu

* Wed Aug 02 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-2mdk
- fix requires

* Wed Jul 26 2000 Alexander Skwar <> 0.3.1-1mdk
- First Mandrake package
