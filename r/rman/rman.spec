Name: rman
Version: 3.2
Release: alt1

Summary: reverse compile man pages from formatted form to a number of source formats
License: Artistic
Group: Development/Other

Url: http://polyglotman.sourceforge.net/rman.html
Source: %name-%version.tar.gz

Patch1: rman-3.2-alt-make.patch

Packager: XOrg Maintainer Team <xorg@packages.altlinux.org>

%description
PolyglotMan   takes  man pages from most of the popular flavors of UNIX
and transforms them into any of a number of text source formats.  Poly-
glotMan  was  formerly  known  as RosettaMan. The name of the binary is
still called rman , for scripts that depend on that name; mnemonically,
just  think "reverse man". Previously PolyglotMan  required pages to be
formatted by nroff prior  to  its  processing.  With  version  3.0,  it
prefers  [tn]roff  source  and usually produces results that are better
yet. And source processing is the only way to translate tables.  Source
format  translation is not as mature as formatted, however, so try for-
matted translation as a backup.

%prep
%setup -q

%patch1 -p1

%build
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Tue Jan 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 3.2-alt1
- initial release

