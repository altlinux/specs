# SPEC file for Hybridfox extension

%define rname	hybridfox
%define version 1.7.000119
%define release alt3
%define cid 	\{2204c510-88f3-11db-b606-0800200c9a66\}
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:	Amazon EC2 plugin for Firefox

License:	Apache License 2.0
Group:		Networking/WWW
URL:		http://code.google.com/p/hybridfox/
BuildArch:	noarch

Source0:	%rname-%version.xpi

BuildRequires(pre): rpm-build-firefox rpm-build-licenses
BuildRequires:  unzip

%description 	
Hybridfox is a Firefox add-on that attempts to get the best of both
worlds of popular Cloud Computing environments, Amazon EC2(public)
and Eucalyptus(private). The idea is to use one Hybridfox tool, to
switch seamlessly between Amazon and Eucalyptus accounts in order to
manage your "Cloud Computing" environment.

%prep
%setup -c

%install
mkdir -p -- %buildroot/%ciddir
cp -r -- * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Wed Jan 18 2012 Alexey Gladkov <legion@altlinux.ru> 1.7.000119-alt3
- Rebuilt with firefox-9.0.1.

* Fri Aug 26 2011 Mykola Grechukh <gns@altlinux.ru> 1.7.000119-alt2
- findreq fixed

* Wed Aug 24 2011 Andrey Cherepanov <cas@altlinux.org> 1.7.000119-alt1
- new version (1.7.000119).

* Thu Aug 04 2011 Alexey Gladkov <legion@altlinux.ru> 1.7.000089-alt1
- new version (1.7.000089).

* Wed May 11 2011 Mykola Grechukh <gns@altlinux.ru> 1.7.000057-alt1
- new version

* Tue Apr 19 2011 Mykola Grechukh <gns@altlinux.ru> 1.6.000041-alt1
- first build
