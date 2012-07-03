%define oldname google-croscore-fonts
%global fontname google-croscore
%global fontconf62 62-%{fontname}
%global fontconf30 30-0-%{fontname}

%global common_desc \
This package contains a collections of fonts that offers improved on-screen \
readability characteristics and the pan-European WGL character set and solves \
the needs of developers looking for width-compatible fonts to address document \
portability across platforms.


Name:           fonts-ttf-google-croscore
Version:        1.21.0
Release:        alt1_3
Summary:        The width-compatible fonts for improved on-screen readability

Group:          Graphical desktop/Other
License:        OFL
#URL:            
Source0:        http://gsdview.appspot.com/chromeos-localmirror/distfiles/croscorefonts-%{version}.tar.gz
Source1:        62-%{fontname}-arimo-fontconfig.conf
Source2:        62-%{fontname}-cousine-fontconfig.conf
Source3:        62-%{fontname}-tinos-fontconfig.conf
Source4:        30-0-%{fontname}-arimo-fontconfig.conf
Source5:        30-0-%{fontname}-cousine-fontconfig.conf
Source6:        30-0-%{fontname}-tinos-fontconfig.conf
Source7:        62-%{fontname}-symbolneu-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
%common_desc


%package common
Group: Graphical desktop/Other
Summary:        Common files of %{oldname}

%description common
This package consists of files used by other %{oldname} packages.

# Repeat for every font family
%package -n fonts-ttf-google-croscore-arimo
Group: Graphical desktop/Other
Summary:       The croscore Arimo family fonts 
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-google-croscore-arimo
%common_desc
Arimo was designed by Steve Matteson as an innovative, refreshing sans serif
design that is metrically compatible with Arial. Arimo offers improved 
on-screen readability characteristics and the pan-European WGL character set 
and solves the needs of developers looking for width-compatible fonts to 
address document portability across platforms.

%files -n fonts-ttf-google-croscore-arimo
%{_fontconfig_templatedir}/*-%{fontname}-arimo.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}-arimo.conf
%{_fontbasedir}/*/%{_fontstem}/Arimo*.ttf

%package -n fonts-ttf-google-croscore-cousine
Group: Graphical desktop/Other
Summary:       The croscore Cousine family fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-google-croscore-cousine
%common_desc
Cousine was designed by Steve Matteson as an innovative, refreshing sans serif
design that is metrically compatible with Courier New. Cousine offers improved
on-screen readability characteristics and the pan-European WGL character set
and solves the needs of developers looking for width-compatible fonts to 
address document portability across platforms.

%files -n fonts-ttf-google-croscore-cousine
%{_fontconfig_templatedir}/*-%{fontname}-cousine.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}-cousine.conf
%{_fontbasedir}/*/%{_fontstem}/Cousine*.ttf

%package -n fonts-ttf-google-croscore-tinos
Group: Graphical desktop/Other
Summary:       The croscore Tinos family fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-google-croscore-tinos
%common_desc
Tinos was designed by Steve Matteson as an innovative, refreshing serif design
that is metrically compatible with Times New Roman. Tinos offers improved
on-screen readability characteristics and the pan-European WGL character set
and solves the needs of developers looking for width-compatible fonts to
address document portability across platforms.

%files -n fonts-ttf-google-croscore-tinos
%{_fontconfig_templatedir}/*-%{fontname}-tinos.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}-tinos.conf
%{_fontbasedir}/*/%{_fontstem}/Tinos*.ttf

%package -n fonts-ttf-google-croscore-symbolneu
Group: Graphical desktop/Other
Summary:       The croscore Symbol Neu family fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-google-croscore-symbolneu
%common_desc
Symbol Neu is a metrically compatible font to Symbol.

%files -n fonts-ttf-google-croscore-symbolneu
%{_fontconfig_templatedir}/*-%{fontname}-symbolneu.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}-symbolneu.conf
%{_fontbasedir}/*/%{_fontstem}/SymbolNeu.ttf

%prep
%setup -q -n croscorefonts-%{version}

%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-arimo.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-cousine.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-tinos.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf30}-arimo.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf30}-cousine.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf30}-tinos.conf
install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-symbolneu.conf

for fconf in %{fontconf62}-arimo.conf %{fontconf30}-arimo.conf \
             %{fontconf62}-cousine.conf %{fontconf30}-cousine.conf \
             %{fontconf62}-tinos.conf %{fontconf30}-tinos.conf \
       %{fontconf62}-symbolneu.conf; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done
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


%files common
%doc LICENSE


%changelog
* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.21.0-alt1_3
- fc import

