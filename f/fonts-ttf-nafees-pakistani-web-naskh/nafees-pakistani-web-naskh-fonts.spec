%define oldname nafees-pakistani-web-naskh-fonts
%global fontname   nafees-pakistani-web-naskh
%global fontconf   67-%{fontname}.conf 
Name:		fonts-ttf-nafees-pakistani-web-naskh
Version:	2.0
Release:	alt1_3
Summary:	Nafees pakistani web naskh font for writing Urdu 

Group:		Graphical desktop/Other
License:	Bitstream Vera
URL:		http://www.crulp.org/index.htm
Source0:	http://www.crulp.org/Downloads/NafeesPakistaniWebNaskh(BTK2.0).ttf
Source1:	%{fontname}-update-preferred-family.pe
Source2:	%{fontconf}
Source3:	http://www.crulp.org/Downloads/NafeesPakistaniWebNaskh(BTK2.0).pdf
Source4:	http://www.crulp.org/software/license/Nafees_Pakistani_Naskh_License.html
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	fontforge
Source44: import.info

%description
This font is developed on Unicode standard and is based \
 on Naskh writing style. \
Guidance and calligraphy of basic glyph s for the font \
has been provided by Syed Jameel-ur- Rehman. 

%prep

%build
%{_bindir}/fontforge %{SOURCE1} '%{SOURCE0}'

%install


#fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
	%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
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

%doc  '%{SOURCE3}' '%{SOURCE4}'


%changelog
* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_3
- fc import

