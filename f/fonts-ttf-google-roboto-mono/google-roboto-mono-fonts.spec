Group: System/Fonts/True type
%define oldname google-roboto-mono-fonts
%global fontconf 64-%{fontname}
%global fontname google-roboto-mono
%global commit0 e4d4513e11593dc7647c283c61e111a4c1ef2153

Name:          fonts-ttf-google-roboto-mono
Version:       2.000986
Release:       alt1_0.1.20150923git
Summary:       Google Roboto Mono fonts

License:       ASL 2.0
URL:           https://www.google.com/fonts/specimen/Roboto+Mono
# There are no tar archive so let's pick all the individual source files from github
Source0:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotomono/RobotoMono-Regular.ttf
Source1:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotomono/RobotoMono-Bold.ttf
Source2:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotomono/RobotoMono-Italic.ttf
Source3:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotomono/RobotoMono-BoldItalic.ttf
Source4:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotomono/RobotoMono-Medium.ttf
Source5:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotomono/RobotoMono-MediumItalic.ttf
Source6:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotomono/RobotoMono-Light.ttf
Source7:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotomono/RobotoMono-LightItalic.ttf
Source8:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotomono/RobotoMono-Thin.ttf
Source9:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotomono/RobotoMono-ThinItalic.ttf
Source10:      https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotomono/LICENSE.txt
Source11:      %{fontname}-fontconfig.conf
Source12:      %{fontname}.metainfo.xml
BuildArch:     noarch

BuildRequires: fontpackages-devel
Source44: import.info

%description
Roboto Mono is a monospaced addition to the Roboto type family. Like the other
members of the Roboto family, the fonts are optimized for readability on
screens across a wide variety of devices and reading environments. While the
monospaced version is related to its variable width cousin, it doesn't hesitate
to change forms to better fit the constraints of a monospaced environment. For
example, narrow glyphs like 'I', 'l' and 'i' have added serifs for more even
texture while wider glyphs are adjusted for weight. Curved caps like 'C' and
'O' take on the straighter sides from Roboto Condensed.

%prep
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .
cp -p %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} .
cp -p %{SOURCE10} %{SOURCE11} %{SOURCE12} .

%build
# nothing to build here

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p RobotoMono-*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE11} \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-fontconfig.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}-fontconfig.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}-fontconfig.conf

install -m 0755 -d %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE12} %{buildroot}%{_datadir}/appdata
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
%{_fontconfig_templatedir}/%{fontconf}-fontconfig.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-fontconfig.conf
%{_fontbasedir}/*/%{_fontstem}/RobotoMono-*.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc LICENSE.txt

%changelog
* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 2.000986-alt1_0.1.20150923git
- new version

