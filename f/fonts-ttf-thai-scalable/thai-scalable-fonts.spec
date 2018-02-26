# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/afm2tfm /usr/bin/fc-cache /usr/bin/fontforge /usr/bin/mkfontdir /usr/bin/mkfontscale /usr/bin/mktexlsr /usr/bin/ttmkfdir /usr/bin/vptovf
# END SourceDeps(oneline)
%define oldname thai-scalable-fonts
%define fontname thai-scalable
%define fontconf 90-%{fontname}-synthetic

%define archivename fonts-tlwg

%define common_desc \
%{archivename} provides a collection of free scalable Thai fonts.

Name:      fonts-ttf-thai-scalable
Version:   0.5.0
Release:   alt2_1
Summary:   Thai TrueType fonts
Group:     System/Fonts/True type
License:   GPLv2+
URL:       http://linux.thai.net/projects/thaifonts-scalable
Source0:   http://linux.thai.net/pub/ThaiLinux/software/%{archivename}/%{archivename}-%{version}.tar.gz
Source1:   %{fontconf}-garuda.conf
Source2:   %{fontconf}-kinnari.conf
Source3:   %{fontconf}-umpush.conf
BuildArch: noarch
BuildRequires: fontforge >= 20071110 ttmkfdir xorg-font-utils
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


%package common
Summary:   Common files of %{oldname}
Group:     System/Fonts/True type

%description common
%common_desc

This package consists of files used by other %{oldname} packages.


# added for F11 can be obsoleted for F13
%package compat
Summary:   thaifonts-scalable compatibility package
Group:     System/Fonts/True type
Obsoletes: thaifonts-scalable < 0.4.11-1
Requires: fonts-ttf-thai-scalable-garuda
Requires: fonts-ttf-thai-scalable-kinnari
Requires: fonts-ttf-thai-scalable-loma
Requires: fonts-ttf-thai-scalable-norasi
Requires: fonts-ttf-thai-scalable-purisa
Requires: fonts-ttf-thai-scalable-sawasdee
Requires: fonts-ttf-thai-scalable-tlwgmono
Requires: fonts-ttf-thai-scalable-tlwgtypewriter
Requires: fonts-ttf-thai-scalable-tlwgtypist
Requires: fonts-ttf-thai-scalable-tlwgtypo
Requires: fonts-ttf-thai-scalable-umpush
Requires: fonts-ttf-thai-scalable-waree

%description compat
This package only exists to help transition thaifonts-scalable users to the new
split renamed package. It will be removed after one distribution release cycle,
please do not reference it or depend on it in any way.

It can be safely uninstalled.


%package -n fonts-ttf-thai-scalable-garuda
Summary:        Thai Garuda fonts
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-garuda
%common_desc

This package provides the Garuda family of Thai fonts.

%files -n fonts-ttf-thai-scalable-garuda
%{_fontconfig_templatedir}/%{fontconf}-garuda.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-garuda.conf
%{_fontbasedir}/*/%{_fontstem}/Garuda*.ttf


%package -n fonts-ttf-thai-scalable-kinnari
Summary:        Thai Kinnari fonts
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-kinnari
%common_desc

This package provides the Kinnari family of Thai fonts.

%files -n fonts-ttf-thai-scalable-kinnari
%{_fontconfig_templatedir}/%{fontconf}-kinnari.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-kinnari.conf
%{_fontbasedir}/*/%{_fontstem}/Kinnari*.ttf


%package -n fonts-ttf-thai-scalable-loma
Summary:        Thai Loma fonts
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-loma
%common_desc

This package provides the Loma family of Thai fonts.

%files -n fonts-ttf-thai-scalable-loma
%{_fontbasedir}/*/%{_fontstem}/Loma*.ttf


%package -n fonts-ttf-thai-scalable-norasi
Summary:        Thai Norasi fonts
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-norasi
%common_desc

This package provides the Norasi family of Thai fonts.

%files -n fonts-ttf-thai-scalable-norasi
%{_fontbasedir}/*/%{_fontstem}/Norasi*.ttf


%package -n fonts-ttf-thai-scalable-purisa
Summary:        Thai Purisa fonts
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-purisa
%common_desc

This package provides the Purisa family of Thai fonts.

%files -n fonts-ttf-thai-scalable-purisa
%{_fontbasedir}/*/%{_fontstem}/Purisa*.ttf


%package -n fonts-ttf-thai-scalable-sawasdee
Summary:        Thai Sawasdee fonts
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-sawasdee
%common_desc

This package provides the Sawasdee family of Thai fonts.

%files -n fonts-ttf-thai-scalable-sawasdee
%{_fontbasedir}/*/%{_fontstem}/Sawasdee*.ttf


%package -n fonts-ttf-thai-scalable-tlwgmono
Summary:        Thai TlwgMono fonts
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-tlwgmono
%common_desc

This package provides the TlwgMono family of Thai fonts.

%files -n fonts-ttf-thai-scalable-tlwgmono
%{_fontbasedir}/*/%{_fontstem}/TlwgMono*.ttf


%package -n fonts-ttf-thai-scalable-tlwgtypewriter
Summary:        Thai TlwgTypewriter fonts
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-tlwgtypewriter
%common_desc

This package provides the TlwgTypewriter family of Thai fonts.

%files -n fonts-ttf-thai-scalable-tlwgtypewriter
%{_fontbasedir}/*/%{_fontstem}/TlwgTypewriter*.ttf


%package -n fonts-ttf-thai-scalable-tlwgtypist
Summary:        Thai TlwgTypist fonts
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-tlwgtypist
%common_desc

This package provides the TlwgTypist family of Thai fonts.

%files -n fonts-ttf-thai-scalable-tlwgtypist
%{_fontbasedir}/*/%{_fontstem}/TlwgTypist*.ttf


%package -n fonts-ttf-thai-scalable-tlwgtypo
Summary:        Thai TlwgTypo fonts
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-tlwgtypo
%common_desc

This package provides the TlwgTypo family of Thai fonts.

%files -n fonts-ttf-thai-scalable-tlwgtypo
%{_fontbasedir}/*/%{_fontstem}/TlwgTypo*.ttf


%package -n fonts-ttf-thai-scalable-umpush
Summary:        Thai Umpush fonts
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-umpush
%common_desc

This package provides the Umpush family of Thai fonts.

%files -n fonts-ttf-thai-scalable-umpush
%{_fontconfig_templatedir}/%{fontconf}-umpush.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-umpush.conf
%{_fontbasedir}/*/%{_fontstem}/Umpush*.ttf


%package -n fonts-ttf-thai-scalable-waree
Summary:        Thai Waree fonts
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-scalable-waree
%common_desc

This package provides the Waree family of Thai fonts.

%files -n fonts-ttf-thai-scalable-waree
%{_fontbasedir}/*/%{_fontstem}/Waree*.ttf


%prep
%setup -q -n %{archivename}-%{version}


%build
%configure --with-ttfdir=%{_fontdir} --enable-ttf --enable-xfontsdir


%install
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

make install DESTDIR=%{buildroot} INSTALL="install -p"

# remove upstream font config
# fontconfig's 65-nonlatin.conf covers 65-ttf-thai-tlwg.conf
rm %{buildroot}%{_sysconfdir}/fonts/conf.avail/*-ttf-thai-tlwg*.conf

# split up 90-ttf-thai-tlwg-synthetic.conf
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-garuda.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-kinnari.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-umpush.conf

for fconf in %{fontconf}-garuda.conf \
             %{fontconf}-kinnari.conf \
             %{fontconf}-umpush.conf ; do
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


%files common
%doc AUTHORS README COPYING NEWS

%files compat
%{_fontbasedir}/*/%{_fontstem}/fonts.dir
%{_fontbasedir}/*/%{_fontstem}/fonts.scale


%changelog
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

