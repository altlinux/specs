Group: System/Fonts/True type
%define oldname naver-nanum-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname naver-nanum
%global fontconf 65-0-%{fontname}

%global common_desc \
Nanum fonts are collection of commonly-used Myeongjo and Gothic Korean \
font families, designed by Sandoll Communication and Fontrix. The \
publisher is Naver Corporation.


Name:       fonts-ttf-naver-nanum
Version:    3.020
Release:    alt2_18.20140930
Summary:    Nanum family of Korean TrueType fonts

License:    OFL
URL:        http://hangeul.naver.com
Source0:    http://appdown.naver.com/naver/font/NanumFont/setup/NanumFontSetup_TTF_ALL_hangeulcamp.exe
Source1:    %{oldname}-barun-gothic-fontconfig.conf
Source2:    %{oldname}-barun-pen-fontconfig.conf
Source3:    %{oldname}-brush-fontconfig.conf
Source4:    %{oldname}-gothic-fontconfig.conf
Source5:    %{oldname}-myeongjo-fontconfig.conf
Source6:    %{oldname}-pen-fontconfig.conf
# License text was taken from the upstream web on May 13 2014:
# http://help.naver.com/ops/step2/faq.nhn?faqId=15879
Source7:    %{oldname}-license.txt
Source8:    %{fontname}-barun-gothic.metainfo.xml
Source9:    %{fontname}-barun-pen.metainfo.xml
Source10:   %{fontname}-brush.metainfo.xml
Source11:   %{fontname}-gothic.metainfo.xml
Source12:   %{fontname}.metainfo.xml
Source13:   %{fontname}-myeongjo.metainfo.xml
Source14:   %{fontname}-pen.metainfo.xml

BuildArch: noarch
BuildRequires: fontpackages-devel
BuildRequires: p7zip

Provides:   nhn-nanum-fonts = %{version}-%{release}
Obsoletes:  nhn-nanum-fonts < %{version}-%{release}
Source44: import.info

%description
%common_desc


%package -n fonts-ttf-naver-nanum-common
Group: System/Fonts/True type
Summary:   Common files of %{oldname}
Provides:  fonts-ttf-nhn-nanum-common = %{version}-%{release}
Obsoletes: fonts-ttf-nhn-nanum-common < %{version}-%{release}

%description -n fonts-ttf-naver-nanum-common
%common_desc

This package consists of files used by other %{oldname} packages.


%package -n fonts-ttf-naver-nanum-barun-gothic
Group: System/Fonts/True type
Summary:   Nanum fonts Barun Gothic font faces
Requires:  fonts-ttf-naver-nanum-common = %{version}-%{release}
Provides:  nhn-nanum-barun-gothic-fonts = %{version}-%{release}
Obsoletes: nhn-nanum-barun-gothic-fonts < %{version}-%{release}

%description -n fonts-ttf-naver-nanum-barun-gothic
%common_desc

This package consists of the Nanum fonts Barun Gothic font faces.

%files -n fonts-ttf-naver-nanum-barun-gothic
%{_fontconfig_templatedir}/%{fontconf}-barun-gothic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-barun-gothic.conf
%{_fontbasedir}/*/%{_fontstem}/NanumBarunGothic.ttf
%{_fontbasedir}/*/%{_fontstem}/NanumBarunGothicBold.ttf
%{_fontbasedir}/*/%{_fontstem}/NanumBarunGothicLight.ttf
%{_fontbasedir}/*/%{_fontstem}/NanumBarunGothicUltraLight.ttf
%{_datadir}/appdata/%{fontname}-barun-gothic.metainfo.xml

%package -n fonts-ttf-naver-nanum-barun-pen
Group: System/Fonts/True type
Summary:   Nanum fonts Barun Pen font faces
Requires:  fonts-ttf-naver-nanum-common = %{version}-%{release}
Provides:  nhn-nanum-barun-pen-fonts = %{version}-%{release}
Obsoletes: nhn-nanum-barun-pen-fonts < %{version}-%{release}

%description -n fonts-ttf-naver-nanum-barun-pen
%common_desc

This package consists of the Nanum fonts Barun Pen font faces.

%files -n fonts-ttf-naver-nanum-barun-pen
%{_fontconfig_templatedir}/%{fontconf}-barun-pen.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-barun-pen.conf
%{_fontbasedir}/*/%{_fontstem}/NanumBarunpenR.ttf
%{_fontbasedir}/*/%{_fontstem}/NanumBarunpenB.ttf
%{_datadir}/appdata/%{fontname}-barun-pen.metainfo.xml

%package -n fonts-ttf-naver-nanum-brush
Group: System/Fonts/True type
Summary:   Nanum fonts Brush font faces
Requires:  fonts-ttf-naver-nanum-common = %{version}-%{release}
Provides:  fonts-ttf-nhn-nanum-brush = %{version}-%{release}
Obsoletes: fonts-ttf-nhn-nanum-brush < %{version}-%{release}

%description -n fonts-ttf-naver-nanum-brush
%common_desc

This package consists of the Nanum fonts Brush font faces.

%files -n fonts-ttf-naver-nanum-brush
%{_fontconfig_templatedir}/%{fontconf}-brush.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-brush.conf
%{_fontbasedir}/*/%{_fontstem}/NanumBrush.ttf
%{_datadir}/appdata/%{fontname}-brush.metainfo.xml

%package -n fonts-ttf-naver-nanum-gothic
Group: System/Fonts/True type
Summary:   Nanum fonts Gothic font faces
Requires:  fonts-ttf-naver-nanum-common = %{version}-%{release}
Provides:  fonts-ttf-nhn-nanum-gothic = %{version}-%{release}
Obsoletes: fonts-ttf-nhn-nanum-gothic < %{version}-%{release}

%description -n fonts-ttf-naver-nanum-gothic
%common_desc

This package consists of the Nanum fonts Gothic font faces.

%files -n fonts-ttf-naver-nanum-gothic
%{_fontconfig_templatedir}/%{fontconf}-gothic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-gothic.conf
%{_fontbasedir}/*/%{_fontstem}/NanumGothic.ttf
%{_fontbasedir}/*/%{_fontstem}/NanumGothicBold.ttf
%{_fontbasedir}/*/%{_fontstem}/NanumGothicExtraBold.ttf
%{_fontbasedir}/*/%{_fontstem}/NanumGothicLight.ttf
%{_datadir}/appdata/%{fontname}-gothic.metainfo.xml

%package -n fonts-ttf-naver-nanum-myeongjo
Group: System/Fonts/True type
Summary:   Nanum fonts Myeongjo font faces
Requires:  fonts-ttf-naver-nanum-common = %{version}-%{release}
Provides:  fonts-ttf-nhn-nanum-myeongjo = %{version}-%{release}
Obsoletes: fonts-ttf-nhn-nanum-myeongjo < %{version}-%{release}

%description -n fonts-ttf-naver-nanum-myeongjo
%common_desc

This package consists of the Nanum fonts Myeongjo font faces.

%files -n fonts-ttf-naver-nanum-myeongjo
%{_fontconfig_templatedir}/%{fontconf}-myeongjo.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-myeongjo.conf
%{_fontbasedir}/*/%{_fontstem}/NanumMyeongjo.ttf
%{_fontbasedir}/*/%{_fontstem}/NanumMyeongjoBold.ttf
%{_fontbasedir}/*/%{_fontstem}/NanumMyeongjoExtraBold.ttf
%{_datadir}/appdata/%{fontname}-myeongjo.metainfo.xml

%package -n fonts-ttf-naver-nanum-pen
Group: System/Fonts/True type
Summary:   Nanum fonts Pen font faces
Requires:  fonts-ttf-naver-nanum-common = %{version}-%{release}
Provides:  fonts-ttf-nhn-nanum-pen = %{version}-%{release}
Obsoletes: fonts-ttf-nhn-nanum-pen < %{version}-%{release}

%description -n fonts-ttf-naver-nanum-pen
%common_desc

This package consists of the Nanum fonts Pen font faces.

%files -n fonts-ttf-naver-nanum-pen
%{_fontconfig_templatedir}/%{fontconf}-pen.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-pen.conf
%{_fontbasedir}/*/%{_fontstem}/NanumPen.ttf
%{_datadir}/appdata/%{fontname}-pen.metainfo.xml

%prep
%setup -n %{oldname}-%{version} -c -T
7z x %{SOURCE0}
mv \$WINDIR/Fonts/*.ttf .
cp -p %{SOURCE7} COPYING


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
     %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-barun-gothic.conf
install -m 0644 -p %{SOURCE2} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-barun-pen.conf
install -m 0644 -p %{SOURCE3} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-brush.conf
install -m 0644 -p %{SOURCE4} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gothic.conf
install -m 0644 -p %{SOURCE5} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-myeongjo.conf
install -m 0644 -p %{SOURCE6} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pen.conf

for fconf in %{fontconf}-barun-gothic.conf \
    %{fontconf}-barun-pen.conf \
    %{fontconf}-brush.conf \
    %{fontconf}-gothic.conf \
    %{fontconf}-myeongjo.conf \
    %{fontconf}-pen.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
     %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE8} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-barun-gothic.metainfo.xml
install -Dm 0644 -p %{SOURCE9} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-barun-pen.metainfo.xml
install -Dm 0644 -p %{SOURCE10} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-brush.metainfo.xml
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-gothic.metainfo.xml
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE13} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-myeongjo.metainfo.xml
install -Dm 0644 -p %{SOURCE14} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-pen.metainfo.xml
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
    esac
    find $RPM_BUILD_ROOT/usr/share/fonts -type f -name '*.'$fontpatt | while read i; do
	j=`echo "$i" | sed -e s,/usr/share/fonts/,/usr/share/fonts/$type/,`;
	install -Dm644 "$i" "$j";
	rm -f "$i";
	olddir=`dirname "$i"`;
	mv -f "$olddir"/{encodings.dir,fonts.{dir,scale,alias}} `dirname "$j"`/ 2>/dev/null ||:
	rmdir -p "$olddir" 2>/dev/null ||:
    done
done
# kill invalid catalogue links
if [ -d $RPM_BUILD_ROOT/etc/X11/fontpath.d ]; then
    find -L $RPM_BUILD_ROOT/etc/X11/fontpath.d -type l -print -delete ||:
    # relink catalogue
    find $RPM_BUILD_ROOT/usr/share/fonts -name fonts.dir | while read i; do
	pri=10;
	j=`echo $i | sed -e s,$RPM_BUILD_ROOT/usr/share/fonts/,,`; type=${j%%%%/*}; 
	pre_stem=${j##$type/}; stem=`dirname $pre_stem|sed -e s,/,-,g`;
	case "$type" in 
	    bitmap) pri=10;;
	    ttf|ttf) pri=50;;
	    type1) pri=40;;
	esac
	ln -s /usr/share/fonts/$j $RPM_BUILD_ROOT/etc/X11/fontpath.d/"$stem:pri=$pri"
    done ||:
fi

%files -n fonts-ttf-naver-nanum-common
%doc COPYING
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Sun Dec 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.020-alt2_18.20140930
- fixed provides/obsoletes

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 3.020-alt1_18.20140930
- update to new release by fcimport

* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 3.020-alt1_15.20140930
- new version

