%define rname	adblock_plus
%define version 2.0.3
%define release alt1
%define cid 	\{d10d0bf8-f5b5-c8b4-a8b2-2b9879e08c5d\}
%define ciddir	%firefox_noarch_extensionsdir/%cid


Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:	Adblock Plus - Firefox Extension

License:	GPL
Group:		Networking/WWW
URL:		http://adblockplus.mozdev.org/

Source0:	http://releases.mozilla.org/pub/mozilla.org/extensions/adblock_plus/%{rname}-%{version}-sm+tb+fn+fx.xpi

BuildArch:	noarch

BuildRequires(pre): rpm-build-firefox unzip

Packager: 	Andrey Cherepanov <cas@altlinux.org>

%description 	
Ever been annoyed by all those ads and banners on the internet that
often take longer to download than everything else on the page? Install
Adblock Plus now and get rid of them.

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
* Tue Jan 24 2012 Andrey Cherepanov <cas@altlinux.org> 2.0.3-alt1
- Version 2.0.3

* Fri Dec 09 2011 Andrey Cherepanov <cas@altlinux.org> 1.3.10-alt0.M60P.1
- Build for Firefox 8.0

* Tue Aug 02 2011 Alexey Gladkov <legion@altlinux.ru> 1.3.9-alt1
- Version 1.3.9.

* Mon Apr 18 2011 L.A. Kostis <lakostis@altlinux.ru> 1.3.6-alt1
- Update to 1.3.6 (now works with fx4).

* Wed Aug 18 2010 L.A. Kostis <lakostis@altlinux.ru> 1.2.2-alt1
- Version 1.2.2.

* Mon Jan 25 2010 L.A. Kostis <lakostis@altlinux.ru> 1.1.3-alt1
- Version 1.1.3.

* Fri Apr 24 2009 L.A. Kostis <lakostis@altlinux.ru> 1.0.2-alt1
- Version 1.0.2.

* Tue Feb 10 2009 L.A. Kostis <lakostis@altlinux.ru> 1.0.1-alt1
- Version 1.0.1.

* Sat Dec 06 2008 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt1
- Version 1.0.

* Thu Jul 10 2008 L.A. Kostis <lakostis@altlinux.ru> 0.7.5.5-alt1
- Version 0.7.5.5.

* Sat May 24 2008 L.A. Kostis <lakostis@altlinux.ru> 0.7.5.4-alt1
- Version 0.7.5.4.

* Fri Nov 09 2007 L.A. Kostis <lakostis@altlinux.ru> 0.7.5.3-alt1
- Version 0.7.5.3.

* Wed Mar 14 2007 L.A. Kostis <lakostis@altlinux.ru> 0.7.2.4-alt1
- Version 0.7.2.4.

* Sun Nov 26 2006 L.A. Kostis <lakostis@altlinux.ru> 0.7.2.2-alt2
- set noarch.
- remove obsoleted macros.

* Sun Nov 26 2006 L.A. Kostis <lakostis@altlinux.ru> 0.7.2.2-alt1
- Version 0.7.2.2 (now works with fx 2.0).

* Wed Sep 27 2006 L.A. Kostis <lakostis@altlinux.ru> 0.7.1.2-alt1.1
- rebuild for Firefox 1.5.0.7.

* Mon Sep 04 2006 L.A. Kostis <lakostis@altlinux.ru> 0.7.1.2-alt1
- Version 0.7.1.2.

* Thu Aug 10 2006 L.A. Kostis <lakostis@altlinux.ru> 0.7.1.1-alt1.1
- rebuild for Firefox 1.5.0.6.

* Wed Aug 02 2006 L.A. Kostis <lakostis@altlinux.ru> 0.7.1.1-alt1
- Version 0.7.1.1.

* Sun Jun 19 2006 LAKostis <lakostis at altlinux.ru> 0.7.0.2-alt1
- 0.7.0.2 release.
- prepare .spec for gear.

* Tue Jun 06 2006 LAKostis <lakostis at altlinux.ru> 0.7.0.1-alt1
- 0.7.0.1 release.
- remove all black magick with .manifest files.

* Sat May 20 2006 LAKostis <lakostis at altlinux.ru> 0.7-alt1
- 0.7 release.

* Mon Feb 13 2006 LAKostis <lakostis at altlinux.ru> 0.6.1.1-alt1
- Initial build for ALTLinux.

