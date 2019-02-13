Group: System/Fonts/True type
%define oldname google-noto-cjk-fonts
%define fedora 28
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit0 32a5844539f2e348ed36b44e990f9b06d7fb89fe
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global fontname google-noto-cjk
%global fontconf google-noto

%global common_desc \
Noto CJK fonts, supporting Simplified Chinese, Traditional Chinese, \
Japanese, and Korean. The supported scripts are Han, Hiragana, Katakana, \
Hangul, and Bopomofo. Latin, Greek, Cyrllic, and various symbols are also \
supported for compatibility with CJK standards. \
%{nil}

Name:           fonts-otf-google-noto-cjk
Version:        20170602
Release:        alt1_9
Summary:        Google Noto Sans CJK Fonts

License:        OFL
URL:            https://github.com/googlei18n/noto-cjk
Source0:        https://github.com/googlei18n/noto-cjk/archive/%{commit0}.tar.gz#/noto-cjk-%{shortcommit0}.tar.gz
Source1:        genfontconf.py
Source2:        genfontconf.sh

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  python3
BuildRequires:  /usr/bin/xmllint
Requires:       fonts-otf-google-noto-sans-cjk-ttc
Requires:       fonts-otf-google-noto-serif-cjk-ttc

%if 0%{?fedora}

Obsoletes:      google-noto-sans-cjk-fonts < 20150617
Provides:       google-noto-sans-cjk-fonts = 20150617

# notocjkrep Package Name
%define notocjkrep(:)\
%define pname %(echo %{*} | tr "A-Z " "a-z-")\
Obsoletes:      google-noto-%{pname}-fonts < 20150617\
Provides:       google-noto-%{pname}-fonts = 20150617\
Obsoletes:      google-noto-cjk-%{pname}-fonts < %{version}-%{release}\
Provides:       google-noto-cjk-%{pname}-fonts = %{version}-%{release}\


%notocjkrep Sans Simplified Chinese
%notocjkrep Sans Traditional Chinese
%notocjkrep Sans Japanese
%notocjkrep Sans Korean

%endif
Source44: import.info


%description
%common_desc

%package -n fonts-otf-google-noto-cjk-common
Group: System/Fonts/True type
Summary:        Common files for Noto CJK fonts

%description -n fonts-otf-google-noto-cjk-common
%common_desc

%package -n fonts-otf-google-noto-sans-cjk-ttc
Summary:	Sans OTC font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-sans-cjk-ttc
%common_desc
Noto font Sans OTC.

%files -n fonts-otf-google-noto-sans-cjk-ttc
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSansCJK-*.ttc
%{_fontconfig_templatedir}/65-0-%{fontconf}-sans-cjk-ttc.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-%{fontconf}-sans-cjk-ttc.conf

%package -n fonts-otf-google-noto-serif-cjk-ttc
Summary:	Serif OTC font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-serif-cjk-ttc
%common_desc
Noto font Serif OTC.

%files -n fonts-otf-google-noto-serif-cjk-ttc
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSerifCJK-*.ttc
%{_fontconfig_templatedir}/65-0-%{fontconf}-serif-cjk-ttc.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-%{fontconf}-serif-cjk-ttc.conf

%package -n fonts-otf-google-noto-sans-cjk-jp
Summary:	Japanese Multilingual Sans OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-sans-cjk-jp
%common_desc
Noto font Japanese Multilingual Sans OTF.

%files -n fonts-otf-google-noto-sans-cjk-jp
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSansCJKjp-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cjk-jp.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cjk-jp.conf

%package -n fonts-otf-google-noto-serif-cjk-jp
Summary:	Japanese Multilingual Serif OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-serif-cjk-jp
%common_desc
Noto font Japanese Multilingual Serif OTF.

%files -n fonts-otf-google-noto-serif-cjk-jp
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSerifCJKjp-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-cjk-jp.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-cjk-jp.conf

%package -n fonts-otf-google-noto-sans-mono-cjk-jp
Summary:	Japanese Multilingual Sans Mono OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-sans-mono-cjk-jp
%common_desc
Noto font Japanese Multilingual Sans Mono OTF.

%files -n fonts-otf-google-noto-sans-mono-cjk-jp
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSansMonoCJKjp-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mono-cjk-jp.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mono-cjk-jp.conf

%package -n fonts-otf-google-noto-sans-cjk-kr
Summary:	Korean Multilingual Sans OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-sans-cjk-kr
%common_desc
Noto font Korean Multilingual Sans OTF.

%files -n fonts-otf-google-noto-sans-cjk-kr
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSansCJKkr-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cjk-kr.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cjk-kr.conf

%package -n fonts-otf-google-noto-serif-cjk-kr
Summary:	Korean Multilingual Serif OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-serif-cjk-kr
%common_desc
Noto font Korean Multilingual Serif OTF.

%files -n fonts-otf-google-noto-serif-cjk-kr
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSerifCJKkr-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-cjk-kr.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-cjk-kr.conf

%package -n fonts-otf-google-noto-sans-mono-cjk-kr
Summary:	Korean Multilingual Sans Mono OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-sans-mono-cjk-kr
%common_desc
Noto font Korean Multilingual Sans Mono OTF.

%files -n fonts-otf-google-noto-sans-mono-cjk-kr
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSansMonoCJKkr-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mono-cjk-kr.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mono-cjk-kr.conf

%package -n fonts-otf-google-noto-sans-cjk-sc
Summary:	Simplified Chinese Multilingual Sans OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-sans-cjk-sc
%common_desc
Noto font Simplified Chinese Multilingual Sans OTF.

%files -n fonts-otf-google-noto-sans-cjk-sc
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSansCJKsc-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cjk-sc.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cjk-sc.conf

%package -n fonts-otf-google-noto-serif-cjk-sc
Summary:	Simplified Chinese Multilingual Serif OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-serif-cjk-sc
%common_desc
Noto font Simplified Chinese Multilingual Serif OTF.

%files -n fonts-otf-google-noto-serif-cjk-sc
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSerifCJKsc-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-cjk-sc.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-cjk-sc.conf

%package -n fonts-otf-google-noto-sans-mono-cjk-sc
Summary:	Simplified Chinese Multilingual Sans Mono OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-sans-mono-cjk-sc
%common_desc
Noto font Simplified Chinese Multilingual Sans Mono OTF.

%files -n fonts-otf-google-noto-sans-mono-cjk-sc
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSansMonoCJKsc-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mono-cjk-sc.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mono-cjk-sc.conf

%package -n fonts-otf-google-noto-sans-cjk-tc
Summary:	Traditional Chinese Multilingual Sans OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-sans-cjk-tc
%common_desc
Noto font Traditional Chinese Multilingual Sans OTF.

%files -n fonts-otf-google-noto-sans-cjk-tc
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSansCJKtc-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cjk-tc.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cjk-tc.conf

%package -n fonts-otf-google-noto-serif-cjk-tc
Summary:	Traditional Chinese Multilingual Serif OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-serif-cjk-tc
%common_desc
Noto font Traditional Chinese Multilingual Serif OTF.

%files -n fonts-otf-google-noto-serif-cjk-tc
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSerifCJKtc-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-cjk-tc.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-cjk-tc.conf

%package -n fonts-otf-google-noto-sans-mono-cjk-tc
Summary:	Traditional Chinese Multilingual Sans Mono OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-sans-mono-cjk-tc
%common_desc
Noto font Traditional Chinese Multilingual Sans Mono OTF.

%files -n fonts-otf-google-noto-sans-mono-cjk-tc
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSansMonoCJKtc-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mono-cjk-tc.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mono-cjk-tc.conf

%package -n fonts-otf-google-noto-sans-jp
Summary:	Japanese Region-specific Sans OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-sans-jp
%common_desc
Noto font Japanese Region-specific Sans OTF.

%files -n fonts-otf-google-noto-sans-jp
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSansJP-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-jp.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-jp.conf

%package -n fonts-otf-google-noto-serif-jp
Summary:	Japanese Region-specific Serif OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-serif-jp
%common_desc
Noto font Japanese Region-specific Serif OTF.

%files -n fonts-otf-google-noto-serif-jp
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSerifJP-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-jp.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-jp.conf

%package -n fonts-otf-google-noto-sans-kr
Summary:	Korean Region-specific Sans OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-sans-kr
%common_desc
Noto font Korean Region-specific Sans OTF.

%files -n fonts-otf-google-noto-sans-kr
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSansKR-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kr.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kr.conf

%package -n fonts-otf-google-noto-serif-kr
Summary:	Korean Region-specific Serif OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-serif-kr
%common_desc
Noto font Korean Region-specific Serif OTF.

%files -n fonts-otf-google-noto-serif-kr
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSerifKR-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-kr.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-kr.conf

%package -n fonts-otf-google-noto-sans-sc
Summary:	Simplified Chinese Region-specific Sans OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-sans-sc
%common_desc
Noto font Simplified Chinese Region-specific Sans OTF.

%files -n fonts-otf-google-noto-sans-sc
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSansSC-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-sc.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-sc.conf

%package -n fonts-otf-google-noto-serif-sc
Summary:	Simplified Chinese Region-specific Serif OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-serif-sc
%common_desc
Noto font Simplified Chinese Region-specific Serif OTF.

%files -n fonts-otf-google-noto-serif-sc
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSerifSC-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-sc.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-sc.conf

%package -n fonts-otf-google-noto-sans-tc
Summary:	Traditional Chinese Region-specific Sans OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-sans-tc
%common_desc
Noto font Traditional Chinese Region-specific Sans OTF.

%files -n fonts-otf-google-noto-sans-tc
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSansTC-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tc.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tc.conf

%package -n fonts-otf-google-noto-serif-tc
Summary:	Traditional Chinese Region-specific Serif OTF font files for %{oldname}
Group:		System/Fonts/True type
Requires:	fonts-otf-%{fontname}-common = %EVR

%description -n fonts-otf-google-noto-serif-tc
%common_desc
Noto font Traditional Chinese Region-specific Serif OTF.

%files -n fonts-otf-google-noto-serif-tc
%dir %_otffontsdir/%{fontname}
%_otffontsdir/%{fontname}/NotoSerifTC-*.otf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-tc.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-tc.conf

%prep
%setup -q -n noto-cjk-%{commit0}
cp -p %{SOURCE1} %{SOURCE2} .
# generate the font conf files
bash -x ./genfontconf.sh


%build


%install
%define _fontdir  %_otffontsdir/%{fontname}
install -m 0755 -d %{buildroot}%{_fontdir}

# copy OTC files
install -m 0644 -p NotoSansCJK-*.ttc %{buildroot}%{_fontdir}
install -m 0644 -p NotoSerifCJK-*.ttc %{buildroot}%{_fontdir}

# copy Multilingual OTF files
install -m 0644 -p NotoSansCJK{jp,kr,sc,tc}-*.otf %{buildroot}%{_fontdir}
install -m 0644 -p NotoSerifCJK{jp,kr,sc,tc}-*.otf %{buildroot}%{_fontdir}
install -m 0644 -p NotoSansMonoCJK{jp,kr,sc,tc}-*.otf %{buildroot}%{_fontdir}

# copy Region-specific OTF
install -m 0644 -p NotoSans{JP,KR,SC,TC}-*.otf %{buildroot}%{_fontdir}
install -m 0644 -p NotoSerif{JP,KR,SC,TC}-*.otf %{buildroot}%{_fontdir}


install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
            %{buildroot}%{_fontconfig_confdir}

for f in sans-cjk-ttc serif-cjk-ttc \
    sans-cjk-jp serif-cjk-jp sans-mono-cjk-jp \
    sans-cjk-kr serif-cjk-kr sans-mono-cjk-kr \
    sans-cjk-sc serif-cjk-sc sans-mono-cjk-sc \
    sans-cjk-tc serif-cjk-tc sans-mono-cjk-tc \
    sans-jp serif-jp \
    sans-kr serif-kr \
    sans-sc serif-sc \
    sans-tc serif-tc;
do
    fconf=$(basename -a *-%{fontconf}-$f.conf)
    if [ "$(echo $fconf | wc -w)" -ne 1 ]; then
       echo "Did not find unique \*-%{fontconf}-$f.conf file"
       exit 1
    fi

    install -m 0644 -p ${fconf} \
                %{buildroot}%{_fontconfig_templatedir}/${fconf}

    ln -s %{_fontconfig_templatedir}/${fconf} \
         %{buildroot}%{_fontconfig_confdir}/${fconf}
done

%files


%files -n fonts-otf-google-noto-cjk-common
%doc NEWS HISTORY README.formats README.third_party
%doc --no-dereference LICENSE


%changelog
* Mon Feb 11 2019 Igor Vlasenko <viy@altlinux.ru> 20170602-alt1_9
- added font subpackages

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 20170602-alt1_2
- update to new release by fcimport

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_5
- converted for ALT Linux by srpmconvert tools

