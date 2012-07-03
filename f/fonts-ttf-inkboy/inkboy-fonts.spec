# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname inkboy-fonts
%global fontname inkboy
%global fontconf 65-%{fontname}.conf
Name:           fonts-ttf-inkboy
Version:        20070624
Release:        alt3_7
Summary:        A clean and usable latin fantasy font
Group:          System/Fonts/True type
License:        OFL
URL:            http://inkboy.fr/html/telechargement-ressources.php
Source0:        http://inkboy.fr/fichiers/inkboyfont.zip
BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
This is a clean and usable latin fantasy font.

%prep
%setup -q -c

%build
for i in FONTLOG.txt OFL.txt OFL-FAQ.txt; do
  sed -i~ -e 's|\r||' $i &&  touch -r $i~ $i
done
for i in FONTLOG.txt; do
  iconv -f iso-8859-1 -t utf-8 $i > $i~ &&  touch -r $i $i~ &&  mv $i~ $i
done

%install
rm -fr %{buildroot}

install -m 0755 -d       %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

cat <<EOF > %{fontconf}
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
    <alias>
        <family>fantasy</family>
        <prefer>
            <family>Inkboy</family>
        </prefer>
    </alias>
    <alias>
        <family>Inkboy</family>
        <default>
            <family>fantasy</family>
        </default>
    </alias>
</fontconfig>
EOF
install -m 0755 -d             %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{fontconf} %{buildroot}%{_fontconfig_templatedir}

install -m 0755 -d             %{buildroot}%{_fontconfig_confdir}
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
%doc FONTLOG.txt OFL.txt OFL-FAQ.txt

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070624-alt3_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070624-alt2_7
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20070624-alt2_6
- rebuild with new rpm-build-fonts

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 20070624-alt1_6
- initial release by fcimport

