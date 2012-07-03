# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname gdouros-aegean-fonts
%global fontname gdouros-aegean
%global fontconf 65-%{fontname}.conf

Name:           fonts-otf-gdouros-aegean
Version:        3.02
Release:        alt3_3
Summary:        A font for ancient scripts in the greater Aegean vicinity

Group:          System/Fonts/True type
License:        Copyright only
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Aegean302.zip
Source1:        %{oldname}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
Aegean covers the following scripts and symbols supported by The Unicode
Standard 5.2: Basic Latin, Greek and Coptic, Greek Extended, some Punctuation
and other Symbols, Linear B Syllabary, Linear B Ideograms, Aegean Numbers,
Ancient Greek Numbers, Ancient Symbols, Phaistos Disc, Lycian, Carian, Old
Italic, Ugaritic, Old Persian, Cypriot Syllabary, Phoenician, Lydian, and
Archaic Greek Musical Notation.

Aegean also covers the following scripts and symbols not yet supported by
Unicode: Cretan Hieroglyphs, Cypro-Minoan, Linear A, the Arkalochori Axe,
Ancient Greek and Old Italic variant alphabets. These are allocated in the
Supplementary Private Use Plane 15.

It was created by George Douros.

%prep
%setup -q -c


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Aegean.otf %{buildroot}%{_fontdir}

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
%{_fontbasedir}/*/%{_fontstem}/Aegean.otf

%doc Aegean302.txt


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.02-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.02-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 3.02-alt2_2
- rebuild with new rpm-build-fonts

* Tue Aug 02 2011 Igor Vlasenko <viy@altlinux.ru> 3.02-alt1_2
- initial release by fcimport

