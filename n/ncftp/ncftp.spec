Name: ncftp
Version: 3.2.4
Release: alt1.qa1
Serial: 1

Packager: Ilya Mashkin <oddity at altlinux dot ru>

Summary: An improved FTP client
Summary(ru_RU.KOI8-R): Улучшенный FTP клиент
License: Artistic
Group: Networking/File transfer
Url: http://www.NcFTP.com/

Source0: %name-%version-src.tar.bz2
Source2: %name-16.png.bz2
Source3: %name-32.png.bz2
Source4: %name-48.png.bz2

#Patch0: ncftp-confirm.patch.bz2
#Patch1: ncftp-3.1.6-DESTDIR.patch.bz2
#Patch2: ncftp-3.0.3-resume.patch.bz2
#Patch3: ncftp-3.0.3-suspend.patch.bz2
#Patch4: ncftp-3.1.1-EPLF.diff.bz2


Patch1: ncftp-3.0.1-pref.patch
Patch2: ncftp-3.0.3-resume.patch
Patch3: ncftp-3.1.5-pmeter.patch
Patch4: ncftp-3.1.5-ncursesw.patch
Patch5: ncftp-3.2.2-no_lfs64_source.patch

# Automatically added by buildreq on Sun Feb 06 2005
BuildRequires: libncurses-devel libtinfo-devel

%description
Ncftp is an improved FTP client.  Ncftp's improvements include support
for command line editing, command histories, recursive gets, automatic
anonymous logins and more.

%description -l ru_RU.KOI8-R
NcFTP - это улучшенный консольный FTP клиент. Улучшения включают в себя 
расширенную командную строку, историю выполняемых команд, автоматический
анонимный вход на FTP сервер и многое другое.

%prep
%setup -q
#patch0 -p0 -b .confirm 
#patch1 -p1
#patch2 -p1 -b .res
##patch3 -p1 -b .suspend
#patch4 -p1 -b .eplf

%patch1 -p0 -b .pref
%patch2 -p1 -b .res
%patch3 -p1 -b .pmeter
#patch4 -p1 -b .ncursesw
#patch5 -p0 -b .no_lfs64_source

%build
%configure --enable-signals
%make_build

%install
mkdir -p %buildroot/{%_bindir,%_man1dir}
%makeinstall BINDIR=$RPM_BUILD_ROOT%_bindir


# icon
mkdir -p %buildroot/{%_miconsdir,%_liconsdir,%_niconsdir}
bzcat %SOURCE2 > $RPM_BUILD_ROOT%_miconsdir/%name.png
bzcat %SOURCE3 > $RPM_BUILD_ROOT%_niconsdir/%name.png
bzcat %SOURCE4 > $RPM_BUILD_ROOT%_liconsdir/%name.png

mkdir -p %buildroot{%_niconsdir,%_miconsdir,%_liconsdir}
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=NCFtp
Comment=An improved FTP client.
Icon=%name
Exec=%name
Terminal=true
Categories=Network;FileTransfer;
EOF

find doc -type f -exec chmod 0644 {} \;


%files
%doc doc/*.txt
%_desktopdir/%name.desktop
%_bindir/*
%_mandir/*/*

%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Sun Apr 17 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.2.4-alt1.qa1
- NMU: converted menu to desktop file

* Fri Apr 16 2010 Ilya Mashkin <oddity@altlinux.ru> 1:3.2.4-alt1
- 3.2.4

* Fri Jan 15 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1:3.2.3-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for ncftp
  * postclean-05-filetriggers for spec file

* Thu Jul 30 2009 Ilya Mashkin <oddity@altlinux.ru> 1:3.2.3-alt1
- 3.2.3

* Mon Nov 16 2008 Ilya Mashkin <oddity at altlinux.ru> 1:3.2.2-alt2
- fix 64-bit build

* Fri Aug 29 2008 Ilya Mashkin <oddity at altlinux.ru> 1:3.2.2-alt1
- new version 3.2.2

* Fri Sep 28 2007 Ilya Mashkin <oddity at altlinux.ru> 1:3.2.1-alt2
- Update patches from Fedora
- Drop Kame IPv6 patch, should fix Fedora bug #153019. Upstream doesn't seem to want to
  support IPv6 just yet, so for people requiring IPv6, switching to lftp or
  some other alternative is probably best.
- Drop epsv patch, since it applied on top of the IPv6 patch.

* Tue Aug 07 2007 Ilya Mashkin <oddity at altlinux.ru> 1:3.2.1-alt1
- new version 3.2.1

* Wed Aug 09 2006 Ilya Mashkin <oddity at altlinux.ru> 1:3.2.0-alt1
- new version 3.2.0

* Mon Mar 27 2006 Ilya Mashkin <oddity at altlinux.ru> 1:3.1.9-alt2
- fix icons

* Fri Apr 15 2005 Ilya Mashkin <oddity at altlinux dot ru> 1:3.1.9-alt1
- 3.1.9

* Sun Feb 06 2005 Ilya Mashkin <oddity at altlinux dot ru> 1:3.1.8-alt2
- apply 5 patches from previous build: confirm, DESTDIR, resume, suspend, EPLF

* Tue Jul 13 2004 Ilya Mashkin <oddity@altlinux.ru> 1:3.1.8-alt1
- Update version to 3.1.8:
- Ncftpget, ncftpput, and ncftpls now try to erase the arguments to the -u/-p/-j (user, password, account) options so they do not show in a "ps" command (Thanks, Konstantin Gavrilenko).
- Recognize broken IBM mainframe FTP servers and work around them.
- Working around a problem with ProFTPD 1.2.9 and later which would cause recursive downloads to fail.
- Fixed a bug where ncftpput in recursive mode could lock up if you used a trailing slash on the directory to upload.
- For the malicious server problem that was addressed in 3.1.5, enhanced the fix for better compatibility with mainframe FTP servers.
- Ncftpget, ncftpput, and ncftpls, and ncftp's open command now accept an additional advanced option (-o) which lets you do things like disable NcFTP's use of SITE UTIME, FEAT, HELP SITE, etc.
- Several HP-UX 10 compatibility bugs fixed (Thanks, Laurent FAILLIE).
- A couple of looping problems with ncftpbatch fixed (Thanks, George Goffe).
- Bug fixed with the upload socket buffer not being set (Thanks, ybobble).
- The utility programs now accept "-" for the config file name used with "-f" to denote standard input (Thanks, Jeremy Monin).
- Bug fixed with ncftpput when using both -c and -A (Thanks, Ken Woodmansee).
- Support for boldface text in Windows version (Thanks, Adam Gates).


* Tue Jan 08 2004 Ilya Mashkin <oddity@altlinux.ru> 1:3.1.7-alt1
- Update version to 3.1.7:
- Fixed a memory leak introduced in 3.1.6.
- Bug fixed with running a shell escape.
- Problem fixed with "ls -a" where occasionally a row with ".." and another file would be omitted. 
- Ncftpbatch now uses the UTC timezone for spool files.
- Recognize broken DG/UX servers and work around them.
- other fixes


* Mon Oct 20 2003 Ilya Mashkin <oddity@altlinux.ru> 1:3.1.6-alt3
- correct spec for current sisyphus requirement

* Wed Sep 24 2003 Ilya Mashkin <oddity@altlinux.ru> 1:3.1.6-alt2
- Spec cleanup

* Thu Sep 04 2003 Ilya Mashkin <oddity@altlinux.ru> 1:3.1.6-alt1
- update version
- fixed problem where high ASCII characters at prompt could it to exit
- many other fixes

* Tue Jul 01 2003 Ilya Mashkin <oddity@altlinux.ru> 1:3.1.5-alt2
- clean build (without patches)

* Fri Nov 22 2002 Rider <rider@altlinux.ru> 1:3.1.5-alt1
- new version (3.1.5)
- fixed specfile bugs
- Russian summary and description

* Wed Sep 25 2002 Rider <rider@altlinux.ru> 1:3.1.4-alt2
- rebuild (gcc 3.2)

* Sat Aug 24 2002 Rider <rider@altlinux.ru> 1:3.1.4-alt1
- 3.1.4

* Sat Jun 01 2002 Rider <rider@altlinux.ru> 1:3.1.3-alt1
- 3.1.3

* Sun Feb 24 2002 Rider <rider@altlinux.ru> 3.1.2-alt1
- 3.1.2

* Sun Feb 10 2002 Rider <rider@altlinux.ru> 3.1.1-alt1
- 3.1.1

* Thu Apr 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.0.3-alt1
- 3.0.3

* Tue Jan 30 2001 Dmitry V. Levin <ldv@fandra.org> 3.0.2-ipl3mdk
- Fixed icon locations.

* Sun Jan 21 2001 Dmitry V. Levin <ldv@fandra.org> 3.0.2-ipl2mdk
- RE adaptions.

* Wed Dec 20 2000 Yves Duret <yduret@mandrakesoft.com> 3.0.2-2mdk
- use %make macro
- fixed some file's permission
- fixed menu entry
- added a large icon

* Thu Oct 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0.2-1mdk
- 3.0.2.

* Fri Sep 29 2000 Daouda Lo <daouda@mandrakesoft.com> 3.0.1-8mdk
- icons should be tranparents.

* Fri Sep 29 2000 Daouda Lo <daouda@mandrakesoft.com> 3.0.1-7mdk
- add icons

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.0.1-6mdk
- automatically added BuildRequires

* Mon Jul 17 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.0.1-4mdk
- use new macros in post and postun scripts

* Thu Jul 06 2000 Christian Zoffoli <czoffoli@linux-mandrake.com> 3.0.1-3mdk.ipv6
- IPv6 support

* Sun Jun 04 2000 David BAUDENS <baudens@mandrakesoft.com> 3.0.1-3mdk
- Fix and use a real %%doc

* Wed Apr  5 2000 Denis Havlik <denis@mandrakesoft.com> 3.0.1-2mdk
- fixed source path

* Mon Apr  3 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0.1-1mdk
- Add menu.
- Change license to Artistic.
- spec-helper purification.
- Upgrade groups.
- 3.0.1 final (correct a lot of bugs).

* Fri Jan  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0beta21-4mdk
- sed 's/1/True/'

* Wed Jan  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0beta21-3mdk
- Oxygen Release.
- Disble confirmation in exit by default.
