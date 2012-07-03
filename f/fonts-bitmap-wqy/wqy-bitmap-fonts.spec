%define oldname wqy-bitmap-fonts
%define fontname  wqy-bitmap
%define fontconf  61-wqy-bitmapsong.conf
%define wqyroot   wqy-bitmapsong

Name:           fonts-bitmap-wqy
Version:        1.0.0
Release:        alt3_0.3.rc1
Summary:        WenQuanYi Bitmap Chinese Fonts

Group:          System/Fonts/True type
License:        GPLv2 with exceptions
URL:            http://wenq.org/enindex.cgi
Source0:        http://downloads.sourceforge.net/wqy/wqy-bitmapsong-bdf-1.0.0-RC1.tar.gz
Source1:        61-wqy-bitmapsong.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel bdftopcf
Source44: import.info

%description
WenQuanYi bitmap fonts include all 20,932 Unicode 5.2
CJK Unified Ideographs (U4E00 - U9FA5) and 6,582
CJK Extension A characters (U3400 - U4DB5) at
5 different pixel sizes (9pt-12X12, 10pt-13X13,
10.5pt-14x14, 11pt-15X15 and 12pt-16x16 pixel).
Use of this bitmap font for on-screen display of Chinese
(traditional and simplified) in web pages and elsewhere
eliminates the annoying "blurring" problems caused by
insufficient "hinting" of anti-aliased vector CJK fonts.
In addition, Latin characters, Japanese Kanas and
Korean Hangul glyphs (U+AC00~U+D7A3) are also included.

%prep
%setup -q -n %{wqyroot}


%build
make wqyv1


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.pcf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}
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
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.pcf

%doc AUTHORS ChangeLog COPYING README LOGO.png
%dir %{_fontbasedir}/*/%{_fontstem}


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_0.3.rc1
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.3.rc1
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.2.rc1
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.2.rc1
- initial release by fcimport

