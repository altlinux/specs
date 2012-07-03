# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname gfs-complutum-fonts
%global fontname gfs-complutum
%global fontconf 61-%{fontname}.conf

%global archivename GFS_COMPLUTUM_OT

Name:    fonts-otf-gfs-complutum
Version: 20070413
Release: alt3_15
Summary: GFS Complutum Greek font

Group:     System/Fonts/True type
License:   OFL
URL:       http://www.greekfontsociety.gr/pages/en_typefaces16th.html
Source0:   http://www.greekfontsociety.gr/%{archivename}.zip
Source1:   %{oldname}-fontconfig.conf


BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
The ancient Greek alphabet evolved during the millenium of the Byzantine era
from majuscule to minuscule form and gradually incorporated a wide array of
ligatures, flourishes and other decorative nuances which defined its
extravagant cursive character. Until the late 15th century, typographers who
had to deal with Greek text avoided emulating this complicated hand; instead
they would use only the twenty four letters of the alphabet separately, often
without accents and other diacritics.

A celebrated example is the type cut and cast for the typesetting of the New
Testament in the so-called Complutensian Polyglot Bible (1512), edited by the
Greek scholar, Demetrios Doukas. The type was cut by Arnaldo GuillA.n de Brocar
and the whole edition was a commision by cardinal Francisco XimA.nez, in the
University of AlcalA. (Complutum), Spain. It is one of the best and most
representative models of this early tradition in Greek typography which was
revived in the early 20th century by the eminent bibliographer of the British
Library, Richard Proctor. A font named Otter Greek was cut in 1903 and a book
was printed using the new type. The original type had no capitals so Proctor
added his own, which were rather large and ill-fitted. The early death of
Proctor, the big size of the font and the different aesthetic notions of the
time were the reasons that Otter Greek was destined to oblivion, as a
curiosity.

Greek Font Society incorporated Brocar's famous and distinctive type in the
commemorative edition of Pindar's Odes for the Athens Olympics (2004) and the
type with a new set of capitals, revived digitaly by George D. Matthiopoulos,
is now available for general use.


%prep
%setup -q -c -T
unzip -j -L -q %{SOURCE0}
chmod 0644 *.txt
for txt in *.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

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
%{_fontbasedir}/*/%{_fontstem}/*.otf

%doc *.txt *.pdf


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070413-alt3_15
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070413-alt2_15
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20070413-alt2_14
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20070413-alt1_14
- initial release by fcimport

