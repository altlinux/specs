# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname tlomt-orbitron-fonts
%global shortfontname orbitron
%global fontname tlomt-%{shortfontname}
%global fontconf 61-%{fontname}.conf

Name:           fonts-otf-tlomt-orbitron
Version:        1.000
Release:        alt3_4
Summary:        Geometric sans-serif typeface

Group:          System/Fonts/True type
License:        OFL
URL:            http://www.theleagueofmoveabletype.com/
Source0:        http://s3.amazonaws.com/theleague-production/fonts/%{shortfontname}.zip
Source1:        %{oldname}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
Orbitron is a geometric sans-serif typeface intended for display purposes. It
features four weights (light, medium, bold, and black), a stylistic
alternative, small caps, and a ton of alternate glyphs. Orbitron was designed
so that graphic designers in the future will have some alternative to typefaces
like Eurostile or Bank Gothic. If youa.'ve ever seen a futuristic sci-fi movie,
you have may noticed that all other fonts have been lost or destroyed in the
apocalypse that led humans to flee earth. Only those very few geometric
typefaces have survived to be used on spaceship exteriors, spacestation
signage, monopolistic corporate branding, uniforms featuring aerodynamic
shoulder pads, etc. Of course Orbitron could also be used on the posters for
the movies portraying this inevitable future.

%prep
%setup -q -n Orbitron
#
# supress windows EOL style
#
sed 's/\r//' Open\ Font\ License.txt > License.new
touch -r Open\ Font\ License.txt License.new
mv License.new Open\ Font\ License.txt


%build


%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p OTF/*.otf %{buildroot}%{_fontdir}

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

%doc readme.txt
%doc Open\ Font\ License.txt

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.000-alt3_4
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.000-alt2_4
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.000-alt2_3
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.000-alt1_3
- initial release by fcimport

