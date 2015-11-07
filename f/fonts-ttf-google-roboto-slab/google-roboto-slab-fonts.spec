Group: System/Fonts/True type
%define oldname google-roboto-slab-fonts
%global fontconf 64-%{fontname}
%global fontname google-roboto-slab
%global commit0 90abd17b4f97671435798b6147b698aa9087612f

Name:          fonts-ttf-google-roboto-slab
Version:       1.100263
Release:       alt1_0.3.20150923git
Summary:       Google Roboto Slab fonts

License:       ASL 2.0
URL:           https://www.google.com/fonts/specimen/Roboto+Slab
# There are no tar archive so let's pick all the individual source files from github
Source0:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/RobotoSlab-Regular.ttf
Source1:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/RobotoSlab-Bold.ttf
Source2:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/RobotoSlab-Light.ttf
Source3:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/RobotoSlab-Thin.ttf
Source4:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/LICENSE.txt
Source5:       %{fontname}-fontconfig.conf
Source6:       %{fontname}.metainfo.xml
BuildArch:     noarch

BuildRequires: fontpackages-devel
Source44: import.info

%description
Roboto has a dual nature. It has a mechanical skeleton and the forms are
largely geometric. At the same time, the font features friendly and open
curves. While some grotesks distort their letterforms to force a rigid
rhythm, Roboto doesn't compromise, allowing letters to be settled into
their natural width. This makes for a more natural reading rhythm more
commonly found in humanist and serif types.

This is the Roboto Slab family, which can be used alongside the normal
Roboto family and the Roboto Condensed family.

%prep
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build
# nothing to build here

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p RobotoSlab-*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE5} \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-fontconfig.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}-fontconfig.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}-fontconfig.conf 

install -m 0755 -d %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE6} %{buildroot}%{_datadir}/appdata
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
%{_fontbasedir}/*/%{_fontstem}/RobotoSlab-*.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc LICENSE.txt

%changelog
* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.100263-alt1_0.3.20150923git
- new version

