%define oldname vlgothic-fonts
# %oldname or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name vlgothic-fonts
%define version 20120618
%define priority	65-1
%define ppriority	65-0
%define fontname	vlgothic
%define	archivename	VLGothic-%{version}
%define	fontconf	%{priority}-%{fontname}-gothic
%define	pfontconf	%{ppriority}-%{fontname}-pgothic
%define	common_desc	\
VLGothic provides Japanese TrueType fonts from the Vine Linux project.\
Most of the glyphs are taken from the M+ and Sazanami Gothic fonts,\
but some have also been improved by the project.

Name:		fonts-ttf-vlgothic
Version:	20120618
Release:	alt1_1
Summary:	Japanese TrueType font

License:	mplus and BSD
Group:		System/Fonts/True type
URL:		http://dicey.org/vlgothic
Source0:	http://osdn.dl.sourceforge.jp/vlgothic/56216/%{archivename}.tar.bz2
Source1:	%{fontname}-fontconfig-pgothic.conf
Source2:	%{fontname}-fontconfig-gothic.conf
BuildArch:	noarch
BuildRequires:	fontpackages-devel

Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	VLGothic-fonts < 20090204-1
Provides:	VLGothic-fonts = %{version}-%{release}
Source44: import.info
%description
%common_desc

This package provides the monospace VLGothic font.

%package	common
Summary:	Common files for VLGothic Japanese TrueType fonts
Group:		System/Fonts/True type

%description	common
%common_desc

This package consists of files used by other %{oldname} packages.

%package -n fonts-ttf-vlgothic-p
Summary:	Proportional Japanese TrueType font
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	VLGothic-fonts-proportional < 20090204-1
Provides:	VLGothic-fonts-proportional = %{version}-%{release}

%description -n fonts-ttf-vlgothic-p
%common_desc

This package provides the VLGothic font with proportional glyphs for some
non-Japanese characters.

%prep
%setup -q -n VLGothic


%build
%{nil}


%install

install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p *.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d	$RPM_BUILD_ROOT%{_fontconfig_templatedir} \
	 		$RPM_BUILD_ROOT%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{pfontconf}.conf
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}.conf

for fconf in %{pfontconf}.conf %{fontconf}.conf; do
	ln -s %{_fontconfig_templatedir}/$fconf $RPM_BUILD_ROOT%{_fontconfig_confdir}/$fconf
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
%doc README* LICENSE*
%dir %{_fontbasedir}/*/%{_fontstem}

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/VL-Gothic-Regular.ttf

%files -n fonts-ttf-vlgothic-p
%{_fontconfig_templatedir}/%{pfontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{pfontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/VL-PGothic-Regular.ttf


%changelog
* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 20120618-alt1_1
- fc import

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 20120325-alt1_1
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20120130-alt2_1
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 20120130-alt1_1
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 20111122-alt2_2
- update to new release by fcimport

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 20111122-alt2_1
- updated dependencies

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 20111122-alt1_1
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20110722-alt2_1
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 20110722-alt1_1
- initial release by fcimport

