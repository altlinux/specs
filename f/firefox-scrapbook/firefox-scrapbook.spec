%define rname	scrapbook
%define cid	\{53A03D43-5363-4669-8190-99061B2DEBA5\}
%define ciddir 	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	1.4.9
Release:	alt1
Summary:	Firefox extension, which helps you to save Web pages and manage the collection

License:	MPL 1.1/GPL 2.0 or later/LGPL 2.1 or later
Group:		Networking/WWW
URL:		http://sessionmanager.mozdev.org/
#URL:		http://amb.vis.ne.jp/mozilla/scrapbook/

Source0:	scrapbook-%version-fx.xpi.zip

BuildArch:	noarch

# Automatically added by buildreq on Tue Dec 02 2008 (-bi)
BuildRequires(pre): rpm-build-firefox
BuildRequires: unzip

%description 
ScrapBook is a Firefox extension, which helps you to save Web pages and manage
the collection. Key features are lightness, speed, accuracy and multi-language
support. Major features are:
  *  Save Web page
  * Save snippet of Web page
  * Save Web site (In-depth Capture)
  * Organize the collection in the same way as Bookmarks
  * Highlighter, Eraser and various page editing features
  * Full text search and quick filtering search
  * Text edit feature resembling Opera's Notes

%prep
%setup -c

%install
install -d %buildroot/%ciddir
cp -r * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%doc LICENSE.txt
%ciddir

%changelog
* Sun Feb 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.9-alt1
- Version 1.4.9

* Wed Oct 19 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.8-alt2
- Rebuild for Firefox 7.0

* Tue Aug 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.8-alt1
- Version 1.4.8

* Thu Aug 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.7-alt1
- Version 1.4.7

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.7-alt1
- Version 1.3.7

* Wed Jan 27 2010 Alexey Gladkov <legion@altlinux.ru> 1.3.6-alt1
- Version 1.3.6

* Fri Oct 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.5-alt1
- Version 1.3.5

* Mon Jul 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.3.12-alt1
- Version 1.3.3.12

* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 1.3.3.9-alt2
- fix for firefox 3.1

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.3.3.9-alt1
- 1.3.3.7 -> 1.3.3.9
- cleanup Buildrequires

* Sun Nov 16 2008 Igor Zubkov <icesik@altlinux.org> 1.3.3.7-alt2
- fix build with fresh rpm
- buildreq

* Fri Jul 04 2008 Igor Zubkov <icesik@altlinux.org> 1.3.3.7-alt1
- 1.3.3.5 -> 1.3.3.7

* Fri Jun 13 2008 Igor Zubkov <icesik@altlinux.org> 1.3.3.5-alt1
- 1.3.3.4 -> 1.3.3.5

* Sun May 18 2008 Igor Zubkov <icesik@altlinux.org> 1.3.3.4-alt1
- 1.3.3.3 -> 1.3.3.4

* Thu May 08 2008 Igor Zubkov <icesik@altlinux.org> 1.3.3.3-alt1
- 1.3.3.2 -> 1.3.3.3

* Tue Apr 15 2008 Igor Zubkov <icesik@altlinux.org> 1.3.3.2-alt1
- 1.3.3.1 -> 1.3.3.2

* Mon Mar 17 2008 Igor Zubkov <icesik@altlinux.org> 1.3.3.1-alt1
- 1.3.3 -> 1.3.3.1

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 1.3.3-alt1
- 1.3.2.5 -> 1.3.3

* Wed Jan 16 2008 Igor Zubkov <icesik@altlinux.org> 1.3.2.5-alt1
- 1.3.1 -> 1.3.2.5

* Tue Nov 27 2007 Igor Zubkov <icesik@altlinux.org> 1.3.1-alt1
- 1.2.0.8 -> 1.3.1

* Thu Sep 27 2007 Igor Zubkov <icesik@altlinux.org> 1.2.0.8-alt2
- rebuild

* Mon Aug 06 2007 Igor Zubkov <icesik@altlinux.org> 1.2.0.8-alt1
- build for Sisyphus

