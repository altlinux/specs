%define cid	langpack-ru@firefox.mozilla.org
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		firefox-ru
Version:	12.0
Release:	alt1
Summary:	Russian (RU) Language Pack for Firefox

License:	MPL/GPL/LGPL
Group:		Networking/WWW
URL:		http://www.mozilla-russia.org/products/firefox/
Packager:	Alexey Gladkov <legion@altlinux.ru>
BuildArch:	noarch

Source0:	ru-%version.xpi

Requires:	firefox >= %version
Requires:	hunspell-ru
Obsoletes:	firefox-ru_yo-dictionary firefox-ru_ie-dictionary
Provides:	firefox-ru_yo-dictionary firefox-ru_ie-dictionary

BuildRequires(pre):	rpm-build-firefox
BuildRequires:		unzip

%description
The Mozilla Firefox Russian translation.

%prep
%setup -c -n %name-%version/%cid

%install
cd ..

%__mkdir_p %buildroot/%ciddir/dictionaries

%__cp -r %cid/* %buildroot/%ciddir
ln -s %_datadir/myspell/ru_RU.aff %buildroot/%ciddir/dictionaries/ru.aff
ln -s %_datadir/myspell/ru_RU.dic %buildroot/%ciddir/dictionaries/ru.dic

#sed -r -i \
#    -e 's,<em:maxVersion>4.0</em:maxVersion>,<em:maxVersion>4.*</em:maxVersion>,g' \
#    -e 's,<em:minVersion>4.0</em:minVersion>,<em:minVersion>4.0</em:minVersion>,g' \
#    %buildroot/%ciddir/install.rdf

%files
%ciddir

%changelog
* Tue May 08 2012 Alexey Gladkov <legion@altlinux.ru> 12.0-alt1
- New version (12.0)

* Tue Apr 24 2012 Alexey Gladkov <legion@altlinux.ru> 11.0-alt1
- New version (11.0)

* Sun Feb 26 2012 Alexey Gladkov <legion@altlinux.ru> 10.0.2-alt1
- New version (10.0.2)

* Mon Jan 09 2012 Alexey Gladkov <legion@altlinux.ru> 9.0.1-alt1
- New version (9.0.1)

* Tue Nov 22 2011 Alexey Gladkov <legion@altlinux.ru> 8.0-alt1
- New version (8.0)

* Wed Oct 12 2011 Alexey Gladkov <legion@altlinux.ru> 7.0.1-alt1
- New version (7.0.1)

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 6.0.2-alt1
- New version (6.0.2)

* Fri Aug 26 2011 Alexey Gladkov <legion@altlinux.ru> 6.0-alt1
- New version (6.0)

* Mon Aug 01 2011 Alexey Gladkov <legion@altlinux.ru> 5.0.1-alt1
- New version (5.0.1)

* Mon May 02 2011 Alexey Gladkov <legion@altlinux.ru> 4.0.1-alt1
- New version (4.0.1)

* Sun Apr 03 2011 Alexey Gladkov <legion@altlinux.ru> 4.0-alt1
- New version (4.0)

* Sun Jan 24 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.0-alt1
- New version (3.6.0)

* Tue Sep 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.2-alt1
- New version (3.5.2)

* Fri Jul 17 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.1-alt1
- New version (3.5.1)

* Thu Jul 02 2009 Alexey Gladkov <legion@altlinux.ru> 3.5-alt2
- Update translation for final release (3.5).

* Thu Jun 04 2009 Alexey Gladkov <legion@altlinux.ru> 3.5-alt1
- New version (3.5)

* Tue Mar 17 2009 Alexey Gladkov <legion@altlinux.ru> 3.1-alt2
- Fix max/min version in install.rdf.

* Mon Jan 26 2009 Alexey Gladkov <legion@altlinux.ru> 3.1-alt1
- New version (3.1-alt1)

* Wed Jul 16 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt2
- Bugfix version.
- Use dictionaries from hunspell-ru.

* Mon Jul 07 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1
- New version (3.0-alt1)
- Add dictionary extension.

* Mon Jun 25 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.4-alt1
- new version (2.0.0.4-alt1)

* Wed Mar 14 2007 Alexey Gladkov <legion@altlinux.ru> 2.0-alt3
- Fix archive packaging bug.

* Sat Mar 10 2007 Alexey Gladkov <legion@altlinux.ru> 2.0-alt2
- rebuild with firefox-2.0.0.2

* Wed Nov 22 2006 Alexey Gladkov <legion@altlinux.ru> 2.0-alt1
- new version (2.0-alt1)

* Mon Sep 18 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.7-alt1
- new version (1.5.0.7-alt1)

* Fri Aug 11 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.6-alt1
- new version (1.5.0.6-alt1)

* Thu Jun 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.4-alt1
- rebuild with firefox 1.5.0.4

* Mon May 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.3-alt1
- new version
- rebuild with firefox 1.5.0.3

* Mon Feb 20 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.1-alt1
- new version

* Mon Dec 19 2005 Alexey Gladkov <legion@altlinux.ru> 1.5-alt1
- new version

* Fri Aug 26 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt3
- firefox after firefox-ru installation will be switched to ru_RU.
- postun script bugfix.

* Tue Aug 16 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt2
- bugfix rebuild.

* Mon Aug 08 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt1
- new version;

* Tue Jun 21 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt1
- rebuild with new firefox.

* Wed Apr 27 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.3-alt1
- new version;

* Sat Mar 05 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.1-alt1.1
- postscript bugfix;

* Wed Mar 02 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.1-alt1
- new version;

* Fri Jan 19 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt2
- rebuild with new firefox.
- Requires to firefox package was relaxed.

* Fri Jan 07 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- new version;
- new extension scheme;

* Mon Jul 05 2004 Alexey Gladkov <legion@altlinux.ru> 0.9.2-alt1
- New version;
- New build scheme.

* Thu Mar 11 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt1
- New build scheme;
- New version.

* Mon Nov 24 2003 Alexey Gladkov <legion@altlinux.ru> 0.7-alt2
- First build for ALT Linux.
