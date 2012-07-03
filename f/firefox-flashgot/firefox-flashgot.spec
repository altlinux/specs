%define rname	flashgot
%define cid 	\{19503e42-ca3c-4c27-b1e2-9cdb2170ee34\}
%define ciddir  %firefox_noarch_extensionsdir/%cid

Summary:	FlashGot extensions for Firefox
Name:		%firefox_name-%rname
Version:	1.3.6
Release:	alt1
Source0:	https://secure.informaction.com/download/releases/%rname-%version.xpi
License:	GPLv2
Group:		Networking/WWW
URL:		http://flashgot.net
Packager:	Alexey Shabalin <shaba@altlinux.ru>

BuildArch:      noarch
BuildRequires(pre):     rpm-build-firefox
BuildRequires:  unzip

Conflicts: %firefox_name-fireget

%description
Enables Firefox, Mozilla Suite, Netscape and Thunderbird to handle single and
massive("all" and "selection") downloads using the most popular external download
managers for Windows, Mac OS X, Linux and FreeBSD(dozens currently supported,
see Extension's Home Page for details).
FlashGot offers also a Build Gallery functionality which helps to synthetize
full media galleries in one page, from serial contents originally scattered
on several pages, for easy and fast "download all".

%prep
%setup -c

%install
mkdir -p %buildroot/%ciddir
cp -r * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
    [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Tue Dec 20 2011 Mykola Grechukh <gns@altlinux.ru> 1.3.6-alt1
- new version

* Tue Aug 09 2011 Mykola Grechukh <gns@altlinux.ru> 1.3.0.5-alt1
- new version

* Thu Jan 27 2011 Alexey Shabalin <shaba@altlinux.ru> 1.2.8.1-alt1
- 1.2.8.1

* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Fri Aug 13 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.1.29-alt1
- 1.2.1.29

* Sun May 16 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.1.22-alt1
- 1.2.1.22

* Mon Mar 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.1.17-alt1
- 1.2.1.17

* Fri Jan 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.1.09-alt1
- 1.2.1.09

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 1.2.1.04-alt1
- 1.2.1.04

* Tue Oct 27 2009 Alexey Shabalin <shaba@altlinux.ru> 1.2.0.7-alt1
- initial build

