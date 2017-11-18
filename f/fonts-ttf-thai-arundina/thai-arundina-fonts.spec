# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/afm2tfm /usr/bin/mktexlsr /usr/bin/vptovf
# END SourceDeps(oneline)
%define oldname thai-arundina-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 0.2.2
%global fontname thai-arundina
%global fontconf 67-%{fontname}
%global archivename fonts-sipa-arundina-%{version}

%global common_desc \
Arundina fonts were created aiming at Bitstream Vera / Dejavu \
compatibility, under SIPA's initiation.  They were then further \
modified by TLWG for certain aspects, such as Latin glyph size \
compatibility and OpenType conformance.

Name:		fonts-ttf-thai-arundina
Version:	0.2.2
Release:	alt1_1
Summary:	Thai Arundina fonts

Group:		System/Fonts/True type
License:	Bitstream Vera
URL:		http://linux.thai.net/projects/fonts-sipa-arundina
Source0:	http://linux.thai.net/pub/thailinux/software/fonts-sipa-arundina/%{archivename}.tar.xz
Source1:	%{oldname}-sans-fontconfig.conf
Source2:	%{oldname}-serif-fontconfig.conf
Source3:	%{oldname}-sans-mono-fontconfig.conf
Source4:	%{fontname}.metainfo.xml
Source5:	%{fontname}-sans.metainfo.xml
Source6:	%{fontname}-sans-mono.metainfo.xml
Source7:	%{fontname}-serif.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontforge libfontforge
BuildRequires:	fontpackages-devel
Source44: import.info

%description
%common_desc


%package -n fonts-ttf-thai-arundina-common
Group: System/Fonts/True type
Summary:	Common files of the Thai Arundina font set

%description -n fonts-ttf-thai-arundina-common
%common_desc


%package -n fonts-ttf-thai-arundina-sans
Group: System/Fonts/True type
Summary:	Variable-width sans-serif Thai Arundina fonts
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-arundina-sans
%common_desc

This package consists of the Thai Arundina sans-serif variable-width
font faces.

%files -n fonts-ttf-thai-arundina-sans
%{_fontconfig_templatedir}/%{fontconf}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans.conf
%{_fontbasedir}/*/%{_fontstem}/ArundinaSans.ttf
%{_fontbasedir}/*/%{_fontstem}/ArundinaSans-Bold.ttf
%{_fontbasedir}/*/%{_fontstem}/ArundinaSans-Oblique.ttf
%{_fontbasedir}/*/%{_fontstem}/ArundinaSans-BoldOblique.ttf
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml


%package -n fonts-ttf-thai-arundina-serif
Group: System/Fonts/True type
Summary:	Variable-width serif Thai Arundina fonts
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-arundina-serif
%common_desc

This package consists of the Thai Arundina serif variable-width
font faces.

%files -n fonts-ttf-thai-arundina-serif
%{_fontconfig_templatedir}/%{fontconf}-serif.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-serif.conf
%{_fontbasedir}/*/%{_fontstem}/ArundinaSerif.ttf
%{_fontbasedir}/*/%{_fontstem}/ArundinaSerif-Bold.ttf
%{_datadir}/appdata/%{fontname}-serif.metainfo.xml


%package -n fonts-ttf-thai-arundina-sans-mono
Group: System/Fonts/True type
Summary:	Monospace sans-serif Thai Arundina fonts
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-thai-arundina-sans-mono
%common_desc

This package consists of the Thai Arundina sans-serif monospace font
faces.

%files -n fonts-ttf-thai-arundina-sans-mono
%{_fontconfig_templatedir}/%{fontconf}-sans-mono.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-mono.conf
%{_fontbasedir}/*/%{_fontstem}/ArundinaSansMono.ttf
%{_fontbasedir}/*/%{_fontstem}/ArundinaSansMono-Bold.ttf
%{_fontbasedir}/*/%{_fontstem}/ArundinaSansMono-Oblique.ttf
%{_fontbasedir}/*/%{_fontstem}/ArundinaSansMono-BoldOblique.ttf
%{_datadir}/appdata/%{fontname}-sans-mono.metainfo.xml


%prep
%setup -q -n %{archivename}


%build
%configure
make


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p arundina/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif.conf
install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-mono.conf

for fconf in %{fontconf}-sans.conf \
    %{fontconf}-serif.conf \
    %{fontconf}-sans-mono.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
     %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE4} \
	%{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE5} \
	%{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
	%{buildroot}%{_datadir}/appdata/%{fontname}-sans-mono.metainfo.xml
install -Dm 0644 -p %{SOURCE7} \
	%{buildroot}%{_datadir}/appdata/%{fontname}-serif.metainfo.xml
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

%files -n fonts-ttf-thai-arundina-common
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc README AUTHORS COPYING NEWS


%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_1
- new version

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_3
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_6
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_2
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_1
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_1
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_2
- update to new release by fcimport

* Tue Nov 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_1
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt3_2
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt2_2
- bugfix release by fcimport

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_2
- initial release by fcimport

