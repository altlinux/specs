# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname gfs-solomos-fonts
%global fontname gfs-solomos
%global fontconf 61-%{fontname}.conf

%global archivename GFS_SOLOMOS_OT

Name:    fonts-otf-gfs-solomos
Version: 20071114
Release: alt3_14
Summary: GFS Solomos oblique Greek font

Group:     System/Fonts/True type
License:   OFL
URL:       http://www.greekfontsociety.gr/pages/en_typefaces19th.html
Source0:   http://www.greekfontsociety.gr/%{archivename}.zip
Source1:   %{oldname}-fontconfig.conf


BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
From the middle of the 19th century an italic font with many calligraphic
overtones was introduced into Greek printing. Its source is unknown, but it
almost certainly was the product of a German or Italian foundry. In the first
type specimen printed in Greece by the typecutter K. Miliadis (1850), the font
was listed anonymously along others of 11pts and in the Gr. Doumas' undated
specimen appeared as A.11pt Greek inclinedA.. For most of the second half of the
century the type was used extensively as an italic for emphasis in words,
sentences or exerpts. In 1889, the folio size Type Specimen of Anestis
Konstantinidis' publishing, printing and type founding establishment also
included the type as A.Greek inclined [9 & 12 pt]A..

Nevertheless, the excessively calligraphic style of the characters, combined
with the steep and uncomfortable obliqueness of the capitals, was out of
favour in the 20th century and the type did not survive the conformity of the
mechanical type cutting and casting.

The font has been digitally revived, as part of our typographic tradition, by
George D. Matthiopoulos and is part of GFS' type library under the name GFS
Solomos, in commemoration of the great Greek poet of the 19th century,
Dionisios Solomos.


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
* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 20071114-alt3_14
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20071114-alt2_14
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20071114-alt2_13
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20071114-alt1_13
- initial release by fcimport

