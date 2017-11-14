Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# set to include Japanese and Korean tables
%define jk_tables 0

# set to include Indic tables
%define indic_tables 0

Name:           scim-tables
Version:        0.5.14
Release:        alt1_3
Summary:        SCIM Generic Table IMEngine

License:        GPLv2+
URL:            http://sourceforge.net/projects/scim
Source0:        http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.gz

BuildRequires:  scim-devel gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel
BuildRequires:  gcc-common

# if autotools scripts modified
BuildRequires:  gettext-tools libasprintf-devel automake libtool intltool

Requires:       scim
Patch1:         scim-tables-0.5.14-bz217639.patch
Patch2:	        scim-tables-0.5.14-bz232860.patch
Source44: import.info

%description
This package contains the Generic Table IMEngine for SCIM.

%package amharic
Group: System/Libraries
Summary:        SCIM tables for Amharic
Requires:       scim-tables = %{version}

%description amharic
This package contains scim-tables files for Amharic input.

%package arabic
Group: System/Libraries
Summary:        SCIM tables for Arabic
Requires:       scim-tables = %{version}

%description arabic
This package contains scim-tables files for Arabic input.

%if %{indic_tables}
%package bengali
Group: System/Libraries
Summary:        SCIM tables for Bengali
Requires:       scim-tables = %{version}

%description bengali
This package contains scim-tables files for Bengali input.
%endif

%package chinese
Group: System/Libraries
Summary:        SCIM tables for Chinese
Requires:       scim-tables = %{version}

%description chinese
This package contains scim-tables files for Chinese input.

%package chinese-extra
Group: System/Libraries
Summary:        Additional SCIM tables for Chinese
Requires:       scim-tables = %{version}

%description chinese-extra
This package contains additional less used scim-tables files for Chinese input.

%if %{indic_tables}
%package gujarati
Group: System/Libraries
Summary:        SCIM tables for Gujarati
Requires:       scim-tables = %{version}

%description gujarati
This package contains scim-tables files for Gujarati input.

%package hindi
Group: System/Libraries
Summary:        SCIM tables for Hindi
Requires:       scim-tables = %{version}

%description hindi
This package contains scim-tables files for Hindi input.
%endif

%if %{jk_tables}
%package japanese
Group: System/Libraries
Summary:        SCIM tables for Japanese
Requires:       scim-tables = %{version}

%description japanese
This package contains scim-tables files for Japanese.
%endif

%if %{indic_tables}
%package kannada
Group: System/Libraries
Summary:        SCIM tables for Kannada
Requires:       scim-tables = %{version}

%description kannada
This package contains scim-tables files for Kannada input.
%endif

%if %{jk_tables}
%package korean
Group: System/Libraries
Summary:        SCIM tables for Korean
Requires:       scim-tables = %{version}

%description korean
This package contains scim-tables files for Korean.
%endif

%if %{indic_tables}
%package malayalam
Group: System/Libraries
Summary:        SCIM tables for Malayalam scripts
Requires:       scim-tables = %{version}

%description malayalam
This package contains scim-tables files for Malayalam languages.
%endif

%if %{indic_tables}
%package marathi
Group: System/Libraries
Summary:        SCIM tables for Marathi
Requires:       scim-tables = %{version}

%description marathi
This package contains scim-tables files for Marathi input.
%endif


%package nepali
Group: System/Libraries
Summary:        SCIM tables for Nepali
Requires:       scim-tables = %{version}

%description nepali
This package contains scim-tables files for Nepali input.

%if %{indic_tables}
%package punjabi
Group: System/Libraries
Summary:        SCIM tables for Punjabi
Requires:       scim-tables = %{version}

%description punjabi
This package contains scim-tables files for Punjabi input.
%endif

%package russian
Group: System/Libraries
Summary:        SCIM tables for Russian
Requires:       scim-tables = %{version}

%description russian
This package contains scim-tables files for Russian input.

%if %{indic_tables}
%package tamil
Group: System/Libraries
Summary:        SCIM tables for Tamil
Requires:       scim-tables = %{version}

%description tamil
This package contains scim-tables files for Tamil input.
%endif

%package thai
Group: System/Libraries
Summary:        SCIM tables for Thai
Requires:       scim-tables = %{version}

%description thai
This package contains scim-tables files for Thai input.

%if %{indic_tables}
%package telugu
Group: System/Libraries
Summary:        SCIM tables for Telugu
Requires:       scim-tables = %{version}

%description telugu
This package contains scim-tables files for Telugu input.
%endif

%package ukrainian
Group: System/Libraries
Summary:        SCIM tables for Ukrainian
Requires:       scim-tables = %{version}

%description ukrainian
This package contains scim-tables files for Ukrainian input.

%package vietnamese
Group: System/Libraries
Summary:        SCIM tables for Vietnamese
Requires:       scim-tables = %{version}

%description vietnamese
This package contains scim-tables files for Vietnamese input.

%package additional
Group: System/Libraries
Summary:        Other miscellaneous SCIM tables
Requires:       scim-tables = %{version}

%description additional
This package contains some miscellaneous scim-tables.


%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
# Upstream did not provide any configure file
autoreconf -ivf
intltoolize --force
%configure --disable-static

# Fix source compilation error
sed -i '698s/#if /#ifdef /g' src/scim_table_imengine_setup.cpp

%make_build

%install
make DESTDIR=${RPM_BUILD_ROOT} install

# kill *.a and *.la files
rm -f ${RPM_BUILD_ROOT}/%{_libdir}/scim-1.0/*/*/*.la

%if !%{indic_tables}
rm ${RPM_BUILD_ROOT}/%{_datadir}/scim/{icons,tables}/{Bengali,Gujarati,Hindi,Kannada,Malayalam,Marathi,Punjabi,Tamil,Telugu}-*
%endif

%if !%{jk_tables}
rm ${RPM_BUILD_ROOT}/%{_datadir}/scim/{icons,tables}/{Hangul,Hanja,HIRAGANA,KATAKANA,Nippon}*
%endif

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/scim-make-table
%{_libdir}/scim-1.0/*/IMEngine/table.so
%{_libdir}/scim-1.0/*/SetupUI/table-imengine-setup.so
%{_datadir}/scim/icons/table.png
%dir %{_datadir}/scim/tables
%{_mandir}/man1/scim-make-table.1*


%files amharic
%{_datadir}/scim/tables/Amharic.bin
%{_datadir}/scim/icons/Amharic.png


%files arabic
%{_datadir}/scim/tables/Arabic.bin
%{_datadir}/scim/icons/Arabic.png


%if %{indic_tables}
%files bengali
%{_datadir}/scim/tables/Bengali-inscript.bin
%{_datadir}/scim/tables/Bengali-probhat.bin
%{_datadir}/scim/icons/Bengali-inscript.png
%{_datadir}/scim/icons/Bengali-probhat.png
%endif

%files chinese
%doc tables/zh/README-*.txt
%{_datadir}/scim/tables/Array30.bin
%{_datadir}/scim/icons/Array30.png
%{_datadir}/scim/tables/CangJie3.bin
%{_datadir}/scim/icons/CangJie3.png
%{_datadir}/scim/tables/CangJie5.bin
%{_datadir}/scim/tables/CantonHK.bin
%{_datadir}/scim/icons/CantonHK.png
%{_datadir}/scim/tables/Quick.bin
%{_datadir}/scim/icons/Quick.png
%{_datadir}/scim/tables/Wubi.bin
%{_datadir}/scim/icons/Wubi.png
%{_datadir}/scim/tables/ZhuYin.bin
%{_datadir}/scim/icons/ZhuYin.png

%files chinese-extra
%doc tables/zh/README-*.txt
%{_datadir}/scim/tables/CNS11643.bin
%{_datadir}/scim/icons/CNS11643.png
%{_datadir}/scim/tables/CangJie.bin
%{_datadir}/scim/icons/CangJie.png
%{_datadir}/scim/tables/Cantonese.bin
%{_datadir}/scim/icons/Cantonese.png
%{_datadir}/scim/tables/Dayi3.bin
%{_datadir}/scim/icons/Dayi.png
%{_datadir}/scim/tables/EZ-Big.bin
%{_datadir}/scim/icons/EZ.png
%{_datadir}/scim/tables/Erbi.bin
%{_datadir}/scim/icons/Erbi.png
%{_datadir}/scim/tables/Erbi-QS.bin
%{_datadir}/scim/icons/Erbi-QS.png
%{_datadir}/scim/tables/Jyutping.bin
%{_datadir}/scim/icons/Jyutping.png
%{_datadir}/scim/tables/Simplex.bin
%{_datadir}/scim/icons/Simplex.png
%{_datadir}/scim/tables/SmartCangJie6.bin
%{_datadir}/scim/icons/SmartCangJie6.png
%{_datadir}/scim/tables/Stroke5.bin
%{_datadir}/scim/icons/Stroke5.png
%{_datadir}/scim/tables/Wu.bin
%{_datadir}/scim/icons/Wu.png
%{_datadir}/scim/tables/ZhuYin-Big.bin
%{_datadir}/scim/icons/ZhuYin.png
%{_datadir}/scim/tables/Ziranma.bin
%{_datadir}/scim/icons/Ziranma.png


%if %{indic_tables}
%files gujarati
%{_datadir}/scim/tables/Gujarati-inscript.bin
%{_datadir}/scim/tables/Gujarati-phonetic.bin
%{_datadir}/scim/icons/Gujarati-inscript.png
%{_datadir}/scim/icons/Gujarati-phonetic.png

%files hindi
%{_datadir}/scim/tables/Hindi-inscript.bin
%{_datadir}/scim/tables/Hindi-phonetic.bin
%{_datadir}/scim/icons/Hindi-inscript.png
%{_datadir}/scim/icons/Hindi-phonetic.png
%endif

%if %{jk_tables}
%files japanese
%doc tables/ja/kanjidic*
%{_datadir}/scim/tables/HIRAGANA.bin
%{_datadir}/scim/tables/KATAKANA.bin
%{_datadir}/scim/tables/Nippon.bin
%{_datadir}/scim/icons/HIRAGANA.png
%{_datadir}/scim/icons/KATAKANA.png
%{_datadir}/scim/icons/Nippon.png
%endif


%if %{indic_tables}
%files kannada
%{_datadir}/scim/tables/Kannada-inscript.bin
%{_datadir}/scim/tables/Kannada-kgp.bin
%{_datadir}/scim/icons/Kannada-inscript.png
%{_datadir}/scim/icons/Kannada-kgp.png
%endif

%if %{jk_tables}
%files korean
%{_datadir}/scim/tables/Hangul.bin
%{_datadir}/scim/tables/HangulRomaja.bin
%{_datadir}/scim/tables/Hanja.bin
%{_datadir}/scim/icons/Hangul.png
%{_datadir}/scim/icons/Hanja.png
%endif


%if %{indic_tables}
%files malayalam
%{_datadir}/scim/tables/Malayalam-inscript.bin
%{_datadir}/scim/icons/Malayalam-inscript.png
%endif

%if %{indic_tables}
%files marathi
%{_datadir}/scim/tables/Marathi-remington.bin
%{_datadir}/scim/icons/Marathi-remington.png
%endif

%files nepali
%{_datadir}/scim/tables/Nepali_*.bin
%{_datadir}/scim/icons/Nepali.png


%if %{indic_tables}
%files punjabi
%{_datadir}/scim/tables/Punjabi-inscript.bin
%{_datadir}/scim/tables/Punjabi-jhelum.bin
%{_datadir}/scim/tables/Punjabi-phonetic.bin
%{_datadir}/scim/icons/Punjabi-inscript.png
%{_datadir}/scim/icons/Punjabi-jhelum.png
%{_datadir}/scim/icons/Punjabi-phonetic.png
%endif


%files russian
%{_datadir}/scim/tables/RussianTraditional.bin
%{_datadir}/scim/tables/Yawerty.bin
%{_datadir}/scim/tables/Translit.bin
%{_datadir}/scim/tables/RussianComputer.bin

%{_datadir}/scim/icons/RussianTraditional.png
%{_datadir}/scim/icons/Yawerty.png
%{_datadir}/scim/icons/Translit.png
%{_datadir}/scim/icons/RussianComputer.png


%if %{indic_tables}
%files tamil
%{_datadir}/scim/tables/Tamil-inscript.bin
%{_datadir}/scim/tables/Tamil-phonetic.bin
%{_datadir}/scim/icons/Tamil-inscript.png
%{_datadir}/scim/icons/Tamil-phonetic.png
%endif


%files thai
%{_datadir}/scim/tables/Thai.bin
%{_datadir}/scim/icons/Thai.png


%if %{indic_tables}
%files telugu
%{_datadir}/scim/tables/Telugu-inscript.bin
%{_datadir}/scim/icons/Telugu-inscript.png
%endif


%files ukrainian
%{_datadir}/scim/tables/Ukrainian-Translit.bin
%{_datadir}/scim/icons/Ukrainian-Translit.png


%files vietnamese
%{_datadir}/scim/tables/Viqr.bin
%{_datadir}/scim/icons/Viqr.png


%files additional
%{_datadir}/scim/tables/classicalhebrew.bin
%{_datadir}/scim/tables/HebrewComputer.bin
%{_datadir}/scim/tables/greekpoly.bin
%{_datadir}/scim/tables/IPA-X-SAMPA.bin
%{_datadir}/scim/tables/IPA-Kirshenbaum.bin
%{_datadir}/scim/tables/LaTeX.bin
%{_datadir}/scim/tables/Uyghur-Romanized.bin
%{_datadir}/scim/tables/Uyghur-Standard.bin
%{_datadir}/scim/icons/HebrewComputer.png
%{_datadir}/scim/icons/IPA-X-SAMPA.png
%{_datadir}/scim/icons/LaTeX.png
%{_datadir}/scim/icons/Uyghur.png

%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.14-alt1_3
- NMU (for oddity@): new version by fcimport

* Wed Nov 18 2015 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.5.12-alt2.qa1
- Rebuilt for gcc5 C++11 ABI.

* Wed Aug 27 2014 Ilya Mashkin <oddity@altlinux.ru> 0.5.12-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.12-alt1_3
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.12-alt1_2
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.12-alt1_1
- initial fc import

