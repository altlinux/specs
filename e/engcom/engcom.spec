Name: engcom
Version: 1.36
Release: alt1

Summary: The Open English-Russian Dictionary of Computer Terms
Summary(ru_RU.KOI8-R): Свободный англо-русский словарь компьютерных терминов

License: FDL
URL: http://www.etersoft.ru/engcom
Group: Text tools

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar
#Source: http://etersoft.ru/download/engcom/%name-%version.tar.bz2

BuildArchitectures: noarch

# Please do not use buildreq
BuildPreReq: dict-tools perl-Unicode-Map8 perl-Unicode-String stardict-tools

%define	dict_name engcom
%define dictdesc The Open English-Russian Dictionary of Computer Terms

# Automatically added by buildreq on Fri Jun 15 2007
BuildRequires: dict-tools makedict perl-Unicode-Map8 python-module-PyXML python-modules-compiler python-modules-email python-modules-encodings python-modules-logging

%description
The %name package contains free (as speech) English-Russian
Dictionary of Computer Terms. It is not academic dictionary.

%description -l ru_RU.KOI8-R
Пакет %name содержит англо-русский словарь компьютерных
терминов, составленный по мотивам реальной жизни.

%package -n mova-%name

Summary: %dictdesc for mova
Summary(ru_RU.KOI8-R): Свободный англо-русский словарь компьютерных терминов для mova
Group: Text tools
Obsoletes: engcom engcom-mova
Provides: engcom engcom-mova
Requires: mova

%description -n mova-%name
The %name package contains free (with FDL license ) English-Russian
Dictionary of Computer Terms in mova format. It is not academic dictionary.

%description -n mova-%name -l ru_RU.KOI8-R
Пакет %name содержит свободный англо-русский словарь компьютерных
терминов в формате mova, составленный по мотивам реальной жизни,
содержанию компьютерной прессы и рассылок.

%package -n dict-%name

Summary: %dictdesc for dict dictionary
Summary(ru_RU.KOI8-R): Свободный англо-русский словарь компьютерных терминов в формате dict
Group: Text tools
Requires: dictd >= 1.7.1

%description -n dict-%name
The %name package contains free (with FDL license) English-Russian
Computer Dictionary in dict format. It is not academic dictionary.

%description -n dict-%name -l ru_RU.KOI8-R
Пакет %name содержит свободный англо-русский словарь компьютерных
терминов в формате словарей dictd, составленный по мотивам реальной жизни,
содержанию компьютерной прессы и рассылок.

%package -n stardict-%name

Summary: The Open English-Russian Dictionary of Computer Terms for stardict dictionary
Summary(ru_RU.KOI8-R): Свободный англо-русский словарь компьютерных терминов в формате stardict
Group: Text tools
Requires: stardict

%description -n stardict-%name
The %name package contains free (with FDL license) English-Russian
Computer Dictionary in stardict format. It is not academic dictionary.

%description -n stardict-%name -l ru_RU.KOI8-R
Пакет %name содержит свободный англо-русский словарь компьютерных
терминов в формате словарей stardict, составленный по мотивам реальной жизни,
содержанию компьютерной прессы и рассылок.

%prep
%setup

%build
export LANG=C
export TITLE="%dictdesc"
export URL="http://engcom.org.ru"
%__make
mv EngCom.koi %dict_name.koi

# FIXME: mueller only convertor
#makedict -i mueller7 -o xdxf %dict_name.koi %dict_name

# Specially modified makedict convertor
./engcom_parser.py %dict_name.koi >%dict_name.tmp
grep -v "<meta_info>" %dict_name.tmp >%dict_name

mkdir -p out
# CHECKME: makes broken dict?
makedict -i xdxf -o dictd %dict_name -d out

makedict -i xdxf -o stardict %dict_name -d out

%install
# install mova files
install -p -m644 -D %dict_name.koi %buildroot%_datadir/dict/%dict_name.koi

# install dict files
cd out/%dict_name
dictzip %dict_name.dict
for i in dict.dz index
do
	install -p -m644 -D %dict_name.$i %buildroot%_datadir/dictd/%dict_name.$i
done
cd -

# install stardict files
cd out/stardict-%dict_name-2.4.2
cat << EOF >> %dict_name.ifo
author=Vitaly Lipatov
email=lav@etersoft.ru
website=http://etersoft.ru
EOF

gzip %dict_name.idx
dictzip %dict_name.dict
for i in dict.dz idx.gz ifo
do
	install -p -m644 -D %dict_name.$i %buildroot%_datadir/stardict/dic/%dict_name.$i
done
cd -

%post -n dict-%name
%_sbindir/dictdconfig -w

%postun -n dict-%name
%_sbindir/dictdconfig -w

%files -n mova-%name
%doc docs
%_datadir/dict/*.koi

%files -n dict-%name
%doc docs
%_datadir/dictd/*

%files -n stardict-%name
%doc docs
%_datadir/stardict/dic/*

%changelog
* Tue Dec 22 2009 Vitaly Lipatov <lav@altlinux.ru> 1.36-alt1
- new version, build from git

* Tue Dec 09 2008 Vitaly Lipatov <lav@altlinux.ru> 1.35-alt2
- cleanup spec (bug #18158)

* Thu Nov 27 2008 Vitaly Lipatov <lav@altlinux.ru> 1.35-alt1
- new version, about 2370 articles
- use post/preun service

* Sat Jan 12 2008 Vitaly Lipatov <lav@altlinux.ru> 1.32-alt1
- new version, about 2300 articles
- use XDXF makedict for dict format converting

* Fri Jun 15 2007 Vitaly Lipatov <lav@altlinux.ru> 1.31-alt1
- rewrote stardict converting with XDXF utility makedict

* Thu Dec 28 2006 Vitaly Lipatov <lav@altlinux.ru> 1.31-alt0.1
- new version 1.31 (with rpmrb script)

* Mon Dec 25 2006 Vitaly Lipatov <lav@altlinux.ru> 1.30-alt0.1
- new version 1.30 (with rpmrb script)

* Sat Jun 24 2006 Vitaly Lipatov <lav@altlinux.ru> 1.29-alt0.1
- new version 1.29 (with rpmrb script)

* Sat Feb 04 2006 Vitaly Lipatov <lav@altlinux.ru> 1.28-alt1
- new version, about 2110 articles

* Tue Jan 03 2006 Vitaly Lipatov <lav@altlinux.ru> 1.27-alt1
- new version, about 2090 articles

* Tue Nov 29 2005 Vitaly Lipatov <lav@altlinux.ru> 1.25-alt1
- new version, about 2070 articles

* Mon Sep 05 2005 Vitaly Lipatov <lav@altlinux.ru> 1.24-alt1
- new version, about 2000 articles

* Thu May 05 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- new version, 1945 articles
  (dedicates to 60 Years to the end of World War II)

* Tue Mar 08 2005 Vitaly Lipatov <lav@altlinux.ru> 0.91-alt1
- new version, about 1880 articles

* Sun Nov 07 2004 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- new version, about 1850 articles

* Sun Jun 13 2004 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- new version, about 1700 articles
- rename from EngCom to engcom
- add stardict format package

* Sun Jan 18 2004 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- correct and update, 1402 articles

* Thu Jan 01 2004 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- update

* Tue Mar 25 2003 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- update

* Thu Jan 30 2003 Alexey Dyachenko <alexd@altlinux.ru> 0.4-alt3
- fix install scripts
- build with standard dictfmt and locale ru_RU.UTF-8

* Sun Dec 15 2002 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt2
- remove preun_service dictd from preuninstall script (bug #1703)
- corrected double spaces in the source file (via problem with dict)
- small updates of dictionary

* Fri Nov 22 2002 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- new version

* Fri Nov 22 2002 Alexey Dyachenko <alexd@altlinux.ru> 0.3-alt3
- fix script for dict format and dictionary name

* Mon Nov 11 2002 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt2
- cleanup spec
- add obsoletes for engcom-mova

* Mon Nov 04 2002 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- rename output packet to mova-engcom
- add new output packet dict-engcom for dict (based on spec from dict-mueller7-utf8)
- update, 1260 articles

* Sun Jun 30 2002 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- new version, 1200 articles

* Fri Jun 14 2002 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt2
- add noarch option
- rename output packet to engcom-mova
- content updated

* Sun Jun 09 2002 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- first public version in rpm

