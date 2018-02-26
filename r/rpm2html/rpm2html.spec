Name: rpm2html
Version: 1.9.7
Release: alt1.2

Summary: Translates an RPM database and dependency information into HTML
License: W3C Copyright (BSD like).
Group: Text tools
Packager: Eugeny A. Rostovtsev (REAL) <real@altlinux.org>

Url: http://rufus.w3.org/linux/rpm2html/
Source0: http://ftp.twaren.net/Unix/NonGNU/rpm2html/rpm2html-1.9.7.tar.gz
Source1: %name-README.ALT
Patch4: rpm2html-1.9.7-alt-rpmts.patch

# Automatically added by buildreq on Mon Jan 05 2009
BuildRequires: bzlib-devel libdb4.7-devel librpm-devel libxml2-devel
BuildPreReq: zlib-devel

%description
The rpm2html utility automatically generates web pages that describe a
set of RPM packages.  The goals of rpm2html are to identify the
dependencies between various packages, and to find the package(s) that
will provide the resources needed to install a given package.  Rpm2html
analyzes the provides and requires of the given set of RPMs, and then
shows the dependency cross-references using hypertext links.  Rpm2html
can now dump the metadata associated with RPM files into standard RDF
files.

%prep
%setup
%patch4 -p0

%add_findreq_skiplist %_datadir/%name

%build
%autoreconf
%configure
%make_build

%install
mkdir -pv %buildroot/var/www/html/rpm2html/local
install -d %buildroot%_datadir/%name
install -pD -m755 %name %buildroot%_bindir/%name
install -pD -m644 %name.config  %buildroot%_sysconfdir/%name.config
install -pD -m644 %name.1  %buildroot%_man1dir/%name.1
install -p -m644 %SOURCE1 README.ALT-ru_RU.KOI8-R
subst 's@url\=\/rpm2html@url=/var/www/html/rpm2html@g' \
	%buildroot/etc/rpm2html.config

%files
%doc CHANGES BUGS Copyright INSTALL PRINCIPLES README* TODO
%doc rpm2html-cdrom.config rpm2html-en.config
%config %_sysconfdir/%name.config
%_datadir/%name
%_man1dir/*
%_bindir/%name
/var/www/html/rpm2html

%changelog
* Sat Mar 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.7-alt1.2
- Fixed build

* Mon Jan 05 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 1.9.7-alt1.1
- Correct spec file for shared libraries, update BuildRequires and
  Packager, remove unused comments

* Thu Jan 01 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 1.9.7-alt1
- Get up from orphaned; new version

* Sat Feb 26 2005 Michael Shigorin <mike@altlinux.ru> 1.8.2-alt2
- removed stale libdb4.2 build dependency

* Wed Mar 10 2004 Michael Shigorin <mike@altlinux.ru> 1.8.2-alt1
- 1.8.2
- applied patch from Evgeniy Kobzev <evgenik diamonds ru>
  (MySQL and some other fixes/improvements), see README.ALT
- updated patch0
- build deps updated
- fixed %files

* Thu Sep 25 2003 Michael Shigorin <mike@altlinux.ru> 1.8.1-alt1
- updated buildrequires
- spec cleanup

* Wed Jul 30 2003 Michael Shigorin <mike@altlinux.ru> 1.8.1-alt0.2
- patched around silly 20-byte limit on version string length
  (who knows if it's limited now anyway?)

* Fri Apr 25 2003 Michael Shigorin <mike@altlinux.ru> 1.8.1-alt0.1
- built for ALT Linux

* Mon Dec 09 2002 Ricardo Erbano <erbano@conectiva.com>
+ 2002-12-09 11:07:01 (20276)
- Fixed build problems with new automake 1.7, (call aclocal and automake), closes: #7150
- BuildRequires to db3-devel

* Tue Nov 19 2002 Ademar de Souza Reis Jr. <ademar@conectiva.com.br>
+ 2002-11-19 14:40:36 (19324)
- I don't have to buildrequire libxml2-devel twice :-)

* Tue Nov 19 2002 Ademar de Souza Reis Jr. <ademar@conectiva.com.br>
+ 2002-11-19 14:36:54 (19323)
- Added build requirements

* Tue Nov 19 2002 Mapi2 <distro@conectiva.com.br>
+ 2002-11-19 14:09:25 (19322)
- Copying release 1.8.1-1cl to releases/ directory.
- Copying release 1.8.1-1cl to pristine/ directory.
- Removing previous pristine/ directory.
- Created directory for version 1.8.1.

* Tue Nov 19 2002 Ademar de Souza Reis Jr. <ademar@conectiva.com.br>
+ 2002-11-19 12:46:09 (19318)
- New upstream release: 1.8.1
- Removed obsolete patches
- Added a compilation patch (rpmts.h doesn't exist in CL, and since it
  compiles fine without it, I just commented out the include line...
  I hope it works :)
- Minor spec cleanup
- Removed old changelog entries

* Tue Sep 03 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-09-03 16:05:21 (13467)
- Copying release 1.7-3cl to releases/ directory.

* Tue Sep 03 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-09-03 16:05:20 (13466)
- Copying release 1.7-3cl to pristine/ directory.

* Tue Sep 03 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-09-03 16:05:19 (13465)
- Removing previous pristine/ directory.

* Tue Sep 03 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-09-03 16:05:17 (13464)
- Imported package from snapshot.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 19:01:32 (9666)
- Copying release 1.7-2cl to releases/ directory.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 19:01:31 (9665)
- Copying release 1.7-2cl to pristine/ directory.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 19:01:30 (9664)
- Removing previous pristine/ directory.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 19:01:28 (9663)
- Imported package from 8.0.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 19:01:26 (9662)
- Created directory for version 1.7.

* Wed Aug 28 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-28 09:35:34 (2983)
- Imported package from 6.0.

* Wed Aug 28 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-28 09:35:28 (2982)
- Created package directory
