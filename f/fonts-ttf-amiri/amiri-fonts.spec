Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname amiri-fonts
%global fontname amiri

%global common_desc \
Amiri is a classical Arabic typeface in Naskh style for typesetting books \
and other running text. \
 \
Amiri is a revival of the beautiful typeface pioneered in early 20th \
century by Bulaq Press in Cairo, also known as Amiria Press, after which \
the font is named.

%global common_desc_ar \
O.U.O.O. O.U.O.U.U.O.U. O.O. U.O.O.U. U.U.O.U. U.O.O.O.O.O. O.U.U.O.O. U.O.U.U.O.U.O. O.U.O.U.U.U.O.. \
O.U.O.O. O.U.O.U.U.O.U. U.U. O.O.U.O.O. U.U.O.O.U.O.O. U.U.O.O. O.U.O.O.O.O.U. O.U.O.U.U.U. O.U.O.U. \
O.U.U.O.O. O.U. U.O.O.O.O. O.U.U.O.U. U.U.O. O.U.O.O.U. O.U.U.O.U. O.U.O.O.O.U.U.O. U.O.U.O.U. O.O.U.O. \
O.U.O.U.O. O.O.U.U.O.O.O.O. O.U.O.U.U.O.U.O.O. U.U.U. U.U.O. O.O.O. O.U.O.O. O.O.U.U..

Name: fonts-ttf-amiri
Version: 0.108
Release: alt1_1
License: OFL

Source0: https://github.com/khaledhosny/amiri-font/releases/download/%{version}/%{fontname}-%{version}.zip
Source1: %{fontname}-quran-fontconfig.conf
Source2: %{fontname}-fontconfig.conf

BuildArch: noarch
BuildRequires: fontpackages-devel
Requires: %{name}-common = %{version}-%{release}

Summary: A classical Arabic font in Naskh style
Summary(ar): الخطوط الأميرية ذات المظهر الأنيق و التّراث العريق
URL: http://www.amirifont.org
Source44: import.info

%description
%common_desc

%description -l ar
%common_desc_ar

%package -n fonts-ttf-amiri-common
Group: System/Fonts/True type

Summary: Common files for %{oldname}
Summary(ar): الملفات العامّة للخطوط الأميرية

%description -n fonts-ttf-amiri-common
%common_desc

This package consists of files used by other %{oldname} packages.

%description -n fonts-ttf-amiri-common -l ar
%common_desc_ar

تتألف هذه الحزمة من ملفات الخط الأميري العامة.

%package -n fonts-ttf-amiri-quran
Group: System/Fonts/True type
Summary: Quran type of Amiri fonts
Summary(ar): النّمط القُرآني من الخط الأميري
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-amiri-quran
%common_desc

This package contains Quran type of Amiri fonts.
%description -n fonts-ttf-amiri-quran -l ar
%common_desc_ar

تحتوي هذه الحُزمة على النّمط القرآني من الخط الأميري.

%prep
%setup -q -n %{fontname}-%{version}

%build
#Nothing to build

%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/67-%{fontname}-quran.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/67-%{fontname}.conf

for fontconf in 67-%{fontname}-quran.conf \
                67-%{fontname}.conf ; do
  ln -s %{_fontconfig_templatedir}/$fontconf \
        %{buildroot}%{_fontconfig_confdir}/$fontconf
done
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

%files -n fonts-ttf-amiri-quran
%{_fontconfig_templatedir}/67-%{fontname}-quran.conf
%config(noreplace) %{_fontconfig_confdir}/67-%{fontname}-quran.conf
%{_fontbasedir}/*/%{_fontstem}/amiri-quran.ttf
%{_fontbasedir}/*/%{_fontstem}/amiri-quran-colored.ttf

%files
%{_fontconfig_templatedir}/67-%{fontname}.conf
%config(noreplace) %{_fontconfig_confdir}/67-%{fontname}.conf
%{_fontbasedir}/*/%{_fontstem}/amiri-regular.ttf
%{_fontbasedir}/*/%{_fontstem}/amiri-slanted.ttf
%{_fontbasedir}/*/%{_fontstem}/amiri-bold.ttf
%{_fontbasedir}/*/%{_fontstem}/amiri-boldslanted.ttf

%files -n fonts-ttf-amiri-common
%doc OFL.txt
%doc amiri-table.pdf NEWS README README-Arabic NEWS-Arabic documentation-arabic.pdf

%changelog
* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.108-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.107-alt1_3
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.107-alt1_2
- converted for ALT Linux by srpmconvert tools

