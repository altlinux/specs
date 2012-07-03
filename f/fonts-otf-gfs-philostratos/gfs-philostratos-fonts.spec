# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname gfs-philostratos-fonts
%global fontname gfs-philostratos
%global fontconf 61-%{fontname}.conf

%global archivename GFS_PHILOSTRATOS

Name:    fonts-otf-gfs-philostratos
Version: 20090902
Release: alt3_3
Summary: A revival of the a.'Griechische Antiquaa.' Greek typeface

Group:     System/Fonts/True type
License:   OFL
URL:       http://www.greekfontsociety.gr/pages/en_typefaces19th.html
Source0:   http://www.greekfontsociety.gr/%{archivename}.zip
Source1:   %{oldname}-fontconfig.conf


BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
Griechische Antiqua was one of the historical Greek typefaces of the late 19th
and early 20th century. It was designed by I'aurice I.duard Pinder, a German
erudite artist and a member of the Academy of Science in Berlin. This is the
most popular version which has appeared from 1870 to 1940 in the German
speaking philological literature and in many classical and Byzantine editions
by publishers like Teubner (in Leipzig) and Weidmann (in Berlin) such as:
Anthology of Byzantine Melos by Wilhelm von Christ and Matthaios
Paranikas (Leipzig 1871), Epicurea, by Heinrich Usener (Leipzig 1887),
Mitrodorous by Alfred Koerte (Leipzig 1890), Pindar by Otto Schroeder (Leipzig
1908), I.I.I. Aeschylus by U. von Wilamowitz-Moellendorff (Berlin 1910, 1915),
Bachylides by Bruno Snell (Leipzig, 1934),  The Vulgata by Alfred Rahlfs
(Stuttgart 1935), Suidas Lexicon by Ada Adler (Leipzig 1928-1938) etc.

E.J. Kenney lamented the abandonment of the type after the 2nd World War as a
great loss for Greek typography (a.'From Script to Printa.', Greek Scripts: An
illustrated Introduction, Society for the Promotion of Hellenic Studies, 2001,
p. 69).

GFS Philostratos was digitized by George D. Matthiopoulos.


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
* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 20090902-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20090902-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20090902-alt2_2
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20090902-alt1_2
- initial release by fcimport

