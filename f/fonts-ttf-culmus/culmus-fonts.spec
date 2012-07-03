%define oldname culmus-fonts
%define fontname culmus
%define fontconf 65-%{fontname}

%define common_desc \
The culmus-fonts package contains fonts for the display of\
Hebrew from the Culmus project.


Name:           fonts-ttf-culmus
Version:        0.121
Release:        alt2_1
Summary:        Fonts for Hebrew from Culmus project

Group:          System/Fonts/True type
License:        GPLv2
URL:            http://culmus.sourceforge.net
Source0:        http://downloads.sourceforge.net/culmus/%{fontname}-%{version}.tar.gz
Source1:        %{fontconf}-aharoni-clm.conf
Source2:        %{fontconf}-caladings-clm.conf
Source3:        %{fontconf}-david-clm.conf
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
Source15:        http://downloads.sourceforge.net/culmus/culmus-type1-0.121.tar.gz
Obsoletes:      culmus-fonts < 0.102-1

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
%common_desc
Meta-package of Culmus fonts which installs various families of culmus project.

%package -n fonts-ttf-culmus-common
Summary:        Common files of culmus-fonts
Group:          System/Fonts/True type
Obsoletes:      culmus-fonts < 0.102-1
%description -n fonts-ttf-culmus-common
%common_desc

This package consists of files used by other %{oldname} packages.


%package -n fonts-type1-culmus-aharoni-clm
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-type1-culmus-aharoni-clm
%common_desc

%files -n fonts-type1-culmus-aharoni-clm
%{_fontconfig_templatedir}/%{fontconf}-aharoni-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-aharoni-clm.conf
%{_fontbasedir}/*/%{_fontstem}/AharoniCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/AharoniCLM-*.pfa

%package -n fonts-type1-culmus-caladings-clm
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-type1-culmus-caladings-clm
%common_desc

%files -n fonts-type1-culmus-caladings-clm
%{_fontconfig_templatedir}/%{fontconf}-caladings-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-caladings-clm.conf
%{_fontbasedir}/*/%{_fontstem}/CaladingsCLM.afm
%{_fontbasedir}/*/%{_fontstem}/CaladingsCLM.pfa

%package -n fonts-type1-culmus-david-clm
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-type1-culmus-david-clm
%common_desc

%files -n fonts-type1-culmus-david-clm
%{_fontconfig_templatedir}/%{fontconf}-david-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-david-clm.conf
%{_fontbasedir}/*/%{_fontstem}/DavidCLM-*.ttf
%{_fontbasedir}/*/%{_fontstem}/DavidCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/DavidCLM-*.pfa

%package -n fonts-type1-culmus-drugulin-clm
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-type1-culmus-drugulin-clm
%common_desc

%files -n fonts-type1-culmus-drugulin-clm
%{_fontconfig_templatedir}/%{fontconf}-drugulin-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-drugulin-clm.conf
%{_fontbasedir}/*/%{_fontstem}/DrugulinCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/DrugulinCLM-*.pfa

%package -n fonts-type1-culmus-ellinia-clm
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-type1-culmus-ellinia-clm
%common_desc

%files -n fonts-type1-culmus-ellinia-clm
%{_fontconfig_templatedir}/%{fontconf}-ellinia-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-ellinia-clm.conf
%{_fontbasedir}/*/%{_fontstem}/ElliniaCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/ElliniaCLM-*.pfa

%package -n fonts-type1-frank-ruehl-clm
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-type1-frank-ruehl-clm
%common_desc

%files -n fonts-type1-frank-ruehl-clm
%{_fontconfig_templatedir}/%{fontconf}-frank-ruehl-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-frank-ruehl-clm.conf
%{_fontbasedir}/*/%{_fontstem}/FrankRuehlCLM-*.ttf
%{_fontbasedir}/*/%{_fontstem}/FrankRuehlCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/FrankRuehlCLM-*.pfa


%package -n fonts-ttf-culmus-hadasim-clm
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-ttf-culmus-hadasim-clm
%common_desc

%files -n fonts-ttf-culmus-hadasim-clm
%{_fontconfig_templatedir}/%{fontconf}-hadasim-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-hadasim-clm.conf
%{_fontbasedir}/*/%{_fontstem}/HadasimCLM-*.ttf

%package -n fonts-ttf-culmus-keteryg
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-ttf-culmus-keteryg
%common_desc

%files -n fonts-ttf-culmus-keteryg
%{_fontconfig_templatedir}/%{fontconf}-keteryg.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-keteryg.conf
%{_fontbasedir}/*/%{_fontstem}/KeterYG-*.ttf


%package -n fonts-ttf-culmus-miriam-clm
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-ttf-culmus-miriam-clm
%common_desc

%files -n fonts-ttf-culmus-miriam-clm
%{_fontconfig_templatedir}/%{fontconf}-miriam-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-miriam-clm.conf
%{_fontbasedir}/*/%{_fontstem}/MiriamCLM-*.ttf
%{_fontbasedir}/*/%{_fontstem}/MiriamCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/MiriamCLM-*.pfa

%package -n fonts-ttf-culmus-miriam-mono-clm
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-ttf-culmus-miriam-mono-clm
%common_desc

%files -n fonts-ttf-culmus-miriam-mono-clm
%{_fontconfig_templatedir}/%{fontconf}-miriam-mono-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-miriam-mono-clm.conf
%{_fontbasedir}/*/%{_fontstem}/MiriamMonoCLM-*.ttf
%{_fontbasedir}/*/%{_fontstem}/MiriamMonoCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/MiriamMonoCLM-*.pfa

%package -n fonts-type1-culmus-nachlieli-clm
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-type1-culmus-nachlieli-clm
%common_desc

%files -n fonts-type1-culmus-nachlieli-clm
%{_fontconfig_templatedir}/%{fontconf}-nachlieli-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-nachlieli-clm.conf
%{_fontbasedir}/*/%{_fontstem}/NachlieliCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/NachlieliCLM-*.pfa


%package -n fonts-ttf-culmus-simple-clm
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-ttf-culmus-simple-clm
%common_desc

%files -n fonts-ttf-culmus-simple-clm
%{_fontconfig_templatedir}/%{fontconf}-simple-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-simple-clm.conf
%{_fontbasedir}/*/%{_fontstem}/SimpleCLM-*.ttf

%package -n fonts-ttf-culmus-stamashkenaz-clm
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-ttf-culmus-stamashkenaz-clm
%common_desc

%files -n fonts-ttf-culmus-stamashkenaz-clm
%{_fontconfig_templatedir}/%{fontconf}-stamashkenaz-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-stamashkenaz-clm.conf
%{_fontbasedir}/*/%{_fontstem}/StamAshkenazCLM.ttf

%package -n fonts-ttf-culmus-stamsefarad-clm
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-ttf-culmus-stamsefarad-clm
%common_desc

%files -n fonts-ttf-culmus-stamsefarad-clm
%{_fontconfig_templatedir}/%{fontconf}-stamsefarad-clm.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-stamsefarad-clm.conf
%{_fontbasedir}/*/%{_fontstem}/StamSefaradCLM.ttf


%package -n fonts-type1-culmus-yehuda-clm
Summary:        Fonts for Hebrew from Culmus project
Group:          System/Fonts/True type
Requires:       fonts-ttf-culmus-common = %{version}-%{release}

%description -n fonts-type1-culmus-yehuda-clm
%common_desc

%files -n fonts-type1-culmus-yehuda-clm
%{_fontbasedir}/*/%{_fontstem}/YehudaCLM-*.afm
%{_fontbasedir}/*/%{_fontstem}/YehudaCLM-*.pfa

%prep
%setup -q -n %{fontname}-%{version}
%setup -c -q -a 15
mv %{fontname}-%{version}/* .
mv %{fontname}-type1-0.121/* .

%build

%install
rm -fr %{buildroot}

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
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-david-clm.conf
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

for fconf in %{fontconf}-aharoni-clm.conf \
             %{fontconf}-caladings-clm.conf \
             %{fontconf}-david-clm.conf \
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
             %{fontconf}-stamsefarad-clm.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done
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


%files -n fonts-ttf-culmus-common
%doc CHANGES GNU-GPL LICENSE LICENSE-BITSTREAM 

%dir %{_fontbasedir}/*/%{_fontstem}


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.121-alt2_1
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.121-alt1_1
- new fc release

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.120-alt2_2
- rebuild with new rpm-build-fonts

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.120-alt1_2
- initial release by fcimport

