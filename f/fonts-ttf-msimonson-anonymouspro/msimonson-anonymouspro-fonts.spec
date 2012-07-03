# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname msimonson-anonymouspro-fonts
%global fontname msimonson-anonymouspro
%global fontconf 61-%{fontname}.conf
%global archivename AnonymousPro

Name:           fonts-ttf-msimonson-anonymouspro
Version:        1.002.001
Release:        alt4_3
Summary:        A coding-friendly monospace font

Group:          System/Fonts/True type
License:        OFL
URL:            http://www.ms-studio.com/FontSales/anonymouspro.html
Source0:        http://www.ms-studio.com/FontSales/AnonymousPro-1.002.zip
Source1:        %{oldname}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info
Provides: fonts-ttf-anonymous = %version-%release
Obsoletes: fonts-ttf-anonymous <= 1.002-alt1


%description
Anonymous Pro is a family of fixed-width fonts designed especially with coding
in mind. Characters that could be mistaken for one another (O, 0, I, l, 1,
etc.) have distinct shapes to make them easier to tell apart in the context of
source code.

It has support for most Western and European Latin-based languages, Greek, and
Cyrillic. It also includes special a.'box drawinga.' characters.

Anonymous Pro is based on an earlier font, Anonymous, which is a TrueType
version of Susan Lesch and David Lamkinsa.' font Anonymous 9, a freeware
Macintosh bitmap font.

It was created by Mark Simonson.

%prep
%setup -q -n %{archivename}-%{version}
for txt in "OFL.txt" "OFL-FAQ.txt"; do
    fold -s $txt > $txt.new
    sed -i 's/\r//' $txt.new
    touch -r $txt $txt.new
    mv $txt.new $txt
done

%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

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

%doc *.txt

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.002.001-alt4_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.002.001-alt3_3
- update to new release by fcimport

* Thu Aug 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.002.001-alt3_2
- really added provides/obsoletes for short names

* Thu Aug 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.002.001-alt2_2
- added provides/obsoletes for short names

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.002.001-alt1_2
- initial release by fcimport

