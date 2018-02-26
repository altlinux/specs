# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-chess.spec,v 1.3 2006/03/03 18:15:40 eugene Exp $

%define pkg_name chess
%define subver b6

Version: 2.0
Release: alt5.%subver
Epoch: 20070423
Name: emacs-%pkg_name
License: GPL
Group: Editors
Summary: Emacs client for Chess playing
Requires: emacs-common chess
Url: http://emacs-chess.sourceforge.net/

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

BuildArch: noarch

Source: %pkg_name-%version%subver.tar.gz
Source1: emacs-%pkg_name-start-script.el
Source2: sounds.tar.bz2
Source3: pieces.tar.bz2

Patch0: chess-2.0b6-empty_pos-move.patch

BuildPreReq: emacs-devel

# Automatically added by buildreq on Tue Jun 17 2003
BuildRequires: emacs-common

%description
Chess.el is an Emacs chess client and library, designed to be used
for writing chess-related programs, or for playing games of chess
against various chess engines, including Internet servers.  The library
can be used for analyzing variations, browsing historical games, or a
multitude of other purposes.

%package el
Summary: The Emacs Lisp sources for bytecode included in %name
Group: Development/Other
Requires: %name = %version-%release

%description el
%name-el contains the Emacs Lisp sources for the bytecode
included in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.

%package pieces
Summary: Additional pieces sets for %name
Group: Editors
Requires: %name = %version-%release

%description pieces
%name-pieces contains additional pieces sets for %name

%package sounds
Summary: Additional WAV files for announce moves verbally
Group: Editors
Requires: %name = %version-%release

%description sounds
%name-sounds contains additional WAV files for announce your opponent's
moves verbally, such as "knight takes at f4"

%prep
%setup -q -n %pkg_name
%patch0 -p1

%build
make clean
make

%install
mkdir -p %buildroot%_emacslispdir/%pkg_name
install -m 644 *.el* *.epd %buildroot%_emacslispdir/%pkg_name
mkdir -p %buildroot%_emacs_etc_dir/%pkg_name
mkdir -p %buildroot%_infodir
install -m 644 *.info* %buildroot%_infodir
pushd %buildroot%_emacs_etc_dir/%pkg_name
tar jxf %SOURCE2
tar jxf %SOURCE3
popd
mkdir -p %buildroot%_sysconfdir/emacs/site-start.d
install -m 644 %SOURCE1 %buildroot%_sysconfdir/emacs/site-start.d/%pkg_name.el
# touch %buildroot%_emacslispdir/%pkg_name/sounds/.nosearch
# touch %buildroot%_emacslispdir/%pkg_name/pieces/.nosearch

%files
%doc README PLAN TODO EPD.txt PGN.txt
%dir %_emacslispdir/%pkg_name
%_emacslispdir/%pkg_name/*.elc
%_emacslispdir/%pkg_name/*.epd
%dir %_emacs_etc_dir/%pkg_name/pieces/
%_emacs_etc_dir/%pkg_name/pieces/xboard/
%_infodir/*
%_sysconfdir/emacs/site-start.d/*

%files el
%doc ChangeLog
%_emacslispdir/%pkg_name/*.el

%files pieces
%_emacs_etc_dir/%pkg_name/pieces/*
%exclude %_emacs_etc_dir/%pkg_name/pieces/xboard

%files sounds
%_emacs_etc_dir/%pkg_name/sounds/


%changelog
* Sat Oct 24 2009 Igor Vlasenko <viy@altlinux.ru> 20070423:2.0-alt5.b6
- applied repocop patch: removed obsolete (un)install_info macros

* Mon Apr 23 2007 Eugene Vlasov <eugvv@altlinux.ru> 20070423:2.0-alt4.b6
- New version, minor bug fixes
- Fixed Url
- Fixed chess-opening.el compilation, replaced assert in chess-pos-move by
  condition
- Cleanup spec, removed %%__ macro
- ChangeLog moved to emacs-chess-el subpackage

* Thu Mar 02 2006 Eugene Vlasov <eugvv@altlinux.ru> 20060302:2.0-alt3.b5
- Build separate packages for pieces and sounds
- Moved pieces and sounds to %_emacs_etc_dir
- Build with emacs-devel

* Sat Oct 15 2005 Eugene Vlasov <eugvv@altlinux.ru> 20051015:2.0-alt2.b5
- Fixed site-start script (#7589)
- Dir %_emacslispdir/%pkg_name now belongs to package
- Added .nosearch files in non-lisp dirs (#7591)
- Removed load-path modification
- Default engine now chess-gnuchess, added requires on chess
- Fixed Url
- Fixed BuildArch
- Cleanup spec

* Fri May 14 2004 Ott Alex <ott@altlinux.ru> 20040514:2.0-alt1.b5
- New beta version

* Thu Oct 16 2003 Ott Alex <ott@altlinux.ru> 2.0b3-alt1
- Initial build
