# BEGIN SourceDeps(oneline):
BuildRequires: python
# END SourceDeps(oneline)
%define oldname sj-fonts
%define fontname sj
%define fontconf 63-%{fontname}

%define common_desc Two fonts by Steve Jordi released under the GPL 

Name:          fonts-ttf-sj
Version:       2.0.2
Release:       alt3_12
Summary:       Two fonts by Steve Jordi released under the GPL

Group:         System/Fonts/True type
License:       GPLv2 with exceptions
URL:           http://sjfonts.sourceforge.net
Source0:       sjfonts-source-2.0.2.tar.bz2
Source1:       %{oldname}-delphine-fontconfig.conf
Source2:       %{oldname}-stevehand-fontconfig.conf
Source3:       %{fontname}-stevehand.metainfo.xml
Source4:       %{fontname}-delphine.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: fontforge
Source44: import.info

%description
%common_desc

%package -n fonts-ttf-sj-common
Summary:       Common files for %{oldname}
Group:         System/Fonts/True type

%description -n fonts-ttf-sj-common
%common_desc

This package consists of files used by other %{oldname} packages.

%package -n fonts-ttf-sj-delphine
Summary:       Handwriting font
Group:         System/Fonts/True type
Requires:      %{name}-common = %{version}-%{release}

%description -n fonts-ttf-sj-delphine
%common_desc

Handwriting font by Steve Jordi covering latin glyphs.

%files -n fonts-ttf-sj-delphine
%{_fontconfig_templatedir}/%{fontconf}-delphine.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-delphine.conf
%{_fontbasedir}/*/%{_fontstem}/Delphine.ttf
%{_datadir}/appdata/%{fontname}-delphine.metainfo.xml

%package -n fonts-ttf-sj-stevehand
Summary:       Handwriting font
Group:         System/Fonts/True type
Requires:      %{name}-common = %{version}-%{release}

%description -n fonts-ttf-sj-stevehand
%common_desc

Handwriting font by Steve Jordi covering latin glyphs.

%files -n fonts-ttf-sj-stevehand
%{_fontconfig_templatedir}/%{fontconf}-stevehand.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-stevehand.conf
%{_fontbasedir}/*/%{_fontstem}/SteveHand.ttf
%{_datadir}/appdata/%{fontname}-stevehand.metainfo.xml

%prep
%setup -n %{oldname}-%{version} -q -c %{oldname}-%{version}

%build
fontforge -lang=ff -script "-" Delphine.sfd SteveHand.sfd <<EOF
i = 1
while ( i < \$argc )
  Open (\$argv[i], 1)
  Generate (\$fontname + ".ttf")
  PrintSetup (5)
  PrintFont (0, 0, "", \$fontname + "-sample.pdf")
  Close()
  i++
endloop
EOF

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-delphine.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-stevehand.conf

for fontconf in %{fontconf}-delphine.conf %{fontconf}-stevehand.conf ; do
  ln -s %{_fontconfig_templatedir}/$fontconf %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-stevehand.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-delphine.metainfo.xml
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

%files -n fonts-ttf-sj-common
%doc COPYING
%doc README

%dir %{_fontbasedir}/*/%{_fontstem}

%changelog
* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt3_12
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt3_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt3_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt3_8
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt3_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_7
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_6
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_6
- initial release by fcimport

