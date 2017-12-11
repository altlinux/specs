Group: System/Fonts/True type
%define oldname eosrei-emojione-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname eosrei-emojione

Name:           fonts-ttf-eosrei-emojione
Version:        1.0
Release:        alt2_5
Summary:        A color emoji font

# Note, the link below is the last "Android" build of the EmijoOne font
# with CC-BY-4.0 assets. Do not update to a newer version.
#
# This package should eventually be replaced by a build of this font:
# https://github.com/EmojiTwo/emojitwo
License:        CC-BY
URL:            https://github.com/eosrei/emojione-color-font
# From https://github.com/emojione/emojione/blob/693a9705f60efd566e40a5c9ec00ca306c9bcbd0/extras/fonts/emojione-android.ttf
Source0:        emojione-android.ttf
Source1:        https://github.com/eosrei/emojione-color-font/raw/master/LICENSE-CC-BY.txt

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
A color and B&W emoji font built primarily from Emoji One artwork with
support for ZWJ, skin tone modifiers and country flags.

Regular B&W outline emoji are included for backwards/fallback compatibility.

It was created by Brad Erickson.

%prep
%setup -n %{oldname}-%{version} -q -T -c

%build
cp -a %{SOURCE1} .

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{buildroot}%{_fontdir}/

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
       %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
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
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/emojione-android.ttf
%doc LICENSE-CC-BY.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Mon Dec 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_5
- added font dir (closes: #34316)

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5
- new version

