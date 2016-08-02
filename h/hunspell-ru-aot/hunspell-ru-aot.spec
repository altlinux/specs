%define oname dict_ru_ru-aot
Name: hunspell-ru-aot
Version: 0.4.0
Release: alt1

Summary: Russian hunspell dictionaries

Group: Text tools
License: LGPL
Url: http://extensions.libreoffice.org/extension-center/russian-spellcheck-dictionary.-based-on-works-of-aot-group

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %oname-%version.tar

Requires: libhunspell
#Obsoletes: hunspell-ru-io < %version
Provides: hunspell-ru

BuildArch: noarch

%description
Russian hunspell (Based on AOT) dictionaries with yo letter
This Russian dictionary is  converted
to Hunspell format by Yakov Reztsov  in 2010, 2011, 2013, 2014, 2015 from
http://sourceforge.net/projects/seman/ (http://www.aot.ru)

%prep
%setup -n %oname-%version

%build

%install
mkdir -p %buildroot%_datadir/myspell
iconv -fKOI8-R -tUTF-8 russian-aot.aff > %buildroot%_datadir/myspell/ru_RU.aff
iconv -fKOI8-R -tUTF-8 russian-aot.dic > %buildroot%_datadir/myspell/ru_RU.dic
%__subst 's|^SET KOI8-R|SET UTF-8|' %buildroot%_datadir/myspell/ru_RU.aff

%files
%_datadir/myspell/ru_RU.*

%changelog
* Tue Aug 02 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- build for ALT Linux Sisyphus (ALT bug #28912)
- update to 0.4.0

* Wed Feb 18  2015 Yakov Reztsov  <yr@myooo.ru> 0.3.9-alt1
- Update dictionary to version  0.3.9

* Thu Mar 18 2014 Yakov Reztsov  <yr@myooo.ru> 0.3.3-alt1
- Update dictionary to version  0.3.3

* Sat Mar 09 2012 Yakov Reztsov  <yr@myooo.ru> 0.2.9-alt1
- Initial release for ALT Linux

