Name: balsa
Version: 2.4.90
Release: alt1.git.18.g76680d4

Summary: Balsa Mail Client
Summary(ru_RU.UTF-8): Графический почтовый клиент Balsa

License: GPL
Group: Networking/Mail
Url: http://pawsa.fedorapeople.org/balsa/

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: %name.tar
Source2: balsa_icons.tar

BuildPreReq: rpm-build-gnome
# Automatically added by buildreq on Thu Apr 12 2012 (-bi)
# optimized out: NetworkManager-devel NetworkManager-glib docbook-dtds elfutils fontconfig fontconfig-devel glib2-devel gnome-doc-utils-xslt gnupg2 libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcanberra-devel libcanberra-gtk-common-devel libcanberra-gtk3 libcom_err-devel libdbus-devel libdbus-glib libdbus-glib-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgnome-keyring libgpg-error libgpg-error-devel libgst-plugins libgtk+3-devel libjavascriptcoregtk3-devel libkrb5-devel libpango-devel libsoup-devel libwayland-client libwayland-server perl-Encode perl-XML-Parser pkg-config python-base python-module-libxml2 python-modules python-modules-compiler python-modules-encodings xml-common xml-utils xsltproc xz zlib-devel
BuildRequires: NetworkManager-glib-devel gnome-doc-utils intltool libcanberra-gtk3-devel libcompface-devel libenchant-devel libesmtp-devel libgmime-devel libgnome-keyring-devel libgpgme-devel libgtksourceview3-devel libgtkspell3-devel libldap-devel libnotify-devel libpcre-devel libsqlite3-devel libssl-devel libwebkitgtk3-devel libxml2-devel python-module-distribute time

BuildRequires: gnome-icon-theme

%description
Balsa is an e-mail reader.  This client is part of the GNOME
desktop environment.  It supports local mailboxes, POP3 and
IMAP.

%description -l ru_RU.UTF-8
Balsa -- это клиент для чтения электронной почты.
Поддерживает работу с локальными почтовыми ящиками, протоколами POP3 и IMAP.

#FIXME
#--with-html-widget=(no|gtkhtml2|gtkhtml3|webkit)
%define def_with_param() %{expand:%%{!?_with_%{1}: %%{!?_without_%{1}: %%{?2: %%global _with_param_%{1} %{2}} %%global _with_%{1} --with-%{1}}}}
%define subst_with_param() %{expand:%%{?_with_%{1}:%%{_with_%{1}}%%{?_with_param_%{1}:=%%{_with_param_%{1}}}}} %{expand:%%{?_without_%{1}:%%{_without_%{1}}%%{?_without_param_%{1}:=%%{_without_param_%{1}}}}}
%define if_with_param() %if %{expand:%%{?_with_%{1}: %%{?2:%%(if [ "%%{_with_param_%{1}}" == "%{2}" ]; then echo 1; else echo 0; fi)}%%{!?2:1}}%%{!?_with_%{1}:0}}

#FIXME make it work
%def_with_param html-widget webkit
%def_with canberra
%def_with compface
%def_with gpgme
%def_disable gregex	# use pcre
%def_with gss
%def_with gtksourceview
%def_with gtkspell
%def_with ldap
%def_with libnotify
%def_with nm
%def_with rubrica
%def_enable smime
%def_with sqlite
%def_with ssl
%def_enable threads

%prep
%setup -q -n %name
tar xf %SOURCE2
mkdir -p m4 ; ln -s %_datadir/gnome-doc-utils/gnome-doc-utils.make gnome-doc-utils.make

%build
%autoreconf ;
#%%{subst_with_param html-widget} \
%configure \
	--enable-pcre \
	--with-esmtp \
	--with-html-widget=webkit \
	%{subst_with canberra} \
	%{subst_with compface} \
	%{subst_with gpgme} \
	%{subst_enable gregex} \
	%{subst_with gss} \
	%{subst_with gtksourceview} \
	%{subst_with gtkspell} \
	%{subst_with ldap} \
	%{subst_with libnotify} \
	%{subst_with nm} \
	%{subst_with rubrica} \
	%{subst_enable smime} \
	%{subst_with sqlite} \
	%{subst_with ssl} \
	%{subst_enable threads} \

%make_build

%install
%makeinstall_std

install -d %buildroot%_miconsdir
install -d %buildroot%_niconsdir
install -d %buildroot%_liconsdir

install -m644 balsa_16.xpm %buildroot%_miconsdir/%name.xpm
install -m644 balsa_32.xpm %buildroot%_niconsdir/%name.xpm
install -m644 balsa_48.xpm %buildroot%_liconsdir/%name.xpm

xz ChangeLog ||:
%find_lang --with-gnome %name

%files -f %name.lang
%doc README COPYING ChangeLog* NEWS TODO AUTHORS HACKING docs/mh-mail-HOWTO
%doc docs/vconvert.awk docs/pine2vcard
%config %_sysconfdir/sound/events/*
%_bindir/*
%_desktopdir/%{name}*.desktop
%_datadir/%name
%_man1dir/%name.1*
%_datadir/sounds/%name
%_pixmapsdir/gnome-balsa2.png
%_miconsdir/%name.xpm
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_iconsdir/hicolor/48x48/mimetypes/*

%changelog
* Fri Apr 20 2012 Ildar Mulyukov <ildar@altlinux.ru> 2.4.90-alt1.git.18.g76680d4
- new version

* Fri Oct 28 2011 Ildar Mulyukov <ildar@altlinux.ru> 2.4.9-alt6.git.71.g369a5cf
- rebuild

* Tue Aug 23 2011 Ildar Mulyukov <ildar@altlinux.ru> 2.4.9-alt5.git.71.g369a5cf
- build GTK3 version with GtkSpell3

* Fri May 27 2011 Ildar Mulyukov <ildar@altlinux.ru> 2.4.9-alt4.git.32.ge3db6d8
- rebuild for GNOME3

* Wed May 25 2011 Ildar Mulyukov <ildar@altlinux.ru> 2.4.9-alt3.git.32.ge3db6d8
- new GIT version
- mimetype x-scheme-handler/mailto added by upstream (closes #25531)

* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 2.4.9-alt2.git.7.gb9f3588
- Fix LDAP support

* Tue Jan 11 2011 Ildar Mulyukov <ildar@altlinux.ru> 2.4.9-alt1.git.7.gb9f3588
- new version
- build with new libcanberra
- threads are enabled again

* Wed Oct 06 2010 Ildar Mulyukov <ildar@altlinux.ru> 2.4.8-alt1.git.8.gd6cdd2d
- new version

* Mon Aug 09 2010 Ildar Mulyukov <ildar@altlinux.ru> 2.4.7_91_gb0a4418-alt1
- fix crashes due to https://bugzilla.gnome.org/show_bug.cgi?id=608337
   through disabling threads

* Tue Jun 01 2010 Ildar Mulyukov <ildar@altlinux.ru> 2.4.7_67_g454a179-alt1
- new version
- fix %%find_lang to consider GNOME files
- change HTML toolkit choice through %%html-widget (doesn't work currently)

* Mon Dec 28 2009 Ildar Mulyukov <ildar@altlinux.ru> 2.4.2_13_gd1822c3-alt1
- new version
- add NetworkManager and libcanberra

* Wed Sep 09 2009 Ildar Mulyukov <ildar@altlinux.ru> 2.4.1_15_g6edf8ef-alt1
- release 2.4.1
- upstream moved to GIT
- gmime-2.4 is now in "master" branch (upstream)
- use libunique
- desktop file fix pushed to upstream
- disable threads due to http://bugzilla.gnome.org/show_bug.cgi?id=580230

* Sat Apr 18 2009 Ildar Mulyukov <ildar@altlinux.ru> 2.3.28_62_gbee3fd3-alt1
- big version change
- gmime-2.4 patch revised
- menu file expelled

* Sun Jan 04 2009 Ildar Mulyukov <ildar@altlinux.ru> 2.3.27-alt2
- improved gmime-2.4 patch: added GMIME_ENABLE_RFC2047_WORKAROUNDS

* Thu Jan 01 2009 Ildar Mulyukov <ildar@altlinux.ru> 2.3.27-alt1
- 2.3.27
- gmime-2.4 patch added
- spec improvements
- some small fixes according to repocop reports

* Mon Jun 16 2008 Ildar Mulyukov <ildar@altlinux.ru> 2.3.25-alt1
- 2.3.25

* Mon Jun 02 2008 Ildar Mulyukov <ildar@altlinux.ru> 2.3.24-alt1
- 2.3.24

* Tue Mar 25 2008 Ildar Mulyukov <ildar@altlinux.ru> 2.3.23-alt1
- 2.3.23
- gtksourceview is back - version 2 is used

* Thu Dec 27 2007 Ildar Mulyukov <ildar@altlinux.ru> 2.3.22-alt1
- 2.3.22

* Wed Dec 12 2007 Ildar Mulyukov <ildar@altlinux.ru> 2.3.21-alt1
- 2.3.21
- removed gtksourceview - version 2 is not supported yet
- added rubrica support

* Tue Oct 30 2007 Ildar Mulyukov <ildar@altlinux.ru> 2.3.20-alt2.SVN7771
- gear/git way to build package
- upstream -> SVN7771
- pcre (my local?) bug workaround is possible with --enable regex_dirty_hack
- %name-2.3.14-alt-configure.patch is no more needed
- changed sqlite -> sqlite3

* Sun Sep 30 2007 Ilya Mashkin <oddity at altlinux.ru> 2.3.20-alt1
- Just build new version 2.3.20
- Add russian description

* Mon Mar 12 2007 Ildar Mulyukov <ildar@altlinux.ru> 2.3.14-alt1
- 2.3.14

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.3.13-alt2.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Wed Jun 28 2006 Ildar Mulyukov <ildar@altlinux.ru> 2.3.13-alt2
- balsa-2.3.12-alt-configure.patch fixed for building on x86_64

* Thu Jun 22 2006 Ildar Mulyukov <ildar@altlinux.ru> 2.3.13-alt1
- 2.3.13

* Sun Nov 21 2004 Andrey Semenov <mitrofan@altlinux.ru> 2.2.6-alt1
- 2.2.6

* Mon Oct 04 2004 Andrey Semenov <mitrofan@altlinux.ru> 2.2.5-alt1
- new version

* Mon Aug 30 2004 Andrey Semenov <mitrofan@altlinux.ru> 2.2.4-alt1
- new version
- periodic expunge configurable
- cleanup IMAP password quering code
- GPE address book support - http://gpe.handhelds.org/projects/GPE-address.shtml
- new configuration druid

* Sat Aug 21 2004 Andrey Semenov <mitrofan@altlinux.ru> 2.2.3-alt1
- new version
- periodic expunge code crash fixed
- fixed recovery from broken IMAP connections
- startup speedup
- some memory leaks fixed

* Tue Aug 10 2004 Andrey Semenov <mitrofan@altlinux.ru> 2.2.2-alt1
- new version
- configurable hiding of deleted messages
- keyboard navigation fixes
- message counting in some edge cases fixed
- GPG fixes

* Tue Aug 03 2004 Andrey Semenov <mitrofan@altlinux.ru> 2.2.1-alt1
- new version
- IMAP mailboxes could be incorrectly marked as read-only
- message selection behaves more sanely
- 64-bit fixes
- memory leaks fixed
- handle better imap servers without server-side threading and limits
  on number of concurent connections
- quick "Sender or Subject" message index filtering
- various UI improvements

* Mon Jul 12 2004 Andrey Semenov <mitrofan@altlinux.ru> 2.2.0-alt1
- new version
- fix 143322, 143263, 145701
- GPGME updates
- GSSAPI IMAP authentication
- more build fixes

* Tue Mar 30 2004 Andrey Semenov <mitrofan@altlinux.ru> 2.0.17-alt1
- build on GNOME-2.6
- fix some GPGME interaction problems
- yet another set of minor fixes

* Mon Jan 19 2004 Andrey Semenov <mitrofan@altlinux.ru> 2.0.16-alt1
- update GPGME support: 124905
- libgtkhtml3 support added
- use bonobo to avoid running of multiple balsa instances
- fix bugs: 103639, 124550, 127422, 129316 and number of others

* Mon Jan 5 2004 Andrey Semenov <mitrofan@altlinux.ru> 2.0.15-alt3
- rebuild with gcc-3.3

* Sun Oct 26 2003 Andrey Semenov <mitrofan@altlinux.ru> 2.0.15-alt2
- Rebuild with libaspell

* Mon Sep 29 2003 Andrey Semenov <mitrofan@altlinux.ru> 2.0.15-alt1
- 2.0.15
- imap folder scanning speedup.
- fix bugs: 121181, 121637, 121867 and others.
- help updates.

* Thu Sep 25 2003 Andrey Semenov <mitrofan@altlinux.ru> 2.0.14-alt2
- Cleanup spec

* Mon Jul 28 2003 Andrey Semenov <mitrofan@altlinux.ru> 2.0.14-alt1
- 2.0.14
- message wrapping improvements, RFC 2646 support.
- experimental LDAP write support (feedback and patches appreciated).
- number of bugs fixed.

* Mon Jul 28 2003 Andrey Semenov <mitrofan@altlinux.ru> 2.0.13-alt1
- 2.0.13

* Mon Jul 7 2003 Andrey Semenov <mitrofan@altlinux.ru> 2.0.12-alt1
- 2.0.12
- Added Undo and Redo in the message composer.
- Occasional mangling of text attachments fixed
- More information about attached messages is shown.

* Sun May 18 2003 Andrey Semenov <mitrofan@altlinux.ru> 2.0.11-alt2
- Cleanup spec

* Mon May 12 2003 Andrey Semenov <mitrofan@altlinux.ru> 2.0.11-alt1
- 2.0.11
- text wrapping improvements.
- charset encoding validation and conversion improvements.
- several message signing and encryption improvelemts.
- minor LDAP fixes (large directories, non-US-ASCII characters).

* Wed Mar 26 2003 Andrey Semenov <mitrofan@altlinux.ru> 2.0.10-alt1
- 2.0.10
- GPG support.
- translation fixes and enhancements.
- large set of UI fixes.
- wrapping cleanups.
- autocommit improvements.
- (lib)mutt buffer overflow fix.
- ...and lots of other bugs fixed.

* Sun Mar 23 2003 Andrey Semenov <mitrofan@altlinux.ru> 2.0.9-alt1
- First version of RPM package.
