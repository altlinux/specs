Group: System/Fonts/True type
%define oldname smc-fonts
%global	fontname	smc

# Common description
%global common_desc \
The SMC Fonts package contains fonts for the display of\
traditional and new Malayalam Script.

Name:		fonts-ttf-smc
Version:	6.1
Release:	alt1_4
Summary:	Open Type Fonts for Malayalam script
License:	GPLv3+ with exceptions and GPLv2+ with exceptions and GPLv2+ and  GPLv2 and GPL+
URL:		http://savannah.nongnu.org/projects/smc
Source0:	http://download.savannah.gnu.org/releases-noredirect/smc/fonts/malayalam-fonts-%{version}.tar.xz
Source1: 65-0-smc-meera.conf
Source2: 67-smc-anjalioldlipi.conf
Source3: 67-smc-dyuthi.conf
Source4: 67-smc-kalyani.conf
Source5: 65-0-smc-rachana.conf
Source6: 67-smc-raghumalayalam.conf
Source7: 67-smc-suruma.conf
BuildArch:	noarch
BuildRequires:	fontpackages-devel > 1.13
BuildRequires:	fontforge >= 20080429
Source44: import.info

%description
%common_desc

%package -n fonts-ttf-smc-common
Group: System/Fonts/True type
Summary:  Common files for smc-fonts

%description -n fonts-ttf-smc-common
%common_desc

%package -n fonts-ttf-smc-dyuthi
Group: System/Fonts/True type
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
%description -n fonts-ttf-smc-dyuthi
The Dyuthi font package contains fonts for the display of
traditional Malayalam Scripts.

%files -n fonts-ttf-smc-dyuthi
%{_fontconfig_templatedir}/67-smc-dyuthi.conf
%config(noreplace) %{_fontconfig_confdir}/67-smc-dyuthi.conf
%{_fontbasedir}/*/%{_fontstem}/Dyuthi*.ttf
%{_datadir}/appdata/smc-dyuthi.metainfo.xml
%doc Dyuthi/COPYING

%package -n fonts-ttf-smc-meera
Group: System/Fonts/True type
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: GPLv2+ with exceptions
%description -n fonts-ttf-smc-meera
The Meera font package contains fonts for the display of
traditional Malayalam Scripts.

%files -n fonts-ttf-smc-meera
%{_fontconfig_templatedir}/65-0-smc-meera.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-smc-meera.conf
%{_fontbasedir}/*/%{_fontstem}/Meera.ttf
%{_datadir}/appdata/smc-meera.metainfo.xml
%doc Meera/COPYING Meera/README


%package -n fonts-ttf-smc-rachana
Group: System/Fonts/True type
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: GPLv2+
%description -n fonts-ttf-smc-rachana
The Rachana font package contains fonts for the display of
traditional Malayalam Scripts.

%files -n fonts-ttf-smc-rachana
%{_fontconfig_templatedir}/65-0-smc-rachana.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-smc-rachana.conf
%{_fontbasedir}/*/%{_fontstem}/Rachana.ttf
%{_datadir}/appdata/smc-rachana.metainfo.xml
%doc Rachana/COPYING Rachana/LICENSE Rachana/README


%package -n fonts-ttf-smc-raghumalayalam
Group: System/Fonts/True type
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
%description -n fonts-ttf-smc-raghumalayalam
The SMC Malayalam fonts package contains fonts for the display of
new Malayalam Scripts.

%files -n fonts-ttf-smc-raghumalayalam
%{_fontconfig_templatedir}/67-smc-raghumalayalam.conf
%config(noreplace) %{_fontconfig_confdir}/67-smc-raghumalayalam.conf
%{_fontbasedir}/*/%{_fontstem}/RaghuMalayalamSans.ttf
%{_datadir}/appdata/smc-raghumalayalam.metainfo.xml
%doc RaghuMalayalamSans/COPYING

%package -n fonts-ttf-smc-suruma
Group: System/Fonts/True type
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: GPLv3 with exceptions
%description -n fonts-ttf-smc-suruma
The Suruma font package contains fonts for the display of
traditional Malayalam Scripts.

%files -n fonts-ttf-smc-suruma
%{_fontconfig_templatedir}/67-smc-suruma.conf
%config(noreplace) %{_fontconfig_confdir}/67-smc-suruma.conf
%{_fontbasedir}/*/%{_fontstem}/Suruma.ttf
%{_datadir}/appdata/smc-suruma.metainfo.xml
%doc Suruma/COPYING Suruma/README

%package -n fonts-ttf-smc-kalyani
Group: System/Fonts/True type
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
%description -n fonts-ttf-smc-kalyani
The Kalyani font package contains fonts for the display of
new Malayalam Scripts.

%files -n fonts-ttf-smc-kalyani
%{_fontconfig_templatedir}/67-smc-kalyani.conf
%config(noreplace) %{_fontconfig_confdir}/67-smc-kalyani.conf
%{_fontbasedir}/*/%{_fontstem}/Kalyani.ttf
%{_datadir}/appdata/smc-kalyani.metainfo.xml
%doc Kalyani/COPYING

%package -n fonts-ttf-smc-anjalioldlipi
Group: System/Fonts/True type
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: OFL
%description -n fonts-ttf-smc-anjalioldlipi
The Anjali OldLipi package contains fonts for the display of
traditional Malayalam Scripts.

%files -n fonts-ttf-smc-anjalioldlipi
%{_fontconfig_templatedir}/67-smc-anjalioldlipi.conf
%config(noreplace) %{_fontconfig_confdir}/67-smc-anjalioldlipi.conf
%{_fontbasedir}/*/%{_fontstem}/AnjaliOldLipi.ttf
%{_datadir}/appdata/smc-anjalioldlipi.metainfo.xml
%doc AnjaliOldLipi/COPYING


%prep
%setup -q -n fonts
sed -i 's/\r//' */COPYING
sed -i 's/\r//' Rachana/LICENSE

%build
chmod +x generate.pe
make

%install
#%%{_fontdir} is shared by all subpackages since they all are for malayalam script only
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p AnjaliOldLipi/*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p Dyuthi/*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p Kalyani/*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p Meera/*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p Rachana/*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p RaghuMalayalamSans/*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p Suruma/*.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/65-0-smc-meera.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-anjalioldlipi.conf
install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-dyuthi.conf
install -m 0644 -p %{SOURCE4} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-kalyani.conf
install -m 0644 -p %{SOURCE5} \
	%{buildroot}%{_fontconfig_templatedir}/65-0-smc-rachana.conf
install -m 0644 -p %{SOURCE6} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-raghumalayalam.conf
install -m 0644 -p %{SOURCE7} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-suruma.conf

for fconf in 65-0-smc-meera.conf \
	     67-smc-anjalioldlipi.conf \
	     67-smc-dyuthi.conf \
	     67-smc-kalyani.conf \
	     65-0-smc-rachana.conf \
	     67-smc-raghumalayalam.conf \
	     67-smc-suruma.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
	%{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream data
install -Dm 0644 -p smc.metainfo.xml \
		%{buildroot}%{_datadir}/appdata/smc.metainfo.xml
install -Dm 0644 -p AnjaliOldLipi/smc-anjalioldlipi.metainfo.xml \
		%{buildroot}%{_datadir}/appdata/smc-anjalioldlipi.metainfo.xml
install -Dm 0644 -p Dyuthi/smc-dyuthi.metainfo.xml \
		%{buildroot}%{_datadir}/appdata/smc-dyuthi.metainfo.xml
install -Dm 0644 -p Kalyani/smc-kalyani.metainfo.xml \
		%{buildroot}%{_datadir}/appdata/smc-kalyani.metainfo.xml
install -Dm 0644 -p Meera/smc-meera.metainfo.xml \
		%{buildroot}%{_datadir}/appdata/smc-meera.metainfo.xml
install -Dm 0644 -p Rachana/smc-rachana.metainfo.xml \
		%{buildroot}%{_datadir}/appdata/smc-rachana.metainfo.xml
install -Dm 0644 -p RaghuMalayalamSans/smc-raghumalayalam.metainfo.xml \
		%{buildroot}%{_datadir}/appdata/smc-raghumalayalam.metainfo.xml
install -Dm 0644 -p Suruma/smc-suruma.metainfo.xml \
		%{buildroot}%{_datadir}/appdata/smc-suruma.metainfo.xml
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


%files -n fonts-ttf-smc-common
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc ChangeLog

%changelog
* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 6.1-alt1_4
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 6.0-alt1_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1_5
- update to new release by fcimport

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1_3
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1_2
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.4-alt3_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.4-alt2_7
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 4.4-alt2_5
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 4.4-alt1_5
- initial release by fcimport

