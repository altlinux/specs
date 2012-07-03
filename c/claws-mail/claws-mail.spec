%define		_name		sylpheed
%define		_newname	claws-mail
%define		branch		claws
#define		cvs		.cvs5
%define     cvs     %nil
%def_disable	gtk3
%def_disable 	debug
Name:	 	%_newname
Version: 3.8.1
Release: alt1

Summary:	The bleeding edge branch of Sylpheed, a GTK+ based, lightweight, and fast e-mail client	 
License: 	%gpl3plus
Group: 		Networking/Mail

Url:		http://%name.sourceforge.net

Source: %name-%version.tar
Patch1:	%name-alt-filters-conv.patch
Patch6: claws-mail-3.7.6-fix-undo-redo-replace.patch
Patch7: claws-mail-alt-textviewer.patch
Patch8: claws-mail-alt-textviewer-pl.patch

# ALT Specific
Patch119: claws-mail-alt-masquerade-deps.patch

Obsoletes:	%_name-%branch < %version
Provides:	%_name-%branch

BuildRequires(pre): rpm-build-licenses

BuildPreReq:	autoconf-common gettext-tools 

BuildRequires: NetworkManager-devel flex libSM-devel libcompface-devel libdbus-glib-devel libenchant-devel libetpan-devel libgnutls-devel libgpgme-devel libldap-devel libpilot-link-devel libstartup-notification-devel libgcrypt-devel zlib-devel
%if_enabled gtk3
BuildRequires: libgtk+3-devel
%else
BuildRequires: libgtk+2-devel
%endif

%description
Claws Mail is an email client (and news reader), based on GTK+, featuring

    Quick response
    Graceful, and sophisticated interface
    Easy configuration, intuitive operation
    Abundant features
    Extensibility

The appearance and interface are designed to be familiar to new users
coming from other popular email clients, as well as experienced users.
Almost all commands are accessible with the keyboard.

The messages are managed in the standard MH format, which features fast
access and data security. You'll be able to import your emails from almost
any other email client, and export them just as easily.

Lots of extra functionality, like an RSS aggregator, calendar, or laptop
LED handling, are provided by extra plugins.

Claws Mail is distributed under the GPL.

%package        devel
Summary:        Development environment for %name
Group:          Development/C
Requires:	%name = %version-%release
Obsoletes:	%_name-%branch-devel < %version
Provides:	%_name-%branch-devel
Requires: rpm-macros-%{name} = %{version}-%{release}

%description 	devel
This package contains the header files and libraries for building program
which use %name.

%package	plugin-dillo
Summary:	Dillo browser plugin for %name
Group:		Networking/Mail
Requires:	%name = %version
Requires:	dillo
Obsoletes:	%_name-%branch-plugin-dillo < %version
Provides:	%_name-%branch-plugin-dillo

%description	plugin-dillo
This plugin for %name lets you see HTML content in the messages by means of
a Dillo embedded browser. This plugin only provides very basic HTML
support; if you want something more, consider installing
%name-plugin-gtkhtml2 package.

%package	plugin-spamassassin
Summary:	SpamAssassin plugin for %name
Group:		Networking/Mail
Requires:	%name = %version
Requires:	spamassassin
Obsoletes:	%_name-%branch-plugin-spamassassin < %version
Provides:	%_name-%branch-plugin-spamassassin

%description	plugin-spamassassin
This plugin for %name provides integration with SpamAssassin.

%package	plugin-bogofilter
Summary:	Bogofilter plugin for %name
Group:		Networking/Mail
Requires:	%name = %version
Requires:	bogofilter bogofilter-utils
Obsoletes:	%_name-%branch-plugin-bogofilter < %version
Provides:	%_name-%branch-plugin-bogofilter

%description	plugin-bogofilter
This plugin for %name provides integration with Bogofilter spam checking
tool.

%package	plugin-trayicon
Summary:	Tray icon plugin for %name
Group:		Networking/Mail
Requires:	%name = %version
Obsoletes:	%_name-%branch-plugin-trayicon < %version
Provides:	%_name-%branch-plugin-trayicon

%description	plugin-trayicon
This plugin for %name provides a tray icon.

%package	plugin-pgpcore
Summary:	Core PGP plugin for %name
Group:		Networking/Mail
Requires:	%name = %version
Obsoletes:	%_name-%branch-plugin-pgpcore < %version
Provides:	%_name-%branch-plugin-pgpcore

%description	plugin-pgpcore
This plugin for %name provides core PGP functionality. It is used by other
encryption/signing plugins.

%package	plugin-pgpmime
Summary:	PGP/MIME plugin for %name
Group:		Networking/Mail
Requires:	%name = %version
Requires:	%name-plugin-pgpcore = %version
Obsoletes:	%_name-%branch-plugin-pgpmime < %version
Provides:	%_name-%branch-plugin-pgpmime

%description	plugin-pgpmime
This plugin for %name lets you create and see messages encrypted/signed
with PGP/MIME.

%package	plugin-pgpinline
Summary:	PGP/Inline plugin for %name
Group:		Networking/Mail
Requires:	%name = %version
Requires:	%name-plugin-pgpcore = %version
Obsoletes:	%_name-%branch-plugin-pgpinline < %version
Provides:	%_name-%branch-plugin-pgpinline

%description	plugin-pgpinline
This plugin for %name lets you create and see messages encrypted/signed
with PGP/Inline.

%package	plugin-smime
Summary:	S/MIME plugin for %name
Group:		Networking/Mail
Requires:	%name = %version
Requires:	%name-plugin-pgpcore = %version
Requires:   dirmngr gnupg2-common
Obsoletes:	%_name-%branch-plugin-smime < %version
Provides:	%_name-%branch-plugin-smime

%description	plugin-smime
This plugin for %name lets you create and see messages encrypted/signed
with S/MIME.

%package	tools
Summary:	Additional tools for %name
Group:		Networking/Mail
Requires:	%name = %version
Requires:       python
BuildRequires:  python
BuildRequires:	python-modules-encodings
BuildPreReq:	perl-MIME-tools
BuildPreReq:	perl-Text-Iconv
BuildPreReq:	perl-XML-SimpleObject
BuildPreReq:	perl-URI
BuildPreReq: 	perl-libwww
BuildPreReq: 	perl-Text-CSV_XS
Obsoletes:	%_name-%branch-tools < %version
Provides:	%_name-%branch-tools

%description	tools
additional tools for %name.


%package -n rpm-macros-%{name}
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
# uncomment if macroses are platform-neutral
#BuildArch: noarch
# helps old apt to resolve file conflict at dist-upgrade (thanks to Stanislav Ievlev)
Conflicts: claws-mail-devel <= 3.7.9-alt1

%description -n rpm-macros-%{name}
Set of RPM macros for packaging %name-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.

%prep
%if "%cvs"==""
%setup -q
%else
%setup -q -n  %_name-%branch
%endif

subst "s,\#\!/usr/bin/python2.2,\#\!/usr/bin/python," tools/vcard2xml.py 
subst "s,\#\!/usr/bin/perl,\#\!/usr/bin/perl -w," tools/OOo2claws-mail.pl
subst "s,sylpheed,sylpheed-claws," tools/OOo2claws-mail.pl
subst "s,%%f,%%N," ./src/prefs_quote.c
echo "Libs: -lenchant -lgnutls" >>%name.pc.in

%patch1 -p1
%patch6 -p0
%patch7 -p1
%patch8 -p1

%patch119 -p1

%autoreconf

%build
%configure \
		--disable-static \
		--disable-rpath \
		--with-lib-prefix=%_usr \
		--with-aspell-includes=%_includedir \
		--with-aspell-libs=%_libdir \
		--with-faqdir=%_datadir/%name \
		--with-manualdir=%_datadir/%name \
		--with-config-dir=.%name \
		--disable-manual \
		%{subst_enable gtk3} \
		%if_enabled debug
		--enable-crash-dialog
		%else
		--disable-crash-dialog
		%endif
%make_build
%make -C tools

%install
%makeinstall_std
%make -C tools install

mkdir -p %buildroot%_datadir/%name/
cp -va  tools %buildroot%_datadir/%name/
rm -vf  %buildroot%_datadir/%name/tools/README*
rm -vf  %buildroot%_datadir/%name/tools/Makefile*

mkdir -p %buildroot/%_iconsdir
install -p -m644 %_newname.png %buildroot/%_iconsdir/%_newname.png
mkdir -p %buildroot%_pixmapsdir
ln -s %_iconsdir/%_newname.png %buildroot%_pixmapsdir

mkdir -p %buildroot%_rpmmacrosdir
cat << EOF >  %buildroot%_rpmmacrosdir/%name
%%_claws_version	%version
%%_claws_plugins_path %%_libdir/%_newname/plugins
%if_enabled gtk3
%%_claws_gtkver	3
%else
%%_claws_gtkver	2
%endif
EOF

# XXX: Make sure the path below is the same as the path above.
%define _claws_plugins_path %_libdir/%_newname/plugins

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog* COPYING INSTALL NEWS README* TODO* RELEASE_NOTES 
%_bindir/%name
%_bindir/%_name-%branch
%_man1dir/%_newname.1.gz
%_desktopdir/*.desktop
%_iconsdir/%_newname.png
%_iconsdir/hicolor/*x*/apps/%_newname.png
%_pixmapsdir/%_newname.png

%files devel
%_includedir/%_newname/*
%_pkgconfigdir/%_newname.pc
%exclude %_rpmmacrosdir/*
#%_rpmmacrosdir/%name

%files plugin-dillo
%_claws_plugins_path/dillo_viewer.so

%files plugin-spamassassin
%_claws_plugins_path/spamassassin.so

%files plugin-bogofilter
%_claws_plugins_path/bogofilter.so

%files plugin-trayicon
%_claws_plugins_path/trayicon.so

%files plugin-pgpcore
%_claws_plugins_path/pgpcore.so

%files plugin-pgpmime
%_claws_plugins_path/pgpmime.so
%_claws_plugins_path/pgpmime.deps

%files plugin-pgpinline
%_claws_plugins_path/pgpinline.so
%_claws_plugins_path/pgpinline.deps

%files plugin-smime
%_claws_plugins_path/smime.so
%_claws_plugins_path/smime.deps

%files tools
%doc tools/README*
%_datadir/%name/tools/*
%exclude %_datadir/%name/tools/update-po

%exclude %_claws_plugins_path/*.la
%exclude %_datadir/doc/%name/RELEASE_NOTES

%files -n rpm-macros-%{name}
%_rpmmacrosdir/*


%changelog
* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 3.8.1-alt1
- Updated to 3.8.1.

* Wed Jan 18 2012 Mikhail Efremov <sem@altlinux.org> 3.8.0-alt1
- Drop obsoleted patches.
- Updated to 3.8.0.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.10-alt1.1
- Rebuild with Python-2.7

* Fri Sep 02 2011 Mikhail Efremov <sem@altlinux.org> 3.7.10-alt1
- Drop module-load-dirty-fix.patch.
- Drop obsoleted patches.
- Fix crash with long MIME type in the header.
- Updated to 3.7.10.

* Tue May 31 2011 Mikhail Efremov <sem@altlinux.org> 3.7.9-alt2
- Rebuild for NM-0.9 support.

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 3.7.9-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-rpm-macros-packaging for claws-mail-devel

* Tue May 03 2011 Mikhail Efremov <sem@altlinux.org> 3.7.9-alt1
- Patches from upstream CVS:
   + Don't show message on right click.
   + Work around for a bug in Gnome Shell.
   + Fix segfault on startup (thanks aris@, closes: #25555).
- Minor spec cleanup.
- Sources: tar.bz2 -> tar.
- Updated to 3.7.9 (closes: #25532).

* Mon Apr 04 2011 Mikhail Efremov <sem@altlinux.org> 3.7.8-alt2
- Fix BR: add libgcrypt-devel and zlib-devel.

* Thu Dec 30 2010 Mikhail Efremov <sem@altlinux.org> 3.7.8-alt1
- textviewer.pl: Added 'gz' extension handler.
- Updated to 3.7.8

* Wed Dec 01 2010 Mikhail Efremov <sem@altlinux.org> 3.7.7-alt2
- tools: don't package update-po script
- textviewer.sh: remove color codes from plain text.
- tools: to masquerade huge and unnecessary dependences.

* Mon Nov 29 2010 Mikhail Efremov <sem@altlinux.org> 3.7.7-alt1
- Updated to 3.7.7

* Thu Jul 22 2010 Mikhail Efremov <sem@altlinux.org> 3.7.6-alt1
- new version (closes: #23780).
- fix undo/redo after replace selected text from context menu.

* Fri Jan 15 2010 Alexey Rusakov <ktirf@altlinux.org> 3.7.4-alt1
- new version.
- patch for ru.po went upstream.
- desktop file installation went upstream.

* Mon Oct 26 2009 Alexey Rusakov <ktirf@altlinux.org> 3.7.3-alt1
- new version (3.7.3).
- patch for crashes after editing displayed headers went upstream.

* Tue Sep 01 2009 Alexey Rusakov <ktirf@altlinux.org> 3.7.2-alt1.1
- rebuild with libldap2.4.

* Wed Jul 08 2009 Alexey Rusakov <ktirf@altlinux.org> 3.7.2-alt1
- new version (3.7.2), with a fix for the Russian translation.
- the fix for building with Automake 1.11 went upstream.
- fixed a crash after editing displayed headers (closes ALT bug 10044).

* Tue May 26 2009 Alexey Rusakov <ktirf@altlinux.org> 3.7.1-alt1
- 3.7.1.
- removed obsolete post/postun macros.
- spec cleanup: use better macros in files list, don't use %%__ macros.
- fixed building with Automake 1.11.
- excluded *.a and *.la files from packaging explicitly.
- package .deps files for plugins that depend on other plugins.
- made plugin descriptions more telling, removed periods from Summaries.
- added %%_claws_plugins_path macro.
- packaged S/MIME plugin.
- added proper Libs: clause to the .pc file so that plugins don't have
  to install additional -devel packages just because there's no them in
  claws-mail-devel dependencies.

* Thu Oct 16 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.6.1.cvs5-alt1.2
-  build with fixed libetpan.

* Mon Oct 13 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.6.1.cvs5-alt1.1
-  build with new libgnutls (libgnutls-new).

* Mon Oct 13 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.6.1.cvs5-alt1
-  Remove OpenSSL code (upstream);
-  BuildReq actualization.

* Sat Oct 11 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.6.1.cvs3-alt1
-  some ssl fixes (upstream).

* Fri Oct 10 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.6.1-alt1
-  3.6.1;
-  use gnutls instead of openssl.

* Mon Oct 06 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.6.0.cvs7-alt1
-  3.6.0.

* Mon Aug 11 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.5.0.cvs57-alt1
-  3.5.0.

* Mon May 19 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.4.0.cvs51-alt1
-  3.4.0.cvs51; 
-  build with networkmanager support.

* Thu Apr 24 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.4.0.cvs10-alt1
-  3.4.0.

* Mon Mar 31 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.3.1.cvs47-alt1
-  fix segfault if /home is full (upstream);
-  add support for png themes (upstream);
-  learn bogofilter from whitelist (upstream).

* Tue Mar 18 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.3.1.cvs30-alt1
-  3.3.1.

* Mon Feb 11 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.3.0.cvs5-alt1
-  3.3.0;
-  remove clamav plugin (upstream, see ChangeLog);
-  remove "kostyli" for old autotools. 

* Thu Jan 10 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.2.0.cvs34-alt1
-  3.2.0.

* Fri Nov 23 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.1.0.cvs26-alt1
-  3.1.0;
-  #13127 fix.

* Thu Oct 11 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.0.2.cvs57-alt1
-  lots of bugfixes (upstream).

* Fri Oct 05 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.0.2.cvs13-alt1
-  3.0.2.

* Thu Sep 27 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.0.1.cvs35-alt1
-  3.0.1;
-  remove russian translation mistakes patch.

* Fri Aug 24 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.10.0.cvs158-alt1
-  security fixes (POP3 Format String Vulnerability, CVE is unpublished now), 10x to ldv@.
-  #9685 fix. 10x to naf@ and ktirf@.

* Thu Aug 16 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.10.0.cvs125-alt1
-  bugfixes.

* Fri Aug 03 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.10.0.cvs81-alt2
-  dirty fix for load modules with invalid license.

* Tue Jul 31 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.10.0.cvs81-alt1
-  2.10.0.cvs81.

* Wed Jul 25 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.10.0.cvs62-alt1
-  2.10.0.

* Fri May 11 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.9.2.cvs5-alt1
-  2.9.2.

* Thu Apr 19 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.9.1.cvs1-alt1
-  2.9.1.

* Wed Mar 21 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.8.1.cvs27-alt1
-  2.8.1.

* Mon Feb 05 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.7.2.cvs22-alt1
-  build with libSM;
-  all patches for tools package has been removed (10x to upstream :)).

* Mon Jan 29 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.7.2.cvs4-alt1
-  2.7.2;
-  build with jPilot support;
-  trayicon plugin improvements.

* Thu Jan 25 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.7.1.cvs55-alt1
-  2.7.1.cvs55.

* Fri Jan 19 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.7.1.cvs32-alt1
-  2.7.1.cvs32.

* Wed Jan 17 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.7.1.cvs11-alt1
-  2.7.1.

* Thu Jan 11 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.7.0.cvs6-alt1
-  2.7.0.

* Fri Dec 15 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.6.1.cvs37-alt1
-  2.6.1.cvs37. bugfixes.

* Mon Dec 04 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.6.1.cvs1-alt1
-  2.6.1.

* Wed Nov 29 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.6.0.cvs65-alt1
-  2.6.0cvs65.
-  name changed to claws-mail.
-  patch 117 added (locale support fix).

* Wed Oct 25 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.5.6.cvs6-alt1
-  2.5.6.

* Thu Sep 28 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.5.2.cvs12-alt1
-  2.5.2.

* Tue Sep 26 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.5.1.cvs1-alt1
-  2.5.1

* Tue Sep 19 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.4.0.cvs198-alt1
-  lots of bugfixes.

* Wed Sep 06 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.4.0.cvs152-alt1
-  2.4.0.cvs152.
-  new bogofilter plugin.

* Mon Aug 28 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.4.0.cvs102-alt1
- 2.4.0.cvs102.
- require autoconf 2.60.

* Fri Aug 11 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.4.0.cvs40-alt1
-  2.4.0. bugfix.

* Wed Aug 09 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.4.0.cvs34-alt1
-  2.4.0.

* Mon Jun 26 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.3.1.cvs20-alt1
-  2.3.1.

* Mon Jun 19 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.3.0.cvs22-alt1
-  2.3.0.

* Mon Jun 05 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.2.1.cvs1-alt1
-  2.2.1.

* Tue May 30 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.2.0.cvs66-alt1
-  much more speed-up :)

* Wed May 24 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.2.0.cvs52-alt1
-  more speed-up for folder operations.

* Tue May 23 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.2.0.cvs47-alt1
-  speed-up folder operations.

* Fri May 19 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.2.0.cvs35-alt1
-  2.2.0

* Wed Apr 12 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.1.0.cvs32-alt1
-  2.1.0.cvs32. bugfixes.

* Wed Apr 12 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.1.0.cvs24-alt1
- 2.1.0 

* Tue Mar 28 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0.cvs178-alt1
-  2.0.0.cvs178. bugfixes. 

* Mon Mar 20 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0.cvs158-alt1
-  2.0.0.cvs158;
-  build with libetpan 0.43.

* Fri Feb 10 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0.cvs41-alt1
-  2.0.0.cvs41.
-  fixes in tools.

* Tue Feb 07 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0.cvs26-alt1
-  improve perfomance.

* Thu Feb 02 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0.cvs8-alt1
-  2.0.0.cvs8.

* Tue Jan 31 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0.cvs2-alt1
-  2.0.0.

* Mon Jan 16 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.100.cvs157-alt1
-  cvs157. HIG'ify.

* Fri Dec 16 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.100.cvs93-alt1
-  1.9.100.cvs93.
-  fixes for menu.

* Wed Dec 07 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.100.cvs71-alt1
-  1.9.100.cvs71.

* Thu Nov 17 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.100.cvs15-alt1
-  1.9.100.cvs15. bugfixes.

* Wed Nov 09 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.100.cvs4-alt1
-  1.9.1.

* Fri Oct 28 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.15.cvs124-alt1
-  cvs124.
-  temporary disabled tools patches (google, freshmeat and sf search).

* Tue Oct 18 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.15.cvs71-alt1
-  1.9.15.cvs71.

* Fri Oct 14 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.15.cvs44-alt1
-  1.9.15.cvs44.

* Wed Oct 12 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.15.cvs30-alt1
-  1.9.15.cvs30.
-  build for altlinux sisyphus.



