%define oldname horai-ume-fonts
# %%oldname or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name horai-ume-fonts
%define version 620
%global fontname horai-ume
%global fontconf 65-%{fontname}
%global archivename umefont_%{version}
%global _docdir_fmt %{oldname}

%global common_desc \
This package contains fonts published by Wataru Horai. It contains Gothic and\
Mincho styles in 19 variants total:\
\
 * Ume Gothic Original, O5, C4, C5, S4, S5\
 * Ume Hy Gothic\
 * Ume P Gothic Original, O5, C4, C5, S4, S5\
 * Ume UI Gothic Original, O5\
 * Ume Mincho Original, S3\
 * Ume P Mincho Original, S3\
\
In addition to Latin, Greek and Cyrilics scripts it provides Hiragana, Katakana\
and CJK. These fonts are suitable for easy on-screen legibility.


Name:           fonts-ttf-horai-ume
Version:        620
Release:        alt1_1
Summary:        Gothic and Mincho fonts designed for easy on-screen legibility

Group:          System/Fonts/True type
License:        mplus
URL:            https://osdn.jp/projects/ume-font/
Source0:        https://osdn.jp/projects/ume-font/downloads/22212/%{archivename}.tar.xz
Source1:        %{fontname}-gothic-fontconfig.conf
Source2:        %{fontname}-hgothic-fontconfig.conf
Source3:        %{fontname}-pgothic-fontconfig.conf
Source4:        %{fontname}-uigothic-fontconfig.conf
Source5:        %{fontname}-mincho-fontconfig.conf
Source6:        %{fontname}-pmincho-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info


%description
%common_desc


%package -n fonts-ttf-horai-ume-gothic
Group: System/Fonts/True type
# tgc4    Ume Gothic C4 / Regular
# tgc5    Ume Gothic C5 / Medium
# tgo4    Ume Gothic / Regular
# tgo5    Ume Gothic O5 / Medium
# tgs4    Ume Gothic S4 / Regular
# tgs5    Ume Gothic S5 / Medium
Summary:        Free Japanese fonts family Ume Gothic

%description -n fonts-ttf-horai-ume-gothic
%common_desc

The Ume Gothic family features sans-serif fonts.


%package -n fonts-ttf-horai-ume-hgothic
Group: System/Fonts/True type
# hgo4    Ume Hy Gothic / Regular
Summary:        Free Japanese fonts family Ume Hy Gothic

%description -n fonts-ttf-horai-ume-hgothic
%common_desc

The Ume Hy Gothic family features sans-serif fonts.


%package -n fonts-ttf-horai-ume-pgothic
Group: System/Fonts/True type
# pgc4    Ume P Gothic C4 / Regular
# pgc5    Ume P Gothic C5 / Medium
# pgo4    Ume P Gothic / Regular
# pgo5    Ume P Gothic O5 / Medium
# pgs4    Ume P Gothic S4 / Regular
# pgs5    Ume P Gothic S5 / Medium
Summary:        Free Japanese fonts family Ume P Gothic

%description -n fonts-ttf-horai-ume-pgothic
%common_desc

The Ume P Gothic family features sans-serif fonts.


%package -n fonts-ttf-horai-ume-uigothic
Group: System/Fonts/True type
# ugo4    Ume UI Gothic / Regular
# ugo5    Ume UI Gothic O5 / Medium
Summary:        Free Japanese fonts family Ume UI Gothic

%description -n fonts-ttf-horai-ume-uigothic
%common_desc

The Ume Gothic family features sans-serif fonts.


%package -n fonts-ttf-horai-ume-pmincho
Group: System/Fonts/True type
# pmo3    Ume P Mincho / Regular
# pms3    Ume P Mincho S3 / Regular
Summary:        Free Japanese fonts family Ume P Mincho

%description -n fonts-ttf-horai-ume-pmincho
%common_desc

The Ume P Mincho family features serif fonts.


%package -n fonts-ttf-horai-ume-mincho
Group: System/Fonts/True type
# tmo3    Ume Mincho / Regular
# tms3    Ume Mincho S3 / Regular
Summary:        Free Japanese fonts family Ume Mincho

%description -n fonts-ttf-horai-ume-mincho
%common_desc

The Ume Mincho family features serif fonts.


%prep
%setup -q -n %{archivename}


%build
chmod -x *


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gothic.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-hgothic.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pgothic.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-uigothic.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mincho.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pmincho.conf

for fconf in %{fontconf}-gothic.conf \
             %{fontconf}-hgothic.conf \
             %{fontconf}-pgothic.conf \
             %{fontconf}-uigothic.conf \
             %{fontconf}-mincho.conf \
             %{fontconf}-pmincho.conf ; do
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


%files -n fonts-ttf-horai-ume-gothic
%{_fontconfig_templatedir}/%{fontconf}-gothic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-gothic.conf
%{_fontbasedir}/*/%{_fontstem}/ume-tg??.ttf
%doc license.html

%files -n fonts-ttf-horai-ume-hgothic
%{_fontconfig_templatedir}/%{fontconf}-hgothic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-hgothic.conf
%{_fontbasedir}/*/%{_fontstem}/ume-hg??.ttf
%doc license.html

%files -n fonts-ttf-horai-ume-pgothic
%{_fontconfig_templatedir}/%{fontconf}-pgothic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-pgothic.conf
%{_fontbasedir}/*/%{_fontstem}/ume-pg??.ttf
%doc license.html

%files -n fonts-ttf-horai-ume-uigothic
%{_fontconfig_templatedir}/%{fontconf}-uigothic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-uigothic.conf
%{_fontbasedir}/*/%{_fontstem}/ume-ug??.ttf
%doc license.html

%files -n fonts-ttf-horai-ume-mincho
%{_fontconfig_templatedir}/%{fontconf}-mincho.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-mincho.conf
%{_fontbasedir}/*/%{_fontstem}/ume-tm??.ttf
%doc license.html

%files -n fonts-ttf-horai-ume-pmincho
%{_fontconfig_templatedir}/%{fontconf}-pmincho.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-pmincho.conf
%{_fontbasedir}/*/%{_fontstem}/ume-pm??.ttf
%doc license.html


%changelog
* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 620-alt1_1
- converted for ALT Linux by srpmconvert tools

