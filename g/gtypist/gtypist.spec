%define _unpackaged_files_terminate_build 1

Name: gtypist
Version: 2.10.1
Release: alt1

Summary: GNU Typist is a universal typing tutor
Summary(ru_RU.UTF8): Клавиатурный тренажер для консоли
Group: Education
License: GPL-3.0-or-later
Url: http://www.gnu.org/software/gtypist
VCS: https://git.savannah.gnu.org/git/gtypist.git

Source: %name-%version.tar
Source1: gtypist-48.png
Source2: gtypist-32.png
Source3: gtypist-16.png
Source4: gtypist-64.png
Patch0: gtypist-2.10.1-debian-gcc14.patch

BuildRequires: libncursesw-devel libtinfo-devel
BuildRequires: emacs-common emacs-leim emacs-gnus rpm-build-emacs
# emacs emacs-el emacs-leim-el
#
BuildRequires: help2man
# explicitly added texinfo for info files
BuildRequires: texinfo
# Upstream now requires gengetopt (README.git)
BuildRequires: gengetopt

%description
GNU Typist (or gtypist) is free software that assist you in learning
to type correctly. It is intended to be used  on a raw terminal without
graphics.

* It comes with several typing tutorials: in English for Qwerty and
Dvorak keyboards, Spanish for Spanish keyboards, as well as simpler
exercices in German, French and Norwegian.

* It interprets a simple and intuitive scripting language that describes
typing tutorials. You can easily modify existing tutorials or create new
ones according to your needs.

* It supports internationalization and already has an interface in
English, Finnish, French, German, Czech and Spanish.

It has been compiled and used in Unix (GNU/Linux, Aix,
Solaris, openBSD) and also in DOS/Windows (DOS 6.22, Windows 98).

%description -l ru_RU.UTF8
GNU Typist - клавиатурный тренажер для консоли, содержит несколько легко
модифицируемых программ обучения для различных языков и клавиатурных
раскладок.

%package -n emacs-mode-gtypist
Summary: Major mode for editing gtypist script-files (*.typ)
Group: Editors
BuildArch: noarch
Requires: gtypist = %version-%release emacs

%description -n emacs-mode-gtypist
emacs-mode-gtypist provides syntax coloring and inserting tags for gtypist
script-files (*.typ)

All Emacs Lisp code is byte-copmpiled, install emacs-mode-gtypist-el for sources.

%package -n emacs-mode-gtypist-el
Summary: The Emacs Lisp sources for bytecode included in emacs-mode-gtypist
Group: Development/Other
BuildArch: noarch
Requires: gtypist = %version-%release

%description -n emacs-mode-gtypist-el
emacs-mode-gtypist-el contains the Emacs Lisp sources for the bytecode
included in the emacs-mode-gtypist package, that extends the Emacs editor.

You need to install emacs-mode-gtypist-el only if you intend to modify any of the
emacs-mode-gtypist code or see some Lisp examples.

%define _emacs_startscriptsdir %_sysconfdir/emacs/site-start.d

%prep
%setup
%autopatch -p1

%build
# We need to explicitly pass prefix to autogen, as the default is incorrect
./autogen.sh --prefix="%_prefix"

%install
%makeinstall_std

# Install menu
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/gtypist.desktop <<EOF
[Desktop Entry]
Type=Application
Name=GNU typist
Comment=Typing tutor
Icon=gtypist
Exec=gtypist
Terminal=true
Categories=Education;ComputerScience;X-Typing;
EOF

# Install icons
install -pD -m644 %SOURCE1 %buildroot%_liconsdir/gtypist.xpm
install -pD -m644 %SOURCE2 %buildroot%_niconsdir/gtypist.xpm
install -pD -m644 %SOURCE3 %buildroot%_miconsdir/gtypist.xpm

# Create gtypist-init.el
mkdir -p %buildroot%_emacs_startscriptsdir
cat <<__INIT__ >%buildroot%_emacs_startscriptsdir/gtypist-init.el
;;; gtypist-init.el --- Startup code for gtypist mode
;;;
;;; Add this to your ~/.emacs or install this file into Emacs' site-start.d
(autoload 'gtypist-mode "gtypist-mode")
(setq auto-mode-alist
    (cons '("\\\\.typ\\\\'" . gtypist-mode) auto-mode-alist))
__INIT__

%find_lang gtypist

%files -f gtypist.lang
%_bindir/*
%_datadir/gtypist
%_datadir/info/gtypist.??.info.xz
%_infodir/gtypist.info.*
%_man1dir/*
%_liconsdir/gtypist.xpm
%_niconsdir/gtypist.xpm
%_miconsdir/gtypist.xpm
%_desktopdir/gtypist.desktop
%doc AUTHORS ChangeLog NEWS README THANKS TODO

%files -n emacs-mode-gtypist
%_emacs_startscriptsdir/*
%_emacslispdir/gtypist-mode.elc

%files -n emacs-mode-gtypist-el
%_emacslispdir/gtypist-mode.el

%changelog
* Wed Oct 29 2025 Pavel Petrykin <silverducks@altlinux.org> 2.10.1-alt1
- New version.

* Mon Mar 21 2022 Ilya Mashkin <oddity@altlinux.ru> 2.9.5-alt2
- add more BR emacs*
- Update License tag

* Mon Nov 20 2017 Igor Vlasenko <viy@altlinux.ru> 2.9.5-alt1
- NMU: updated to 2.9.5

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1.1
- NMU: added BR: texinfo

* Mon Feb 03 2014 Yuri N. Sedunov <aris@altlinux.org> 2.9.4-alt1
- 2.9.4

* Sun Nov 24 2013 Yuri N. Sedunov <aris@altlinux.org> 2.9.3-alt1
- 2.9.3
- updated buildreqs
- fixed desktop file

* Fri Mar 29 2013 Andrey Cherepanov <cas@altlinux.org> 2.8.3-alt2.qa2
- Fix build with new version of xorg

* Sat Apr 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.8.3-alt2.qa1
- NMU: converted menu to desktop file

* Thu Nov 11 2010 Andrey Cherepanov <cas@altlinux.org> 2.8.3-alt2
- update Russian translataion
- fix run in Russian locale (closes: #24543)

* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.8.3-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for gtypist
  * obsolete-call-in-post-install-info for gtypist
  * postclean-05-filetriggers for spec file

* Fri Apr 10 2009 Ilya Mashkin <oddity@altlinux.ru> 2.8.3-alt1
- 2.8.3

* Thu Sep 25 2008 Ilya Mashkin <oddity@altlinux.ru> 2.8-alt1
- 2.8

* Tue Sep 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.7-alt1
- 2.7
- emacs-mode* packages.

* Sat Sep 07 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.6-alt2
- Fixed menu script - now it launching gtypist in xterm window due
  to kde konsole bugs

* Tue Apr 30 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.6-alt1
- 2.6

* Mon Jan 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.5-alt1
- First build for Sisyphus.
