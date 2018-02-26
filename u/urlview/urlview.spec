# Emacs, look here: -*- coding: cyrillic-cp1251 -*-
Name: urlview
Version: 0.9
Release: alt2
Serial: 1

Group: Networking/Other
%define CommonSummary A URL extractor/viewer for use with Mutt
##Offset several bytes before Russian characters.############################
%define CommonSummaryRU Вытаскивает и просматривает URL-ы для пользователей Mutt
%if_with slang
Summary: %CommonSummary (SLang variant).
Summary(ru_RU.CP1251): %CommonSummaryRU (вариант на SLang).
%else
Summary: %CommonSummary (ncurses variant).
Summary(ru_RU.CP1251): %CommonSummaryRU (вариант на ncurses).
%endif
License: GPL

Packager: Alexey Morsov <swi@altlinux.ru>

Requires: url_handler
Requires: common-licenses

Source: rsync://ftp.mutt.org::mutt/contrib/%name-%version.tar.bz2

# From Debian urlview-0.9-2.1
Source1: %name-0.9-htmlworkaround.debian.txt

# From Mdk urlview-0.9-4mdk
Patch1: %name-0.9-comma.patch

# From Debian urlview-0.9-2.1
Patch3: %name-0.9-sysconf.debian.patch

# From RedHat mutt-1.2.5i-17
Patch5: %name-0.9-correct-c.redhat.patch

# Fix aditional \n in the end of the url
Patch6: %name-0.9-cr.patch

# throw the dependency on libtinfo away (since libncurses-devel requires it)
# Automatically added by buildreq on Sun Sep 21 2003
BuildRequires: OpenSP sgml-tools
BuildRequires: groff

%if_with slang
BuildRequires(build): libslang-devel
%else
BuildRequires(build): libncurses-devel 
%endif
BuildRequires(build): automake = 1.4
%set_automake_version 1.4

%description
%name extracts URLs from a given text file, and presents a menu
of URLs to view using a user specified command.

%if_with slang
(Linked with S-Lang library.)
%else
(Linked with ncurses library.)
%endif

%description -l ru_RU.CP1251
%name вытаскивает URL-ы из данного текстового файла и 
предоставляет пользователю меню для выбора URL-а 
для просмотра при помощи заранее определённой команды.

%if_with slang
(Скомпоновано с библиотекой S-Lang.)
%else
(Скомпоновано с библиотекой ncurses.)
%endif

%prep
%setup
%patch1 -p1 -b .comma
%patch3 -p1 -b .sysconf
%patch5 -p1 -b .correct-c
%patch6 -p1

%build

%configure %{?_with_slang}

%make_build

# Generate HTML docs:
sgml2html %name.sgml \
    && %__mv %name.html %name.bad.html \
    && %__install -m0644 %SOURCE1 %name.html \
    && cat %name.bad.html >> %name.html

%install
mkdir -p "$RPM_BUILD_ROOT"{%_bindir,%_mandir/man1,%_sysconfdir/%name}
%makeinstall
install -p -m644 %name.conf.suse \
    "$RPM_BUILD_ROOT"%_sysconfdir/%name/system.%name

# link the license
%__ln_s -f %_licensedir/GPL-2 COPYING


%files

#dir %_sysconfdir/%name - belongs to url_handler pkg since 0.9-ipl8mdk
%config(noreplace) %_sysconfdir/%name/system.%name

%_bindir/*

%_mandir/man?/*
%doc AUTHORS ChangeLog README sample.%name

# Hack for symlink ;-)
%doc --no-dereference COPYING

%doc %name.html

%triggerpostun  -- %name < 0.9-ipl3mdk
moved="$(
    for f in %_sysconfdir/%name.conf*; do
	[ -e "$f" ] \
	    && install -D "$f" "%_sysconfdir/%name/old/${f##*/}" \
	    && { rm -f "$f"; echo -n "$f "; }
    done
)"
if [ "$moved" ]; then
    echo "Moving $moved to %_sysconfdir/%name/old/"
fi

%changelog
* Fri Apr 08 2011 Alexey Morsov <swi@altlinux.ru> 1:0.9-alt2
- fix build

* Fri Feb 08 2008 Alexey Morsov <swi@altlinux.ru> 1:0.9-alt1
- change release from ipl* to alt (new sisyphus_check)

* Mon May 07 2007 Alexey Morsov <swi@altlinux.ru> 0.9-ipl8mdk.2
- fix previsious patch (recomended by Lost)

* Mon May 07 2007 Alexey Morsov <swi@altlinux.ru> 0.9-ipl8mdk.1
- add patch for remove \n at the end of url

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.9-ipl8mdk.0
- Automated rebuild.

* Thu Sep 18 2003 Ivan Zakharyaschev <imz@altlinux.ru> 0.9-ipl8mdk
- split pkg (src): urlview + url_handler;
- update BuildReqs;
- translate Summary & description into Russian.

* Sat Feb  8 2003 Ivan Zakharyaschev <imz@altlinux.ru> 0.9-ipl7mdk
- url_handler.sh:
  + more quotes (to prevent expansion in wrong places; fixes No. 0001108);
  + accept ./* as file-URL, too (fixes No. 0001098 at http://bugs.altlinux.ru);
- spec-file:
  + drop PreReq on sh-utils, use bash parameter expansion to get the basename.

* Sun Nov  3 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.9-ipl6mdk
- rebuild

* Mon Apr 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.9-ipl5mdk
- url_handlers: added "file" method (by default, equals to http).
- url_handler.sh: added "file" protocol recognition (#0000838).

* Thu Apr 11 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.9-ipl4mdk
- url_handler.sh: 
  + clean up (ldv, imz);
  + extract the program lists to %_sysconfdir/urlview/url_handlers;
  + include user's configuration from ~/.etc/urlview/url_handlers;
  + case-insensitive protocol matching (fixes \#824 at bugs.altlinux.ru);
- url_handlers:
  + add mozilla -compose for mailto (fixes \#510 at bugs.altlinux.ru);
- spec-file:
  + maintaining patches is difficult, so use our own source for url_handler.sh;

* Thu Nov 29 2001 Ivan Zakharyaschev <imz@altlinux.ru> 0.9-ipl3mdk
- put a symlink to GPL-2 from common-licenses instead of the COPYING file
- a special directory %_sysconfdir/%name/ to hold both the conf-file and
  the script to start browsers (since it should be editable by the 
  administrator -- it contains paths and preferences) (debian)
- add nohup-mode to start programs in X (debian)
- add more url-handlers:
  + gecko-based HTTP-browsers;
  + Sylpheed & mailto program (Mutt remains the first);
  + gFTP client;
- documentation in HTML added;
- make the url-handler script more flexible (path lists implemented 
  with Bash arrays)
- correct C code (redhat)
- 2 variants of build: linked either with ncurses (default now) or slang.

* Fri Nov 10 2000 Dmitry V. Levin <ldv@fandra.org> 0.9-ipl2mdk
- Fixed paths for browsers.

* Thu Oct 12 2000 Dmitry V. Levin <ldv@fandra.org> 0.9-ipl1mdk
- RE adaptions.
- Automatically added BuildRequires.

* Wed Aug 16 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.9-1mdk
- 0.9
- include patch to escape commas passed via openURL by <ben@reser.org>

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.8.1-5mdk
- automatically added BuildRequires

* Fri Jul 28 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.8.1-4mdk
- BM + bzipped alpha file

* Mon Jul 10 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 0.8.1-3mdk
- makeinstall macro
- macroszifications

* Wed May 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.8.1-2mdk
- On alpha get a regex.o compiled and linked for alpha.

* Mon Apr 03 2000 Daouda Lo <daouda@mandrasoft.com> 0.8.1-1mdk
- fresh release 0.8.1
- added define section in spec
- cleanup spec file

* Thu Mar 23 2000 Daouda Lo <daouda@mandrakesoft.com> 0.7-6mdk
- fix group
* Sat Nov 06 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Mar 18 1999 Bill Nottingham <notting@redhat.com>
- strip binary
- fix defaults some

* Sat Dec 12 1998 Bill Nottingham <notting@redhat.com>
- initial build
