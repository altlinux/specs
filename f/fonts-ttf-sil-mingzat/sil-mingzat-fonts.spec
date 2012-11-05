# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname sil-mingzat-fonts
%global fontname sil-mingzat
%global fontconf 65-%{fontname}.conf
%global archivename Mingzat

Name:    fonts-ttf-sil-mingzat
Version: 0.020
Release: alt1_1
Summary: A font for Lepcha script
Group:   System/Fonts/True type
License: OFL
URL:     http://scripts.sil.org/Mingzat
# The source link is a redirect and is not directly accessible
Source0: %{archivename}-%{version}.zip
Source1: %{oldname}-fontconfig.conf
BuildArch: noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
Mingzat is based on Jason Glavy's JG Lepcha font which was a custom-encoded
font. The goal for this product was to provide a single Unicode-based font
that would contain all Lepcha characters. In addition, there is provision for
other Latin characters and symbols. This font makes use of state-of-the-art
font technologies (Graphite and OpenType) to support the need for conjuncts
and to position arbitrary combinations of Lepcha glyphs and combining marks
optimally. 

%prep
%setup -q -n '%{archivename}'
for F in *.txt; do
   sed -i 's/\r//' "$F"
done

%build
# Nothing there

%install
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
%doc *.txt

%changelog
* Mon Nov 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1_1
- fc import

