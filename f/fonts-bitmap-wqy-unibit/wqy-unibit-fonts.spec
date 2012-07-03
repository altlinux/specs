%define oldname wqy-unibit-fonts
%define fontname wqy-unibit

Name:           fonts-bitmap-wqy-unibit
Version:        1.1.0
Release:        alt3_9
Summary:        WenQuanYi Unibit Bitmap Font

Group:          System/Fonts/True type
License:        GPLv2 with exceptions
URL:            http://wenq.org/enindex.cgi
Source0:        http://downloads.sourceforge.net/wqy/wqy-unibit-bdf-%{version}-1.tar.gz

BuildArch:      noarch
BuildRequires:  fontpackages-devel bdftopcf
Source44: import.info

%description
The Wen Quan Yi Unibit is designed as a dual-width (16x16,16x8) 
bitmap font to provide the most complete international symbol 
coverage, serving as the system-wide fall-back font. This font 
has covered over 46000 Unicode code points in BMP.
It is intended to supersede the outdated GNU Unifont.
This font was created by merging the latest update of GNU 
Unifont [GPL] (by Roman Czyborra and David Starner et al., the 
font was last updated in 2004), WenQuanYi Bitmap Song [GPL] 
0.8.1 (by Qianqian Fang and WenQuanYi contributors) and 
Fixed-16x8 [public domain] bitmap fonts from X11 core fonts. 
The entire CJK Unified Ideographics (U4E00-U9FA5) and CJK Unified 
Ideographics Extension A(U3400-U4DB5) blocks were replaced by 
high-quality glyphs from China National Standard GB19966-2005 
(public domain). Near a thousand of non-CJK characters were improved by 
WenQuanYi contributors via their collaborative font editing website at
http://wenq.org/eindex.cgi?Unicode_Chart_EN

%prep
%setup -q -n %{fontname}


%build
make

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.pcf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz afm pfa pfb; do
    case "$fontpatt" in 
	pcf*) type=bitmap;;
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


%files
%{_fontbasedir}/*/%{_fontstem}/*.pcf

%doc AUTHORS ChangeLog COPYING README
%dir %{_fontbasedir}/*/%{_fontstem}


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt3_9
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_9
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_8
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_8
- initial release by fcimport

