# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs22.spec,v 1.60 2006/09/12 18:38:21 eugene Exp $

%define emacs_version 24.1
%define gnus_version 5.13
%define shortname emacs
%define tramp_version 2.2.3
%define speedbar_version 1.0
%define erc_version 5.3
%define nxml_version 0.2.20041004
%define cedet_version 1.0

%define cedet_release alt3

%define cvsdate 20090110
%define rel_base alt2

# subpackages to build;
%def_enable nox
%def_enable athena
%def_enable gtk
%def_enable gtk3
%def_enable motif

Name: emacs24
Version: %emacs_version
%ifdef cvsbuild
Release: %rel_base.%cvsdate
%else
%ifdef pretest
Release: %rel_base.%pretest
%else
Release: %rel_base
%endif
%endif

Group: Editors
Summary: GNU Emacs text editor
License: GPLv3 or later

URL: http://www.gnu.org/software/emacs/

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

%ifdef cvsbuild
Source0: %shortname-%cvsdate.tar
%else
Source0: %shortname-%emacs_version.tar
%endif

Source7: README.KOI8-U

# from Serhij Hlodin
Source16: CHANGES.ukr
Source17: INSTALL.ukr
Source18: README.UK

Source24: %name-nox.alternatives
Source25: %name-athena.alternatives
Source26: %name-motif.alternatives
Source27: %name-gtk.alternatives
Source28: %name-gtk3.alternatives

# Mdk's and ALT's global configs merged: the X resources
Source31: %shortname-22.0.91-alt0.19-xresources-ALT

# List of some large .elc files to be compressed:
#Source40: %shortname-21.2-el-to-compress.ls

Source41: emacs21-rus-win-keyboard-alt2.el

Source50: README.ALT-ru_RU.KOI8-R
Source51: check-shadows

Source60: %name.desktop

Source70: configure-lispintro
Source71: configure-lispref

# We use awk for output parsing and error-msg detection:
BuildRequires(build): awk
# We use zme:
BuildRequires(install): bzip2-utils
# <term.h> is there since then:
BuildRequires(build): libtinfo >= 5.2.20020622-alt2
# Emacs now requires Texinfo version 4.2.
BuildRequires(build): texinfo >= 4.2

# %_configure_target must set --host= for a correct emacs build;
# added since then:
BuildRequires(build): rpm >= 4.0.4-alt12

# We need sendmail to properly dump emacs during bootstrap
BuildRequires(build): sendmail-common

# We need emacs-base
BuildPreReq: %shortname-base >= 0.0.5-alt2

BuildPreReq: python-base python-modules-compiler python-modules-encodings rpm-build-python

# Now el-pkgutils in emacs-devel
BuildPreReq: %shortname-devel
# All emacs pkgs should be removed from the list.

# BuildPreReq: tetex-core tetex-latex

# Build gtk binary with sound
BuildRequires(build): libalsa-devel

# Requires for UI build
BuildRequires(build): libtinfo-devel
# athena
%if_enabled athena
BuildRequires(build): libXaw3d-devel libXaw-devel
%endif
# motif
%if_enabled motif
BuildRequires(build): openmotif-devel
%endif
# gtk
%if_enabled gtk
BuildRequires(build): libgtk+2-devel
%endif
# gtk3
%if_enabled gtk3
BuildRequires(build): libgtk+3-devel
%endif

# Xft support
BuildRequires(build): libXft-devel

# Mouse support in console
BuildRequires(build): libgpm-devel

# Requires for graphics support
BuildRequires(build): libjpeg-devel
BuildRequires(build): libpng-devel
BuildRequires(build): libtiff-devel
BuildRequires(build): libgif-devel
BuildRequires(build): libXpm-devel
BuildRequires(build): librsvg-devel
BuildRequires(build): libImageMagick-devel

# GnuTLS support
BuildRequires(build): libgnutls-devel

# libxml2 support
BuildRequires(build): libxml2-devel

# SELinux support
BuildRequires(build): libselinux-devel

# Requires for D-bus support in X builds
BuildRequires(build): libdbus-devel

# for update_desktopdb
# Requires(post,postun): desktop-file-utils
# BuildPreReq: desktop-file-utils

# Strange build deps:
#BuildRequires: postfix, w3m

# Automatically added by buildreq on Thu Apr 02 2009
BuildRequires: imake libXext-devel libXmu-devel libXp-devel libXpm-devel tzdata xorg-cf-files

%description
Emacs is an extensible, customizable, self-documenting real-time
display editor.  Emacs contains special code editing features, an
extension language (Emacs Lisp), and the capability to read mail, news
and more without leaving the editor.

This package includes things you need to run the Emacs editor, so you
need to install this package if you intend to use Emacs.  You also
need to install the actual Emacs program package (%name-nox or
%name-X11).  Install %name-nox if you are not going to use the X
Window System; install %name-X11 if you will be using X.

#
%package common
Summary: Things needed to run the GNU Emacs text editor
Summary(ru_RU.UTF-8): Необходимое для запуска текстового редактора GNU Emacs
Group: Editors
Provides: %_libexecdir/%shortname
Obsoletes: %name
Obsoletes: %shortname-common
Provides: %shortname-common = %emacs_version-%release
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: emacs21-common
Obsoletes: emacs22-common
Obsoletes: emacs23-common
Provides: emacs21-common = %emacs_version-%release
Provides: emacs22-common = %emacs_version-%release
Provides: emacs23-common = %emacs_version-%release
# Common is useless without an Emacs binary:
Requires: %name = %emacs_version-%release
# speedbar now separate package
Requires: %shortname-speedbar
# tramp now separate package
Requires: %shortname-tramp

Requires: %shortname-base >= 0.0.5-alt2

Conflicts: etcskel < 2.0.2-alt1
Conflicts: emacs-prog-modes < 0.1-alt7
# ispell-uk 0.5 is broken, and can cause hang in flyspell mode
Conflicts: ispell-uk < 0.6-alt1
# emacs24 have ses inside
Obsoletes: %shortname-ses <= 1.0-alt2.031130
Provides: %shortname-ses = %emacs_version-%release
# emacs24 conflicts with old emacs-w3 (with url package inside)
Conflicts: %shortname-w3 <= 4.0-alt0.8.pre.47
Provides: %shortname-url = %emacs_version-%release
# gnuserv seems needed to be build with emacs24
Conflicts: %shortname-gnuserv <= 3.12.7-alt1

# otherwise we have heavy useless dependency on python
AutoReq: yes, nopython

%description common
GNU Emacs is an extensible, customizable, self-documenting real-time
display editor.  Emacs contains special code editing features, an
extension language (Emacs Lisp), and the capability to read mail, news
and more without leaving the editor.

This package includes things you need to run the Emacs editor, so you
need to install this package if you intend to use Emacs.  You also
need to install the actual Emacs program package (%name-nox or
%name-X11).  Install %name-nox if you are not going to use the X
Window System; install %name-X11 if you will be using X.

#
%package el
Summary: The sources for Lisp programs included with GNU Emacs
Summary(ru_RU.UTF-8): Исходный код Lisp программ, поставляемых с GNU Emacs
Group: Development/Other
BuildArch: noarch
Requires: %name-common = %emacs_version-%release
Obsoletes: %shortname-el
Provides: %shortname-el = %emacs_version-%release
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: emacs21-el
Obsoletes: emacs22-el
Obsoletes: emacs23-el
Provides: emacs21-el = %emacs_version-%release
Provides: emacs22-el = %emacs_version-%release
Provides: emacs23-el = %emacs_version-%release

%description el
Emacs-el contains the Emacs Lisp sources for many of the programs
included with the main GNU Emacs text editor package.

You need to install %name-el only if you intend to modify any of the
Emacs packages or see some Lisp examples.

If you need the sources for %name-leim, install %name-leim-el.

#
%package leim
Summary: GNU Emacs Lisp code for input methods for internationalization
Summary(ru_RU.UTF-8): Код GNU Emacs Lisp для методов ввода
Group: Editors
BuildArch: noarch
Requires: %name-common = %emacs_version-%release
Obsoletes: %shortname-leim
Provides: %shortname-leim = %emacs_version-%release
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: emacs21-leim
Obsoletes: emacs22-leim
Obsoletes: emacs23-leim
Provides: emacs21-leim = %emacs_version-%release
Provides: emacs22-leim = %emacs_version-%release
Provides: emacs23-leim = %emacs_version-%release

%description leim
The Lisp code for input methods for various international scripts for GNU Emacs.

#
%package leim-el
Summary: The Emacs Lisp source code for input methods included in %name-leim
Summary(ru_RU.UTF-8): Исходный код Lisp для методов ввода, поставляемых с %name-leim
Group: Development/Other
BuildArch: noarch
Requires: %name-leim = %emacs_version-%release
Obsoletes: %shortname-leim-el
Provides: %shortname-leim-el = %emacs_version-%release
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: emacs21-leim-el
Obsoletes: emacs22-leim-el
Obsoletes: emacs23-leim-el
Provides: emacs21-leim-el = %emacs_version-%release
Provides: emacs22-leim-el = %emacs_version-%release
Provides: emacs23-leim-el = %emacs_version-%release

%description leim-el
Emacs-leim-el contains the Emacs Lisp sources for the Emacs Lisp code
for input methods for various international scripts of GNU Emacs.

You need to install %name-leim-el only if you intend to modify any of theses
GNU Emacs packages, see some Lisp examples or for reference for configuring your
localized input methods.

#
%if_enabled nox
%package nox
Summary: The GNU Emacs text editor without support for the X Window System
Summary(ru_RU.UTF-8): Текстовый редактор GNU Emacs без поддержки X Window System
Group: Editors
PreReq: %name-common = %emacs_version-%release
Provides: %name = %emacs_version-%release
Provides: emacsen
Provides: %shortname = %emacs_version-%release
Obsoletes: %shortname-nox
Provides: %shortname-nox = %emacs_version-%release
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: emacs21-nox
Obsoletes: emacs22-nox
Obsoletes: emacs23-nox
Provides: emacs21-nox = %emacs_version-%release
Provides: emacs22-nox = %emacs_version-%release
Provides: emacs23-nox = %emacs_version-%release
# 0.2.0 for new alternatives format
PreReq: alternatives >= 0.2.0
Provides: /usr/bin/emacs

%description nox
Emacs-nox is the GNU Emacs text editor program without support for
the X Window System.

You need to install this package only if you plan on exclusively using
GNU Emacs without the X Window System (%name-X11-athena, %name-X11-motif, 
%name-X11-gtk will work both in X and out of X, but %name-nox will only work 
outside of X). You will also need to install the %name-common package in
order to run GNU Emacs.
%endif

#
%package X11
Summary: Things needed to run the GNU Emacs text editor in X Window System
Summary(ru_RU.UTF-8): Необходимое для запуска редактора GNU Emacs в X Window System
Group: Editors
BuildArch: noarch
PreReq: %name-common = %emacs_version-%release
Requires: emacs-X11-program
Conflicts: app-defaults < 0.2.1-alt1
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: %shortname-X11
Obsoletes: emacs22-X11
Obsoletes: emacs23-X11
Provides: emacs22-X11 = %emacs_version-%release
Provides: emacs23-X11 = %emacs_version-%release

%description X11
This package includes things you need to run the Emacs editor in X Window
System, so you need to install this package if you intend to use Emacs with X
Window.  You also need to install the actual Emacs program package
(%name-X11-athena, %name-X11-motif or %name-X11-gtk). You will also need to
install the %name-common package in order to run GNU Emacs.

#
%if_enabled athena
%package X11-athena
Summary: The GNU Emacs text editor for the X Window System (athena)
Summary(ru_RU.UTF-8): Текстовый редактор GNU Emacs для X Window System (athena)
Group: Editors
PreReq: %name-common = %emacs_version-%release
PreReq: %name-X11 = %emacs_version-%release
Provides: %name = %emacs_version-%release
Provides: emacsen
Provides: emacs-X11-program
Provides: %shortname = %emacs_version-%release
Provides: %shortname-X11 = %emacs_version-%release
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: emacs21-X11
Obsoletes: emacs22-X11-athena
Obsoletes: emacs23-X11-athena
Provides: emacs21-X11 = %emacs_version-%release
Provides: emacs22-X11-athena = %emacs_version-%release
Provides: emacs23-X11-athena = %emacs_version-%release
# 0.2.0 for new alternatives format
PreReq: alternatives >= 0.2.0
Provides: /usr/bin/emacs

%description X11-athena
Emacs-X11-athena includes the GNU Emacs text editor program for use with the X
Window System using athena widget set (it provides support for the mouse and
other GUI elements).  Emacs-X11-athena will also run GNU Emacs outside of X,
but it has a larger memory footprint than the 'non-X' GNU Emacs package
(%name-nox).

Install %name-X11-athena if you are going to use Emacs with the X Window
System and you like athena look.  You should also install %name-X11-athena if
you are going to run GNU Emacs both with and without X (it will work fine both
ways).  You will also need to install the %name-common and %name-X11 package
in order to run Emacs.
%endif

#
%if_enabled motif
%package X11-motif
Summary: The GNU Emacs text editor for the X Window System (motif)
Summary(ru_RU.UTF-8): Текстовый редактор GNU Emacs для X Window System (motif)
Group: Editors
PreReq: %name-common = %emacs_version-%release
PreReq: %name-X11 = %emacs_version-%release
Provides: %name = %emacs_version-%release
Provides: emacsen
Provides: emacs-X11-program
Provides: %shortname = %emacs_version-%release
Provides: %shortname-X11 = %emacs_version-%release
# 0.2.0 for new alternatives format
PreReq: alternatives >= 0.2.0
Provides: /usr/bin/emacs
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: emacs22-X11-motif
Obsoletes: emacs23-X11-motif
Provides: emacs22-X11-motif = %emacs_version-%release
Provides: emacs23-X11-motif = %emacs_version-%release

%description X11-motif
Emacs-X11-motif includes the GNU Emacs text editor program for use with the X
Window System using motif toolkit (it provides support for the mouse and
other GUI elements).  Emacs-X11-motif will also run GNU Emacs outside of X, but
it has a larger memory footprint than the 'non-X' GNU Emacs package
(%name-nox).

Install %name-X11-motif if you are going to use Emacs with the X Window
System and you like motif look.  You should also install %name-X11-motif if you
are going to run GNU Emacs both with and without X (it will work fine both
ways).  You will also need to install the %name-common and %name-X11 package in
order to run Emacs.
%endif

#
%if_enabled gtk
%package X11-gtk
Summary: The GNU Emacs text editor for the X Window System (gtk)
Summary(ru_RU.UTF-8): Текстовый редактор GNU Emacs для X Window System (gtk)
Group: Editors
PreReq: %name-common = %emacs_version-%release
PreReq: %name-X11 = %emacs_version-%release
Provides: %name = %emacs_version-%release
Provides: emacsen
Provides: emacs-X11-program
Provides: %shortname = %emacs_version-%release
Provides: %shortname-X11 = %emacs_version-%release
# 0.2.0 for new alternatives format
PreReq: alternatives >= 0.2.0
Provides: /usr/bin/emacs
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: emacs22-X11-gtk
Obsoletes: emacs23-X11-gtk
Provides: emacs22-X11-gtk = %emacs_version-%release
Provides: emacs23-X11-gtk = %emacs_version-%release

%description X11-gtk
Emacs-X11-gtk includes the GNU Emacs text editor program for use with the X
Window System using gtk+ toolkit v.2 (it provides support for the mouse and
other GUI elements).  Emacs-X11-gtk will also run GNU Emacs outside of X, but
it has a larger memory footprint than the 'non-X' GNU Emacs package
(%name-nox).

Install %name-X11-gtk if you are going to use Emacs with the X Window
System and you like gtk+ look.  You should also install %name-X11-gtk if you
are going to run GNU Emacs both with and without X (it will work fine both
ways).  You will also need to install the %name-common and %name-X11 package
in order to run Emacs.
%endif

#
%if_enabled gtk3
%package X11-gtk3
Summary: The GNU Emacs text editor for the X Window System (gtk3)
Summary(ru_RU.UTF-8): Текстовый редактор GNU Emacs для X Window System (gtk3)
Group: Editors
PreReq: %name-common = %emacs_version-%release
PreReq: %name-X11 = %emacs_version-%release
Provides: %name = %emacs_version-%release
Provides: emacsen
Provides: emacs-X11-program
Provides: %shortname = %emacs_version-%release
Provides: %shortname-X11 = %emacs_version-%release
# 0.2.0 for new alternatives format
PreReq: alternatives >= 0.2.0
Provides: /usr/bin/emacs
# emacs24 obsoletes emacs21, emacs22 and emacs23
Provides: emacs24-X11-gtk3 = %emacs_version-%release

%description X11-gtk3
Emacs-X11-gtk3 includes the GNU Emacs text editor program for use with the X
Window System using gtk+ toolkit v.3 (it provides support for the mouse and
other GUI elements).  Emacs-X11-gtk3 will also run GNU Emacs outside of X, but
it has a larger memory footprint than the 'non-X' GNU Emacs package
(%name-nox).

Install %name-X11-gtk3 if you are going to use Emacs with the X Window
System and you like gtk+ look.  You should also install %name-X11-gtk3 if you
are going to run GNU Emacs both with and without X (it will work fine both
ways).  You will also need to install the %name-common and %name-X11 package
in order to run Emacs.
%endif


#
%package info
Summary: Info docs for GNU Emacs text editor
Summary(ru_RU.UTF-8): Документация по GNU Emacs в формате Info
Group: Editors
BuildArch: noarch
Obsoletes: emacs22-info
Obsoletes: emacs23-info
Provides: emacs22-info = %emacs_version-%release
Provides: emacs23-info = %emacs_version-%release
Requires: %name-common = %emacs_version-%release

%description info
This package contain full GNU Emacs documentation in Info format except
Emacs Lisp language documentation that contains in %name-elisp-manual
package

#
%package elisp-manual
Summary: Emacs Lisp Manual
Summary(ru_RU.UTF-8): Руководство по языку Emacs Lisp
Group: Editors
BuildArch: noarch
Requires: %name-common = %emacs_version-%release
# obsoletes old elisp-manual
Obsoletes: %shortname-elisp-manual <= 2.8-alt1
Provides: %shortname-elisp-manual = %emacs_version-%release
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: emacs22-elisp-manual
Obsoletes: emacs23-elisp-manual
Provides: emacs22-elisp-manual = %emacs_version-%release
Provides: emacs23-elisp-manual = %emacs_version-%release

%description elisp-manual
This package contain full description of Emacs Lisp language

#
%package gnus
Version: %gnus_version
Summary: Gnus package for Emacs
Summary(ru_RU.UTF-8): Пакет Gnus для Emacs
Group: Editors
BuildArch: noarch
Requires: %name-common = %emacs_version-%release
Conflicts: %shortname-ngnus
Provides: gnus
# obsoletes old gnus
Obsoletes: %shortname-gnus <= 5.10.6
Provides: %shortname-gnus = %gnus_version-%release
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: emacs22-gnus
Obsoletes: emacs23-gnus
Provides: emacs22-gnus = %gnus_version-%release
Provides: emacs23-gnus = %gnus_version-%release

%description gnus
Gnus is a program for Emacs which enable read news and mail from Emacs.

All Emacs Lisp code is byte-copmpiled, install %name-gnus-el for sources.

#
%package gnus-el
Version: %gnus_version
Summary: The Emacs Lisp sources for bytecode included in %name-gnus
Summary(ru_RU.UTF-8): Исходный код Lisp для байткода из %name-gnus
Group: Development/Other
BuildArch: noarch
Requires: %name-common = %emacs_version-%release
Requires: %name-gnus = %gnus_version-%release
# obsoletes old gnus
Obsoletes: %shortname-gnus-el <= 5.10.6
Provides: %shortname-gnus-el = %gnus_version-%release
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: emacs22-gnus-el
Obsoletes: emacs23-gnus-el
Provides: emacs22-gnus-el = %gnus_version-%release
Provides: emacs23-gnus-el = %gnus_version-%release

%description gnus-el
%name-gnus-el contains the Emacs Lisp sources for the bytecode
included in the %name-gnus package, that extends the Emacs editor.

You need to install %name-gnus-el only if you intend to modify any of the
%name-gnus code or see some Lisp examples.

#
%package speedbar
Version: %speedbar_version
Summary: Speedbar package for Emacs
Group: Editors
BuildArch: noarch
Requires: %name-common = %emacs_version-%release
Provides: speedbar
Provides: %shortname-speedbar = %speedbar_version-%release
# obsoletes old speedbar
Conflicts: %shortname-cedet <= 1.0-alt0.7.beta3b
Obsoletes: %shortname-cedet-speedbar <= 0.15beta2-alt0.8.beta3b
Provides: %shortname-cedet-speedbar = %speedbar_version-%release
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: emacs22-speedbar
Obsoletes: emacs23-speedbar
Provides: emacs22-speedbar = %speedbar_version-%release
Provides: emacs23-speedbar = %speedbar_version-%release

%description speedbar
Speedbar - Everything browser for Emacs.

#
%package erc
Version: %erc_version
Summary: Emacs client for IRC
Summary(ru_RU.UTF-8): IRC Клиент для Emacs
Group: Networking/IRC
BuildArch: noarch
Requires: %name-common = %emacs_version-%release
Provides: %shortname-erc = %erc_version-%release
# obsoletes old emacs-erc
Obsoletes: %shortname-erc <= 5.0.4-alt1
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: emacs22-erc
Obsoletes: emacs23-erc
Provides: emacs22-erc = %erc_version-%release
Provides: emacs23-erc = %erc_version-%release

%description erc
ERC is an IRC client for Emacs.

#
%package erc-el
Version: %erc_version
Summary: The Emacs Lisp sources for bytecode included in %name-erc
Summary(ru_RU.UTF-8): Исходный код Lisp для байткода из %name-erc
Group: Development/Other
BuildArch: noarch
Requires: %name-common = %emacs_version-%release
Requires: %name-erc = %erc_version-%release
Obsoletes: emacs22-erc-el
Obsoletes: emacs23-erc-el
Provides: emacs22-erc-el = %emacs_version-%release
Provides: emacs23-erc-el = %emacs_version-%release

%description erc-el
%name-erc-el contains the Emacs Lisp sources for the bytecode
included in the %name-erc package, that extends the Emacs editor.

You need to install %name-erc-el only if you intend to modify any of the
%name-erc code or see some Lisp examples.

#
%package tramp
Version: %tramp_version
Summary: Tramp package for Emacs
Summary(ru_RU.UTF-8): Пакет Tramp для Emacs
Group: Editors
BuildArch: noarch
Requires: %name-common = %emacs_version-%release
Provides: %shortname-tramp = %tramp_version-%release
Obsoletes: %shortname-tramp < %tramp_version
# emacs24 obsoletes emacs21, emacs22 and emacs23
Obsoletes: emacs22-tramp
Obsoletes: emacs23-tramp
Provides: emacs22-tramp = %tramp_version-%release
Provides: emacs23-tramp = %tramp_version-%release

%description tramp
TRAMP stands for `Transparent Remote (file) Access, Multiple
Protocol'.  This package provides remote file editing, similar to
Ange-FTP.

The difference is that Ange-FTP uses FTP to transfer files between
the local and the remote host, whereas TRAMP uses a combination of
`rsh' and `rcp' or other work-alike programs, such as 'ssh'/'scp'.

#
%package tramp-el
Version: %tramp_version
Summary: The Emacs Lisp sources for bytecode included in %name-tramp
Summary(ru_RU.UTF-8): Исходный код Lisp для байткода из %name-tramp
Group: Development/Other
BuildArch: noarch
Requires: %name-common = %emacs_version-%release
Requires: %name-tramp = %tramp_version-%release
Obsoletes: emacs22-tramp-el
Obsoletes: emacs23-tramp-el
Provides: emacs22-tramp-el = %emacs_version-%release
Provides: emacs23-tramp-el = %emacs_version-%release

%description tramp-el
%name-tramp-el contains the Emacs Lisp sources for the bytecode
included in the %name-tramp package, that extends the Emacs editor.

You need to install %name-tramp-el only if you intend to modify any of the
%name-tramp code or see some Lisp examples.

#
%package nxml-mode
Version: %nxml_version
Summary: Emacs mode for editing XML
Summary(ru_RU.UTF-8): Режим Emacs для редактирования XML
Group: Editors
BuildArch: noarch
Requires: %name-common = %emacs_version-%release
Obsoletes: %shortname-nxml-mode < %nxml_version
Provides: %shortname-nxml-mode = %nxml_version-%release
Obsoletes: emacs22-nxml-mode
Obsoletes: emacs23-nxml-mode
Provides: emacs22-nxml-mode = %emacs_version-%release
Provides: emacs23-nxml-mode = %emacs_version-%release

%description nxml-mode
This is a new major mode for GNU Emacs for editing XML documents. It
supports editing well-formed XML documents and also provides
schema-sensitive editing of XML documents using RELAX NG Compact Syntax.

#
%package nxml-mode-el
Version: %nxml_version
Summary: The Emacs Lisp sources for bytecode included in %name-nxml-mode
Summary(ru_RU.UTF-8): Исходный код Lisp для байткода из %name-nxml-mode
Group: Development/Other
BuildArch: noarch
Requires: %name-common = %emacs_version-%release
Requires: %name-nxml-mode = %nxml_version-%release
Obsoletes: emacs22-nxml-mode-el
Obsoletes: emacs23-nxml-mode-el
Provides: emacs22-nxml-mode-el = %emacs_version-%release
Provides: emacs23-nxml-mode-el = %emacs_version-%release

%description nxml-mode-el
%name-nxml-mode-el contains the Emacs Lisp sources for the bytecode
included in the %name-nxml-mode package, that extends the Emacs editor.

You need to install %name-nxml-mode-el only if you intend to modify any of the
%name-nxml-mode code or see some Lisp examples.


#
%package cedet
Version: %cedet_version
Release: %cedet_release
Summary: CEDET - Collection of Emacs Development Enviromnent Tools
Group: Editors
BuildArch: noarch
Requires: %name-common = %emacs_version
Obsoletes: %shortname-cedet < %cedet_version-%cedet_release
Provides: %shortname-cedet = %cedet_version-%cedet_release
Obsoletes: emacs22-cedet
Obsoletes: emacs23-cedet
Provides: emacs22-cedet = %emacs_version-%release
Provides: emacs23-cedet = %emacs_version-%release

%description cedet
CEDET - Collection of Emacs Development Enviromnent Tools

CEDET is a top-level project containing several individual package for Emacs,
including:
   EIEIO - CLOS layer for Emacs Lisp
   Semantic - Parser Infrastructure for Emacs
   Speedbar - Everything browser
   EDE - File manager/ Makefile generator
   COGRE - Connected Graph Editor

#
%package cedet-el
Version: %cedet_version
Release: %cedet_release
Summary: The Emacs Lisp sources for bytecode included in %name-cedet
Summary(ru_RU.UTF-8): Исходный код Lisp для байткода из %name-cedet
Group: Development/Other
BuildArch: noarch
Requires: %name-common = %emacs_version
Requires: %name-cedet = %cedet_version-%cedet_release
Obsoletes: emacs22-cedet-el
Obsoletes: emacs23-cedet-el
Provides: emacs22-cedet-el = %emacs_version-%release
Provides: emacs23-cedet-el = %emacs_version-%release

%description cedet-el
%name-cedet-el contains the Emacs Lisp sources for the bytecode
included in the %name-cedet package, that extends the Emacs editor.

You need to install %name-cedet-el only if you intend to modify any of the
%name-cedet code or see some Lisp examples.


%prep
%setup -n %shortname

# Ukrainian docs:
cp %SOURCE16 .
cp %SOURCE17 .
cp %SOURCE18 .
cp %SOURCE7 .

# README.ALT
cp %SOURCE50 .

perl -pi -e 's|(\.\./info/[[:alpha:]-]+)|$1.info|g' doc/emacs/*
perl -pi -e 's|(\.\./info/[[:alpha:]-]+)|$1.info|g' doc/misc/*
# rm -rf info/*

# Touch changed el files
touch lisp/faces.el lisp/gnus/mm-util.el lisp/gnus/rfc2047.el \
    lisp/international/mule-cmds.el lisp/jka-cmpr-hook.el \
    lisp/language/cyril-util.el lisp/language/cyrillic.el \
    lisp/mouse-sel.el lisp/mouse.el lisp/saveplace.el \
    lisp/term/x-win.el lisp/textmodes/ispell.el

%define Substage printf 'Substage #%%s. %%s:\\n'

# We build five binaries (with X and without X support) 
# in several symmetric substages.

%Substage 0 "Clear and create the build directories"
[ -d build-nox ] && rm -rf build-nox; mkdir -p build-nox
[ -d build-athena ] && rm -rf build-athena; mkdir -p build-athena
[ -d build-motif ] && rm -rf build-motif; mkdir -p build-motif
[ -d build-gtk ] && rm -rf build-gtk; mkdir -p build-gtk
[ -d build-gtk3 ] && rm -rf build-gtk3; mkdir -p build-gtk3

%build
autoconf -f
# Try to detect errors and break on errors:
%define detect_elisp_errs 2>&1 | awk '/!! /{ r++; } END{ if (r) printf "There were %%d errors while recompiling Emacs Lisp modules.\\n", r; exit r; } /.*/'

# We do not want to use anything from an existing Emacs installation:
export EMACSLOADPATH="$(pwd)"/lisp

# we require at least one binary to use at substage 3 and later
%if_enabled gtk3
  %define stage3bin gtk3
%else
  %if_enabled gtk
    %define stage3bin gtk
  %else
    %if_enabled athena
      %define stage3bin athena
    %else
      %if_enabled motif
        %define stage3bin motif
      %else
        %if_enabled nox
          %define stage3bin nox
        %else
          echo "ERROR: You disabled all %shortname binary subpackages!"
          echo "enable at least one (nox, athena, motif or gtk) binary subpackage."
          exit 11;
        %endif
      %endif
    %endif
  %endif
%endif

%Substage 1 "Configure"

%define _configure_script ../configure
%if_enabled nox
pushd build-nox
%configure --sharedstatedir=/var --with-pop --with-x=no --without-sound --with-gpm --without-dbus --without-rsvg --without-compress-info --with-wide-int
popd
%endif
%if_enabled athena
pushd build-athena
%configure --sharedstatedir=/var --with-pop --with-x-toolkit=athena --with-png --with-jpeg --with-xpm --with-gif --with-tiff --enable-font-backend --with-freetype --with-xft --with-dbus --without-rsvg --without-compress-info --with-wide-int
popd
%endif
%if_enabled gtk
pushd build-gtk
%configure --sharedstatedir=/var --with-pop --with-x-toolkit=gtk --with-png --with-jpeg --with-xpm --with-gif --with-tiff --with-gpm --enable-font-backend --with-freetype --with-xft --with-dbus --with-rsvg --without-compress-info --with-wide-int
popd
%endif
%if_enabled motif
# export CFLAGS="%optflags -I%_prefix/X11R6/include"
# export LDFLAGS="-Wl,-L%_prefix/X11R6/%_lib"
pushd build-motif
%configure --sharedstatedir=/var --with-pop --with-x-toolkit=motif --with-png --with-jpeg --with-xpm --with-gif --with-tiff --enable-font-backend --with-freetype --with-xft --with-dbus --without-rsvg --without-compress-info --with-wide-int
popd
%endif
%if_enabled gtk3
pushd build-gtk3
%configure --sharedstatedir=/var --with-pop --with-x-toolkit=gtk3 --with-png --with-jpeg --with-xpm --with-gif --with-tiff --with-gpm --enable-font-backend --with-freetype --with-xft --with-dbus --with-rsvg --without-compress-info --with-wide-int
popd
%endif

%Substage 2 "Initial make all" 
#no SMP
%if_enabled nox
%ifdef cvsbuild
pushd build-nox; make bootstrap; popd
%else
pushd build-nox; make; popd
%endif
%endif
%if_enabled athena
%ifdef cvsbuild
pushd build-athena; make bootstrap; popd
%else
pushd build-athena; make; popd
%endif
%endif
%if_enabled motif
%ifdef cvsbuild
pushd build-motif; make bootstrap; popd
%else
pushd build-motif; make; popd
%endif
%endif
%if_enabled gtk
%ifdef cvsbuild
pushd build-gtk; make bootstrap; popd
%else
pushd build-gtk; make; popd
%endif
%endif
%if_enabled gtk3
%ifdef cvsbuild
pushd build-gtk3; make bootstrap; popd
%else
pushd build-gtk3; make; popd
%endif
%endif

%Substage 3 "Make supplementary (and important) things only once (asymmetricly) 
 (for possibly more capabilities -- in the X build)"

pushd build-%stage3bin
make -C doc/emacs
make -C doc/misc
# Removed recompilation lisp sources on third stage - make bootstrap do it
%ifndef cvsbuild
{
    # Recompile so that the patches we have applied are effective:
    # The goal `updates' should update all the generated code
    # (autoloads, custom-deps etc.). 
    # Also compile php-mode and the small new file for Cyrillic support.
    make -C lisp \
        updates \
        international/cyrillic-codepages-setup.elc \
        recompile
#       progmodes/php-mode.elc \
} %detect_elisp_errs
%endif
popd # build-%stage3bin

%Substage 4 "Final make all (now that we have all patched Lisp code compiled, 
 also a bit asymmetric), clean previous binaries"

%define override_from_stage3() if [ ! '%stage3bin'=='%{1}' ]; then rm -rf etc leim; ln -s -f ../build-%stage3bin/{etc,leim} . ; fi

# no SMP
%if_enabled athena
pushd build-athena
  # Override some data with more complete from the X build
  # (exactly the X variant of the data will be included in the package,
  # so emacs-athena has to work correctly in this environment):
  %override_from_stage3 athena
  rm -f src/emacs src/emacs-*
  make
popd
%endif
%if_enabled motif
pushd build-motif
  # Override some data with more complete from the X build
  # (exactly the X variant of the data will be included in the package,
  # so emacs-motif has to work correctly in this environment):
  %override_from_stage3 motif
  rm -f src/emacs src/emacs-*
  make
popd
%endif
%if_enabled nox
pushd build-nox
  # Override some data with more complete from the X build
  # (exactly the X variant of the data will be included in the package,
  # so emacs-nox has to work correctly in this environment):
  %override_from_stage3 nox
  rm -f src/emacs src/emacs-*
  make
popd
%endif
%if_enabled gtk
pushd build-gtk
  # Override some data with more complete from the X build
  # (exactly the X variant of the data will be included in the package,
  # so emacs-nox has to work correctly in this environment):
  %override_from_stage3 gtk
  rm -f src/emacs src/emacs-*
  make
popd
%endif
%if_enabled gtk3
pushd build-gtk3
  # Override some data with more complete from the X build
  # (exactly the X variant of the data will be included in the package,
  # so emacs-nox has to work correctly in this environment):
  %override_from_stage3 gtk3
  rm -f src/emacs src/emacs-*
  make
popd
%endif

%install
mkdir -p %buildroot%prefix
# GZIP_PROG= for disable compress installed .el files - this function better
# realized in el-pkgutils
%makeinstall -C build-%stage3bin
%if_enabled nox
install -p -m755 build-nox/src/%shortname %buildroot%_bindir/%name-nox
%endif
%if_enabled athena
install -p -m755 build-athena/src/%shortname %buildroot%_bindir/%name-athena
%endif
%if_enabled motif
install -p -m755 build-motif/src/%shortname %buildroot%_bindir/%name-motif
%endif
%if_enabled gtk
install -p -m755 build-gtk/src/%shortname %buildroot%_bindir/%name-gtk
%endif
%if_enabled gtk3
install -p -m755 build-gtk3/src/%shortname %buildroot%_bindir/%name-gtk3
%endif
# remove the installed duplicate emacs binary
# -- it'll be a link managed by `alternatives':
rm -f %buildroot%_bindir/%shortname
rm -f %buildroot%_bindir/%shortname-%emacs_version

################
# Menu support #
################
%if_with menu
  install -d %buildroot%_menudir
  cat <<'EOF' > %buildroot%_menudir/%name-X11
?package(%name-X11): \
	needs="X11" \
	section="Applications/Editors" \
	icon="%name.png" \
	title="GNU Emacs 24" \
	longtitle="Powerful editor from the GNU project" \
	command="emacs-X11"
EOF
%else
  install -d %buildroot%_desktopdir
  install -p -m644  %SOURCE60 %buildroot%_desktopdir/%name.desktop
%endif
# backwards compatibility with Master 2x/Compact 30
%{?!_niconsdir:%define _niconsdir %_iconsdir}
# New emacs icons (from Andrew Zhilin)
# now make install do it
# install -p -m644 -D etc/images/icons/hicolor/16x16/apps/emacs.png %buildroot%_miconsdir/%name.png
# install -p -m644 -D etc/images/icons/hicolor/32x32/apps/emacs.png %buildroot%_niconsdir/%name.png
# install -p -m644 -D etc/images/icons/hicolor/48x48/apps/emacs.png %buildroot%_liconsdir/%name.png
# install -p -m644 -D etc/images/icons/hicolor/24x24/apps/emacs.png %buildroot%_iconsdir/hicolor/24x24/apps/%name.png
# install -p -m644 -D etc/images/icons/hicolor/128x128/apps/emacs.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png
mv %buildroot%_miconsdir/emacs.png %buildroot%_miconsdir/%name.png
mv %buildroot%_niconsdir/emacs.png %buildroot%_niconsdir/%name.png
mv %buildroot%_liconsdir/emacs.png %buildroot%_liconsdir/%name.png
mv %buildroot%_iconsdir/hicolor/24x24/apps/emacs.png %buildroot%_iconsdir/hicolor/24x24/apps/%name.png
mv %buildroot%_iconsdir/hicolor/128x128/apps/emacs.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png
mv %buildroot%_iconsdir/hicolor/scalable/apps/emacs.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

# All the install's below have nothing to do with the Source directory
# So we want to make the command arguments shorter 
# by replacing "$RPM_BUILD_ROOT" with "."

pushd %buildroot # there will be a popd below

# leim's Makefile doesn't ignore .orig; remove them:
find .%_datadir/%shortname/%emacs_version/leim -type f -name '*.orig' -print0 \
     | xargs -0 rm -f

# Site start configuration:
# Link to a file provided by emacsen-startscripts pkg:
(cd .%_datadir/emacs/%emacs_version/lisp; ln -s ../../../../..%_sysconfdir/emacs/site-start.el)
# making start scripts
mkdir -p %buildroot%_emacs_sitestart_dir
install -p -m0644 %SOURCE41 %buildroot%_emacs_sitestart_dir/rus-win-keyboard.el

#######################
# Various other stuff #
#######################

# mkdir -p .%_libdir/%shortname/site-lisp

mv .%_mandir/man1/{,g}ctags.1
mv .%_bindir/{,g}ctags

# Exclude speedbar:
# rm -f .{%_datadir/%shortname/%emacs_version/lisp,%_infodir}/speedbar*

# Exclude antlr-mode:
# rm -f .%_datadir/%shortname/%emacs_version/lisp/progmodes/antlr-mode.el*

# Remove Gnus:
# rm -f .%_datadir/%shortname/%emacs_version/lisp/gnus/format-spec*
# rm -rf .%_datadir/%shortname/%emacs_version/lisp/gnus 
# rm -f .%_infodir/{gnus,emacs-mime,message}*
# rm -rf .%_datadir/%shortname/%emacs_version/etc/gnus*

rm -f .%_infodir/info*
rm -f .%_infodir/dir

########################
# Alternatives support #
########################
install -d %buildroot%_altdir
%if_enabled nox
install -p -m644 %SOURCE24 %buildroot%_altdir/%name-nox
%endif
%if_enabled athena
install -p -m644 %SOURCE25 %buildroot%_altdir/%name-athena
%endif
%if_enabled motif
install -p -m644 %SOURCE26 %buildroot%_altdir/%name-motif
%endif
%if_enabled gtk
install -p -m644 %SOURCE27 %buildroot%_altdir/%name-gtk
%endif
%if_enabled gtk3
install -p -m644 %SOURCE28 %buildroot%_altdir/%name-gtk3
%endif

###############
# X resources #
###############
xrdir=%_sysconfdir/X11/app-defaults
mkdir -p ."$xrdir"
install -p -m0644 %SOURCE31 ."$xrdir/Emacs"
unset xrdir

popd # "$RPM_BUILD_ROOT"

#####################
# Create file lists #
#####################
# INFO
%define common_infos ada-mode,auth,autotype,calc,ccmode,cl,dbus,dired-x,ebrowse,ediff,edt,efaq,emacs,emacs-gnutls,epa,ert,eshell,eudc,flymake,forms,idlwave,mairix-el,mh-e,newsticker,org,pcl-cvs,pgg,rcirc,reftex,remember,sasl,sc,ses,smtpmail,url,vip,viper,widget,woman
%define gnus_infos emacs-mime,gnus,message,sieve
%define gnus_infos_pattern gnus\\|emacs-mime\\|message\\|sieve
%define speedbar_infos_pattern speedbar
%define cedet_infos ede,eieio,semantic
%define cedet_infos_pattern ede\\|eieio\\|semantic
%define erc_infos_pattern erc
%define tramp_infos_pattern tramp
%define nxml_infos_pattern nxml-mode
%define elisp_infos_pattern elisp\\|eintr

# source emacs pgktools (bash functions that call el-functions)
. %_emacs_etc_dir/el-pkgutils/el-pkgutils.sh
EMACS_BIN="%name-%stage3bin"
EMACS_SEARCH_ROOT="$RPM_BUILD_ROOT"
EL_PKGUTILS_ROOT=""
# Clear the lists:
rm -f {main,leim}{,-el}.ls info.ls

# Generate them:
# INFO
common_infos=( $(ls "$RPM_BUILD_ROOT"%_infodir/*.info \
| sed -e "s:^$RPM_BUILD_ROOT%_infodir/::" \
| sed -e 's:\.info$::' | sort -u \
| egrep -v %gnus_infos_pattern \
| egrep -v %speedbar_infos_pattern \
| egrep -v %cedet_infos_pattern \
| egrep -v %erc_infos_pattern \
| egrep -v %tramp_infos_pattern \
| egrep -v %nxml_infos_pattern \
| egrep -v %elisp_infos_pattern ) )

( # save IFS
IFS=,
if [[ '%common_infos' != "${common_infos[*]}" ]]; then
      echo "common_infos lists do not match, correct them!"
      exit 1
fi
) || false

# fraction \
#  '(dirs "%_libexecdir/%shortname/%emacs_version" "%%dir") "main.ls"' \
#  '(files "%_libexecdir/%shortname/%emacs_version"
#     (lambda(f) (if (string-match "/movemail$" f) "%%attr(-,root,mail)")) )
#   "main.ls"' \
#  \
#  '(dirs "%_datadir/%shortname/%emacs_version/etc" "%%dir") "main.ls"' \
#  '(files "%_datadir/%shortname/%emacs_version/etc"
#     (lambda(f) (if (string-match "gnus" f) "#")) )
#   "main.ls"'

find "$RPM_BUILD_ROOT%_libexecdir/%shortname/%emacs_version" \
    "$RPM_BUILD_ROOT%_datadir/%shortname/%emacs_version/etc" -type d -print \
    | awk '// {gsub ("%buildroot","",$0); print "%%dir " $0}' > main.ls
find "$RPM_BUILD_ROOT%_libexecdir/%shortname/%emacs_version" -type f -print | awk '/\/movemail$/ { printf "%%attr(-,root,mail) "} // {gsub ("%buildroot","",$0); print $0}' >> main.ls
find "$RPM_BUILD_ROOT%_datadir/%shortname/%emacs_version/etc" -type f -print | awk '/gnus/ { printf "#"} // {gsub ("%buildroot","",$0); print $0}' >> main.ls

# FIXME look into el-pkgutils.el to see what broken
# standard_fraction_el_elc main "%_datadir/%shortname/%emacs_version/lisp"
# standard_fraction_el_elc leim "%_datadir/%shortname/%emacs_version/leim"

# INFO
printf '%%s\n' %_infodir/{%common_infos}'.info*' > info.ls
# mv $RPM_BUILD_ROOT%_infodir/dir $RPM_BUILD_ROOT%_infodir/elisp.dir

# Prepare the trick for linking etc/ into docs:
ln -s $(relative %_emacs_datadir/%emacs_version/etc %_docdir/%name-%emacs_version/etc) etc/

# Substitute emacs24-common with emacs-common for buildreq
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
echo %shortname-common > %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-common
# Substitute emacs24-leim with emacs-leim for buildreq
echo %shortname-leim > %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-leim
# Substitute emacs24-gnus with emacs-gnus for buildreq
echo %shortname-gnus > %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-gnus
# Substitute emacs24-X11.* with emacs-X11 for buildreq
echo %shortname-X11 > %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-X11
%if_enabled athena
echo %shortname-X11 > %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-X11-athena
%endif
%if_enabled motif
echo %shortname-X11 > %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-X11-motif
%endif
%if_enabled gtk
echo %shortname-X11 > %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-X11-gtk
%endif
%if_enabled gtk3
echo %shortname-X11 > %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-X11-gtk3
%endif
%if_enabled nox
# Substitute emacs24-nox with emacs-nox for buildreq
echo %shortname-nox > %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-nox
%endif

# check-shadows script
install -p -m755 %SOURCE51 %buildroot%_bindir/check-shadows


#
%files common -f main.ls
%doc BUGS README README.KOI8-U README.UK CHANGES.ukr INSTALL.ukr README.ALT-ru_RU.KOI8-R
# The trick for symlinking etc/:
%doc --no-dereference etc/etc

# %config(noreplace) %_sysconfdir/emacs/site-start.d/php.el

%_bindir/*
%if_enabled nox
%exclude %_bindir/%name-nox
%endif
%if_enabled athena
%exclude %_bindir/%name-athena
%endif
%if_enabled motif
%exclude %_bindir/%name-motif
%endif
%if_enabled gtk
%exclude %_bindir/%name-gtk
%endif
%if_enabled gtk3
%exclude %_bindir/%name-gtk3
%endif

%_mandir/man?/*

%dir %_libexecdir/%shortname
# %dir %_libdir/%shortname/site-lisp

# For now game scores stored separately in each user's home directory
# %attr(2755, root, games) %_libdir/%shortname/%emacs_version/%_target_platform/update-game-score

#%dir %_emacslispdir
%_emacslispdir/*.el*
%dir %_emacs_datadir/%emacs_version
%dir %_emacs_datadir/%emacs_version/site-lisp
%_emacs_datadir/%emacs_version/site-lisp/*

# Elisp files
%_emacs_datadir/%emacs_version/lisp/
# except *.el.gz files
%exclude %_emacs_datadir/%emacs_version/lisp/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/calc/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/calendar/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/emacs-lisp/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/emulation/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/eshell/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/international/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/language/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/mail/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/mh-e/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/net/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/obsolete/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/org/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/play/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/progmodes/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/term/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/textmodes/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/url/*.el.gz

# Some .el-files that have .elc-companions,
# but are still preferrable to have in the main
# package (for reference) may be listed here:
#%_datadir/%name/%emacs_version/lisp/bindings.el -- probably there is no need for this
#%_datadir/%name/%emacs_version/lisp/mail/sc.el
#%_datadir/%name/%emacs_version/lisp/term-nasty.el

# This should be a symlink
%_emacs_datadir/%emacs_version/lisp/site-start.el

# GNUS files
%exclude %_emacs_datadir/%emacs_version/etc/images/gnus/
%exclude %_emacs_datadir/%emacs_version/etc/images/smilies/
%exclude %_emacs_datadir/%emacs_version/lisp/gnus/
%exclude %_emacs_datadir/%emacs_version/etc/gnus
%exclude %_emacs_datadir/%emacs_version/etc/GNUS-NEWS

# CEDET files
%exclude %_emacs_datadir/%emacs_version/lisp/cedet/

# speedbar into separate package
%exclude %_emacs_datadir/%emacs_version/lisp/dframe.elc
%exclude %_emacs_datadir/%emacs_version/lisp/sb-image.elc
%exclude %_emacs_datadir/%emacs_version/lisp/speedbar.elc
# erc into separate package
%exclude %_emacs_datadir/%emacs_version/etc/ERC-NEWS
%exclude %_emacs_datadir/%emacs_version/lisp/erc/
# tramp into separate package
%exclude %_emacs_datadir/%emacs_version/lisp/net/tramp*.elc
# nxml-mode into separate package
%exclude %_emacs_datadir/%emacs_version/lisp/nxml/
%exclude %_emacs_datadir/%emacs_version/etc/NXML-NEWS
%exclude %_emacs_datadir/%emacs_version/etc/nxml/
%exclude %_emacs_datadir/%emacs_version/etc/schema/

%_emacs_sitestart_dir/*

# Game scores
# %dir %attr(775, games, games) %_localstatedir/games/%shortname
# %config(noreplace) %attr(664, games, games) %_localstatedir/games/%shortname/*

# Substitute for buidreq
%_sysconfdir/buildreqs/packages/substitute.d/%name-common

# %exclude %_infodir/dir
%exclude %_localstatedir/games/%shortname

#
%files el
%_emacs_datadir/%emacs_version/lisp/*.el.gz
%_emacs_datadir/%emacs_version/lisp/calc/*.el.gz
%_emacs_datadir/%emacs_version/lisp/calendar/*.el.gz
%_emacs_datadir/%emacs_version/lisp/emacs-lisp/*.el.gz
%_emacs_datadir/%emacs_version/lisp/emulation/*.el.gz
%_emacs_datadir/%emacs_version/lisp/eshell/*.el.gz
%_emacs_datadir/%emacs_version/lisp/international/*.el.gz
%_emacs_datadir/%emacs_version/lisp/language/*.el.gz
%_emacs_datadir/%emacs_version/lisp/mail/*.el.gz
%_emacs_datadir/%emacs_version/lisp/mh-e/*.el.gz
%_emacs_datadir/%emacs_version/lisp/net/*.el.gz
%_emacs_datadir/%emacs_version/lisp/obsolete/*.el.gz
%_emacs_datadir/%emacs_version/lisp/org/*.el.gz
%_emacs_datadir/%emacs_version/lisp/play/*.el.gz
%_emacs_datadir/%emacs_version/lisp/progmodes/*.el.gz
%_emacs_datadir/%emacs_version/lisp/term/*.el.gz
%_emacs_datadir/%emacs_version/lisp/textmodes/*.el.gz
%_emacs_datadir/%emacs_version/lisp/url/*.el.gz
# erc into separate package
%exclude %_emacs_datadir/%emacs_version/lisp/erc/
# tramp into separate package
%exclude %_emacs_datadir/%emacs_version/lisp/net/tramp*.el.*
# nxml-mode into separate package
%exclude %_emacs_datadir/%emacs_version/lisp/nxml/

#
%files leim
# Substitute for buidreq
%_sysconfdir/buildreqs/packages/substitute.d/%name-leim
%_emacs_datadir/%emacs_version/leim/
# except *.el.gz files
%exclude %_emacs_datadir/%emacs_version/leim/ja-dic/*.el.gz
%exclude %_emacs_datadir/%emacs_version/leim/quail/*.el.gz

#
%files leim-el
%_emacs_datadir/%emacs_version/leim/ja-dic/*.el.gz
%_emacs_datadir/%emacs_version/leim/quail/*.el.gz

#
%if_enabled nox
%files nox
%_bindir/%name-nox
%_altdir/%name-nox
# Substitute for buidreq
%_sysconfdir/buildreqs/packages/substitute.d/%name-nox
%endif

#
%files X11
%config(noreplace) %_sysconfdir/X11/app-defaults/*
%if_with menu
  %_menudir/%name-X11
%else
  %_desktopdir/%name.desktop
%endif
# backwards compatibility with Master 2x/Compact 30
%{?!_niconsdir:%define _niconsdir %_iconsdir}
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/24x24/apps/%name.png
%_iconsdir/hicolor/128x128/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/scalable/mimetypes/emacs-document.svg
%exclude %_niconsdir/emacs22.png
%exclude %_miconsdir/emacs22.png
%exclude %_liconsdir/emacs22.png
%exclude %_iconsdir/hicolor/24x24/apps/emacs22.png
%exclude %_desktopdir/emacs.desktop
# Substitute for buidreq
%_sysconfdir/buildreqs/packages/substitute.d/%name-X11

#
%if_enabled athena
%files X11-athena
%_bindir/%name-athena
%_altdir/%name-athena
# Substitute for buidreq
%_sysconfdir/buildreqs/packages/substitute.d/%name-X11-athena
%endif

#
%if_enabled motif
%files X11-motif
%_bindir/%name-motif
%_altdir/%name-motif
# Substitute for buidreq
%_sysconfdir/buildreqs/packages/substitute.d/%name-X11-motif
%endif

#
%if_enabled gtk
%files X11-gtk
%_bindir/%name-gtk
%_altdir/%name-gtk
# Substitute for buidreq
%_sysconfdir/buildreqs/packages/substitute.d/%name-X11-gtk
%endif

#
%if_enabled gtk3
%files X11-gtk3
%_bindir/%name-gtk3
%_altdir/%name-gtk3
# Substitute for buidreq
%_sysconfdir/buildreqs/packages/substitute.d/%name-X11-gtk3
%endif

#
%files info -f info.ls

#
%files elisp-manual
%_infodir/eintr*
%_infodir/elisp*

#
%files gnus
%doc %_emacs_datadir/%emacs_version/etc/GNUS-NEWS
%dir %_emacs_datadir/%emacs_version/lisp/gnus
%_emacs_datadir/%emacs_version/lisp/gnus/*.elc
%_emacs_datadir/%emacs_version/etc/gnus*
%_emacs_datadir/%emacs_version/etc/images/gnus/
%_emacs_datadir/%emacs_version/etc/images/smilies/
%_emacs_datadir/%emacs_version/etc/images/gnus.pbm
%_emacs_datadir/%emacs_version/etc/refcards/gnus*
%_infodir/gnus*
%_infodir/message*
%_infodir/emacs-mime*
%_infodir/sieve*
# Substitute for buidreq
%_sysconfdir/buildreqs/packages/substitute.d/%name-gnus

#
%files gnus-el
%_emacs_datadir/%emacs_version/lisp/gnus/*.el.*

#
%files speedbar
%_emacs_datadir/%emacs_version/lisp/dframe.elc
%_emacs_datadir/%emacs_version/lisp/sb-image.elc
%_emacs_datadir/%emacs_version/lisp/speedbar.elc
%_infodir/speedbar*

#
%files erc
%_emacs_datadir/%emacs_version/etc/ERC-NEWS
%dir %_emacs_datadir/%emacs_version/lisp/erc
%_emacs_datadir/%emacs_version/lisp/erc/*.elc
%_infodir/erc*

%files erc-el
%_emacs_datadir/%emacs_version/lisp/erc/*.el.*

#
%files tramp
%_emacs_datadir/%emacs_version/lisp/net/tramp*.elc
%_infodir/tramp*

%files tramp-el
%_emacs_datadir/%emacs_version/lisp/net/tramp*.el.*

#
%files nxml-mode
%_emacs_datadir/%emacs_version/lisp/nxml/
%exclude %_emacs_datadir/%emacs_version/lisp/nxml/*.el.*
%_emacs_datadir/%emacs_version/etc/NXML-NEWS
%_emacs_datadir/%emacs_version/etc/nxml
%_emacs_datadir/%emacs_version/etc/schema
%_infodir/nxml-mode*

%files nxml-mode-el
%_emacs_datadir/%emacs_version/lisp/nxml/*.el.*

#
%files cedet
%_emacs_datadir/%emacs_version/lisp/cedet/
%exclude %_emacs_datadir/%emacs_version/lisp/cedet/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/cedet/ede/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/cedet/semantic/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/cedet/semantic/analyze/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/cedet/semantic/bovine/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/cedet/semantic/decorate/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/cedet/semantic/symref/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/cedet/semantic/wisent/*.el.gz
%exclude %_emacs_datadir/%emacs_version/lisp/cedet/srecode/*.el.gz
%_infodir/ede*
%_infodir/eieio*
%_infodir/semantic*

#
%files cedet-el
%_emacs_datadir/%emacs_version/lisp/cedet/*.el.gz
%_emacs_datadir/%emacs_version/lisp/cedet/ede/*.el.gz
%_emacs_datadir/%emacs_version/lisp/cedet/semantic/*.el.gz
%_emacs_datadir/%emacs_version/lisp/cedet/semantic/analyze/*.el.gz
%_emacs_datadir/%emacs_version/lisp/cedet/semantic/bovine/*.el.gz
%_emacs_datadir/%emacs_version/lisp/cedet/semantic/decorate/*.el.gz
%_emacs_datadir/%emacs_version/lisp/cedet/semantic/symref/*.el.gz
%_emacs_datadir/%emacs_version/lisp/cedet/semantic/wisent/*.el.gz
%_emacs_datadir/%emacs_version/lisp/cedet/srecode/*.el.gz


%changelog
* Thu Jun 21 2012 Terechkov Evgenii <evg@altlinux.org> 24.1-alt2
- Rebuild with new libImageMagick

* Mon Jun 11 2012 Terechkov Evgenii <evg@altlinux.org> 24.1-alt1
- 24.1

* Wed May 23 2012 Terechkov Evgenii <evg@altlinux.org> 23.3-alt4
- Fix build with new binutils
- Cedet release updated

* Tue Apr 05 2011 Eugene Vlasov <eugvv@altlinux.ru> 23.3-alt3
- New version

* Tue May 18 2010 Eugene Vlasov <eugvv@altlinux.ru> 23.2-alt2
- New version
- New subpackages - cedet and cedet-el
- Removed font set from app-defaults resources
- eshel and org el-files moved to el subpackage

* Tue Oct 13 2009 Eugene Vlasov <eugvv@altlinux.ru> 23.1-alt1
- New version
- Requires cleanup
- Obsoletes emacs22
- Build athena and motif binary with sound support
- Applied CVS fix for build with gcc-4.4.2

* Mon Jun 22 2009 Eugene Vlasov <eugvv@altlinux.ru> 23.0.95-alt0.13.pretest
- New pretest version
- Removed deprecated post/postun install_info/uninstall_info calls

* Thu Apr 02 2009 Eugene Vlasov <eugvv@altlinux.ru> 23.0.92-alt0.12.pretest
- Fixed lisp files recompilation, touch changed files

* Thu Apr 02 2009 Eugene Vlasov <eugvv@altlinux.ru> 23.0.92-alt0.11.pretest
- New pretest version
- Updated build requires

* Sat Jan 10 2009 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.10.20090110
- New snapshot
- Removed deprecated post/postun register_alternatives and
  unregister_alternatives calls

* Sun Nov 16 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.9.20081116
- New snapshot
- Updated build requires
- Modified desktop entry: removed deprecated Encoding key, removed empty
  Path key
- Removed deprecated post/postun update_menus and update_desktop_database
  calls

* Sun Sep 28 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.8.20080928
- New snapshot
- Updated infos list

* Fri Jun 06 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.7.20080606
- New snapshot

* Thu May 01 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.6.20080501
- New snapshot
- Updated README.ALT-ru_RU.KOI8-R, replaced all 22 version occurences to 23
- Added update_desktopdb and clean_desktopdb post/postun macro for X11
  package
- Removed from build requires linux-libc-headers
- Exclude GNUS-NEWS and etc/gnus/ from emacs23-common
- Pack scalable/mimetypes/emacs-document.svg icon

* Wed Mar 19 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.5.20080320
- New snapshot, tramp recursive load fixes
- Fixed "Invalid face slant: roman" when using XFT fonts

* Tue Mar 18 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.4.20080318
- New snapshot
- Build X variants with dbus
- Build GTK variant with rsvg support

* Sat Mar 08 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.3.20080308
- New snapshot (CVS head), updated tramp version
- Changed icon set, install all icon sizes
- Removed README.unicode doc file
- Modified mime types list in desktop file

* Mon Jan 07 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.2.20080106
- New snapshot
- Updated gnus version
- Disabled dvi docs build
- Info documentation packaged in emacs23-info
- Corrected infos list (added dbus, nxml-mode and remember info)
- Build nxml-mode as separate package
- Used supplied procedure for pack *.el files, looks like el-pkgutils
  broken now
- Fixed doc list
- Fixed elisp files lists
- Fixed gnus files list

* Mon Nov 05 2007 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.1.20071102
- New snapshot
- Updated tramp and erc versions
- Reapplied patches that affect files in man/, lispref/ and lispintro/ (all
  docs source located now in doc/)
- Changed dvi build code for new docs source location
- Gnus: don't pack ChangeLog files

* Tue Aug 14 2007 Eugene Vlasov <eugvv@altlinux.ru> 23.0.0-alt0.2.20070814
- New snapshot, possibly fixed bootstrap segfault
- Updated license tag to GPLv3 or later
- Updated tramp version

* Thu Jul 26 2007 Eugene Vlasov <eugvv@altlinux.ru> 23.0.0-alt0.1.20070721
- Initial GNU Emacs 23 build (from emacs-unicode-2 cvs snapshot)
- Build from GIT, all patches applied to git tree
- Updated packages versions
- Used make bootstrap and no lisp recompilation for cvs build
- Modified configure parameters:
  * Used --enable-font-backend --with-freetype --with-xft for for all
    variants except nox
  * Used --with-gpm for nox and gtk variants
- Renamed and modified for emacs23 alternatives and desktop files
- Updated build requires
- Added conflicts to emacs22

* Tue Jun 05 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.1-alt1
- 22.1 release
- Regenerated and reorganized build requires
- Used "make" instead "make bootstrap", restored old build procedure (with
  lisp files recompilation on third stage)

* Thu May 24 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.990-alt0.28.pretest
- New pretest version
- Simplified build - removed lisp files recompilation on third stage, rebuild
  only nox binary on final stage

* Sat Apr 21 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.98-alt0.27.pretest
- New pretest version
- Rediffed more-cyrillic patch

* Fri Apr 06 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.97-alt0.26.pretest
- New pretest version
- Added Provides: /usr/bin/emacs to packages with emacs binaries

* Fri Mar 23 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.96-alt0.25.pretest
- New pretest version

* Wed Mar 07 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.95-alt0.24.pretest
- New pretest version
- Rediffed more-cyrillic patch
- Autoconf used again, all patches to configure.in returned

* Wed Feb 07 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.93-alt0.23.pretest
- alt-system patch applied to configure script (#10781)
- README.ALT - added warning about emacs22-nox restrictions, added some
  words about sound support in emacs22-X11-gtk
- Build gtk binary with sound support

* Sat Jan 27 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.93-alt0.22.pretest
- New pretest version
- Tramp filename completion fixed in upstream - patch removed
- Update tramp version
- Used supplied configure script (now autoconf 2.61 needed)
- Patch for X resource default search path applied to configure script

* Sun Jan 07 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.92-alt0.21.pretest
- Fixed tramp filename completion, updated tramp.el to CVS version (#10603)

* Fri Dec 22 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.92-alt0.20.pretest
- New pretest version
- Selection coding use fixed in upstream - patch removed
- Update ERC version

* Tue Nov 28 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.91-alt0.19.pretest
- Fixed use selection coding. Fix from CVS, solves problems with copy/yank
  non iso-latin-1 letters
- Removed pointer color modification from app-defaults file

* Sat Nov 25 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.91-alt0.18.pretest
- New pretest version
- Rediffed info_install patch
- Removed mode-line attributes modifications from app-defaults file
- Fixed default path for search application X resource

* Tue Oct 31 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.90-alt0.17.pretest
- First emacs22 pretest version
- Fixed build dvi manuals
- Removed %%__ macro

* Sun Oct 08 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.16.20061008
- New snapshot
- Rediffed alt-system patch

* Tue Sep 12 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.15.20060912
- New snapshot
- Update erc version
- Update tramp version
- Build .dvi manuals fixed in upstream, patch for elisp.texi removed

* Sat Jul 15 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.14.20060715
- New snapshot
- Enabled build motif binary for all arch
- Build tramp as separate package
- Increased obsoletes version for emacs-tramp
- Update erc version
- Excluded erc files from emacs22-el
- Moved ERC-NEWS to emacs22-erc
- Reverted @fonttextsize addition in elisp.texi

* Wed Jun 14 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.13.20060614
- New snapshot (closes #9635)
- Corrected infos list (removed emacs-extra)

* Sat Apr 29 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.12.20060429
- New snapshot
- Removed motif headers hack
- Disabled build motif binary for x86_64
- Increased PURESIZE

* Thu Apr 20 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.11.20060420
- New snapshot
- Disabled modification of face-font-selection-order default value
- Droped useless dependency on python (Igor Vlasenko)
- Added optional build with menu, not desktop-file, fixed menu-file (Igor
  Vlasenko)
- For backward compatibility with old distribution define %%_niconsdir if not
  defined (Igor Vlasenko)

* Sun Mar 19 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.10.20060319
- New snapshot
- Rediffed jka-compr_bz2_load patch
- Turned back fix for build with motif (for x86_64 build)
- Used %%_niconsdir macro instead of %%_iconsdir for 32x32 icon, renamed icons
- Menu-file replaced by desktop-file
- Fixed info installation

* Thu Feb 23 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.9.20060223
- New snapshot
- Rediffed uk patch (ispell-local-dictionary-alist accept now any coding 
  system, supported by Emacs)

* Sun Feb 12 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.8.20060211
- New snapshot
- Obsoletes emacs-ses <= 1.0-alt2.031130
- Added (consp) check for save-place-alist elements, loaded from
  ~/.emacs-places (#9053)
- Removed fix for build with motif and Xaw3d

* Fri Feb 03 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.7.20060203
- New snapshot
- Added conflict with emacs-gnuserv <= 3.12.7-alt1
- Support for optional build of athena, motif, gtk, nox (Igor Vlasenko)
- Added .dvi files to elisp-manual (Igor Vlasenko)
- Fix for flyspell-buffer merged into upstream
- Rediffed clipboard patch
- Fixed build with motif and Xaw3d
- Added rcirc manual to infos list
- Fixed unpackaged files warning
- Fixed x86_64 build (Igor Vlasenko)
- ERC package included in upstream, build as separate package, obsolete
  old emacs-erc
- el-pkgutils 'fraction' calls replaced with awk code (Igor Vlasenko)

* Sun Dec 11 2005 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.6.20051211
- New snapshot
- Now emacs22 obsoletes emacs21, emacs-tramp, emacs-ses, emacs-elisp-manual
- Build speedbar as separate package
- Fix flyspell-buffer for large tex files (thanks to Igor Vlasenko for
  notifying)
- Fix spell checking with aspell in locale coding other than dictionary 
  coding (thanks to Igor Vlasenko for notifying)

* Tue Nov 22 2005 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.5.20051122
- New snapshot
- Rediffed more-cyrillic-support patch, require cyrillic-codepages-setup 
  only if purify-flag is nil (not while preparing to dump)
- Disabled builtin compress function for installed .el files (used compress
  function from el-pkgutils)
- Cleanup requires
- Added conflict with old emacs-w3 (with url package inside)
- Used new emacs icons (from Andrew Zhilin)
- Site-start script emacs21-rus-win-keyboard.el renamed to rus-win-keyboard.el

* Mon Oct 24 2005 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.4.20051024
- New snapshot
- Added ".bz2" to default value jka-compr-load-suffixes (to enable load
  bzipped libraries and for .el.bz2 source navigation from *Help* window)
- More substitutes for buildreq
- Don't exclude antlr-mode
- Modified build requires for M24 compatibilty (Igor Vlasenko)
- Added README.ALT
- Added check-shadows script for check list of Emacs Lisp files that
  shadow other files (#2622)
- Removed fix for mh-e autoloads
- Fixed macros warnings
- Build with emacs-devel
- Removed dir %%_libdir/%shortname/site-lisp
- Added dir %%_libdir/emacs (emacs-base no more provides this dir)
- Enabled search of aspell dictionaries. Now it preserve elements of
  ispell-dictionary-alist for dictionaries that are not found
- Rediffed patch for decoding headers in gnus
- PGG now part of %name-common (info pages moved too)
- Fixed Summary
- Removed SGID bit of update-game-score binary

* Sat Oct 08 2005 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.3.20051008
- New snapshot
- Temporary disable finding aspell dictionaries
- Build gnus
- Build with new speedbar
- Now required emacs-base >= 0.0.4-alt5
- Fixed missing menu icons (thanks to viy@)
- Fixed command in menu file
- Fixed build-time generating autoloads for mh-e
- Added fix for decoding in gnus invalid encoded headers

* Fri Sep 23 2005 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.2.20050923
- New snapshot
- Corrected infos list
- Added conflict with emacs-tramp
- Used relative symlink in documentation dir
- Changed X resources default font
- Added substitute emacs22-common with emacs-common for buildreq (#5500)
- Rediffed clipboard patch

* Mon Sep 05 2005 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.1.20050902
- CVS snapshot fork
- Rediffed and reworked patches:
  * %shortname-21.2-alt-system.patch
  * %shortname-21.3-alt3-clipboard.patch
  * %shortname-21.2-hide-rcs-deps.patch
  * %shortname-21.2-Meta-Alt-Ctrl-Hyper-super-discard-state.patch
  * %shortname-21.2-pc-select-private-mark.patch
  * %shortname-21.2-face-font-selection-slant-important.patch
  * %shortname-21.3-rh-no_rpath.patch
  * %shortname-21.3-alt4-uk.patch
  * leim-21.1-uk.patch
  * leim-20.6-belarusian.patch
  * %shortname-21.3-ispell-belarusian.patch
  * %shortname-21.3-ispell-russianw.patch
  * %shortname-21.3-alt1-more-cyrillic-support.patch
  * %shortname-21.2-alt12-tutorial-ru.patch
- Removed patches (merged into upstream)
  * %shortname-21.2-HEAD-pc-select.diff
  * %shortname-21.2-ediff-diff-options-check-c.patch
  * %shortname-21.3-use-handler-for-load-of-absolute.patch
  * %shortname-21.3-use-handler-for-load-of-suffixed.patch
  * %shortname-21.2-x86_64.patch
  * %shortname-21.1-lang-env-prereqs.patch
- Build separate packages for athena, motif and gtk binaries
- New alternatives format
- Build ELisp manual
- Updated BuildRequires

* Thu Jul 07 2005 Igor Vlasenko <viy@altlinux.org> 21.3-alt11.vla2
- added conflict with ispell-uk<0.6

* Thu Jun 30 2005 Igor Vlasenko <viy@altlinux.org> 21.3-alt11.vla1
- fixed bug #6853 shift+7 in cyrillic-ukrainian-ms
- fixed bug #835 (added belarussian ispell dict)
- fixed bug #6855 (re-added ukrainian ispell dict)
- fixed bug #6842 (patched emacs21-rus-win-keyboard.el)

* Fri Feb 11 2005 Kachalov Anton <mouse@altlinux.ru> 21.3-alt11
- support for x86_64 (#6089)

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 21.3-alt10.1.1
- Rebuilt with libtiff.so.4.

* Thu Jun 10 2004 Stanislav Ievlev <inger@altlinux.org> 21.3-alt10.1
- NMU: fix alternatives usage (rename candidates in remove_alternative macros)

* Mon May 03 2004 Ott Alex <ott@altlinux.ru> 21.3-alt10
- Fix bug #2676
- Fix bug #883
- Fix bug #1159
- Fix bug #1502
- Fix bug #2217
- Fix bug #3885
- Fix bug #2566

* Sat Mar 27 2004 Ott Alex <ott@altlinux.ru> 21.3-alt9
- Fixing entry in menu

* Sat Jan 31 2004 Ott Alex <ott@altlinux.ru> 21.3-alt8
- Fixing entry in menu
- Install new smtpmail with support of SMTP Auth

* Mon Jan 12 2004 Ott Alex <ott@altlinux.ru> 21.3-alt7
- Fixing spec to properly rebuild

* Sat Jan 10 2004 Ott Alex <ott@altlinux.ru> 21.3-alt6
- Name changed to emacs21 
- Remove compression of .elc files
- Remove dependence on speedbar
- Remove gnus and dependence on it
- Added missed buildreq on sendmail
- Move emacs-pkgtools to emacs-base

* Sun Nov 30 2003 Ott Alex <ott@altlinux.ru> 21.3-alt5
- Reorganize package 
- move php-mode.el to emacs-prog-modes package

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 21.3-alt4.1
- new alternatives format

* Fri Apr  4 2003 Ivan Zakharyaschev <imz@altlinux.ru> 21.3-alt4
- lisp: autoload `cyrillic-encode-koi8-r-char' (was lost in patch20 "uk")

* Tue Apr  3 2003 Ivan Zakharyaschev <imz@altlinux.ru> 21.3-alt3
- mouse & PRIMARY X selection: restore the behaviour introduced
  by 21.2-alt11-clipboard.patch (lost in 21.3-alt1; patch3)

* Tue Apr  1 2003 Ivan Zakharyaschev <imz@altlinux.ru> 21.3-alt2
- built-in `load': always use the load-handler if it is present 
  (e.g. for compressed .elc's; fixes No. 0002355; patches 11 and 12);
- lisp: 
  + `vc-cvs-registered' function: split into parts for autoloading
    without any loops (No. 0002334 at bugs.altlinux.ru; patch13);
  + php-mode updated to 1.04;
- docs: include AUTHORS, symlink etc/;
- spec:
  + make updates (regenerate autoloads, cus-deps etc.) at the %%build stage;
  + supply install-info path to %%makeinstall (to get less error msgs);

* Tue Mar 25 2003 Ivan Zakharyaschev <imz@altlinux.ru> 21.3-alt1
- new upstream version;
- files: include /usr/bin/{ebrowse,grep-changelog} in emacs-common pkg
  (No. 0002354 at bugs.altlinux.ru)
- Cyrillic support improvements (patch33):
  + language-env detection improved for be*, ru*, uk* & *iso8859-5 locales;
  + info manual reflects the support for various Cyrillic-based language-envs
    (based on the "uk" patch);
  + Ukrainian word for "Ukrainian" fixed in HELLO (No. 0002213);
- spec & patches (not visible to a user): 
  + simplify the menu file (s:%%version:X11:);
  + include /usr/bin/* in emacs-common pkg (and exclude emacs-{nox,X11});
  + patch3 (clipboard): default xselection coding-system value is already correct upstream;
  + patch9 (regex-encoded): upstream (not ours);
  + patch20 (uk): redone, some parts extended and moved to patch33 (more-cyrillic);
  + patch31 (dumbterm-for-compile): finally upstream;
  + patch32 (cp866fix): upstream;

* Fri Mar 14 2003 Stanislav Ievlev <inger@altlinux.ru> 21.2-alt16
- PreReq fixes

* Wed Mar 12 2003 Stanislav Ievlev <inger@altlinux.ru> 21.2-alt15
- moved to new alternatives scheme
- warning to maintainer: added missing PreReq on update-alternatives


* Mon Feb 10 2003 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt14
- changes to better support various Cyrillic X fonts 
  (news in patch33):
  + faces.el: face-font-registry-alternatives: list the wide-spread 
    alternatives for Cyrillic iso8859-5 (microsoft-cp1251, koi8-u, koi8);
  + fontset.el: leave "ISO8859-5" as the REGISTRY-ENCODING for Cyrillic;
  + fontset.el: change the FAMILY for Cyrillic from "*" (any) to nil 
    (the same a sthe default), because Cyrillic is like Latin: the family
    plays just hte same role;
  + describe koi8-c X font encoding (for now, just as an alias for koi8-u);
  (patch10):
  + make :slant the most important property when selecting a font for a face
    (imho, the absence of slanted fonts makes the visual appearance dull);
  (source31):
  + remove all font-related settings from /etc/X11/app-defaults/Emacs (which
    used to be brute), add only "Emacs.default.attributeFamily: fixed";
  + now, there is no need to specify rather brute values in localized
    /etc/X11/Xresources.* in order to get the right encoded Cyrillic font --
    we get it without any special X resources, if the Cyrillic font is 
    available (modify app-defaults accordingly!);
    (a part of the fix for No. 0000825, 0001478, 0001681; complete 0000997);
- open bzipped2 .el files (as well as gzipped which was supported before)
  when following links from the Help buffer (e.g., C-h v) (patch1;
  fixes No. 0001927 at http://bugs.altlinux.ru).

* Mon Feb 10 2003 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt13
- fix regex processing for some specially encoded texts (patch9, useful
  for Gnus, sent by Alex Ott <ottalex@narod.ru>);
- add BuildRequires(install): bzip2-utils (to fix No. 0001911).

* Sun Dec  8 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt12
- files: 
  + include non-el/elc files from lisp/ (mainly xpm; fixes No. 0001387);
  + exclude gnus/ from emacs-common (it was included in a previous revision);
  + compress .el-files in *-el pkgs;
- corrected TUTORIAL.ru (Alex Ott <ottalex@narod.ru>);
- spec-file: thoroughly check that all info-files are included
  (fixes No. 0001386);

* Sun Nov 17 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt11
- make possible primary X selection setting & pasting with mouse
  (in addition to clipboard manipulation with keys; fixes No. 1356);
- pc-selection-mode: turn-offable; no conflict with traditional 
  selection manipulation keys (like C-space; fixes No. 1357 at 
  bugs.altlinux.ru);
- lisp/ediff-diff.el: refine the check for valid ediff-diff-options;

* Sat Nov  9 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt10
- make finer distinction between koi8-r & koi8-u font encodings
  (fixes No. 997 at bugs.altlinux.ru).

* Fri Nov  8 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt9
- make keys like C-h, M-x work even when the (say) Russian XKB 
  group is active (patch5, discard almost the whole state if
  a certain modifier is detected; fixes No. 852 at bugs.altlinux.ru).
  (Please REPORT any related misbehaviors!)

* Thu Nov  7 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt8
- use --host=%%_target_platform for ./configure (fixes No. 1535
  at bugs.altlinux.ru).

* Tue Nov  5 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt7
- lisp: leave gnus/format-spec.el* in the main pkg (do not put in gnus):
  kind of essential library (required by tramp);
- scripts:
  + do not install {dir,info}.info; do install idlwave.info;
  + do not install speedbar.info (belongs to the speedbar package);
    WARNING: unless you reinstall emacs-speedbar, its info entry won't
    appear in the catalog;
- gnus subpkg:
  + Provides: gnus = %%name:%%version-%%release; Conflicts: gnus !=...; 
    I suppose other Gnus pkgs should do the same;
  + move {emacs-mime,message}.info to this subpkg.

* Sun Nov  3 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt6
- install more info;
- separate gnus{,-el} (alternatives would be complex in this case due to
  info and etc/, so other gnus should merely conflict with these ones).

* Fri Jul 19 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt5
- follow the convention about using POSIX locks (with fcntl(2)) for 
  mailbox access (in movemail; nnmbox users take care on your own!);
- drop privileges of movemail utility (no dot-locking in /var/mail/); 
- link with tinfo, not ncurses (everything is there in the latest release);
- remove termcap from build deps;
- lisp: drop speedbar.el{,c}, speedbar.info -- you will find it 
        in a separate pkg (Alex Ott <ottalex@narod.ru>);
- etc: add TUTORIAL.ru (Alex Ott);
- rcs-checkin: hide the dependencies on rcs (mhz).

* Sun Apr 14 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt4
- lisp: 
  + add support for X Compound Text with Extended Segments
    in koi8-u and microsoft-cp1251 (koi8-r support already present
    in the offcial GNU release; this is the complete fix for \#786
    at bugs.altlinux.ru);
  + add cp1251 item to the list of choices for ispell coding;
- package:
  + correct preun-scripts (alternative management) (Sorry, you will 
    have to uninstall 21.2-alt3 manually with --noscripts);

* Fri Apr 12 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt3
- rename: /usr/bin/emacs-21.2 to /usr/bin/emacs-X11
  (to overcome the alternatives nightmare);

* Fri Apr 12 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt2
- package: 
  + add Confilcts on older etcskel & app-defaults (the
    old ones use values considered bad for 21.2);
  + Groups of *-el subpkgs changed to Development/Other;
- lisp: add support for X fonts in koi8 and *1251;


* Mon Apr  8 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt1
- new mainstream release (21.2):
  + now supports ICCCM Extended Segments in X selctions (fixes \#786 at
    bugs.altlinux.ru) -- don't forget to sync etcskel's to use c-text 
    for selections;
- lisp: 
  + prefer clipboard over primary selection (the reasononig given in
    \#795 at bugs.altlinux.ru);
  + the default value for selection-coding-system: 
    compound-text -> compound-text-with-extensions (this is the second part of
    the fix for \#786 at bugs.altlinux.ru)
  + Encoded-kb mode indicator turned off in mainstream release, so 
    we are not applying our previous patch any more;
-config:
  + use "Emacs" class as a specifier for X resourcers (was: "emacs" name)
    (fixes \#764 at bugs.altlinux.ru) -- don't forget to sync /etc/Xresources;
- spec-file:
  + dumbterm-for-compile patch regenerated;
  + alternatives: 
    * weights for alternatives shifted by %%{alternativeMajor}00;
    * removal in %%preun to avoid collisions;

* Thu Mar  1 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.1-alt13
- fix broken deps between emacsen-startscripts and and emacs-{X11,nox}:
  the pkgs with Emacs executables now provide `emacsen'.

* Thu Feb 28 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.1-alt12
- make co-existence with other Emacsen (XEmacs) easier:
  + move the site start scripts to a separate pkg (emacsen-startscripts; 
    they should be shared between GNU and X- Emacsen); buildreq rules for
    the directory with the scripts also moved to that pkg;
  + emacs-{nox,X11} provide emacsen (should be also provided 
    by XEmacs binaries);
  + emacs-{nox,X11} require emacsen-startscripts (should be also required 
    by XEmacs binaries);

* Sat Feb 25 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.1-alt11
- get rid of the inconsistency in versions and documentation data between 
  emacs-X11 and emacs-nox variants (fixes \#601, \#612 in bugs.altlinux.ru)
  (%%build stage modified to achieve this);
- add more strict %%release dependencies;
- add support for loading bzipped2 .el/.elc; compress several large files;
- lisp:
    + encoded-kbd: make indicator string shorter;
    + cyrillic-codepages-setup: override `valid-codes' property with more 
      correct values (this fixes hanging on C-x; Note: if you do 
      codepage-setup manually, then it is not fixed for you);
- config:
    + macros: rename noXlaunch -> TTYlaunch;
    + mouse: attempt to use mouse in Linux console and Xterm;
    + initial-features: turn on column-number and eldoc (for el only) modes;
- spec-file:
  + %%install: handle menu simpler;
  + make a patch instead of the separate HELLO.re (append it to Patch20);
  + %%install: generate filelists using el-pkgutils (it should be used also
    in other pkgs with Emacs Lisp code);

* Sun Feb  9 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.1-alt10
- lisp: 
  + new version of php-mode (1.0.2); compile it;
    on site-start, initialize autoload of it (php-mode);
  + add more seamless support for Cyrillic language environments based
    on CP1251, CP866 and CP1125;
  + fix CP866 table;
- config:
  + special bindings for selection management discarded -- the defaults 
    work fine (even for X); support for analogous KeyPad bindings added 
    (suggested by vyt@vzljot.ru);
  + X resources: set our values for colour classes; use "Helv" font 
    family for the menu;
  + do not fail completely if the Flyspell feature fails;
  + mouse wheel support turned on;
  + defined GNU-/XEmacs and Xlaunch macros (to be used in personal configs, etcskels);
  + split the config into small parts;
- menu: explicitly specify the X11-variant of emacs;
- spec-file:
  + Head: thrown away unused and recompiled sources; 
    not used terminfo patch left for a while: do we need it??;
  + build: do not copy any byte-compiled .elc files into the build 
    tree -- all of them now get recompiled from the patched sources 
    (particularly quail/cyrillic.elc from leim);
  + install: move menu entry to a separate file;
  + scriplets: use %%*_menus macros;
  + install: cut down "$RPM_BUILD_ROOT" usage;
  + detect errors during Emacs Lisp compilation;

* Thu Jan 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 21.1-alt9
- Added emacs filter for buildreq.

* Thu Dec 27 2001 Ivan Zakharyaschev <imz@altlinux.ru> 21.1-alt8
- configuration:
  + really turn on pc-selection-mode;
  + move frame properties from site-start.el to X resources;
- lisp: really apply our patches by recompiling the patched sources;
- .el/.elc fractions improved:
  + do not loose any not-compiled .el-files in the emacs-common pkg;
  + split emacs-el into emacs-el and emacs-leim-el subpkgs;
- "TERM in Compile" patch extended (idea by rms@gnu.org);

* Wed Dec 26 2001 Ivan Zakharyaschev <imz@altlinux.ru> 21.1-alt7
- inherit ispell-dictionary value from the DICTIONARY environment variable
- fix the "TERM in Compile" patch -- now it works

* Wed Dec 26 2001 Ivan Zakharyaschev <imz@altlinux.ru> 21.1-alt6
- configuration from MdkRE's etcskel-* merged into the global Emacs' config
- set TERM=dumb for compile (for nice output of colorgcc and other programs)
- set ownership on various directories for clean pkg removal
- FAQ excluded from the documentation

* Tue Nov 20 2001 AEN <aen@logic.ru> 21.1-alt5
- update-alternatives fixed (bug 168,169)
- new php-mode.el (bug 170)

* Thu Nov 15 2001 AEN <aen@logic.ru> 21.1-alt4
- fix typo in previous changelog record
- some MDK improvements added

* Tue Nov 13 2001 AEN <aen@logic.ru> 21.1-alt3
- ukrainiazation from Serhii Hlodin

* Thu Nov 1 2001 AEN <aen@logic.ru> 21.1-alt2
- leim cyrillic patches restored

* Mon Oct 22 2001 AEN <aen@logic.ru> 21.1-alt1
- new version

* Fri May 18 2001 Stanislav Ievlev <inger@altlinux.ru> 20.7-ipl9mdk
- Repackaged.
- Moved common %name stuff to %name-common subpackage.
- Used update-alternatives for %name-nox and %name-X11 subpackages.
- Fixed terminfo linkage.

* Sat Feb 17 2001 AEN <aen@logic.ru>
- groups names fixed

* Sat Jan 20 2001 AEN <aen@logic.ru>
- belarusian script in HELLO fixed (Alexander Bokovoy)

* Tue Dec 26 2000 AEN <aen@logic.ru>
- spec cleanup

* Thu Dec 07 2000 AEN <aen@logic.ru>
- 20.7
- rebuild for 7.2RE

* Sat Mar 11 2000 Oleg Tihonov <tihonov@ffke-campus.mipt.ru>
- load belarusian code at startup

* Thu Jan 13 2000 Oleg Tihonov <tihonov@ffke-campus.mipt.ru>
- added belarusian language support

* Tue Nov 9 1999 AEN <aen@logic.ru>
- bzipped man-pages
- custom.gz removed
- build for 6.1RE

* Fri Sep 17 1999 Oleg Tihonov <tihonov@ffke-campus.mipt.ru>
- move to 20.4
- add Ukrainian patches

* Wed May 26 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- move the %_bindir/%name script to the %name package

* Wed May 26 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- s/arch-redhat-linux/arch-mandrake-linux
- replace %name with a shell script that runs either %name-nox or
  %name-20.3
- s/%name/%name-20.3/ in %name.wmconfig (wmconfig is always X)

* Fri Apr 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adpatations.
- Bzip2 info/man pages.
- Path to handle bzip2 on info files.

* Wed Mar 31 1999 Preston Brown <pbrown@redhat.com>
- updated mh-utils %name lisp file to match our nmh path locations

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 9)

* Fri Feb 26 1999 Cristian Gafton <gafton@redhat.com>
- linker scripts hack to make it build on the alpha

* Fri Jan  1 1999 Jeff Johnson <jbj@redhat.com>
- add leim package (thanks to Pavel.Janik@inet.cz).

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Wed Sep 30 1998 Cristian Gafton <gafton@redhat.com>
- backed up changes to uncompress.el (it seems that the one from 20.2 works
  much better)

* Mon Sep 28 1998 Jeff Johnson <jbj@redhat.com>
- eliminate /tmp race in rcs2log

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- upgrade to 20.3

* Tue Jun  9 1998 Jeff Johnson <jbj@redhat.com>
- add --with-pop to X11 compile.
- include contents of %_datadir/.../etc with main package.

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Mon Jun 01 1998 David S. Miller <davem@dm.cobaltmicro.com>
- fix signals when linked with glibc on non-Intel architectures
  NOTE: This patch is not needed with %name >20.2

* Thu May 07 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- added %_libdir/%name/20.2/*-mandrake-linux directory in the filelist

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- alpha started to like %name-nox again :-)

* Thu Nov  6 1997 Michael Fulbright <msf@redhat.com>
- alpha just doesnt like %name-nox, taking it out for now

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- added multibyte support back into %name 20.2
- added wmconfig for X11 %name
- fixed some errant buildroot references

* Thu Oct 23 1997 Michael Fulbright <msf@redhat.com>
- joy a new version of %name! Of note - no lockdir any more.
- use post/preun sections to handle numerous GNU info files

* Mon Oct 06 1997 Erik Troan <ewt@redhat.com>
- stopped stripping it as it seems to break things

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- turned off ecoff support on the Alpha (which doesn't build anymore)

* Mon Jun 16 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Fri Feb 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved ctags to gctags to fit in the more powerful for C (but less
  general) exuberant ctags as the binary %_bindir/ctags and the
  man page /usr/man/man1/ctags.1

# Local Variables:
# compile-command: "rpm -ba --sign --target=i686 emacs22.spec"
# End:
