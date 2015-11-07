Group: System/Fonts/True type
%define oldname labelleaurore-fonts
%global fontname labelleaurore
%global fontconf 61-%{fontname}-fonts.conf
%global alphatag 20140913hg


Name:          fonts-ttf-labelleaurore
Version:       1.001
Release:       alt1_0.3.%{alphatag}
Summary:       La Belle Aurore font by Kimberly Geswein
License:       OFL
URL:           http://www.google.com/fonts/specimen/La+Belle+Aurore
Source0:       https://googlefontdirectory.googlecode.com/hg/ofl/labelleaurore/LaBelleAurore.ttf
Source1:       https://googlefontdirectory.googlecode.com/hg/ofl/labelleaurore/OFL.txt
Source10:      %{fontconf}
BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: ttname
Source44: import.info

%description
This whimsical, romantic handwriting is inspired by the romance of
Casablanca. It is not a true script, but has many curls and tendrils similar to
a script font.


%prep
%setup -n %{oldname}-%{version} -qTc
cp -p %{SOURCE0} %{SOURCE1} .


%build
ttname --copyright="$(head -n1 OFL.txt)" --license="$(cat OFL.txt)" --license-url="http://scripts.sil.org/OFL" *.ttf || exit 0

%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} \
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
%doc OFL.txt


%changelog
* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.001-alt1_0.3.20140913hg
- new version

