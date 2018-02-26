# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname gfs-neohellenic-fonts
%global fontname gfs-neohellenic
%global fontconf 60-%{fontname}.conf

%global archivename GFS_NEOHELLENIC_OT

Name:    fonts-otf-gfs-neohellenic
Version: 20090918
Release: alt3_3
Summary: A 20th century Greek typeface

Group:     System/Fonts/True type
License:   OFL
URL:       http://www.greekfontsociety.gr/pages/en_typefaces20th.html
Source0:   http://www.greekfontsociety.gr/%{archivename}.zip
Source1:   %{oldname}-fontconfig.conf


BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
The design of new Greek typefaces always followed the growing needs of the
Classical Studies in the major European Universities. Furthermore, by the end
of the 19th century bibliology had become an established section of Historical
Studies, and, as John Bowman commented, the prevailing attitude was that Greek
types should adhere to a lost idealized, yet undefined, greekness of yore.
Especially in Great Britain this tendency remained unchallenged in the first
decades of the 20th century, both by Richard Proctor, curator of the incunabula
section in the British Museum Library and his successor Victor Scholderer.

In 1927, Scholderer, on behalf of the Society for the Promotion of Greek
Studies, got involved in choosing and consulting the design and production of a
Greek type called New Hellenic cut by the Lanston Monotype Corporation. He
chose the revival of a round, and almost monoline type which had first appeared
in 1492 in the edition of Macrobius, ascribable to the printing shop of
Giovanni Rosso (Joannes Rubeus) in Venice. New Hellenic was the only successful
typeface in Great Britain after the introduction of Porson Greek well over a
century before. The type, since to 1930a.'s, was also well received in Greece,
albeit with a different design for Ksi and Omega.

GFS digitized the typeface (1993-1994) funded by the Athens Archeological
Society with the addition of a new set of epigraphical symbols. Later (2000)
more weights were added (italic, bold and bold italic) as well as a latin
version.


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
* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 20090918-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20090918-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20090918-alt2_2
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20090918-alt1_2
- initial release by fcimport

