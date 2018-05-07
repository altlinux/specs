Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/afm2tfm /usr/bin/fc-cache /usr/bin/mkfontdir /usr/bin/mkfontscale /usr/bin/mktexlsr /usr/bin/ttmkfdir /usr/bin/vptovf
# END SourceDeps(oneline)
%define oldname thai-scalable-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname thai-scalable
%global fontconf 90-%{fontname}-synthetic

%global archivename fonts-tlwg

%global common_desc \
%{archivename} provides a collection of free scalable Thai fonts.

Name:      fonts-ttf-thai-scalable
Version:   0.6.5
Release:   alt1_1
Summary:   Thai TrueType fonts
License:   GPLv2+ and Bitstream Vera
URL:       http://linux.thai.net/projects/thaifonts-scalable
Source0:   http://linux.thai.net/pub/ThaiLinux/software/%{archivename}/%{archivename}-%{version}.tar.xz
Source1:   %{fontconf}-garuda.conf
Source2:   %{fontconf}-kinnari.conf
Source3:   %{fontconf}-umpush.conf
Source4:   %{fontconf}-laksaman.conf

#Appdata Metainfo
Source11:  %{fontname}-garuda.metainfo.xml
Source12:  %{fontname}-kinnari.metainfo.xml
Source13:  %{fontname}-loma.metainfo.xml
Source14:  %{fontname}-norasi.metainfo.xml
Source15:  %{fontname}-purisa.metainfo.xml
Source16:  %{fontname}-sawasdee.metainfo.xml
Source17:  %{fontname}-tlwgmono.metainfo.xml
Source18:  %{fontname}-tlwgtypewriter.metainfo.xml
Source19:  %{fontname}-tlwgtpist.metainfo.xml
Source20:  %{fontname}-tlwgtypo.metainfo.xml
Source21:  %{fontname}-umpush.metainfo.xml
Source22:  %{fontname}-waree.metainfo.xml
Source23:  %{fontname}-laksaman.metainfo.xml


BuildArch: noarch
BuildRequires: fontforge libfontforge
BuildRequires: fontpackages-devel
Source44: import.info
Provides: fonts-ttf-thai = 0.1-alt7
Obsoletes: fonts-ttf-thai < 0.1-alt7

%description
%common_desc

Thai scalable fonts included here are:
- Kinnari, Garuda and Norasi from the National Font project
- DB Thai Text from DearBook
- TlwgMono, PseudoMono, Purisa by TLWG


%package -n fonts-ttf-thai-scalable-common
Summary:   Common files of %{oldname}
Group:     System/Fonts/True type

%description -n fonts-ttf-thai-scalable-common
%common_desc

This package consists of files used by other %{oldname} packages.


%package -n fonts-ttf-thai-scalable-garuda
Group: System/Fonts/True type
Summary:        Thai Garuda fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-garuda
%common_desc

This package provides the Garuda family of Thai fonts.

%files -n fonts-ttf-thai-scalable-garuda
%{_fontconfig_templatedir}/%{fontconf}-garuda.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-garuda.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Garuda*.ttf
%{_datadir}/appdata/%{fontname}-garuda.metainfo.xml


%package -n fonts-ttf-thai-scalable-kinnari
Group: System/Fonts/True type
Summary:        Thai Kinnari fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-kinnari
%common_desc

This package provides the Kinnari family of Thai fonts.

%files -n fonts-ttf-thai-scalable-kinnari
%{_fontconfig_templatedir}/%{fontconf}-kinnari.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-kinnari.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Kinnari*.ttf
%{_datadir}/appdata/%{fontname}-kinnari.metainfo.xml


%package -n fonts-ttf-thai-scalable-loma
Group: System/Fonts/True type
Summary:        Thai Loma fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-loma
%common_desc

This package provides the Loma family of Thai fonts.

%files -n fonts-ttf-thai-scalable-loma
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Loma*.ttf
%{_datadir}/appdata/%{fontname}-loma.metainfo.xml


%package -n fonts-ttf-thai-scalable-norasi
Group: System/Fonts/True type
Summary:        Thai Norasi fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-norasi
%common_desc

This package provides the Norasi family of Thai fonts.

%files -n fonts-ttf-thai-scalable-norasi
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Norasi*.ttf
%{_datadir}/appdata/%{fontname}-norasi.metainfo.xml


%package -n fonts-ttf-thai-scalable-purisa
Group: System/Fonts/True type
Summary:        Thai Purisa fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-purisa
%common_desc

This package provides the Purisa family of Thai fonts.

%files -n fonts-ttf-thai-scalable-purisa
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Purisa*.ttf
%{_datadir}/appdata/%{fontname}-purisa.metainfo.xml


%package -n fonts-ttf-thai-scalable-sawasdee
Group: System/Fonts/True type
Summary:        Thai Sawasdee fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-sawasdee
%common_desc

This package provides the Sawasdee family of Thai fonts.

%files -n fonts-ttf-thai-scalable-sawasdee
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Sawasdee*.ttf
%{_datadir}/appdata/%{fontname}-sawasdee.metainfo.xml


%package -n fonts-ttf-thai-scalable-tlwgmono
Group: System/Fonts/True type
Summary:        Thai TlwgMono fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-tlwgmono
%common_desc

This package provides the TlwgMono family of Thai fonts.

%files -n fonts-ttf-thai-scalable-tlwgmono
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/TlwgMono*.ttf
%{_datadir}/appdata/%{fontname}-tlwgmono.metainfo.xml


%package -n fonts-ttf-thai-scalable-tlwgtypewriter
Group: System/Fonts/True type
Summary:        Thai TlwgTypewriter fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-tlwgtypewriter
%common_desc

This package provides the TlwgTypewriter family of Thai fonts.

%files -n fonts-ttf-thai-scalable-tlwgtypewriter
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/TlwgTypewriter*.ttf
%{_datadir}/appdata/%{fontname}-tlwgtypewriter.metainfo.xml


%package -n fonts-ttf-thai-scalable-tlwgtypist
Group: System/Fonts/True type
Summary:        Thai TlwgTypist fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-tlwgtypist
%common_desc

This package provides the TlwgTypist family of Thai fonts.

%files -n fonts-ttf-thai-scalable-tlwgtypist
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/TlwgTypist*.ttf
%{_datadir}/appdata/%{fontname}-tlwgtpist.metainfo.xml


%package -n fonts-ttf-thai-scalable-tlwgtypo
Group: System/Fonts/True type
Summary:        Thai TlwgTypo fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-tlwgtypo
%common_desc

This package provides the TlwgTypo family of Thai fonts.

%files -n fonts-ttf-thai-scalable-tlwgtypo
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/TlwgTypo*.ttf
%{_datadir}/appdata/%{fontname}-tlwgtypo.metainfo.xml


%package -n fonts-ttf-thai-scalable-umpush
Group: System/Fonts/True type
Summary:        Thai Umpush fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-umpush
%common_desc

This package provides the Umpush family of Thai fonts.

%files -n fonts-ttf-thai-scalable-umpush
%{_fontconfig_templatedir}/%{fontconf}-umpush.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-umpush.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Umpush*.ttf
%{_datadir}/appdata/%{fontname}-umpush.metainfo.xml

%package -n fonts-ttf-thai-scalable-laksaman
Group: System/Fonts/True type
Summary:        Thai Laksaman fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-laksaman
%common_desc

This package provides the Laksaman family of Thai fonts.

%files -n fonts-ttf-thai-scalable-laksaman
%{_fontconfig_templatedir}/%{fontconf}-laksaman.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-laksaman.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Laksaman*.ttf
%{_datadir}/appdata/%{fontname}-laksaman.metainfo.xml

%package -n fonts-ttf-thai-scalable-waree
Group: System/Fonts/True type
Summary:        Thai Waree fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-waree
%common_desc

This package provides the Waree family of Thai fonts.

%files -n fonts-ttf-thai-scalable-waree
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Waree*.ttf
%{_datadir}/appdata/%{fontname}-waree.metainfo.xml


%prep
%setup -q -n %{archivename}-%{version}


%build
%configure --with-ttfdir=%{_fontdir} --enable-ttf
make


%install
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

make install DESTDIR=%{buildroot} INSTALL="install -p"

# remove upstream font config
# fontconfig's 65-nonlatin.conf covers 65-ttf-thai-tlwg.conf
rm %{buildroot}%{_datadir}/fontconfig/conf.avail/64-15-laksaman.conf
rm %{buildroot}%{_datadir}/fontconfig/conf.avail/64-*-tlwg*.conf
rm %{buildroot}%{_datadir}/fontconfig/conf.avail/89-tlwg*-synthetic.conf

# split up 90-ttf-thai-tlwg-synthetic.conf
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-garuda.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-kinnari.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-umpush.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-laksaman.conf

for fconf in %{fontconf}-garuda.conf \
             %{fontconf}-kinnari.conf \
             %{fontconf}-umpush.conf \
	     %{fontconf}-laksaman.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-garuda.metainfo.xml
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-kinnari.metainfo.xml
install -Dm 0644 -p %{SOURCE13} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-loma.metainfo.xml
install -Dm 0644 -p %{SOURCE14} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-norasi.metainfo.xml
install -Dm 0644 -p %{SOURCE15} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-purisa.metainfo.xml
install -Dm 0644 -p %{SOURCE16} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sawasdee.metainfo.xml
install -Dm 0644 -p %{SOURCE17} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-tlwgmono.metainfo.xml
install -Dm 0644 -p %{SOURCE18} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-tlwgtypewriter.metainfo.xml
install -Dm 0644 -p %{SOURCE19} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-tlwgtpist.metainfo.xml
install -Dm 0644 -p %{SOURCE20} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-tlwgtypo.metainfo.xml
install -Dm 0644 -p %{SOURCE21} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-umpush.metainfo.xml
install -Dm 0644 -p %{SOURCE22} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-waree.metainfo.xml
install -Dm 0644 -p %{SOURCE23} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-laksaman.metainfo.xml
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

%files -n fonts-ttf-thai-scalable-common
%doc AUTHORS README COPYING NEWS


%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.5-alt1_1
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1_1
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2_9
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2_6
- update to new release by fcimport

* Sun Nov 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2_5
- update to new release by fcimport

* Wed Nov 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2_3
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2_2
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2_1
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_1
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.17-alt1_2
- update to new release by fcimport

* Tue Nov 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.17-alt1_1
- update to new release by fcimport

* Thu Sep 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.15-alt3_2
- added fonts-ttf-thai Provides:/Obsoletes:

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.15-alt2_2
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.15-alt1_2
- initial release by fcimport

