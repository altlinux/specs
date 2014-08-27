# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize gcc-c++
# END SourceDeps(oneline)
# set to include Japanese and Korean tables
%define jk_tables 0

# set to include Indic tables
%define indic_tables 0

Name: scim-tables
Version: 0.5.12
Release: alt2
Summary: SCIM Generic Table IMEngine
Packager: Ilya Mashkin <oddity@altlinux.ru>
License: GPLv2+
Group: System/Libraries
Url: http://sourceforge.net/projects/scim
Source0: http://downloads.sourceforge.net/scim/%name-%version.tar.gz
Source1: ZhuYin.txt.in
Source2: ZhuYin-Big.txt.in
Source3: Cantonese.txt.in
Source4: CangJie5.txt.in
Source5: CangJie5.png

BuildRequires: scim-devel gtk2-devel
# if autotools scripts modified
BuildRequires: gettext-devel automake libtool intltool
Requires: scim
Patch1: scim-tables-0.5.7-2.bz217639.patch
Patch2: scim-tables-0.5.7-5.bz232860.patch
Source44: import.info

%description
This package contains the Generic Table IMEngine for SCIM.

%package amharic
Summary: SCIM tables for Amharic
Group: System/Libraries
Requires: scim-tables = %version

%description amharic
This package contains scim-tables files for Amharic input.

%package arabic
Summary: SCIM tables for Arabic
Group: System/Libraries
Requires: scim-tables = %version

%description arabic
This package contains scim-tables files for Arabic input.

%if %indic_tables
%package bengali
Summary: SCIM tables for Bengali
Group: System/Libraries
Requires: scim-tables = %version

%description bengali
This package contains scim-tables files for Bengali input.
%endif

%package chinese
Summary: SCIM tables for Chinese
Group: System/Libraries
Requires: scim-tables = %version

%description chinese
This package contains scim-tables files for Chinese input.

%package chinese-extra
Summary: Additional SCIM tables for Chinese
Group: System/Libraries
Requires: scim-tables = %version

%description chinese-extra
This package contains additional less used scim-tables files for Chinese input.

%if %indic_tables
%package gujarati
Summary: SCIM tables for Gujarati
Group: System/Libraries
Requires: scim-tables = %version

%description gujarati
This package contains scim-tables files for Gujarati input.

%package hindi
Summary: SCIM tables for Hindi
Group: System/Libraries
Requires: scim-tables = %version

%description hindi
This package contains scim-tables files for Hindi input.
%endif

%if %jk_tables
%package japanese
Summary: SCIM tables for Japanese
Group: System/Libraries
Requires: scim-tables = %version

%description japanese
This package contains scim-tables files for Japanese.
%endif

%if %indic_tables
%package kannada
Summary: SCIM tables for Kannada
Group: System/Libraries
Requires: scim-tables = %version

%description kannada
This package contains scim-tables files for Kannada input.
%endif

%if %jk_tables
%package korean
Summary: SCIM tables for Korean
Group: System/Libraries
Requires: scim-tables = %version

%description korean
This package contains scim-tables files for Korean.
%endif

%if %indic_tables
%package malayalam
Summary: SCIM tables for Malayalam scripts
Group: System/Libraries
Requires: scim-tables = %version

%description malayalam
This package contains scim-tables files for Malayalam languages.
%endif

%if %indic_tables
%package marathi
Summary: SCIM tables for Marathi
Group: System/Libraries
Requires: scim-tables = %version

%description marathi
This package contains scim-tables files for Marathi input.
%endif

%package nepali
Summary: SCIM tables for Nepali
Group: System/Libraries
Requires: scim-tables = %version

%description nepali
This package contains scim-tables files for Nepali input.

%if %indic_tables
%package punjabi
Summary: SCIM tables for Punjabi
Group: System/Libraries
Requires: scim-tables = %version

%description punjabi
This package contains scim-tables files for Punjabi input.
%endif

%package russian
Summary: SCIM tables for Russian
Group: System/Libraries
Requires: scim-tables = %version

%description russian
This package contains scim-tables files for Russian input.

%if %indic_tables
%package tamil
Summary: SCIM tables for Tamil
Group: System/Libraries
Requires: scim-tables = %version

%description tamil
This package contains scim-tables files for Tamil input.
%endif

%package thai
Summary: SCIM tables for Thai
Group: System/Libraries
Requires: scim-tables = %version

%description thai
This package contains scim-tables files for Thai input.

%if %indic_tables
%package telugu
Summary: SCIM tables for Telugu
Group: System/Libraries
Requires: scim-tables = %version

%description telugu
This package contains scim-tables files for Telugu input.
%endif

%package ukrainian
Summary: SCIM tables for Ukrainian
Group: System/Libraries
Requires: scim-tables = %version

%description ukrainian
This package contains scim-tables files for Ukrainian input.

%package vietnamese
Summary: SCIM tables for Vietnamese
Group: System/Libraries
Requires: scim-tables = %version

%description vietnamese
This package contains scim-tables files for Vietnamese input.

%package additional
Summary: Other miscellaneous SCIM tables
Group: System/Libraries
Requires: scim-tables = %version

%description additional
This package contains some miscellaneous scim-tables.

%prep
%setup
%__cp %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %_builddir/%name-%version/tables/zh/

%patch1 -p1 -b .1-217639
%patch2 -p1 -b .2-232860

%build
autoreconf -ivf
intltoolize --force
autoreconf
%configure --disable-static
make  %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# kill *.a and *.la files
rm -f $RPM_BUILD_ROOT/%_libdir/scim-1.0/*/*/*.la

# Insert CangJie5 icon mod.
%__cp %SOURCE5 $RPM_BUILD_ROOT/%_datadir/scim/icons/

%if !%indic_tables
rm $RPM_BUILD_ROOT/%_datadir/scim/{icons,tables}/{Bengali,Gujarati,Hindi,Kannada,Malayalam,Marathi,Punjabi,Tamil,Telugu}-*
%endif

%if !%jk_tables
rm $RPM_BUILD_ROOT/%_datadir/scim/{icons,tables}/{Hangul,Hanja,HIRAGANA,KATAKANA,Nippon}*
%endif

%find_lang %name

%files -f %name.lang
%_bindir/scim-make-table
%_libdir/scim-1.0/*/IMEngine/table.so
%_libdir/scim-1.0/*/SetupUI/table-imengine-setup.so
%_datadir/scim/icons/table.png
%dir %_datadir/scim/tables
%_mandir/man1/scim-make-table.1*

%files amharic
%_datadir/scim/tables/Amharic.bin
%_datadir/scim/icons/Amharic.png

%files arabic
%_datadir/scim/tables/Arabic.bin
%_datadir/scim/icons/Arabic.png

%if %indic_tables
%files bengali
%_datadir/scim/tables/Bengali-inscript.bin
%_datadir/scim/tables/Bengali-probhat.bin
%_datadir/scim/icons/Bengali-inscript.png
%_datadir/scim/icons/Bengali-probhat.png
%endif

%files chinese
%doc tables/zh/README-*.txt
%_datadir/scim/tables/Array30.bin
%_datadir/scim/icons/Array30.png
%_datadir/scim/tables/CangJie3.bin
%_datadir/scim/icons/CangJie3.png
%_datadir/scim/tables/CangJie5.bin
%_datadir/scim/icons/CangJie5.png
%_datadir/scim/tables/CantonHK.bin
%_datadir/scim/icons/CantonHK.png
%_datadir/scim/tables/Quick.bin
%_datadir/scim/icons/Quick.png
%_datadir/scim/tables/Wubi.bin
%_datadir/scim/icons/Wubi.png
%_datadir/scim/tables/ZhuYin.bin
%_datadir/scim/icons/ZhuYin.png

%files chinese-extra
%doc tables/zh/README-*.txt
%_datadir/scim/tables/CNS11643.bin
%_datadir/scim/icons/CNS11643.png
%_datadir/scim/tables/CangJie.bin
%_datadir/scim/icons/CangJie.png
%_datadir/scim/tables/Cantonese.bin
%_datadir/scim/icons/Cantonese.png
%_datadir/scim/tables/Dayi3.bin
%_datadir/scim/icons/Dayi.png
%_datadir/scim/tables/EZ-Big.bin
%_datadir/scim/icons/EZ.png
%_datadir/scim/tables/Erbi.bin
%_datadir/scim/icons/Erbi.png
%_datadir/scim/tables/Erbi-QS.bin
%_datadir/scim/icons/Erbi-QS.png
%_datadir/scim/tables/Jyutping.bin
%_datadir/scim/icons/Jyutping.png
%_datadir/scim/tables/Simplex.bin
%_datadir/scim/icons/Simplex.png
%_datadir/scim/tables/SmartCangJie6.bin
%_datadir/scim/icons/SmartCangJie6.png
%_datadir/scim/tables/Stroke5.bin
%_datadir/scim/icons/Stroke5.png
%_datadir/scim/tables/Wu.bin
%_datadir/scim/icons/Wu.png
%_datadir/scim/tables/ZhuYin-Big.bin
%_datadir/scim/icons/ZhuYin.png
%_datadir/scim/tables/Ziranma.bin
%_datadir/scim/icons/Ziranma.png

%if %indic_tables
%files gujarati
%_datadir/scim/tables/Gujarati-inscript.bin
%_datadir/scim/tables/Gujarati-phonetic.bin
%_datadir/scim/icons/Gujarati-inscript.png
%_datadir/scim/icons/Gujarati-phonetic.png

%files hindi
%_datadir/scim/tables/Hindi-inscript.bin
%_datadir/scim/tables/Hindi-phonetic.bin
%_datadir/scim/icons/Hindi-inscript.png
%_datadir/scim/icons/Hindi-phonetic.png
%endif

%if %jk_tables
%files japanese
%doc tables/ja/kanjidic*
%_datadir/scim/tables/HIRAGANA.bin
%_datadir/scim/tables/KATAKANA.bin
%_datadir/scim/tables/Nippon.bin
%_datadir/scim/icons/HIRAGANA.png
%_datadir/scim/icons/KATAKANA.png
%_datadir/scim/icons/Nippon.png
%endif

%if %indic_tables
%files kannada
%_datadir/scim/tables/Kannada-inscript.bin
%_datadir/scim/tables/Kannada-kgp.bin
%_datadir/scim/icons/Kannada-inscript.png
%_datadir/scim/icons/Kannada-kgp.png
%endif

%if %jk_tables
%files korean
%_datadir/scim/tables/Hangul.bin
%_datadir/scim/tables/HangulRomaja.bin
%_datadir/scim/tables/Hanja.bin
%_datadir/scim/icons/Hangul.png
%_datadir/scim/icons/Hanja.png
%endif

%if %indic_tables
%files malayalam
%_datadir/scim/tables/Malayalam-inscript.bin
%_datadir/scim/icons/Malayalam-inscript.png
%endif

%if %indic_tables
%files marathi
%_datadir/scim/tables/Marathi-remington.bin
%_datadir/scim/icons/Marathi-remington.png
%endif

%files nepali
%_datadir/scim/tables/Nepali_*.bin
%_datadir/scim/icons/Nepali.png

%if %indic_tables
%files punjabi
%_datadir/scim/tables/Punjabi-inscript.bin
%_datadir/scim/tables/Punjabi-jhelum.bin
%_datadir/scim/tables/Punjabi-phonetic.bin
%_datadir/scim/icons/Punjabi-inscript.png
%_datadir/scim/icons/Punjabi-jhelum.png
%_datadir/scim/icons/Punjabi-phonetic.png
%endif

%files russian
%_datadir/scim/tables/RussianTraditional.bin
%_datadir/scim/tables/Yawerty.bin
%_datadir/scim/tables/Translit.bin
%_datadir/scim/icons/RussianTraditional.png
%_datadir/scim/icons/Yawerty.png
%_datadir/scim/icons/Translit.png

%if %indic_tables
%files tamil
%_datadir/scim/tables/Tamil-inscript.bin
%_datadir/scim/tables/Tamil-phonetic.bin
%_datadir/scim/icons/Tamil-inscript.png
%_datadir/scim/icons/Tamil-phonetic.png
%endif

%files thai
%_datadir/scim/tables/Thai.bin
%_datadir/scim/icons/Thai.png

%if %indic_tables
%files telugu
%_datadir/scim/tables/Telugu-inscript.bin
%_datadir/scim/icons/Telugu-inscript.png
%endif

%files ukrainian
%_datadir/scim/tables/Ukrainian-Translit.bin
%_datadir/scim/icons/Ukrainian-Translit.png

%files vietnamese
%_datadir/scim/tables/Viqr.bin
%_datadir/scim/icons/Viqr.png

%files additional
%_datadir/scim/tables/classicalhebrew.bin
%_datadir/scim/tables/greekpoly.bin
%_datadir/scim/tables/IPA-X-SAMPA.bin
%_datadir/scim/tables/IPA-Kirshenbaum.bin
%_datadir/scim/tables/LaTeX.bin
%_datadir/scim/tables/Uyghur-Romanized.bin
%_datadir/scim/tables/Uyghur-Standard.bin
%_datadir/scim/icons/IPA-X-SAMPA.png
%_datadir/scim/icons/LaTeX.png
%_datadir/scim/icons/Uyghur.png

%changelog
* Wed Aug 27 2014 Ilya Mashkin <oddity@altlinux.ru> 0.5.12-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.12-alt1_3
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.12-alt1_2
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.12-alt1_1
- initial fc import

