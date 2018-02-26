# SPEC file for Simple Calc extension

%define rname	quicknote
%define version 0.6.0.10
%define release alt3
%define cid 	\{C0CB8BA3-6C1B-47e8-A6AB-1FAB889562D9\}
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:	QuickNote plugin for Firefox
Summary(ru_RU.UTF-8): расширение QuickNote для Firefox

License:	%mpl 1.1 / %gpl2plus
Group:		Networking/WWW
URL:		http://quicknote.mozdev.org
#URL:		https://addons.mozilla.org/en-US/firefox/addon/quicknote/
BuildArch:	noarch

Packager:       Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	%{rname}-%version-fx+tb.xpi

BuildRequires(pre): rpm-build-firefox rpm-build-licenses
BuildRequires:  unzip

%description
QuickNote is a Mozilla/Firefox/Thunderbird extension
for quick note taking.

%description -l ru_RU.UTF-8
QuickNote - расширение для Mozilla/Firefox/Thunderbird,
позволяющее быстро делать короткие заметки.

%prep
%setup -c

%install
mkdir -p -- %buildroot/%ciddir
cp -r -- * %buildroot/%ciddir
subst 's,<em:maxVersion>5\.\*</em:maxVersion>,<em:maxVersion>7\.\*</em:maxVersion>,g' %buildroot/%ciddir/install.rdf

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Thu Oct 20 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.10-alt3
- Rebuild with Firefox 7.0

* Wed Aug 24 2011 Andrey Cherepanov <cas@altlinux.org> 0.6.0.10-alt2
- Rebuild with Firefox 6.0

* Sat Aug 13 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.10-alt1
- Rebuild for Firefox 5.0
- New version

* Sun Apr 17 2011 Alexey Gladkov <legion@altlinux.ru> 0.6.0.8-alt1
- New version (0.6.0.8).

* Wed Jan 27 2010 Alexey Gladkov <legion@altlinux.ru> 0.6.0.5-alt1
- New version (0.6.0.5).

* Thu Jun 04 2009 Alexey Gladkov <legion@altlinux.ru> 0.6.0.4-alt3
- Rebuild for Firefox 3.5

* Sun Mar 15 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.4-alt2
- Rebuild for Firefox 3.1

* Fri Jul 11 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.4-alt1
- New version

* Thu Jul 10 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.3-alt9
- Rebuild for Firefox 3.0

* Sat Dec 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.3-alt8
- Rebuild for Firefox 2.0.0.11

* Fri Nov 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.3-alt7
- Rebuild for Firefox 2.0.0.9

* Fri Oct 26 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.3-alt6
- Rebuild for Firefox 2.0.0.8

* Fri Aug 03 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.3-alt5
- Rebuild for Firefox 2.0.0.6

* Sat Jul 21 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.3-alt4
- Rebuild for Firefox 2.0.0.5

* Thu Jul 05 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.3-alt3
- Rebuild for Firefox 2.0.0.4

* Wed Mar 14 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.3-alt2
- Rebuild for Firefox 2.0.0.2

* Mon Dec 04 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.3-alt1
- New version
- Rebuild for Firefox 2.0
  - removes obsolete macros
  - replace 'set_firefox_noarch' macro with 'BuildArch' tag

* Sun Sep 24 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.2-alt4
- Rebuild for Firefox 1.5.0.7

* Wed Aug 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.2-alt3
- Rebuild for Firefox 1.5.0.6

* Sun Jul 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.2-alt2
- Fix for #9803, adding chrome.manifest

* Thu Jun 15 2006 Alexey Gladkov <legion@altlinux.ru> 0.6.0.2-alt1.1.1
- NMU: rebuild with firefox 1.5.0.4

* Mon May 15 2006 Alexey Gladkov <legion@altlinux.ru> 0.6.0.2-alt1.1
- NMU: rebuild with firefox 1.5.0.3

* Mon Feb 20 2006 Alexey Gladkov <legion@altlinux.ru> 0.6.0.2-alt1
- NMU
- new version
- rebuild with firefox 1.5.0.1

* Tue Dec 20 2005 Alexey Gladkov <legion@altlinux.ru> 0.6.0-alt1.1
- rebuild with firefox-1.5
- spec changes:
  * BuildRequires fix;
  * ghost file added;
  * new macros was used to fix multiarch problem.

* Sun Nov 20 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0-alt1
- First build for ALT Linux

* Tue Sep 6 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0-alt0
- Initial build
