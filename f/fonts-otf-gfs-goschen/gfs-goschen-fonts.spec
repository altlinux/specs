# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname gfs-goschen-fonts
%global fontname gfs-goschen
%global fontconf 64-%{fontname}.conf

%global archivename GFS_GOSCHEN

Name:    fonts-otf-gfs-goschen
Version: 20100203
Release: alt3_3
Summary: A 19th century Greek typeface

Group:     System/Fonts/True type
License:   OFL
URL:       http://www.greekfontsociety.gr/pages/en_typefaces19th.html
Source0:   http://www.greekfontsociety.gr/%{archivename}.zip
Source1:  %{oldname}-fontconfig.conf


BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
Georg Joachim GA.schen founded in 1782 the publishing house of G.J.
GA.schensche Verlagsbuchhandlung in Leipzig and was one of the most active
publishers of the period in Germany. GA.schen was very interested in
typography, influenced by the fame and quality of the editions of G. Bodoni
and F. Didot.

In 1797, he collaborated with the leading scholar of the period, Johann Jakob
Griesbach, to edit and publish the New Testament in Greek for which he formed
a committee of scholars to decide the new Greek type which were eventually
cut by Johann Prillwitz. The book appeared in 1803 and the types show many
influences from the Greek types of Bodoni. Their characteristic was the
neoclassical form of marked contrast between thick and thin strokes, the
cursive style and the large size of the font.

The design was too cumbersome to allow general use and can be considered
successful only for its indirect influence on the later cut Greek Leipzig
type. It is, however, part of the greater heritage of Greek type design and
therefore the type has been digitized by George D. Matthiopoulos in 2009 and
is part of GFS' type library under the name GFS GA.schen cursive, in
commemoration of the great German publisher.


%prep
%setup -q -c -T
unzip -j -L -q %{SOURCE0}
chmod 0644 *.txt
for txt in *.txt ; do
   fold -s $txt > $txt.new && \
   sed -i 's/\r//' $txt.new && \
   touch -r $txt $txt.new && \
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
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100203-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100203-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20100203-alt2_2
- rebuild with new rpm-build-fonts

* Tue Aug 02 2011 Igor Vlasenko <viy@altlinux.ru> 20100203-alt1_2
- initial release by fcimport

