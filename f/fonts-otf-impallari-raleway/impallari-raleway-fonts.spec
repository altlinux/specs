Group: System/Fonts/True type
%define oldname impallari-raleway-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname impallari-raleway
%global fontconf 63-%{fontname}.conf

# https://github.com/impallari/Raleway
%global commit          6c67ab1f7aa65c442bd2745bb9d4ef1cd7bc01fa
%global commit_date     20161116
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           fonts-otf-impallari-raleway
Version:        3.0
Release:        alt1_3.git%{commit_date}.%{shortcommit}
Summary:        Elegant sans-serif typeface family
License:        OFL
URL:            https://github.com/impallari/Raleway

Source0:        %{url}/archive/%{commit}/%{fontname}-%{shortcommit}.tar.gz
Source1:        %{oldname}.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch

BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Source44: import.info



%description
Raleway is an elegant sans-serif typeface family.

Initially designed by Matt McInerney as a single thin weight, it was
expanded into a 9 weight family by Pablo Impallari and Rodrigo
Fuenzalida in 2012 and iKerned by Igino Marini. In 2013 the Italics
were added.

It is a display face and the download features both old style and
lining numerals, standard and discretionary ligatures, a pretty complete
set of diacritics, as well as a stylistic alternate inspired by more
geometric sans-serif typefaces than its neo-grotesque inspired default
character set.


%prep
%setup -q -n Raleway-%{commit}


%build


%install
install -m 0755 -d %{buildroot}/%{_fontdir}

%global originals fonts/v3.000\ Fontlab/OTF

# Raleway Black
cp -pav '%{originals}/Raleway-Black-Original.otf' %{buildroot}/%{_fontdir}/Raleway-Black.otf
cp -pav '%{originals}/Raleway-Black-Italic-Original.otf' %{buildroot}/%{_fontdir}/Raleway-Black-Italic.otf

# Raleway Bold
cp -pav '%{originals}/Raleway-Bold-Original.otf' %{buildroot}/%{_fontdir}/Raleway-Bold.otf
cp -pav '%{originals}/Raleway-Bold-Italic-Original.otf' %{buildroot}/%{_fontdir}/Raleway-Bold-Italic.otf

# Raleway ExtraBold
cp -pav '%{originals}/Raleway-ExtraBold-Original.otf' %{buildroot}/%{_fontdir}/Raleway-ExtraBold.otf
cp -pav '%{originals}/Raleway-ExtraBold-Italic-Original.otf' %{buildroot}/%{_fontdir}/Raleway-ExtraBold-Italic.otf

# Raleway ExtraLight
cp -pav '%{originals}/Raleway-ExtraLight-Original.otf' %{buildroot}/%{_fontdir}/Raleway-ExtraLight.otf
cp -pav '%{originals}/Raleway-ExtraLight-Italic-Original.otf' %{buildroot}/%{_fontdir}/Raleway-ExtraLight-Italic.otf

# Raleway Light
cp -pav '%{originals}/Raleway-Light-Original.otf' %{buildroot}/%{_fontdir}/Raleway-Light.otf
cp -pav '%{originals}/Raleway-Light-Italic-Original.otf' %{buildroot}/%{_fontdir}/Raleway-Light-Italic.otf

# Raleway Medium
cp -pav '%{originals}/Raleway-Medium-Original.otf' %{buildroot}/%{_fontdir}/Raleway-Medium.otf
cp -pav '%{originals}/Raleway-Medium-Italic-Original.otf' %{buildroot}/%{_fontdir}/Raleway-Medium-Italic.otf

# Raleway Regular
cp -pav '%{originals}/Raleway-Regular-Original.otf' %{buildroot}/%{_fontdir}/Raleway-Regular.otf
cp -pav '%{originals}/Raleway-Regular-Italic-Original.otf' %{buildroot}/%{_fontdir}/Raleway-Regular-Italic.otf

# Raleway SemiBold
cp -pav '%{originals}/Raleway-SemiBold-Original.otf' %{buildroot}/%{_fontdir}/Raleway-SemiBold.otf
cp -pav '%{originals}/Raleway-SemiBold-Italic-Original.otf' %{buildroot}/%{_fontdir}/Raleway-SemiBold-Italic.otf

# Raleway Thin
cp -pav '%{originals}/Raleway-Thin-Original.otf' %{buildroot}/%{_fontdir}/Raleway-Thin.otf
cp -pav '%{originals}/Raleway-Thin-Italic-Original.otf' %{buildroot}/%{_fontdir}/Raleway-Thin-Italic.otf


install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} %{buildroot}%{_fontconfig_confdir}/%{fontconf}


# Add AppStream metadata
mkdir -p %{buildroot}/%{_datadir}/appdata
cp -pav %{SOURCE2} %{buildroot}/%{_datadir}/appdata/%{fontname}.metainfo.xml
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


%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{fontname}.metainfo.xml


%global fontnames Black,Black-Italic,Bold,Bold-Italic,ExtraBold,ExtraBold-Italic,ExtraLight,ExtraLight-Italic,Light,Light-Italic,Medium,Medium-Italic,Regular,Regular-Italic,SemiBold,SemiBold-Italic,Thin,Thin-Italic


%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Raleway-Black.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-Black-Italic.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-Bold.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-Bold-Italic.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-ExtraBold.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-ExtraBold-Italic.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-ExtraLight.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-ExtraLight-Italic.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-Light.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-Light-Italic.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-Medium.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-Medium-Italic.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-Regular.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-Regular-Italic.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-SemiBold.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-SemiBold-Italic.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-Thin.otf
%{_fontbasedir}/*/%{_fontstem}/Raleway-Thin-Italic.otf

%doc --no-dereference OFL.txt

%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_3.git20161116.6c67ab1
- update to new release by fcimport

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_2.git20161116.6c67ab1.1
- new version

