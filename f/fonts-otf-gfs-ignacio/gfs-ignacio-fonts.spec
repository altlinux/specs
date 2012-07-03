# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname gfs-ignacio-fonts
%global fontname gfs-ignacio
%global fontconf 61-%{fontname}.conf

%global archivename GFS_IGNACIO

Name:    fonts-otf-gfs-ignacio
Version: 20090923
Release: alt3_3
Summary: A majuscule Greek font

Group:     System/Fonts/True type
License:   OFL
URL:       http://www.greekfontsociety.gr/pages/en_typefaces_majuscules.html
Source0:   http://www.greekfontsociety.gr/%{archivename}.zip
Source1:   %{oldname}-fontconfig.conf


BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
As it is known, the Greek alphabet was used in majuscule form for over a
millennium before the minuscule letters gradually replaced it until they became
the official script in the 9th century A.D. Thereafter, majuscule letters were
confined to sparse use as initials or elaborate titles until the Italian
Renaissance.

The new art of Typography, as well as the need of the humanists to mimic the
ancient Greco-Roman period brought back the extensive use of the majuscule
letter-forms in both Latin and Greek typography. Greek books of the time were
printed using the contemporary Byzantine hand with which they combined capital
letters modelled on the Roman antiquity, i.e. with thick and thin strokes and
serifs. At the same time the Byzantine majuscule tradition, principally used on
theological editions, remainned alive until the early 19th century.

This font has been designed by George D. Matthiopoulos.


%prep
%setup -q -c -T
unzip -j -L -q %{SOURCE0}
chmod 0644 *.txt

for txt in *.txt ; do
   fold -s $txt > $txt.new &&\
   sed -i 's/\r//' $txt.new &&\
   touch -r $txt $txt.new &&\
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

%doc *.txt


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20090923-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20090923-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20090923-alt2_2
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20090923-alt1_2
- initial release by fcimport

