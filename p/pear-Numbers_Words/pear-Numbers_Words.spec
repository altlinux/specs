%define pear_name Numbers_Words

Name: pear-Numbers_Words
Version: 0.15.0
Release: alt2

Summary: The PEAR Numbers_Words package provides methods for spelling numerals in words

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

%description
With Numbers_Words class you can convert numbers
written in arabic digits to words in several languages.
You can convert an integer between -infinity and infinity.
If your system does not support such long numbers you can
call Numbers_Words::toWords() with just a string.

With the Numbers_Words::toCurrency($num, $locale, 'USD') method
you can convert a number (decimal and fraction part) to words with
currency name.

The following languages are supported:
    * bg (Bulgarian) by Kouber Saparev
    * cs (Czech) by Petr 'PePa' Pavel
    * de (German) by me
    * dk (Danish) by Jesper Veggerby
    * en_100 (Donald Knuth system, English) by me
    * en_GB (British English) by me
    * en_US (American English) by me
    * es (Spanish Castellano) by Xavier Noguer
    * es_AR (Argentinian Spanish) by Martin Marrese
    * et (Estonian) by Erkki Saarniit
    * fr (French) by Kouber Saparev
    * fr_BE (French Belgium) by Kouber Saparev and Philippe Bajoit
    * he (Hebrew) by Hadar Porat
    * hu_HU (Hungarian) by Nils Homp
    * id (Indonesian) by Ernas M. Jamil and Arif Rifai Dwiyanto
    * it_IT (Italian) by Filippo Beltramini and Davide Caironi
    * lt (Lithuanian) by Laurynas Butkus
    * nl (Dutch) by WHAM van Dinter
    * pl (Polish) by me
    * pt_BR (Brazilian Portuguese) by Marcelo Subtil Marcal and Mario
H.C.T.
    * ru (Russian) by Andrey Demenev
    * sv (Swedish) by Robin Ericsson

%prep
%setup -c -n %pear_name-%version
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_testdir/Numbers_Words/
%pear_dir/Numbers/Words.php
%pear_dir/Numbers/Words/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.15.0-alt2
- autorebuild for correct requires(pre) (see bug #16086)

* Mon Jan 21 2008 Vitaly Lipatov <lav@altlinux.ru> 0.15.0-alt1
- initial build for ALT Linux Sisyphus

