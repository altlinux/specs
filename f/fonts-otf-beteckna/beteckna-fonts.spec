# BEGIN SourceDeps(oneline):
BuildRequires: python
# END SourceDeps(oneline)
%define oldname beteckna-fonts
%global	fontname	beteckna
%global common_desc \
This font is available from beteckna.se, it is a geometric sans-serif \
typeface inspired by Paul Renners popular type, Futura. It was drawn by \
Johan Mattsson in Maj 2007. The font is free, licensed under terms of the \
GNU GPL. This version supports English and a few nordic languages. \
Special character &#x2708; ( a'. ) depicts two cats.

%global fontconf	60-%{fontname}-fonts

Name:		fonts-otf-beteckna
Version:	0.3
Release:	alt4_15
Summary:	Beteckna sans-serif fonts

Group:		System/Fonts/True type
License:	GPLv2
URL:		http://gnu.ethz.ch/linuks.mine.nu/beteckna/
Source0:	http://gnu.ethz.ch/linuks.mine.nu/beteckna/beteckna-0.3.tar.gz
Source1:	%{oldname}-fontconfig.conf
Source2:	%{oldname}-lower-case-fontconfig.conf
Source3:	%{oldname}-small-caps-fontconfig.conf
Source4:	%{fontname}.metainfo.xml
Source5:	%{fontname}-lower-case.metainfo.xml
Source6:	%{fontname}-small-caps.metainfo.xml

BuildArch:	noarch
BuildRequires: fontforge libfontforge, fontpackages-devel
Requires:	%{name}-common = %{version}
Source44: import.info

%description
%common_desc

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/Beteckna.otf

%package	-n fonts-otf-beteckna-common
Group: System/Fonts/True type
Summary:	Common files of %{oldname}

%description -n fonts-otf-beteckna-common
%common_desc

This package consists of files used by other %{oldname} packages.


# 1 Lower Case
%package -n fonts-otf-beteckna-lower-case
Group: System/Fonts/True type
Summary:	Beteckna lower case sfd fonts
Requires:	%{name}-common = %{version}

%description -n fonts-otf-beteckna-lower-case
%common_desc

These are lower case Beteckna Fonts.

%files -n fonts-otf-beteckna-lower-case
%{_fontconfig_templatedir}/%{fontconf}-lower-case.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-lower-case.conf
%{_fontbasedir}/*/%{_fontstem}/BetecknaLowerCase*.otf
%{_datadir}/appdata/%{fontname}-lower-case.metainfo.xml


# 1 Small Caps
%package -n fonts-otf-beteckna-small-caps
Group: System/Fonts/True type
Summary:	Beteckna small caps sfd fonts
Requires:	%{name}-common = %{version}

%description -n fonts-otf-beteckna-small-caps
%common_desc

These are small caps Beteckna Fonts.

%files -n fonts-otf-beteckna-small-caps
%{_fontconfig_templatedir}/%{fontconf}-small-caps.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-small-caps.conf
%{_fontbasedir}/*/%{_fontstem}/BetecknaSmallCaps.otf
%{_datadir}/appdata/%{fontname}-small-caps.metainfo.xml

%prep
%setup -q -n beteckna-0.3

fold -s CHANGELOG > CHANGELOG.new
sed -i 's/\r//' CHANGELOG.new
touch -r CHANGELOG CHANGELOG.new
mv CHANGELOG.new CHANGELOG


%build
fontforge -lang=ff -script "-" Beteckna*.sfd << EOF
i = 1
while ( i < \$argc )
	Open (\$argv[i], 1)
	otfile = \$fontname + ".otf"
	Generate(otfile,"otf")
	Close()
	i++
endloop
EOF

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}


install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-small-caps.conf
install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-lower-case.conf

for fconf in %{fontconf}.conf %{fontconf}-lower-case.conf %{fontconf}-small-caps.conf ; 
do
	ln -s %{_fontconfig_templatedir}/$fconf %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE5} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-lower-case.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-small-caps.metainfo.xml
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

%files -n fonts-otf-beteckna-common
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc AUTHORS LICENSE CHANGELOG readme.html

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.3-alt4_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.3-alt4_14
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt4_13
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt4_12
- bugfix: fixed subpackage name

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt3_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt3_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt3_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt3_9
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt3_8
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_8
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_7
- rebuild with new rpm-build-fonts

* Thu Aug 04 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_7
- initial release by fcimport

