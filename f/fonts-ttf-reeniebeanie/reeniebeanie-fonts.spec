Group: System/Fonts/True type
%define oldname reeniebeanie-fonts
%global fontname reeniebeanie
%global fontconf 61-%{fontname}-fonts.conf
%global alphatag 20140913hg


Name:          fonts-ttf-reeniebeanie
Version:       1.000
Release:       alt1_0.5.%{alphatag}
Summary:       Reenie Beanie font by James Grieshaber
License:       OFL
URL:           http://www.google.com/fonts/specimen/Reenie+Beanie
Source0:       https://googlefontdirectory.googlecode.com/hg/ofl/reeniebeanie/ReenieBeanie.ttf
Source1:       https://googlefontdirectory.googlecode.com/hg/ofl/reeniebeanie/OFL.txt
Source10:      %{fontconf}
BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: ttname
Source44: import.info

%description
Reenie Beanie is a fun font based on basic ball-point pen handwriting. It has a
playful and loose look, which lends itself to casual and informal messages. With
a little imagination, Reenie Beanie could be used to represent the scribbling of
a mad scientist, or the recipes of a genius chef.


%prep
%setup -n %{oldname}-%{version} -qTc
cp -p %{SOURCE0} %{SOURCE1} .
# Correct wrong-file-end-of-line-encoding error for OFL.txt
sed -i 's/\r$//' OFL.txt


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
* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.000-alt1_0.5.20140913hg
- new version

