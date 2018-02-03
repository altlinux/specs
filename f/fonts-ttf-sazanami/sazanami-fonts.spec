BuildRequires: python-module-numpy-addons
%define oldname sazanami-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global	priority	70
%global	fontname	sazanami
%global	fontconf	%{priority}-%{fontname}
%global catalogue	%{_sysconfdir}/X11/fontpath.d
%global	common_desc	\
The Sazanami type faces are automatically generated from Wadalab font kit.\
They also contains some embedded Japanese bitmap fonts.

Name:		fonts-ttf-sazanami
Version:	0.20040629
Release:	alt9_29
BuildArch:	noarch
BuildRequires:	ttmkfdir >= 3.0.6
BuildRequires:	mkfontdir fonts-bitmap-misc
BuildRequires:	fontpackages-devel
BuildRequires:	fonttools
URL:		http://efont.sourceforge.jp/

Source0:	http://globalbase.dl.sourceforge.jp/efont/10087/sazanami-20040629.tar.bz2
Source1:	fonts.alias.sazanami-gothic
Source2:	fonts.alias.sazanami-mincho
Source3:	%{fontname}-gothic-fontconfig.conf
Source4:	%{fontname}-mincho-fontconfig.conf
Patch1:		uni7E6B-gothic.patch
Patch2:		uni7E6B-mincho.patch
Patch3:		uni8449-mincho.patch

Summary:	Sazanami Japanese TrueType fonts
License:	BSD
Group:		System/Fonts/True type
Source44: import.info

%description
%common_desc

%package	-n fonts-ttf-sazanami-common
Summary:	Common files for Sazanami Japanese TrueType fonts
Group:		System/Fonts/True type

%description	-n fonts-ttf-sazanami-common
%common_desc

This package consists of files used by other %{oldname} packages.

%package -n fonts-ttf-sazanami-gothic
Summary:	Sazanami Gothic Japanese TrueType font
License:	BSD
Group:		System/Fonts/True type
Conflicts:	fonts-japanese <= 0.20061016-9.fc8
Provides:	ttfonts-ja = 1.2-37, %{fontname}-fonts-gothic = %{version}-%{release}
Obsoletes:	ttfonts-ja < 1.2-37, %{fontname}-fonts-gothic < 0.20040629-6.20061016
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-sazanami-gothic
%common_desc

This package contains Japanese TrueType font for Gothic type face.

%package -n fonts-ttf-sazanami-mincho
Summary:	Sazanami Mincho Japanese TrueType font
License:	BSD
Group:		System/Fonts/True type
Conflicts:	fonts-japanese <= 0.20061016-9.fc8
Provides:	ttfonts-ja = 1.2-37, %{fontname}-fonts-mincho = %{version}-%{release}
Obsoletes:	ttfonts-ja < 1.2-37, %{fontname}-fonts-mincho < 0.20040629-6.20061016
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-sazanami-mincho
%common_desc

This package contains Japanese TrueType font for Mincho type face.

%prep
%setup -q -n sazanami-20040629

%build
#rhbz#196433: modify the ttfs to change the glyph for 0x7E6B
ttx -i -a -e sazanami-gothic.ttf
patch -b -z .uni7E6B sazanami-gothic.ttx %{PATCH1}
touch -r sazanami-gothic.ttf sazanami-gothic.ttx
rm sazanami-gothic.ttf
ttx -b sazanami-gothic.ttx
touch -r sazanami-gothic.ttx sazanami-gothic.ttf

ttx -i -a -e sazanami-mincho.ttf
patch -b -z .uni7E6B sazanami-mincho.ttx %{PATCH2}
patch -b -z .uni8449 sazanami-mincho.ttx %{PATCH3}
touch -r sazanami-mincho.ttf sazanami-mincho.ttx
rm sazanami-mincho.ttf
ttx -b sazanami-mincho.ttx
touch -r sazanami-mincho.ttx sazanami-mincho.ttf

%install

install -dm 0755 $RPM_BUILD_ROOT%{_fontdir}/{gothic,mincho}
install -pm 0644 sazanami-gothic.ttf $RPM_BUILD_ROOT%{_fontdir}/gothic
install -pm 0644 sazanami-mincho.ttf $RPM_BUILD_ROOT%{_fontdir}/mincho

install -dm 0755 $RPM_BUILD_ROOT%{_fontconfig_templatedir} \
		 $RPM_BUILD_ROOT%{_fontconfig_confdir}
install -pm 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}-gothic.conf
install -pm 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}-mincho.conf

for fontconf in %{fontconf}-gothic.conf %{fontconf}-mincho.conf; do
	ln -s %{_fontconfig_templatedir}/$fontconf $RPM_BUILD_ROOT%{_fontconfig_confdir}/$fontconf
done

install -dm 0755 $RPM_BUILD_ROOT%{catalogue}
install -pm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_fontdir}/gothic/fonts.alias
install -pm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_fontdir}/mincho/fonts.alias

# Create fonts.scale and fonts.dir
%{_bindir}/ttmkfdir -d $RPM_BUILD_ROOT%{_fontdir}/gothic -o $RPM_BUILD_ROOT%{_fontdir}/gothic/fonts.scale
%{_bindir}/mkfontdir $RPM_BUILD_ROOT%{_fontdir}/gothic
%{_bindir}/ttmkfdir -d $RPM_BUILD_ROOT%{_fontdir}/mincho -o $RPM_BUILD_ROOT%{_fontdir}/mincho/fonts.scale
%{_bindir}/mkfontdir $RPM_BUILD_ROOT%{_fontdir}/mincho

# Install catalogue symlink
ln -sf %{_fontdir}/gothic $RPM_BUILD_ROOT%{catalogue}/%{oldname}-gothic
ln -sf %{_fontdir}/mincho $RPM_BUILD_ROOT%{catalogue}/%{oldname}-mincho
# broken aliases - no jisx0201.1976-0 in fonts.dir
sed -i -e '/jisx0201.1976-0/d' `find %buildroot%_datadir -type f -name fonts.alias`
sed -i -e 's/\.ttf -[^-]*-/.ttf -misc-/' `find %buildroot%_datadir -type f \( -name fonts.dir -or -name fonts.scale \)`
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


%files -n fonts-ttf-sazanami-gothic
%{_fontconfig_templatedir}/%{fontconf}-gothic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-gothic.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/gothic/sazanami-gothic.ttf

%dir %{_fontbasedir}/*/%{_fontstem}/gothic
%{catalogue}/%{fontname}-gothic*
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/gothic/fonts.dir
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/gothic/fonts.scale
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/gothic/fonts.alias

%files -n fonts-ttf-sazanami-mincho
%{_fontconfig_templatedir}/%{fontconf}-mincho.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-mincho.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/mincho/sazanami-mincho.ttf

%dir %{_fontbasedir}/*/%{_fontstem}/mincho
%{catalogue}/%{fontname}-mincho*
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/mincho/fonts.dir
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/mincho/fonts.scale
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/mincho/fonts.alias

%files -n fonts-ttf-sazanami-common
%doc doc README
%dir %{_fontbasedir}/*/%{_fontstem}

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt9_29
- update to new release by fcimport

* Wed Dec 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt9_28
- fixed build

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt8_28
- added appdata

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt8_22
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt8_20
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt8_19
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt8_18
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt8_17
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt7_17
- update to new release by fcimport

* Thu Sep 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt7_16
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt7_15
- rebuild with rpm-build-fonts alt3

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt6_15
- rebuild with new rpm-build-fonts

* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt5_15
- dropped jisx0201.1976-0 encoding in fonts.alias

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt4_15
- use ttmkfdir instead of fontscale (for correct spacing in XLFD)

* Mon Aug 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt3_15
- rebuild with new fontpackages-devel

* Mon Aug 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt2_15
- bugfix release by fcimport

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040629-alt1_15
- initial release by fcimport

