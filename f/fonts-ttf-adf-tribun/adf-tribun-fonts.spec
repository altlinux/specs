# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname adf-tribun-fonts
%global fontname adf-tribun
%global fontconf 60-%{fontname}.conf

%global archivename Tribun-Std

Name:    fonts-ttf-adf-tribun
Version: 1.13
Release: alt3_4
Summary: A newsprint-like serif typeface

Group:     System/Fonts/True type
License:   GPLv2+ with exceptions
URL:       http://arkandis.tuxfamily.org/adffonts.html
Source0:   http://arkandis.tuxfamily.org/fonts/%{archivename}.zip
Source1:   http://arkandis.tuxfamily.org/docs/Tribun-Cat.pdf
Source11:  %{oldname}-fontconfig.conf


BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
Hirwen Harendal started in 1999 the realization of a first font family, aiming
to create another a.'Times New Romana.'a.. He does not consider this endeavour a huge
success. However, he transformed Tribun progessively since then to give it its
own character.

The idea was to achieve newsprint-like rendering. To this effect, the glyph
bodies, serifs, or even extenders are not normalised and use irregular strokes.
This is most visible in italics though those variations stay imperceptible at
small sizes.

Italics proved time-consuming. They are never an easy thing to draw.
Nevertheless, the designer considers them very close to those of a.'Timesa.', with
some variations.

The medium weight uses a stronger stroke. It can be used for emphasis, or for
effects in titles. That being said it has also been used for body copy. It is
also slightly expanded to complete the face offerings.

The condensed version is a bit unusual, since it stands in for both normal and
medium condensed. After several trials, Hirwen decided an intermediate weight
rendered much better both for document display and in print. Secondly, he took
great care to keep readability excellent, and this even for italics.

This font family is particularly well suited for text, display, or
presentations. It is also ideal for all Web publications. It can serve as
alternative to a.'Times New Romana.' and other similar fonts.


%prep
%setup -q -n %{archivename}
install -m 0644 -p %{SOURCE1} .
for txt in NOTICE */COPYING ; do
   fold -s $txt > $txt.new &&\
   sed -i 's/\r//' $txt.new &&\
   touch -r $txt $txt.new &&\
   mv $txt.new $txt
done


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p TTF/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE11} \
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

%doc NOTICE TTF/COPYING *.pdf

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_4
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.13-alt2_4
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.13-alt2_3
- rebuild with new rpm-build-fonts

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_3
- initial release by fcimport

