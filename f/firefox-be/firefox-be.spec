%define rname	be
%define cid	langpack-be@firefox.mozilla.org
%define ciddir 	%firefox_noarch_extensionsdir/%cid

Name:		firefox-be
Version:	13.0.1
Release:	alt1
Summary:	Belarusian (BE) Language Pack for Firefox

License:	GPL
Group:		Networking/WWW
URL:		http://mozilla-be.sourceforge.net

Source0:	%rname.xpi

Requires:	hunspell-%rname

BuildRequires(pre):	rpm-build-firefox
BuildRequires:		unzip

BuildArch: 		noarch

Packager:	Alexey Gladkov <legion@altlinux.ru>

%description
The Mozilla Firefox Belarusian translation.

%prep
%setup -c -n %name-%version/%cid

%install
cd ..
mkdir -p %buildroot/%ciddir/dictionaries
cp -r %cid/* %buildroot/%ciddir
ln -s %_datadir/myspell/be_BY.aff %buildroot/%ciddir/dictionaries/%rname.aff
ln -s %_datadir/myspell/be_BY.dic %buildroot/%ciddir/dictionaries/%rname.dic

%files
%ciddir

%changelog
* Tue Jul 10 2012 Alexey Gladkov <legion@altlinux.ru> 13.0.1-alt1
- New version (13.0.1).

* Tue May 08 2012 Alexey Gladkov <legion@altlinux.ru> 12.0-alt1
- New version (12.0).

* Wed Apr 25 2012 Alexey Gladkov <legion@altlinux.ru> 11.0-alt1
- New version (11.0).

* Sun Feb 26 2012 Alexey Gladkov <legion@altlinux.ru> 10.0.2-alt1
- New version (10.0.2).

* Wed Jan 18 2012 Alexey Gladkov <legion@altlinux.ru> 9.0.1-alt1
- New version (9.0.1).

* Mon Nov 21 2011 Alexey Gladkov <legion@altlinux.ru> 8.0-alt1
- New version (8.0).

* Wed Oct 12 2011 Alexey Gladkov <legion@altlinux.ru> 7.0.1-alt1
- New version (7.0.1).

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 6.0.2-alt1
- New version (6.0.2).

* Fri Aug 26 2011 Alexey Gladkov <legion@altlinux.ru> 6.0-alt1
- New version (6.0).

* Mon Aug 01 2011 Alexey Gladkov <legion@altlinux.ru> 5.0.1-alt1
- New version (5.0.1).

* Tue May 03 2011 Alexey Gladkov <legion@altlinux.ru> 4.0.1-alt1
- New version (4.0.1).

* Mon Apr 18 2011 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt2
- Remove bundled dictionary, use system hunspell.

* Mon Apr 18 2011 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt1.1
- fix typo in buildreq.

* Mon Apr 18 2011 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt1
- Rebuild for fx4. Consolidate translation with spellcheck dictionary
  like -ru version.

* Sun Mar 18 2007 L.A. Kostis <lakostis@altlinux.ru> 2.0-alt2
- fix extensions dir.
- use unzip instead internal rpm commands.

* Sun Nov 26 2006 L.A. Kostis <lakostis@altlinux.ru> 2.0-alt1
- new version for Firefox 2.0.
- remove obsoleted macros.

* Wed Sep 27 2006 L.A. Kostis <lakostis@altlinux.ru> 1.5.0.7-alt1
- rebuild for Firefox 1.5.0.7.

* Thu Aug 10 2006 L.A. Kostis <lakostis@altlinux.ru> 1.5.0.6-alt1
- rebuild for Firefox 1.5.0.6.
- prepare for gear.

* Thu Jun 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.4-alt1
- rebuild with firefox 1.5.0.4

* Mon May 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.3-alt1
- made from 20060312 translation snapshot.
- rebuild with firefox 1.5.0.3

* Sun Dec 25 2005 LAKostis <lakostis at altlinux.ru> 1.5-alt1
- made from 20051217 translation snapshot.
- rebuild with new firefox.
- update .spec for new build scheme.

* Thu Nov 10 2005 Konstantin A Lepikhov (L.A. Kostis) <lakostis@altlinux.ru> 1.0.7-alt1.5
- rebuild with new firefox.

* Thu Oct 13 2005 Konstantin A Lepikhov (L.A. Kostis) <lakostis@altlinux.ru> 1.0.7-alt1.4
- rebuild with new firefox.

* Fri Aug 26 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt1.3
- firefox after firefox-ru installation will be switched to be_BY.
- postun script bugfix.

* Tue Aug 16 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt1.1.2
- bugfix rebuild.

* Mon Aug 15 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt1.1.1
- Rebuild with new firefox.

* Tue Jul 12 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt1.1
- fix URL.

* Tue Jul 05 2005 Michael Shigorin <mike@altlinux.org> 1.0.5-alt1
- rebuilt for Sisyphus, lakostis' package

* Wed Jul 05 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt0
- made from 20050119 translation snapshot.
- First build for ALT Linux.
