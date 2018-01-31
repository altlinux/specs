Name: bonito2-open
Version: 3.99.9
Release: alt1.corbama1

Summary: Bonito is a graphical user interface to corpora mantained by Manatee
License: LGPLv2+
Group: System/Libraries
Url: http://nlp.fi.muni.cz/trac/noske/wiki/Downloads
Packager: Kirill Maslinsky <kirill@altlinux.org>
BuildRequires: python-module-cheetah python-module-distribute time
ExclusiveArch: x86_64


Source: %name-%version.tar
Source100: bonito2.conf
Patch: %name-%version-%release.patch

%description
Bonito is a graphical user interface to corpora mantained by Manatee. It is
available as a standalone graphical application in Tcl/Tk (version Bonito1, not
developed/supported anymore) and web interface in Python (version Bonito2,
under constant development). 

%prep
%setup
%patch -p1

%build
#export 
autoreconf -fisv
%configure MANATEE_REGISTRY=%_localstatedir/manatee 
%make_build 

%install
%makeinstall_std
%find_lang ske
mkdir -p %buildroot/%_sysconfdir/httpd2/conf/sites-available
install %SOURCE100 %buildroot/%_sysconfdir/httpd2/conf/sites-available/bonito2.conf

%files -f ske.lang
%python_sitelibdir_noarch/bonito/
%_datadir/bonito/
%_bindir/*
%_sysconfdir/httpd2/conf/sites-available/bonito2.conf


%changelog
* Wed Jan 31 2018 Kirill Maslinsky <kirill@altlinux.org> 3.99.9-alt1.corbama1
- 3.99.9

* Mon Mar 13 2017 Kirill Maslinsky <kirill@altlinux.org> 3.88.9-alt1.corbama3
- N'Ko added to the interface translation switch

* Fri Mar 03 2017 Kirill Maslinsky <kirill@altlinux.org> 3.88.9-alt1.corbama2
- N'Ko translation updated

* Wed Oct 19 2016 Kirill Maslinsky <kirill@altlinux.org> 3.88.9-alt1.corbama1
- Verson up: 3.88.9
- build exclusively on x86_64 due to discontinued support of 
  manatee-open on i586.

* Sat Sep 17 2016 Kirill Maslinsky <kirill@altlinux.org> 3.80.5-alt1.corbama5
- Fix bug in concordance save template

* Sat Jul 16 2016 Kirill Maslinsky <kirill@altlinux.org> 3.80.5-alt1.corbama4
- More adaptive right-to-left handling
- N'Ko translation of the interface; French translation updated

* Tue Mar 29 2016 Kirill Maslinsky <kirill@altlinux.org> 3.80.5-alt1.corbama3
- Fix right-to-left rendering

* Sun Dec 06 2015 Kirill Maslinsky <kirill@altlinux.org> 3.80.5-alt1.corbama2
- reintroduce French interface language

* Sun Dec 06 2015 Kirill Maslinsky <kirill@altlinux.org> 3.80.5-alt1.corbama1
- update to upstream version 3.80.5

* Sat Dec 05 2015 Kirill Maslinsky <kirill@altlinux.org> 3.80.5-alt1
- 3.80.5

* Wed Mar 18 2015 Kirill Maslinsky <kirill@altlinux.org> 3.48.9-alt1.corbama1
- update to upstream version 3.48.9

* Wed Mar 18 2015 Kirill Maslinsky <kirill@altlinux.org> 3.48.9-alt1
- 3.48.9

* Fri Oct 04 2013 Kirill Maslinsky <kirill@altlinux.org> 2.91.13-alt1.corbama2.1
- show concordance in IGT-like format:
  each annotation level is on a separate line

* Fri Oct 04 2013 Kirill Maslinsky <kirill@altlinux.org> 2.91.13-alt1.corbama2
- revert obsolete patches
- include locale files
- build as noarch

* Wed Oct 02 2013 Kirill Maslinsky <kirill@altlinux.org> 2.91.13-alt1.corbama1
- version up

* Mon Nov 26 2012 Kirill Maslinsky <kirill@altlinux.org> 2.68-alt1.corbama3
- fix unquoted values passed in href 

* Mon Nov 26 2012 Kirill Maslinsky <kirill@altlinux.org> 2.68-alt1.corbama2
- rebrand for corbama
- accumulate current fixes and additions

* Tue Apr 10 2012 Kirill Maslinsky <kirill@altlinux.org> 2.68-alt1
- Initial build for Sisyphus

