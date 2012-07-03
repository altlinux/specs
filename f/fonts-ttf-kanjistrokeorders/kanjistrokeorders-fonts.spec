# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname kanjistrokeorders-fonts
%define version 2.016
%define name kanjistrokeorders-fonts
%global fontname kanjistrokeorders
%global fontconf 69-%{fontname}.conf
%global archivename KanjiStrokeOrders_v%{version}

Name:    fonts-ttf-kanjistrokeorders
Version: 2.016
Release: alt2_2
Summary: Font to view stroke order diagrams for Kanji, Kana and etc
License: BSD
Group:   System/Fonts/True type
URL:     http://sites.google.com/site/nihilistorguk/
Source0: http://sites.google.com/site/nihilistorguk/Home/%{archivename}.zip
Source1: %{oldname}-fontconfig.conf
BuildArch: noarch
BuildRequires: fontpackages-devel
Source44: import.info
%description
This font will assist people who are learning kanji, and will help teachers of
Japanese in the preparation of classroom material.
In the parts of your document where you want the kanji to be annotated with
stroke order numbers simply set your document s font to KanjiStrokeOrders.
You will need to set the size of the font to be large to allow the stroke
order numbers to show up: 100pt seems to be the minimum usable size.


%prep
%setup -q -c
sed -i 's#\r##g' copyright.txt
sed -i 's#\r##g' readme_en_v%{version}.txt

%build
%{nil}


%install

install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p *.ttf $RPM_BUILD_ROOT%{_fontdir}

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
%{_fontbasedir}/*/%{_fontstem}/*.ttf
%doc *.pdf *.txt


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.016-alt2_2
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 2.016-alt1_2
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.016-alt1_1
- rebuild with new rpm-build-fonts

* Sun Aug 07 2011 Igor Vlasenko <viy@altlinux.ru> 2.015-alt1_2
- initial release by fcimport

