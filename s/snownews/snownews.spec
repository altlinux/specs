Name: snownews
Version: 1.5.10
Release: alt3.1

Summary: Text mode RSS newsreader
License: GPL2
Group: Networking/News

Url: http://home.kcore.de/~kiza/software/snownews/

Source: %name-%version.tar
Source1: %name.desktop

# add more html entities
Patch1: %name-1.5.1-alt-html_entities.patch
Patch2: %name-1.5.10-alt-DSO.patch

# Automatically added by buildreq on Mon Dec 15 2008 (-bi)
BuildRequires: common-licenses libncursesw-devel libxml2-devel perl-XML-LibXML zlib-devel

%description
Snownews is a text mode RSS/RDF newsreader. It supports all versions
of RSS natively, and other feed formats via plugins. It depends on
ncurses and uses libxml2 for XML parsing.

%prep
%setup
%patch1 -p1
%patch2 -p2

%build
mv doc/man/ru_RU.KOI8-R doc/man/ru
mv doc/man/ru/%name.1.ru_RU.KOI8-R.in doc/man/ru/%name.1.ru.in
sed -i 's/-lncurses/-lncursesw/g;s/ru_RU.KOI8-R/ru/g' configure Makefile scripts/install.sh
./configure
%make_build PREFIX=%prefix EXTRA_CFLAGS='%optflags'

%install
%makeinstall PREFIX=%buildroot%prefix
%find_lang --with-man %name
ln -s -f %_datadir/license/GPL-2 COPYING
mkdir -p %buildroot%_desktopdir
install -m 644 %SOURCE1 %buildroot%_desktopdir/

%files -f %name.lang
%_bindir/%name
%_bindir/opml2snow
%_bindir/snow2opml
%_man1dir/%name.*
%_man1dir/opml2snow.*
%_desktopdir/%name.desktop
%doc AUTHOR Change* CREDITS README*
%doc --no-dereference COPYING

%changelog
* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.10-alt3.1
- Fixed build

* Sun Apr 17 2011 Lenar Shakirov <snejok@altlinux.ru> 1.5.10-alt3
- Fixed build: zlib-devel added to BuildReqs
- Spec cleaned: thanks to rpmcs!

* Tue Dec 16 2008 Terechkov Evgenii <evg@altlinux.ru> 1.5.10-alt2
- Desktop file added

* Tue Dec 16 2008 Terechkov Evgenii <evg@altlinux.ru> 1.5.10-alt1
- Picked up from orphaned
- Link with ncursesw, not ncurses
- Werror mode disabled
- Patch0 dropped (seems not needed anymore)

* Sun Aug 01 2004 Alexey Tourbin <at@altlinux.ru> 1.5.3-alt1
- 1.5.1 -> 1.5.3

* Tue Mar 09 2004 Alexey Tourbin <at@altlinux.ru> 1.5.1-alt1
- initial revision:
  + alt-langinfo.patch: use nl_langinfo(3) to override default charset
  + alt-html_entities.patch: more html entities added
  + fixed %prefix/man -> %_mandir
  + Werror mode enabled
