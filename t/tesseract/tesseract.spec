%set_verify_elf_method none

Name:     tesseract
Version:  3.02
Release:  alt1.r723

Summary:  Raw Open source OCR Engine

License:  Apache License
Group:    Graphics
Url:      http://code.google.com/p/tesseract-ocr

Packager: Andrey Cherepanov <cas@altlinux.org> 

Source:   http://tesseract-ocr.googlecode.com/files/%name-%version.tar

BuildRequires: gcc-c++ 
BuildRequires: libtiff-devel
BuildRequires: libleptonica-devel >= 1.60

%description
A commercial quality OCR engine originally developed at HP between 1985
and 1995. In 1995, this engine was among the top 3 evaluated by UNLV. It
was open-sourced by HP and UNLV in 2005. From 2007 it is developed by
Google.

%package devel
Summary:  Development files for tesseract
Group:    Development/C
Requires: %name

%description devel
The %{name}-devel package contains header file for
developing applications that use %{name}.

%package langpack-bg
Group:   Graphics
Summary: Bulgarian language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-bul = %version
Obsoletes: tesseract-bul < %version

%description langpack-bg
Data files required to recognize Bulgarian OCR.

%package langpack-ca
Group:   Graphics
Summary: Catalan language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-cat = %version
Obsoletes: tesseract-cat < %version

%description langpack-ca
Data files required to recognize Catalan OCR.

%package langpack-cs
Group:   Graphics
Summary: Czech language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-ces = %version
Obsoletes: tesseract-ces < %version

%description langpack-cs
Data files required to recognize Czech OCR.

%package langpack-zh_CN
Group:   Graphics
Summary: Simplified Chinese language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-chi_sim = %version
Obsoletes: tesseract-chi_sim < %version

%description langpack-zh_CN
Data files required to recognize Simplified Chinese OCR.

%package langpack-zh_TW
Group:   Graphics
Summary: Traditional Chinese language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-chi_tra = %version
Obsoletes: tesseract-chi_tra < %version

%description langpack-zh_TW
Data files required to recognize Traditional Chinese OCR.

%package langpack-da-frak
Group:   Graphics
Summary: Danish (Fraktur) language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-dan-frak = %version
Obsoletes: tesseract-dan-frak < %version

%description langpack-da-frak
Data files required to recognize Danish (Fraktur) OCR.

%package langpack-da
Group:   Graphics
Summary: Danish language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-dan = %version
Obsoletes: tesseract-dan < %version

%description langpack-da
Data files required to recognize Danish OCR.

%package langpack-de-frak
Group:   Graphics
Summary: German (Fraktur) language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-deu-frak = %version
Obsoletes: tesseract-deu-frak < %version

%description langpack-de-frak
Data files required to recognize German (Fraktur) OCR.

%package langpack-de
Group:   Graphics
Summary: German language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-deu = %version
Obsoletes: tesseract-deu < %version

%description langpack-de
Data files required to recognize German OCR.

%package langpack-el
Group:   Graphics
Summary: Greek language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-ell = %version
Obsoletes: tesseract-ell < %version

%description langpack-el
Data files required to recognize Greek OCR.

%package langpack-en
Group:   Graphics
Summary: English language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-eng = %version
Obsoletes: tesseract-eng < %version

%description langpack-en
Data files required to recognize English OCR.

%package langpack-es
Group:   Graphics
Summary: Spanish language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-spa = %version
Obsoletes: tesseract-spa < %version

%description langpack-es
Data files required to recognize Spanish OCR.

%package langpack-fi
Group:   Graphics
Summary: Finnish language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-fin = %version
Obsoletes: tesseract-fin < %version

%description langpack-fi
Data files required to recognize Finnish OCR.

%package langpack-fr
Group:   Graphics
Summary: French language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-fra = %version
Obsoletes: tesseract-fra < %version

%description langpack-fr
Data files required to recognize French OCR.

%package langpack-hu
Group:   Graphics
Summary: Hungarian language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-hun = %version
Obsoletes: tesseract-hun < %version

%description langpack-hu
Data files required to recognize Hungarian OCR.

%package langpack-id
Group:   Graphics
Summary: Indonesian language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-ind = %version
Obsoletes: tesseract-ind < %version

%description langpack-id
Data files required to recognize Indonesian OCR.

%package langpack-it
Group:   Graphics
Summary: Italian language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-ita = %version
Obsoletes: tesseract-ita < %version

%description langpack-it
Data files required to recognize Italian OCR.

%package langpack-ja
Group:   Graphics
Summary: Japanese language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-jpn = %version
Obsoletes: tesseract-jpn < %version

%description langpack-ja
Data files required to recognize Japanese OCR.

%package langpack-ko
Group:   Graphics
Summary: Korean language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-kor = %version
Obsoletes: tesseract-kor < %version

%description langpack-ko
Data files required to recognize Korean OCR.

%package langpack-lv
Group:   Graphics
Summary: Latvian language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-lav = %version
Obsoletes: tesseract-lav < %version

%description langpack-lv
Data files required to recognize Latvian OCR.

%package langpack-lt
Group:   Graphics
Summary: Lithuanian language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-lit = %version
Obsoletes: tesseract-lit < %version

%description langpack-lt
Data files required to recognize Lithuanian OCR.

%package langpack-nl
Group:   Graphics
Summary: Dutch language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-nld = %version
Obsoletes: tesseract-nld < %version

%description langpack-nl
Data files required to recognize Dutch OCR.

%package langpack-nn
Group:   Graphics
Summary: Norwegian language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-nor = %version
Obsoletes: tesseract-nor < %version

%description langpack-nn
Data files required to recognize Norwegian OCR.

%package langpack-pl
Group:   Graphics
Summary: Polish language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-pol = %version
Obsoletes: tesseract-pol < %version

%description langpack-pl
Data files required to recognize Polish OCR.

%package langpack-pt
Group:   Graphics
Summary: Portuguese language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-por = %version
Obsoletes: tesseract-por < %version

%description langpack-pt
Data files required to recognize Portuguese OCR.

%package langpack-ro
Group:   Graphics
Summary: Romanian language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-ron = %version
Obsoletes: tesseract-ron < %version

%description langpack-ro
Data files required to recognize Romanian OCR.

%package langpack-ru
Group:   Graphics
Summary: Russian language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-rus = %version
Obsoletes: tesseract-rus < %version

%description langpack-ru
Data files required to recognize Russian OCR.

%package langpack-sk
Group:   Graphics
Summary: Slovakian language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-slk = %version
Obsoletes: tesseract-slk < %version

%description langpack-sk
Data files required to recognize Slovakian OCR.

%package langpack-sl
Group:   Graphics
Summary: Slovenian language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-slv = %version
Obsoletes: tesseract-slv < %version

%description langpack-sl
Data files required to recognize Slovenian OCR.

%package langpack-sr
Group:   Graphics
Summary: Serbian (Latin) language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-srp = %version
Obsoletes: tesseract-srp < %version

%description langpack-sr
Data files required to recognize Serbian (Latin) OCR.

%package langpack-sv
Group:   Graphics
Summary: Swedish language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-swe = %version
Obsoletes: tesseract-swe < %version

%description langpack-sv
Data files required to recognize Swedish OCR.

%package langpack-tl
Group:   Graphics
Summary: Tagalog language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-tgl = %version
Obsoletes: tesseract-tgl < %version

%description langpack-tl
Data files required to recognize Tagalog OCR.

%package langpack-tr
Group:   Graphics
Summary: Turkish language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-tur = %version
Obsoletes: tesseract-tur < %version

%description langpack-tr
Data files required to recognize Turkish OCR.

%package langpack-uk
Group:   Graphics
Summary: Ukrainian language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-ukr = %version
Obsoletes: tesseract-ukr < %version

%description langpack-uk
Data files required to recognize Ukrainian OCR.

%package langpack-vi
Group:   Graphics
Summary: Vietnamese language pack for tesseract
BuildArch: noarch
Requires: tesseract >= 3.00
Provides:  tesseract-vie = %version
Obsoletes: tesseract-vie < %version

%description langpack-vi
Data files required to recognize Vietnamese OCR.

%prep
%setup -q

%build
sh autogen.sh
export CFLAGS=
export CXXFLAGS=
%add_optflags %optflags_shared
%configure --disable-static
%make_build

%install
%makeinstall_std
# Install traineddata
mkdir -p %buildroot%_datadir/tessdata/
cp -v tessdata/*.traineddata %buildroot%_datadir/tessdata/

%files
%doc AUTHORS COPYING ChangeLog README
%_bindir/*
%dir %_datadir/tessdata/
%exclude %_datadir/tessdata/*
%_libdir/lib*.so.*
%doc %_man1dir/*
%doc %_man5dir/*

%files devel
%_includedir/%name/
%_libdir/lib*.so

%files langpack-bg
%_datadir/tessdata/bul.traineddata

%files langpack-ca
%_datadir/tessdata/cat.traineddata

%files langpack-cs
%_datadir/tessdata/ces.traineddata

%files langpack-zh_CN
%_datadir/tessdata/chi_sim.traineddata

%files langpack-zh_TW
%_datadir/tessdata/chi_tra.traineddata

%files langpack-da-frak
%_datadir/tessdata/dan-frak.traineddata

%files langpack-da
%_datadir/tessdata/dan.traineddata

%files langpack-de-frak
%_datadir/tessdata/deu-frak.traineddata

%files langpack-de
%_datadir/tessdata/deu.traineddata

%files langpack-el
%_datadir/tessdata/ell.traineddata

%files langpack-en
%_datadir/tessdata/eng.traineddata

%files langpack-es
%_datadir/tessdata/spa.traineddata

%files langpack-fi
%_datadir/tessdata/fin.traineddata

%files langpack-fr
%_datadir/tessdata/fra.traineddata

%files langpack-hu
%_datadir/tessdata/hun.traineddata

%files langpack-id
%_datadir/tessdata/ind.traineddata

%files langpack-it
%_datadir/tessdata/ita.traineddata

%files langpack-ja
%_datadir/tessdata/jpn.traineddata

%files langpack-ko
%_datadir/tessdata/kor.traineddata

%files langpack-lv
%_datadir/tessdata/lav.traineddata

%files langpack-lt
%_datadir/tessdata/lit.traineddata

%files langpack-nl
%_datadir/tessdata/nld.traineddata

%files langpack-nn
%_datadir/tessdata/nor.traineddata

%files langpack-pl
%_datadir/tessdata/pol.traineddata

%files langpack-pt
%_datadir/tessdata/por.traineddata

%files langpack-ro
%_datadir/tessdata/ron.traineddata

%files langpack-ru
%_datadir/tessdata/rus.traineddata

%files langpack-sk
%_datadir/tessdata/slk.traineddata

%files langpack-sl
%_datadir/tessdata/slv.traineddata

%files langpack-sr
%_datadir/tessdata/srp.traineddata

%files langpack-sv
%_datadir/tessdata/swe.traineddata

%files langpack-tl
%_datadir/tessdata/tgl.traineddata

%files langpack-tr
%_datadir/tessdata/tur.traineddata

%files langpack-uk
%_datadir/tessdata/ukr.traineddata

%files langpack-vi
%_datadir/tessdata/vie.traineddata


%changelog
* Thu May 03 2012 Andrey Cherepanov <cas@altlinux.org> 3.02-alt1.r723
- New version 3.02
- Major changes:
  * Added simultaneous multi-language capability.
  * Added experimental equation detector.
  * Improved handling of resolution from input images.
  * Major improvements to layout analysis for better image detection,
    diacritic detection, better textline finding, better tabstop finding.
  * Improved line detection and removal.
  * Many other fixes, including the way in which the chopper finds chops
    and messes with the outline while it does so.
- Build both executables and dictionaries from one package

* Wed Aug 31 2011 Andrey Cherepanov <cas@altlinux.org> 3.00-alt1
- New version 3.00 (closes: #25477)
- Add optflags_shared for build (closes: #25249)

* Tue Apr 26 2011 Fr. Br. George <george@altlinux.ru> 2.04-alt2
- Fix debuginfo

* Wed Sep 23 2009 Fr. Br. George <george@altlinux.ru> 2.04-alt1
- Version up

* Sat Nov 08 2008 Vitaly Lipatov <lav@altlinux.ru> 2.03-alt2
- fix build with gcc 4.3

* Fri May 09 2008 Vitaly Lipatov <lav@altlinux.ru> 2.03-alt1
- new version 2.03 (with rpmrb script)

* Wed Oct 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.01-alt1
- new version 2.01 (with rpmrb script)

* Tue Jul 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.00-alt1
- initial build for Sisyphus
