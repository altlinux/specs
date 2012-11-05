%define oldname kalapi-fonts
%global fontname kalapi
%global fontconf 67-%{fontname}.conf

Name:           fonts-ttf-kalapi
Version:        0.1
Release:        alt1_2
Summary:        OpenType sanserif font for Gujarati script
Group:          System/Fonts/True type
License:        OFL
URL:            https://github.com/gujaratilexicon
Source0:        https://github.com/downloads/gujaratilexicon/font-kalapi/font-kalapi-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge
BuildRequires:  fontpackages-devel
Source1: 67-kalapi.conf
Source2: Makefile
Patch1: font-name.patch
Source44: import.info


%description
This package provides a free Gujarati script TrueType/OpenType font.


%prep
%setup -q -n font-kalapi
mv KalapiUnicode.sfd Kalapi.sfd
%patch1 -p1 -b .1-changing-font-name


%build
cp -p %{SOURCE1}  %{SOURCE2} .
make

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
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

%doc COPYRIGHT OFL.txt README.md


%changelog
* Mon Nov 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_2
- fc import

