Name: alt-docs-genextras
Version: 0.3
Release: alt5
Group: Books/Other
Packager: Kirill Maslinsky <kirill@altlinux.org>

Source0: %name.tar.bz2

License: GPL
BuildArch: noarch
Url: http://docs.altlinux.ru
Requires: mktemp

Summary: Script to generate ALT Linux Documentation Issues index
Summary(ru_RU.KOI8-R): Скрипт для обновления списка установленных выпусков документации

%description
Script to generate ALT Linux installed Documentation issues index. 
It should be called automatically in postinstall 
and postuninstall scripts of the documentation packages (docs-issue-*) 
so that user shouldn't worry (and even know) about this script.

%description -l ru_RU.KOI8-R
Скрипт для обновления списка установленных выпусков 
документации ALT Linux. Он должен вызываться автоматически после
установки и удаления каждого пакета выпуска документации
(docs-issue-*), так что пользователь не должен беспокоиться 
(и даже знать) об этом скрипте.

%prep
%setup -q -n %name-%version

%install
%__mkdir_p %buildroot%_bindir
%__mv %_builddir/%name-%version/alt-docs-genextras %buildroot%_bindir/

%files
%_bindir/alt-docs-genextras
%doc AUTHORS README.ru.txt README.first TODO

%changelog
* Thu Apr 17 2008 Kirill Maslinsky <kirill@altlinux.org> 0.3-alt5
- bugfix (#12466, #13742)
- usability: issue absracts separated visually with <HR> (azol@)

* Fri Sep 29 2006 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt4
- spec:
  + added dependency on mktemp (fixes #9786)
  + added Packager tag
- docs:
  + obsolete stuff removed
  + relevant description added
  + links to actual project page and related packages added

* Tue Oct 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt3
- upcoming www documentation:
	+ alternatives removed 
	+ now creating relative links for index.html instead of absolute ones
- all extras stuff removed (now extras considered just normal documentation modules)

* Sat Jun 26 2004 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt2
- Removed dependencies on alt-docs-extra and alt-docs-distrib
- Changed mode for alt-docs-genextras from 700 to 722

* Fri Jun 25 2004 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt1
- Typos and style corrected at the index page
- Added dependency on alt-docs-distrib

* Sat Jun 05 2004 Kirill Maslinsky <kirill@altlinux.ru> 0.2-alt1
- ATTENTION: syntax changed for alt-docs-extras-* packages
- All package-related information merged in one docfile
- Added possibility to classify documentation in several sections
- Added detailed README describing syntax and usage

* Thu May 13 2004 Kirill Maslinsky <kirill@altlinux.ru> 0.1-alt1
- initial working release 

* Wed May 12 2004 Kirill Maslinsky <kirill@altlinux.ru> 0.1-pre4
- correctly working script

* Tue May 11 2004 Kirill Maslinsky <kirill@altlinux.ru> 0.1-pre3
- removed sed options uncompatible with sed 3.02

* Tue May 11 2004 Kirill Maslinsky <kirill@altlinux.ru> 0.1-pre2
- corrected build errors

* Tue May 11 2004 Kirill Maslinsky <kirill@altlinux.ru> 0.1-pre1
- initial release



