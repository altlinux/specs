%define cid 	firebug@software.joehewitt.com
%define ciddir	%firefox_noarch_extensionsdir/%cid

Serial: 1

Name:		firefox-firebug
Version:	1.8.3
Release:	alt1

Summary:	Powerful debugger for JavaScript and HTML

License:	GPL
Group:		Development/Debuggers
URL:		http://www.getfirebug.com/

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	firebug-%version.xpi

BuildArch:	noarch

BuildRequires(pre):	rpm-build-firefox unzip

%description 	
FireBug is a new tool that aids with debugging Javascript, DHTML, and Ajax. It
is like a combination of the Javascript Console, DOM Inspector, and a command
line Javascript interpreter.

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
* Thu Oct 27 2011 Mykola Grechukh <gns@altlinux.ru> 1:1.8.3-alt1
- 1.8.3 version

* Wed Aug 24 2011 Andrey Cherepanov <cas@altlinux.org> 1:1.8.1-alt1
- 1.8.1 version.

* Mon Aug 01 2011 Alexey Gladkov <legion@altlinux.ru> 1:1.8.0-alt1
- 1.8.0 version.

* Thu Apr 07 2011 Alexey Gladkov <legion@altlinux.ru> 1:1.7.0-alt1
- 1.7.0 version.

* Sun Jan 24 2010 Alexey Gladkov <legion@altlinux.ru> 1:1.5.0-alt1
- 1.5.0 version.

* Fri Jun 05 2009 Alexey Gladkov <legion@altlinux.ru> 1:1.4.0-alt1.a31
- 1.4.0 alpha31 version.

* Tue Mar 10 2009 Alexey Gladkov <legion@altlinux.ru> 1:1.4.0-alt1.a12
- Update specfile.

* Tue Feb 10 2009 L.A. Kostis <lakostis@altlinux.ru> 1:1.4.0-alt0.a12
- 1.4.0 alpha12 version.

* Thu Sep 25 2008 L.A. Kostis <lakostis@altlinux.ru> 1:1.2.1-alt1
- 1.2.1 version.

* Fri Aug 08 2008 L.A. Kostis <lakostis@altlinux.ru> 1:1.2.0-alt1.b7
- 1.2.0b7 version.
- ready for Firefox 3.0.

* Fri Nov 09 2007 L.A. Kostis <lakostis@altlinux.ru> 1:1.0.5-alt1
- 1.0.5 release.

* Wed Mar 14 2007 L.A. Kostis <lakostis@altlinux.ru> 1:1.0.1-alt1
- 1.0.1 release.

* Sun Jan 28 2007 L.A. Kostis <lakostis@altlinux.ru> 1.0rel-alt1
- 1.0 release.

* Thu Dec 14 2006 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt1.b5
- 1.0beta5 version.

* Wed Dec 06 2006 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt1.b2
- New 1.0beta2 version.

* Sun Nov 26 2006 L.A. Kostis <lakostis@altlinux.ru> 0.4.1-alt1
- 0.4.1 version.
- cleanup obsoleted macros.
- set noarch explicitly.

* Wed Sep 27 2006 L.A. Kostis <lakostis@altlinux.ru> 0.4-alt1.1.1.1
- rebuild for Firefox 1.5.0.7.

* Thu Aug 10 2006 L.A. Kostis <lakostis@altlinux.ru> 0.4-alt1.1.1
- rebuild for Firefox 1.5.0.6.

* Thu Jun 15 2006 Alexey Gladkov <legion@altlinux.ru> 0.4-alt1.1
- NMU: rebuild with firefox 1.5.0.4

* Tue Jun 06 2006 LAKostis <lakostis at altlinux.ru> 0.4-alt1
- 0.4 version.

* Mon May 15 2006 Alexey Gladkov <legion@altlinux.ru> 0.3.2-alt1
- NMU: new version, rebuild with firefox 1.5.0.3

* Sat Mar 18 2006 LAKostis <lakostis at altlinux.ru> 0.2.3-alt1
- Initial build for ALTLinux.

