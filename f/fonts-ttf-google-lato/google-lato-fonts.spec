%define oldname google-lato-fonts
%global fontname google-lato
%global fontconf 61-%{fontname}.conf

Name:           fonts-ttf-google-lato
Version:        1.011
Release:        alt3_3
Summary:        A sanserif typeface family

Group:          System/Fonts/True type
License:        OFL
URL:            http://code.google.com/webfonts/family?family=Lato
Source0:        %{oldname}-%{version}.tar.bz2
# Most recent versions of the fonts are in the Google Font Directory Mercurial
# repository. To retrieve them, invoke this script.
Source1:        %{oldname}-generate-tarball.sh
Source2:        %{oldname}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
Lato is a sanserif typeface family designed in the Summer 2010 by Warsaw-based
designer A.ukasz Dziedzic ("Lato" means "Summer" in Polish). In December 2010 the
Lato family was published under the open-source Open Font License by his foundry
tyPoland, with support from Google.

When working on Lato, A.ukasz tried to carefully balance some potentially
conflicting priorities. He wanted to create a typeface that would seem quite
"transparent" when used in body text but would display some original treats when
used in larger sizes. He used classical proportions (particularly visible in the
uppercase) to give the letterforms familiar harmony and elegance. At the same
time, he created a sleek sanserif look, which makes evident the fact that Lato
was designed in 2010 - even though it does not follow any current trend.

The semi-rounded details of the letters give Lato a feeling of warmth, while the
strong structure provides stability and seriousness. "Male and female, serious
but friendly. With the feeling of the Summer," says A.ukasz.

Lato consists of five weights (plus corresponding italics), including a
beautiful hairline style. The first release only includes the Western character
set, but pan-European Latin, Cyrillic and Greek extensions, as well as small
caps and other typographic niceties are expected in 2011.


%prep
%setup -q -n %{oldname}-%{version}

# Fix wrong end-of-lines encoding
sed "s/\r//" OFL.txt > OFL.txt.new
touch -r OFL.txt OFL.txt.new
mv OFL.txt.new OFL.txt


%build


%install
rm -fr $RPM_BUILD_ROOT

install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p *.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d $RPM_BUILD_ROOT%{_fontconfig_templatedir} $RPM_BUILD_ROOT%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} $RPM_BUILD_ROOT%{_fontconfig_confdir}/%{fontconf}
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
%doc OFL.txt


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.011-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.011-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.011-alt2_2
- rebuild with new rpm-build-fonts

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.011-alt1_2
- initial release by fcimport

