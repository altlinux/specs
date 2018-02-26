Name: weechat
Version: 0.3.5
Release: alt2.1

Summary: fast, light & extensible IRC client
License: GPLv3
Group: Networking/IRC

URL: http://www.weechat.org/
Source: %name-%version.tar

# Automatically added by buildreq on Thu Oct 20 2011
BuildRequires: asciidoc libaspell-devel libgcrypt-devel libgnutls-devel liblua5-devel libncursesw-devel libruby-devel perl-devel python-devel ruby source-highlight tcl-devel

# used only in aclocal
BuildRequires: libgtk+2-devel

%description
WeeChat is a fast, light and extensible chat client. It runs on many
platforms (including Linux, BSD and Mac OS).
WeeChat is:
- modular: a lightweight core with plugins around
- multi-protocols: IRC and Jabber (other soon)
- extensible: C plugins and scripts (Perl, Python, Ruby, Lua and Tcl)
- free software: released under GPLv3 license
- fully documented: user's guide, API, FAQ,.. translated in many languages
Development is very active, and bug fixes are very fast!

%package plugin-aspell
Summary: Aspell plugin for weechat
Group: Networking/IRC
Requires: %name = %version-%release

%description plugin-aspell
This package contains aspell plugin for weechat.

%package plugin-lua
Summary: Lua plugin for weechat
Group: Networking/IRC
Requires: %name = %version-%release

%description plugin-lua
This package contains lua plugin for weechat.

%package plugin-perl
Summary: Perl plugin for weechat
Group: Networking/IRC
Requires: %name = %version-%release

%description plugin-perl
This package contains perl plugin for weechat.

%package plugin-python
Summary: Python plugin for weechat
Group: Networking/IRC
Requires: %name = %version-%release

%description plugin-python
This package contains python plugin for weechat.

%package plugin-ruby
Summary: Ruby plugin for weechat
Group: Networking/IRC
Requires: %name = %version-%release

%description plugin-ruby
This package contains ruby plugin for weechat.

%package plugin-tcl
Summary: Tcl plugin for weechat
Group: Networking/IRC
Requires: %name = %version-%release

%description plugin-tcl
This package contains ruby plugin for weechat.

%prep
%setup

# build plugins as plugins, not libs
find ./src/plugins -name "Makefile*" -print0 | xargs -r0 subst 's,\(\-module\),\1 -avoid-version,' --

%build
./autogen.sh

%configure \
	--enable-perl \
	--enable-python \
	--enable-ruby \
	--enable-lua \
	--enable-gnutls \
	--disable-gtk \
	--disable-qt \
	--enable-aspell \
	--enable-doc

%make_build

%install
%make_install DESTDIR=%buildroot install

ln -s %name-curses %buildroot%_bindir/%name

%find_lang %name

%files -f %name.lang
%_bindir/*
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/charset.so
%_libdir/%name/plugins/alias.so
%_libdir/%name/plugins/fifo.so
%_libdir/%name/plugins/irc.so
%_libdir/%name/plugins/logger.so
%_libdir/%name/plugins/relay.so
%_libdir/%name/plugins/rmodifier.so
%_libdir/%name/plugins/xfer.so
%_mandir/man?/*
%_defaultdocdir/%name

%files plugin-aspell
%_libdir/%name/plugins/aspell.so

%files plugin-lua
%_libdir/%name/plugins/lua.so

%files plugin-perl
%_libdir/%name/plugins/perl.so

%files plugin-python
%_libdir/%name/plugins/python.so

%files plugin-ruby
%_libdir/%name/plugins/ruby.so

%files plugin-tcl
%_libdir/%name/plugins/tcl.so

%changelog
* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.5-alt2.1
- Rebuild with Python-2.7

* Thu Oct 20 2011 Alexey Tourbin <at@altlinux.ru> 0.3.5-alt2
- Rebuilt for perl-5.14.

* Thu Sep 01 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.3.5-alt1
- 0.3.5.

* Thu Jan 27 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.3.4-alt1
- 0.3.4.
- Introduce -plugin-tcl subpackage.
- Update Summary and Descriptions, made some spec cleanups.

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt2.1
- Rebuilt with python 2.6

* Sat Jul 04 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2.6-alt2
- Rebuilt with Ruby 1.9
- Fixed build with new gnutls
- Removed obsolete %%update_menus/%%clean_menus calls

* Fri Sep 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.2.6-alt1
- 0.2.6.
- License: GPLv3.

* Wed Jun 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.2.5-alt1
- 0.2.5.

* Fri Apr 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.2.4-alt1
- 0.2.4.

* Thu Oct 19 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.2.1-alt2
- 0.2.1.

* Wed May 31 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.1.7-alt2.1
- Rebuild with libgnutls.so.13 .

* Tue Mar 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.1.7-alt2
- fix build with new ruby.

* Sat Jan 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.1.7-alt1
- 0.1.7 release.

* Thu Oct 06 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.5-alt1
- 0.1.5 release.
- fixed absolute link.
- added ruby plugins support.

* Tue Jul 05 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.3-alt1
- 0.1.3 release

* Sat Jun 11 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.2.1-alt1
- 0.1.2.1 release.
- python interface added.

* Fri Apr 08 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.1-alt2
- 0.1.1 release.

* Fri Mar 04 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.1-alt1
- 0.1.1 CVS from 04032005.

* Mon Nov 22 2004 Pavlov Konstantin <thresh@altlinux.ru> 0.0.9-alt0.1pre2
- 0.0.9pre1 development version.
- initial build for sisyphus
