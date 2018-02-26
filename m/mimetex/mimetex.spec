Name: mimetex
Version: 1.71
Release: alt1.rev20090617

Summary: Mimetex ets you easily embed LaTeX math in your html pages 
License: GPL
Group: Networking/Other

Url: http://www.forkosh.com/mimetex.html
Source0: %name-%version.tar.bz2
Packager: Vladimir A. Svyatoshenko <svyt@altlinux.ru>

#AutoReqProv: no
Requires: webserver-common 
BuildRequires: rpm-build-webserver-common
Conflicts: moodle-filter-mimetex

%define installdir %webserver_cgibindir

%description
  MimeTeX, licensed under the gpl, lets you easily embed LaTeX math in your html pages.  It parses 
a LaTeX math expression and immediately emits the corresponding gif image, rather than the usual 
TeX dvi. And mimeTeX is an entirely separate little program that doesn't use TeX or its fonts in 
any way. It's just one cgi that you put in your site's cgi-bin/ directory, with no other 
dependencies. So mimeTeX is very easy to install. And it's equally easy to use. Just place an 
html <img> tag in your document wherever you want to see the corresponding LaTeX expression.

%prep
%setup -q -n %name

%build
gcc -DAA mimetex.c gifsave.c -lm -o mimetex.cgi

%__rm *.c 
%__rm *.h 

%install
%__install -pD -m755 mimetex.cgi %buildroot%installdir/mimetex.cgi

%files
%installdir/mimetex.cgi
%doc COPYING README mimetex.html

%changelog
* Tue Jul 14 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.71-alt1.rev20090617
- new security update revision

* Fri Dec 12 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.70-alt1.1
- move webserver-common from BuildRequires to Requires

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.70-alt1
- new version

* Mon Sep 08 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.64-alt2
- add build requires on rpm-build-webserver-common

* Tue Jul 08 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.64-alt1
- first build for AltLinux

