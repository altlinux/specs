%define rname	spoofstick-firefox
%define version 1.06
%define release alt4
%define cid 	\{ebcf8b39-5cb1-4233-9edf-7d6533455b8d\}
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-spoofstick
Version:	%version
Release:	%release

Summary:	SpoofStick extension for Mozilla Firefox

License:	Freeware
Group:		Networking/WWW
URL:		http://www.spoofstick.com/firefox.html

Packager:	LAKostis <lakostis at altlinux.ru>
Source0:	%rname.xpi
Source1:	spoofstick-firefox-chrome.manifest

BuildArch: noarch

BuildRequires(pre):	rpm-build-firefox unzip
Requires:	%firefox_name >= 2.0

%description 	
SpoofStick makes it easier to spot a spoofed website by prominently displaying
only the most relevant domain information.  It's not a comprehensive solution,
but it's a good start.

%prep
%setup -c

%install
%__mkdir_p %buildroot/%ciddir
%__cp -r * %buildroot/%ciddir
%__subst 's@>1.6a2<@>2.0.0.*<@' %buildroot/%ciddir/install.rdf
%__cp -a -- %SOURCE1 %buildroot/%ciddir/chrome.manifest

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Sun Nov 26 2006 L.A. Kostis <lakostis@altlinux.ru> 1.06-alt4
- cleanup obsoleted macros.

* Sun Nov 26 2006 L.A. Kostis <lakostis@altlinux.ru> 1.06-alt3
- Rebuild for fx 2.0:
  + fix MaxVer requires (due stalled upstream);
  + simplify requires;
  + set buildarch to noarch.

* Wed Sep 27 2006 L.A. Kostis <lakostis@altlinux.ru> 1.06-alt2.1.1.1.1
- rebuild for Firefox 1.5.0.7.

* Thu Aug 10 2006 L.A. Kostis <lakostis@altlinux.ru> 1.06-alt2.1.1.1
- rebuild for Firefox 1.5.0.6.

* Thu Jun 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.06-alt2.1.1
- NMU: rebuild with firefox 1.5.0.4

* Mon May 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.06-alt2.1
- NMU: rebuild with firefox 1.5.0.3

* Mon Feb 20 2006 Alexey Gladkov <legion@altlinux.ru> 1.06-alt2
- NMU: rebuild with firefox 1.5.0.1

* Sat Dec 25 2005 LAKostis <lakostis at altlinux.ru> 1.06-alt1
- new version.
- rebuild with new packaging scheme.
- rebuild with new firefox.

* Mon Oct 10 2005 LAKostis <lakostis at altlinux.ru> 1.05-alt1
- Initial build for ALTLinux.

