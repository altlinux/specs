Name: gtypist
Version: 2.8.3
Release: alt2.qa1

Summary: GNU Typist is a universal typing tutor
Summary(ru_RU.KOI8-R): Клавиатурный тренажер для консоли
Group: Education
License: GPL
Url: http://www.gnu.org/software/%name
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source: ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.bz2
Source1: %name-48.png
Source2: %name-32.png
Source3: %name-16.png
Source4: %name-64.png
Source5: ru.po

# Automatically added by buildreq on Tue Sep 30 2003
BuildRequires: xorg-x11-libs libX11-locales emacs-common emacs-leim libXaw3d libjpeg libncurses-devel libtiff libtinfo-devel libungif xpm

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

%description -l ru_RU.KOI8-R
GNU Typist - клавиатурный тренажер для консоли, содержит несколько легко
модифицируемых программ обучения для различных языков и клавиатурных
раскладок.

%package -n emacs-mode-%name
Summary: Major mode for editing %name script-files (*.typ)
Group: Editors
Requires: %name = %version-%release emacs

%description -n emacs-mode-%name
emacs-mode-%name provides syntax coloring and inserting tags for %name
script-files (*.typ)

All Emacs Lisp code is byte-copmpiled, install emacs-mode-%name-el for sources.

%package -n emacs-mode-%name-el
Summary: The Emacs Lisp sources for bytecode included in emacs-mode-%name
Group: Development/Other
Requires: %name = %version-%release

%description -n emacs-mode-%name-el
emacs-mode-%name-el contains the Emacs Lisp sources for the bytecode
included in the emacs-mode-%name package, that extends the Emacs editor.

You need to install emacs-mode-%name-el only if you intend to modify any of the
emacs-mode-%name code or see some Lisp examples.

%define _emacs_startscriptsdir %_sysconfdir/emacs/site-start.d

%prep
%setup -q
cp -f %SOURCE5 po/ru.po

%build
%configure
%make_build
make -C po update-gmo

%install
%makeinstall

# Install menu
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=GNU typist
Comment=Typing tutor
Icon=%name
Exec=%name
Terminal=false
Categories=Education;ComputerScience;X-Typing;
EOF

# Install icons
install -pD -m644 %{SOURCE1} %buildroot%_liconsdir/%name.xpm
install -pD -m644 %{SOURCE2} %buildroot%_niconsdir/%name.xpm
install -pD -m644 %{SOURCE3} %buildroot%_miconsdir/%name.xpm

# Create %name-init.el
mkdir -p %buildroot%_emacs_startscriptsdir
cat <<__INIT__ >%buildroot%_emacs_startscriptsdir/%name-init.el
;;; %name-init.el --- Startup code for gtypist mode
;;;
;;; Add this to your ~/.emacs or install this file into Emacs' site-start.d
(autoload 'gtypist-mode "gtypist-mode")
(setq auto-mode-alist       
    (cons '("\\\\.typ\\\\'" . gtypist-mode) auto-mode-alist))
__INIT__

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_infodir/%name.info.*
%_man1dir/*
%_liconsdir/%name.xpm
%_niconsdir/%name.xpm
%_miconsdir/%name.xpm
%_desktopdir/%{name}.desktop
%doc AUTHORS ChangeLog NEWS README THANKS TODO

%files -n emacs-mode-%name
%_emacs_startscriptsdir/*
%_emacslispdir/%name-mode.elc

%files -n emacs-mode-%name-el
%_emacslispdir/%name-mode.el

%changelog
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
