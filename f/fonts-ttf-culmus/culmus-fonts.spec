Group: System/Fonts/True type
%define oldname culmus-fonts
%global fontname culmus
%global fontconfd 65-%{fontname}
%global fontconf 66-%{fontname}

%global common_desc \
The culmus-fonts package contains fonts for the display of\
Hebrew from the Culmus project.


Name:           fonts-ttf-culmus
Version:        0.130
Release:        alt2_9
Summary:        Fonts for Hebrew from Culmus project

License:        GPLv2
URL:            http://culmus.sourceforge.net
Source0:        http://downloads.sourceforge.net/culmus/%{fontname}-%{version}.tar.gz
Source1:        %{fontconf}-aharoni-clm.conf
Source2:        %{fontconf}-caladings-clm.conf
Source3:        %{fontconfd}-david-clm.conf
Source4:        %{fontconf}-drugulin-clm.conf
Source5:        %{fontconf}-ellinia-clm.conf
Source6:        %{fontconf}-frank-ruehl-clm.conf
Source7:        %{fontconf}-miriam-clm.conf
Source8:        %{fontconf}-miriam-mono-clm.conf
Source9:        %{fontconf}-nachlieli-clm.conf
Source10:        %{fontconf}-hadasim-clm.conf
Source11:        %{fontconf}-keteryg.conf
Source12:        %{fontconf}-simple-clm.conf
Source13:        %{fontconf}-stamashkenaz-clm.conf
Source14:        %{fontconf}-stamsefarad-clm.conf
Source15:        %{fontconf}-shofar.conf
Source16:        http://downloads.sourceforge.net/culmus/culmus-type1-0.121.tar.gz
Obsoletes:      culmus-fonts < 0.102-1

#for appstream metainfo
Source50:       %{fontname}-aharoni-clm.metainfo.xml
Source51:       %{fontname}-caladings-clm.metainfo.xml
Source52:       %{fontname}-david-clm.metainfo.xml
Source53:       %{fontname}-drugulin-clm.metainfo.xml
Source54:       %{fontname}-ellinia-clm.metainfo.xml
Source55:       %{fontname}-frank-ruehl-clm.metainfo.xml
Source56:       %{fontname}-hadasim-clm.metainfo.xml
Source57:       %{fontname}-keteryg.metainfo.xml
Source58:       %{fontname}-miriam-clm.metainfo.xml
Source59:       %{fontname}-miriam-mono-clm.metainfo.xml
Source60:       %{fontname}-nachlieli-clm.metainfo.xml
Source61:       %{fontname}-simple-clm.metainfo.xml
Source62:       %{fontname}-stamashkenaz-clm.metainfo.xml
Source63:       %{fontname}-stamsefarad-clm.metainfo.xml
Source64:       %{fontname}-yehuda-clm.metainfo.xml
Source65:       %{fontname}-shofar.metainfo.xml
Source66:       %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
%common_desc
Meta-package of Culmus fonts which installs various families of culmus project.

%package -n fonts-ttf-culmus-common
Group: System/Fonts/True type
Summary:        Common files of culmus-fonts
%description -n fonts-ttf-culmus-common
%common_desc

This package consists of files used by other %{oldname} packages.

%package -n fonts-type1-culmus-aharoni-clm
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-type1-culmus-aharoni-clm
%common_desc

%files -n fonts-type1-culmus-aharoni-clm
%{_fontconfig_templatedir}/%{fontconf}-aharoni-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-aharoni-clm.conf
%{_fontbasedir}/*/%{_fontstem}/AharoniCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/AharoniCLM-*.pfa
%{_datadir}/appdata/%{fontname}-aharoni-clm.metainfo.xml

%package -n fonts-type1-culmus-caladings-clm
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-type1-culmus-caladings-clm
%common_desc

%files -n fonts-type1-culmus-caladings-clm
%{_fontconfig_templatedir}/%{fontconf}-caladings-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-caladings-clm.conf
%{_fontbasedir}/*/%{_fontstem}/CaladingsCLM.afm
%{_fontbasedir}/*/%{_fontstem}/CaladingsCLM.pfa
%{_datadir}/appdata/%{fontname}-caladings-clm.metainfo.xml

%package -n fonts-type1-culmus-david-clm
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-type1-culmus-david-clm
%common_desc

%files -n fonts-type1-culmus-david-clm
%{_fontconfig_templatedir}/%{fontconfd}-david-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconfd}-david-clm.conf
%{_fontbasedir}/*/%{_fontstem}/DavidCLM-*.ttf
%{_fontbasedir}/*/%{_fontstem}/DavidCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/DavidCLM-*.pfa
%{_datadir}/appdata/%{fontname}-david-clm.metainfo.xml

%package -n fonts-type1-culmus-drugulin-clm
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-type1-culmus-drugulin-clm
%common_desc

%files -n fonts-type1-culmus-drugulin-clm
%{_fontconfig_templatedir}/%{fontconf}-drugulin-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-drugulin-clm.conf
%{_fontbasedir}/*/%{_fontstem}/DrugulinCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/DrugulinCLM-*.pfa
%{_datadir}/appdata/%{fontname}-drugulin-clm.metainfo.xml

%package -n fonts-type1-culmus-ellinia-clm
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-type1-culmus-ellinia-clm
%common_desc

%files -n fonts-type1-culmus-ellinia-clm
%{_fontconfig_templatedir}/%{fontconf}-ellinia-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-ellinia-clm.conf
%{_fontbasedir}/*/%{_fontstem}/ElliniaCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/ElliniaCLM-*.pfa
%{_datadir}/appdata/%{fontname}-ellinia-clm.metainfo.xml

%package -n fonts-type1-frank-ruehl-clm
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-type1-frank-ruehl-clm
%common_desc

%files -n fonts-type1-frank-ruehl-clm
%{_fontconfig_templatedir}/%{fontconf}-frank-ruehl-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-frank-ruehl-clm.conf
%{_fontbasedir}/*/%{_fontstem}/FrankRuehlCLM-*.ttf
%{_fontbasedir}/*/%{_fontstem}/FrankRuehlCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/FrankRuehlCLM-*.pfa
%{_datadir}/appdata/%{fontname}-frank-ruehl-clm.metainfo.xml


%package -n fonts-ttf-culmus-hadasim-clm
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-ttf-culmus-hadasim-clm
%common_desc

%files -n fonts-ttf-culmus-hadasim-clm
%{_fontconfig_templatedir}/%{fontconf}-hadasim-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-hadasim-clm.conf
%{_fontbasedir}/*/%{_fontstem}/HadasimCLM-*.ttf
%{_datadir}/appdata/%{fontname}-hadasim-clm.metainfo.xml

%package -n fonts-ttf-culmus-keteryg
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-ttf-culmus-keteryg
%common_desc

%files -n fonts-ttf-culmus-keteryg
%{_fontconfig_templatedir}/%{fontconf}-keteryg.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-keteryg.conf
%{_fontbasedir}/*/%{_fontstem}/KeterYG-*.ttf
%{_datadir}/appdata/%{fontname}-keteryg.metainfo.xml


%package -n fonts-ttf-culmus-miriam-clm
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-ttf-culmus-miriam-clm
%common_desc

%files -n fonts-ttf-culmus-miriam-clm
%{_fontconfig_templatedir}/%{fontconf}-miriam-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-miriam-clm.conf
%{_fontbasedir}/*/%{_fontstem}/MiriamCLM-*.ttf
%{_fontbasedir}/*/%{_fontstem}/MiriamCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/MiriamCLM-*.pfa
%{_datadir}/appdata/%{fontname}-miriam-clm.metainfo.xml

%package -n fonts-ttf-culmus-miriam-mono-clm
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-ttf-culmus-miriam-mono-clm
%common_desc

%files -n fonts-ttf-culmus-miriam-mono-clm
%{_fontconfig_templatedir}/%{fontconf}-miriam-mono-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-miriam-mono-clm.conf
%{_fontbasedir}/*/%{_fontstem}/MiriamMonoCLM-*.ttf
%{_fontbasedir}/*/%{_fontstem}/MiriamMonoCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/MiriamMonoCLM-*.pfa
%{_datadir}/appdata/%{fontname}-miriam-mono-clm.metainfo.xml

%package -n fonts-type1-culmus-nachlieli-clm
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-type1-culmus-nachlieli-clm
%common_desc

%files -n fonts-type1-culmus-nachlieli-clm
%{_fontconfig_templatedir}/%{fontconf}-nachlieli-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-nachlieli-clm.conf
%{_fontbasedir}/*/%{_fontstem}/NachlieliCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/NachlieliCLM-*.pfa
%{_datadir}/appdata/%{fontname}-nachlieli-clm.metainfo.xml


%package -n fonts-ttf-culmus-simple-clm
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-ttf-culmus-simple-clm
%common_desc

%files -n fonts-ttf-culmus-simple-clm
%{_fontconfig_templatedir}/%{fontconf}-simple-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-simple-clm.conf
%{_fontbasedir}/*/%{_fontstem}/SimpleCLM-*.ttf
%{_datadir}/appdata/%{fontname}-simple-clm.metainfo.xml

%package -n fonts-ttf-culmus-stamashkenaz-clm
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-ttf-culmus-stamashkenaz-clm
%common_desc

%files -n fonts-ttf-culmus-stamashkenaz-clm
%{_fontconfig_templatedir}/%{fontconf}-stamashkenaz-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-stamashkenaz-clm.conf
%{_fontbasedir}/*/%{_fontstem}/StamAshkenazCLM.ttf
%{_datadir}/appdata/%{fontname}-stamashkenaz-clm.metainfo.xml

%package -n fonts-ttf-culmus-stamsefarad-clm
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-ttf-culmus-stamsefarad-clm
%common_desc

%files -n fonts-ttf-culmus-stamsefarad-clm
%{_fontconfig_templatedir}/%{fontconf}-stamsefarad-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-stamsefarad-clm.conf
%{_fontbasedir}/*/%{_fontstem}/StamSefaradCLM.ttf
%{_datadir}/appdata/%{fontname}-stamsefarad-clm.metainfo.xml


%package -n fonts-type1-culmus-yehuda-clm
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-type1-culmus-yehuda-clm
%common_desc

%files -n fonts-type1-culmus-yehuda-clm
%{_fontbasedir}/*/%{_fontstem}/YehudaCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/YehudaCLM-*.pfa
%{_datadir}/appdata/%{fontname}-yehuda-clm.metainfo.xml

%package -n fonts-ttf-culmus-shofar
Group: System/Fonts/True type
Summary:        Fonts for Hebrew from Culmus project
Requires:       fonts-ttf-culmus-common = %{version}

%description -n fonts-ttf-culmus-shofar
%common_desc

%files -n fonts-ttf-culmus-shofar
%{_fontconfig_templatedir}/%{fontconf}-shofar.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-shofar.conf
%{_fontbasedir}/*/%{_fontstem}/Shofar*.ttf
%{_datadir}/appdata/%{fontname}-shofar.metainfo.xml

%prep
%setup -q -n %{fontname}-%{version}
%setup -n %{oldname}-%{version} -c -q -a 16
mv %{fontname}-%{version}/* .
mv %{fontname}-type1-0.121/* .

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0644 -p *.afm %{buildroot}%{_fontdir}
install -m 0644 -p *.pfa %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-aharoni-clm.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-caladings-clm.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconfd}-david-clm.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-drugulin-clm.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-ellinia-clm.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-frank-ruehl-clm.conf
install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-miriam-clm.conf
install -m 0644 -p %{SOURCE8} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-miriam-mono-clm.conf
install -m 0644 -p %{SOURCE9} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nachlieli-clm.conf
install -m 0644 -p %{SOURCE10} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-hadasim-clm.conf
install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-keteryg.conf
install -m 0644 -p %{SOURCE12} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-simple-clm.conf
install -m 0644 -p %{SOURCE13} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-stamashkenaz-clm.conf
install -m 0644 -p %{SOURCE14} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-stamsefarad-clm.conf
install -m 0644 -p %{SOURCE15} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-shofar.conf

for fconf in %{fontconf}-aharoni-clm.conf \
             %{fontconf}-caladings-clm.conf \
             %{fontconfd}-david-clm.conf \
             %{fontconf}-drugulin-clm.conf \
             %{fontconf}-ellinia-clm.conf \
             %{fontconf}-frank-ruehl-clm.conf \
             %{fontconf}-miriam-clm.conf \
             %{fontconf}-miriam-mono-clm.conf \
             %{fontconf}-nachlieli-clm.conf \
             %{fontconf}-hadasim-clm.conf \
             %{fontconf}-keteryg.conf \
             %{fontconf}-simple-clm.conf \
             %{fontconf}-stamashkenaz-clm.conf \
             %{fontconf}-stamsefarad-clm.conf \
             %{fontconf}-shofar.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE50} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-aharoni-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE51} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-caladings-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE52} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-david-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE53} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-drugulin-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE54} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-ellinia-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE55} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-frank-ruehl-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE56} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-hadasim-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE57} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-keteryg.metainfo.xml
install -Dm 0644 -p %{SOURCE58} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-miriam-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE59} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-miriam-mono-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE60} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-nachlieli-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE61} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-simple-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE62} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-stamashkenaz-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE63} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-stamsefarad-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE64} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-yehuda-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE65} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-shofar.metainfo.xml
install -Dm 0644 -p %{SOURCE66} \
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


%files -n fonts-ttf-culmus-common
%doc CHANGES GNU-GPL LICENSE LICENSE-BITSTREAM 
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.130-alt2_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.130-alt2_7
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.130-alt2_6
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.130-alt2_5
- bugfix: fixed subpackage name

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.130-alt1_5
- update to new release by fcimport

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.130-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.130-alt1_3
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.130-alt1_2
- update to new release by fcimport

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.130-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.121-alt2_5
- update to new release by fcimport

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.121-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.121-alt2_3
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.121-alt2_2
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.121-alt2_1
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.121-alt1_1
- new fc release

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.120-alt2_2
- rebuild with new rpm-build-fonts

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.120-alt1_2
- initial release by fcimport

