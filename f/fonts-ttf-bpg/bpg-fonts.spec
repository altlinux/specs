Epoch: 1
Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname bpg-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname bpg
%global fontconf 64-%{fontname}.conf
%global common_ver 20120413

%global common_desc BPG Fonts are a set of GPL licensed Georgian Unicode fonts.

Name:		fonts-ttf-bpg
Summary: 	Georgian Unicode fonts
Version:	%{common_ver}
Release:	alt5_14
# Font exception
# See: http://groups.google.com/group/bpg-fonts/web/gpl-gnu-license
# No version of the GPL is specified.
License:	GPL+ with exceptions
# Source was found here:
# http://bpgfonts.wordpress.com/category/gpl-gnu/
# But the link is annoying:
# http://www.box.com/s/1f344f181567cb897395
Source0:	BPG_GPL_GNU_Fonts_2012.zip
Source1:	%{oldname}-algeti-fontconfig.conf
Source2:	%{oldname}-chveulebrivi-fontconfig.conf
Source3:	%{oldname}-courier-fontconfig.conf
Source4:	%{oldname}-courier-s-fontconfig.conf
Source5:	%{oldname}-elite-fontconfig.conf
Source6:	%{oldname}-glaho-fontconfig.conf
Source7:	%{oldname}-ingiri-fontconfig.conf
Source8:	%{oldname}-nino-medium-fontconfig.conf
Source9:	%{oldname}-nino-medium-cond-fontconfig.conf
Source10:	%{oldname}-sans-fontconfig.conf
Source11:	%{oldname}-sans-medium-fontconfig.conf
Source12:	%{oldname}-sans-modern-fontconfig.conf
Source13:	%{oldname}-sans-regular-fontconfig.conf
Source14:	%{oldname}-serif-fontconfig.conf
Source15:	%{oldname}-serif-modern-fontconfig.conf
# The source for this one is buried in javascript garbage:
# http://cid-2b325d7bf5367fe3.skydrive.live.com/self.aspx/Fonts%20%E1%83%A4%E1%83%9D%E1%83%9C%E1%83%A2%E1%83%94%E1%83%91%E1%83%98/GPL%20|0%20GNU%20Fonts/BPG|_Excelsior|_GPL|0GNU.zip
# Also, I renamed it to remove the &
# Now part of the main fontset zip.
# Source16:	BPG_Excelsior_GPL_and_GNU.zip
Source17:	%{oldname}-excelsior-fontconfig.conf
# New fonts in 2012
Source18:	%{oldname}-classic-fontconfig.conf
Source19:	%{oldname}-excelsior-caps-fontconfig.conf
Source20:	%{oldname}-excelsior-condenced-fontconfig.conf
Source21:	%{oldname}-gorda-fontconfig.conf
Source22:	%{oldname}-irubaqidze-fontconfig.conf
Source23:	%{oldname}-mikhail-stephan-fontconfig.conf
Source24:	%{oldname}-mrgvlovani-fontconfig.conf
Source25:	%{oldname}-mrgvlovani-caps-fontconfig.conf
Source26:	%{oldname}-nateli-fontconfig.conf
Source27:	%{oldname}-nateli-caps-fontconfig.conf
Source28:	%{oldname}-nateli-condenced-fontconfig.conf
Source29:	%{oldname}-ucnobi-fontconfig.conf
Source30:	%{oldname}-dedaena-block-fontconfig.conf
Source31:	%{oldname}-dejavu-sans-fontconfig.conf
# Appdata Metainfo
Source51:       %{fontname}-algeti.metainfo.xml
Source52:       %{fontname}-chveulebrivi.metainfo.xml
Source53:       %{fontname}-classic.metainfo.xml
Source54:       %{fontname}-courier.metainfo.xml
Source55:       %{fontname}-courier-s.metainfo.xml
Source56:       %{fontname}-dedaena-block.metainfo.xml
Source57:       %{fontname}-dejavu-sans.metainfo.xml
Source58:       %{fontname}-elite.metainfo.xml
Source59:       %{fontname}-excelsior.metainfo.xml
Source60:       %{fontname}-excelsior-caps.metainfo.xml
Source61:       %{fontname}-excelsior-condenced.metainfo.xml
Source62:       %{fontname}-glaho.metainfo.xml
Source63:       %{fontname}-gorda.metainfo.xml
Source64:       %{fontname}-ingiri.metainfo.xml
Source65:       %{fontname}-irubaqidze.metainfo.xml
Source66:       %{fontname}-mikhail-stephan.metainfo.xml
Source67:       %{fontname}-mrgvlovani.metainfo.xml
Source68:       %{fontname}-mrgvlovani-caps.metainfo.xml
Source69:       %{fontname}-nateli.metainfo.xml
Source70:       %{fontname}-nateli-caps.metainfo.xml
Source71:       %{fontname}-nateli-condenced.metainfo.xml
Source72:       %{fontname}-nino-medium.metainfo.xml
Source73:       %{fontname}-nino-medium-cond.metainfo.xml
Source74:       %{fontname}-sans.metainfo.xml
Source75:       %{fontname}-sans-medium.metainfo.xml
Source76:       %{fontname}-sans-modern.metainfo.xml
Source77:       %{fontname}-sans-regular.metainfo.xml
Source78:       %{fontname}-serif.metainfo.xml
Source79:       %{fontname}-serif-modern.metainfo.xml
Source80:       %{fontname}-ucnobi.metainfo.xml
# 2017 DejaVu Unicode updates
Source81:       BPG-2017-DejaVuSans.zip
Source82:       BPG-2017-DejaVuSansCondensed.zip
Source83:       BPG-2017-DejaVuSansMono.zip
Source84:       BPG-2017-DejaVuSerif.zip
Source85:       BPG-2017-DejaVuSerifCondensed.zip
Source86:       %{fontname}-dejavu-sans-mono.metainfo.xml
Source87:       %{oldname}-dejavu-sans-mono-fontconfig.conf
Source88:       %{fontname}-dejavu-serif.metainfo.xml
Source89:       %{oldname}-dejavu-serif-fontconfig.conf

# Docs
Source100:	README
Source101:	http://www.gnu.org/licenses/gpl-3.0.txt

URL:		http://groups.google.com/group/bpg-fonts
BuildRequires:	fontpackages-devel
BuildArch:	noarch
Source44: import.info

%description
%common_desc

%package -n fonts-ttf-bpg-common
Group: System/Fonts/True type
Summary:	Common files for BPG Georgian fonts (documentation...)

%description -n fonts-ttf-bpg-common
%common_desc

This package consists of files used by other BPG font packages.

%package -n fonts-ttf-bpg-algeti
Group: System/Fonts/True type
Summary:	Algeti Family of BPG Georgian Fonts
Version:	2.005
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-algeti
%common_desc

This package contains the Algeti font family.

%files -n fonts-ttf-bpg-algeti
%{_fontconfig_templatedir}/%{fontconf}-algeti.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-algeti.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Algeti*.ttf"
%{_datadir}/appdata/%{fontname}-algeti.metainfo.xml

%package -n fonts-ttf-bpg-chveulebrivi
Group: System/Fonts/True type
Summary:	Chveulebrivi family of BPG Georgian fonts
Version:	3.002
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-chveulebrivi
%common_desc

This package contains the Chveulebrivi font family.

%files -n fonts-ttf-bpg-chveulebrivi
%{_fontconfig_templatedir}/%{fontconf}-chveulebrivi.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-chveulebrivi.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Chveulebrivi_*.ttf"
%{_datadir}/appdata/%{fontname}-chveulebrivi.metainfo.xml

%package -n fonts-ttf-bpg-classic
Group: System/Fonts/True type
Summary:	Classic family of BPG Georgian fonts
Version:	8.500
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-classic
%common_desc

This package contains the Classic font family.

%files -n fonts-ttf-bpg-classic
%{_fontconfig_templatedir}/%{fontconf}-classic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-classic.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Classic_*.otf"
%{_datadir}/appdata/%{fontname}-classic.metainfo.xml

%package -n fonts-ttf-bpg-courier
Group: System/Fonts/True type
Summary:	Courier family of BPG Georgian fonts
Version:	4.002
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-courier
%common_desc

This package contains the Courier font family.

%files -n fonts-ttf-bpg-courier
%{_fontconfig_templatedir}/%{fontconf}-courier.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-courier.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Courier_GPL*.ttf"
%{_datadir}/appdata/%{fontname}-courier.metainfo.xml

%package -n fonts-ttf-bpg-courier-s
Group: System/Fonts/True type
Summary:	Courier S family of BPG Georgian fonts
Version:	4.000
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-courier-s
%common_desc

This package contains the Courier S font family.

%files -n fonts-ttf-bpg-courier-s
%{_fontconfig_templatedir}/%{fontconf}-courier-s.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-courier-s.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Courier_S*.ttf"
%{_datadir}/appdata/%{fontname}-courier-s.metainfo.xml

%package -n fonts-ttf-bpg-dedaena-block
Group: System/Fonts/True type
Summary:	DedaEna Block family of BPG Georgian fonts
Version:	3.005
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-dedaena-block
%common_desc

This package contains the DedaEna Block font family.

%files -n fonts-ttf-bpg-dedaena-block
%{_fontconfig_templatedir}/%{fontconf}-dedaena-block.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-dedaena-block.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_DedEena_Block*.ttf"
%{_datadir}/appdata/%{fontname}-dedaena-block.metainfo.xml

%package -n fonts-ttf-bpg-dejavu-sans
Group: System/Fonts/True type
Summary:	DejaVu Sans with BPG Georgian changes
Version:	2017.2.005
License:	Bitstream Vera
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-dejavu-sans
%common_desc

This package contains an improved version of DejaVu Sans with BPG Georgian
changes.

%files -n fonts-ttf-bpg-dejavu-sans
%{_fontconfig_templatedir}/%{fontconf}-bpg-dejavu-sans.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-bpg-dejavu-sans.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_DejaVu_Sans_*.ttf"
%{_fontbasedir}/*/%{_fontstem}/"BPG_DejaVu_SansCondensed_*.ttf"
%{_datadir}/appdata/%{fontname}-dejavu-sans.metainfo.xml

%package -n fonts-ttf-bpg-dejavu-sans-mono
Group: System/Fonts/True type
Summary:	DejaVu Sans Mono with BPG Georgian changes
Version:	2017.3.003
License:	Bitstream Vera
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-dejavu-sans-mono
%common_desc

This package contains an improved version of DejaVu Sans Mono with BPG Georgian
changes.

%files -n fonts-ttf-bpg-dejavu-sans-mono
%{_fontconfig_templatedir}/%{fontconf}-bpg-dejavu-sans-mono.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-bpg-dejavu-sans-mono.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_DejaVu_SansMono*.ttf"
%{_datadir}/appdata/%{fontname}-dejavu-sans-mono.metainfo.xml

%package -n fonts-ttf-bpg-dejavu-serif
Group: System/Fonts/True type
Summary:	DejaVu Serif with BPG Georgian changes
Version:	2017.2.37
License:	Bitstream Vera
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-dejavu-serif
%common_desc

This package contains an improved version of DejaVu Serif with BPG Georgian
changes.

%files -n fonts-ttf-bpg-dejavu-serif
%{_fontconfig_templatedir}/%{fontconf}-bpg-dejavu-serif.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-bpg-dejavu-serif.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_DejaVu_Serif_*.ttf"
%{_fontbasedir}/*/%{_fontstem}/"BPG_DejaVu_SerifCondensed_*.ttf"
%{_datadir}/appdata/%{fontname}-dejavu-serif.metainfo.xml


%package -n fonts-ttf-bpg-elite
Group: System/Fonts/True type
Summary:	Elite family of BPG Georgian fonts
Version:	3.000
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-elite
%common_desc

This package contains the Elite font family.

%files -n fonts-ttf-bpg-elite
%{_fontconfig_templatedir}/%{fontconf}-elite.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-elite.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Elite*.ttf"
%{_datadir}/appdata/%{fontname}-elite.metainfo.xml

%package -n fonts-ttf-bpg-excelsior
Group: System/Fonts/True type
Summary:	Excelsior family of BPG Georgian fonts
Version:	2.03
Requires:	%{name}-common = %{common_ver}-%{release}
License:	Bitstream Vera

%description -n fonts-ttf-bpg-excelsior
%common_desc

This package contains the Excelsior font family.

%files -n fonts-ttf-bpg-excelsior
%{_fontconfig_templatedir}/%{fontconf}-excelsior.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-excelsior.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Excelsior_GPL*.ttf"
%{_datadir}/appdata/%{fontname}-excelsior.metainfo.xml

%package -n fonts-ttf-bpg-excelsior-caps
Group: System/Fonts/True type
Summary:	Excelsior Caps family of BPG Georgian fonts
Version:	2.003
Requires:	%{name}-common = %{common_ver}-%{release}
License:	Bitstream Vera

%description -n fonts-ttf-bpg-excelsior-caps
%common_desc

This package contains the Excelsior Caps font family.

%files -n fonts-ttf-bpg-excelsior-caps
%{_fontconfig_templatedir}/%{fontconf}-excelsior-caps.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-excelsior-caps.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Excelsior_Caps*.ttf"
%{_datadir}/appdata/%{fontname}-excelsior-caps.metainfo.xml

%package -n fonts-ttf-bpg-excelsior-condenced
Group: System/Fonts/True type
Summary:	Excelsior Condenced family of BPG Georgian fonts
Version:	2.003
Requires:	%{name}-common = %{common_ver}-%{release}
License:	Bitstream Vera

%description -n fonts-ttf-bpg-excelsior-condenced
%common_desc

This package contains the Excelsior Condenced font family.

%files -n fonts-ttf-bpg-excelsior-condenced
%{_fontconfig_templatedir}/%{fontconf}-excelsior-condenced.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-excelsior-condenced.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Excelsior_Condenced*.ttf"
%{_datadir}/appdata/%{fontname}-excelsior-condenced.metainfo.xml

%package -n fonts-ttf-bpg-glaho
Group: System/Fonts/True type
Summary:	Glaho family of BPG Georgian fonts
Version:	9.000
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-glaho
%common_desc

This package contains the Glaho font family.
%files -n fonts-ttf-bpg-glaho
%{_fontconfig_templatedir}/%{fontconf}-glaho.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-glaho.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Glaho*.ttf"
%{_datadir}/appdata/%{fontname}-glaho.metainfo.xml

%package -n fonts-ttf-bpg-gorda
Group: System/Fonts/True type
Summary:	Gorda family of BPG Georgian fonts
Version:	2.003
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-gorda
%common_desc

This package contains the Gorda font family.

%files -n fonts-ttf-bpg-gorda
%{_fontconfig_templatedir}/%{fontconf}-gorda.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-gorda.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Gorda*.ttf"
%{_datadir}/appdata/%{fontname}-gorda.metainfo.xml

%package -n fonts-ttf-bpg-ingiri
Group: System/Fonts/True type
Summary:	Ingiri family of BPG Georgian fonts
Version:	4.000
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-ingiri
%common_desc

This package contains the Ingiri font family.

%files -n fonts-ttf-bpg-ingiri
%{_fontconfig_templatedir}/%{fontconf}-ingiri.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-ingiri.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Ingiri*.ttf"
%{_datadir}/appdata/%{fontname}-ingiri.metainfo.xml

%package -n fonts-ttf-bpg-irubaqidze
Group: System/Fonts/True type
Summary:	Irubaqidze family of BPG Georgian fonts
Version:	1.000
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-irubaqidze
%common_desc

This package contains the Irubaqidze font family. In 1628 Georgian printing 
types were produced for the first time, in Rome. The "Georgian-Italian 
Dictionary"  and "Georgian Prayers" were printed in Rome, 1629, by Stephano 
Paolini and Nikiphore Irbach (Irubakhidze-Cholokashvili). In 1643, in Rome, 
"Georgian Grammar" by Francisco-Maria Majio was printed, using Nuskhuri, 
Asomtavruli and Mkhedruli. Majio spent 7 years in Georgia studying Georgian 
language, scripture and grammar. Font "BPG Irubaqidze" is a modernized 
replica of this casted type. 

%files -n fonts-ttf-bpg-irubaqidze
%{_fontconfig_templatedir}/%{fontconf}-irubaqidze.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-irubaqidze.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Irubaqidze*.otf"
%{_datadir}/appdata/%{fontname}-irubaqidze.metainfo.xml

%package -n fonts-ttf-bpg-mikhail-stephan
Group: System/Fonts/True type
Summary:	Mikhail Stephan family of BPG Georgian fonts
Version:	2.500
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-mikhail-stephan
%common_desc

This package contains the Mikhail Stephan font family. This type was first 
produced in 1709, by the printing-house of King Vahtang VI. In 1712, it was
used to print "The Knight in the Panther's Skin" by Shota Rustaveli, then 
"New Testament" and "The Bible" were printed using updated types prepared 
in Tbilisi by Hungarian Master Michael Stefan Hungaro-Valakhian.

%files -n fonts-ttf-bpg-mikhail-stephan
%{_fontconfig_templatedir}/%{fontconf}-mikhail-stephan.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-mikhail-stephan.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Mikhail_Stephan*.otf"
%{_datadir}/appdata/%{fontname}-mikhail-stephan.metainfo.xml

%package -n fonts-ttf-bpg-mrgvlovani
Group: System/Fonts/True type
Summary:	Mrgvlovani family of BPG Georgian fonts
Version:	1.002
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-mrgvlovani
%common_desc

This package contains the Mrgvlovani font family.

%files -n fonts-ttf-bpg-mrgvlovani
%{_fontconfig_templatedir}/%{fontconf}-mrgvlovani.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-mrgvlovani.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Mrgvlovani_GPL*.ttf"
%{_datadir}/appdata/%{fontname}-mrgvlovani.metainfo.xml

%package -n fonts-ttf-bpg-mrgvlovani-caps
Group: System/Fonts/True type
Summary:	Mrgvlovani Caps family of BPG Georgian fonts
Version:	1.002
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-mrgvlovani-caps
%common_desc

This package contains the Mrgvlovani Caps font family.

%files -n fonts-ttf-bpg-mrgvlovani-caps
%{_fontconfig_templatedir}/%{fontconf}-mrgvlovani-caps.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-mrgvlovani-caps.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Mrgvlovani_Caps_*.ttf"
%{_datadir}/appdata/%{fontname}-mrgvlovani-caps.metainfo.xml

%package -n fonts-ttf-bpg-nateli
Group: System/Fonts/True type
Summary:	Nateli family of BPG Georgian fonts
Version:	2.003
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-nateli
%common_desc

This package contains the Nateli font family.

%files -n fonts-ttf-bpg-nateli
%{_fontconfig_templatedir}/%{fontconf}-nateli.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-nateli.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Nateli_GPL*.ttf"
%{_datadir}/appdata/%{fontname}-nateli.metainfo.xml

%package -n fonts-ttf-bpg-nateli-caps
Group: System/Fonts/True type
Summary:	Nateli Caps family of BPG Georgian fonts
Version:	2.003
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-nateli-caps
%common_desc

This package contains the Nateli Caps font family.

%files -n fonts-ttf-bpg-nateli-caps
%{_fontconfig_templatedir}/%{fontconf}-nateli-caps.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-nateli-caps.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Nateli_Caps*.ttf"
%{_datadir}/appdata/%{fontname}-nateli-caps.metainfo.xml

%package -n fonts-ttf-bpg-nateli-condenced
Group: System/Fonts/True type
Summary:	Nateli Condenced family of BPG Georgian fonts
Version:	2.003
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-nateli-condenced
%common_desc

This package contains the Nateli Condenced font family.

%files -n fonts-ttf-bpg-nateli-condenced
%{_fontconfig_templatedir}/%{fontconf}-nateli-condenced.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-nateli-condenced.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Nateli_Condenced*.ttf"
%{_datadir}/appdata/%{fontname}-nateli-condenced.metainfo.xml

%package -n fonts-ttf-bpg-nino-medium
Group: System/Fonts/True type
Summary:	Nino Medium family of BPG Georgian fonts
Version:	4.005
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-nino-medium
%common_desc

This package contains the Nino Medium font family.

%files -n fonts-ttf-bpg-nino-medium
%{_fontconfig_templatedir}/%{fontconf}-nino-medium.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-nino-medium.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Nino_Medium_GPL*.ttf"
%{_datadir}/appdata/%{fontname}-nino-medium.metainfo.xml

%package -n fonts-ttf-bpg-nino-medium-cond
Group: System/Fonts/True type
Summary:	Nino Medium Cond family of BPG Georgian fonts
Version:	4.005
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-nino-medium-cond
%common_desc

This package contains the Nino Medium Cond font family.

%files -n fonts-ttf-bpg-nino-medium-cond
%{_fontconfig_templatedir}/%{fontconf}-nino-medium-cond.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-nino-medium-cond.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Nino_Medium_Cond*.ttf"
%{_datadir}/appdata/%{fontname}-nino-medium-cond.metainfo.xml

%package -n fonts-ttf-bpg-sans
Group: System/Fonts/True type
Summary:	Sans family of BPG Georgian fonts
Version:	1.005
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-sans
%common_desc

This package contains the Sans font family.

%files -n fonts-ttf-bpg-sans
%{_fontconfig_templatedir}/%{fontconf}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Sans_GPL*.ttf"
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml

%package -n fonts-ttf-bpg-sans-medium
Group: System/Fonts/True type
Summary:	Sans Medium family of BPG Georgian fonts
Version:	1.005
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-sans-medium
%common_desc

This package contains the Sans Medium font family.

%files -n fonts-ttf-bpg-sans-medium
%{_fontconfig_templatedir}/%{fontconf}-sans-medium.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-medium.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Sans_Medium*.ttf"
%{_datadir}/appdata/%{fontname}-sans-medium.metainfo.xml

%package -n fonts-ttf-bpg-sans-modern
Group: System/Fonts/True type
Summary:	Sans Modern family of BPG Georgian fonts
Version:	2.025
License:	Bitstream Vera
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-sans-modern
%common_desc

This package contains the Sans Modern font family.

%files -n fonts-ttf-bpg-sans-modern
%{_fontconfig_templatedir}/%{fontconf}-sans-modern.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-modern.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Sans_Modern*.ttf"
%{_datadir}/appdata/%{fontname}-sans-modern.metainfo.xml

%package -n fonts-ttf-bpg-sans-regular
Group: System/Fonts/True type
Summary:	Sans Regular family of BPG Georgian fonts
Version:	1.005
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-sans-regular
%common_desc

This package contains the Sans Regular font family.

%files -n fonts-ttf-bpg-sans-regular
%{_fontconfig_templatedir}/%{fontconf}-sans-regular.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-regular.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Sans_Regular*.ttf"
%{_datadir}/appdata/%{fontname}-sans-regular.metainfo.xml

%package -n fonts-ttf-bpg-serif
Group: System/Fonts/True type
Summary:	Serif family of BPG Georgian fonts
Version:	1.005
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-serif
%common_desc

This package contains the Serif font family.

%files -n fonts-ttf-bpg-serif
%{_fontconfig_templatedir}/%{fontconf}-serif.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-serif.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Serif_GPL*.ttf"
%{_datadir}/appdata/%{fontname}-serif.metainfo.xml

%package -n fonts-ttf-bpg-serif-modern
Group: System/Fonts/True type
Summary:	Serif Modern family of BPG Georgian fonts
Version:	2.028
License:	Bitstream Vera
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-serif-modern
%common_desc

This package contains the Serif Modern font family.

%files -n fonts-ttf-bpg-serif-modern
%{_fontconfig_templatedir}/%{fontconf}-serif-modern.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-serif-modern.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Serif_Modern*.ttf"
%{_datadir}/appdata/%{fontname}-serif-modern.metainfo.xml

%package -n fonts-ttf-bpg-ucnobi
Group: System/Fonts/True type
Summary:	Ucnobi family of BPG Georgian fonts
Version:	3.300
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-ucnobi
%common_desc

This package contains the Ucnobi font family.

%files -n fonts-ttf-bpg-ucnobi
%{_fontconfig_templatedir}/%{fontconf}-ucnobi.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-ucnobi.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/"BPG_Ucnobi*.otf"
%{_datadir}/appdata/%{fontname}-ucnobi.metainfo.xml

%prep
%setup -q -c -n %{oldname} -a 81 -a 82 -a 83 -a 84 -a 85
mkdir -p Docs/
cp -p %{SOURCE100} %{SOURCE101} Docs/

# cleanup dejavu
## this one is out of date
rm -rf BPG_DejaVu_Sans_2011_GPL-GNU.ttf
## nuke the .jpg files
rm -rf BPG*.jpg
## fix naming on the new ones
mv "BPG 2017 DejaVuSans.ttf" "BPG_DejaVu_Sans_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSans-Bold.ttf" "BPG_DejaVu_Sans_Bold_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSans-BoldOblique.ttf" "BPG_DejaVu_Sans_BoldOblique_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSans-Oblique.ttf" "BPG_DejaVu_Sans_Oblique_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVu Sans Caps.ttf" "BPG_DejaVu_Sans_Caps_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSansMono.ttf" "BPG_DejaVu_SansMono_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSansMono-Bold.ttf" "BPG_DejaVu_SansMono_Bold_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSansMono-BoldOblique.ttf" "BPG_DejaVu_SansMono_BoldOblique_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSansMono-Oblique.ttf" "BPG_DejaVu_SansMono_Oblique_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSansCondensed.ttf" "BPG_DejaVu_SansCondensed_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSansCondensed-Bold.ttf" "BPG_DejaVu_SansCondensed_Bold_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSansCondensed-BoldOblique.ttf" "BPG_DejaVu_SansCondensed_BoldOblique2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSansCondensed-Oblique.ttf" "BPG_DejaVu_SansCondensed_Oblique2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSerif.ttf" "BPG_DejaVu_Serif_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSerif-Bold.ttf" "BPG_DejaVu_Serif_Bold_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSerif-BoldItalic.ttf" "BPG_DejaVu_Serif_BoldItalic_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSerif-Italic.ttf" "BPG_DejaVu_Serif_Italic_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSerifCondensed.ttf" "BPG_DejaVu_SerifCondensed_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSerifCondensed-Bold.ttf" "BPG_DejaVu_SerifCondensed_Bold_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSerifCondensed-BoldItalic.ttf" "BPG_DejaVu_SerifCondensed_BoldItalic_2017_GPL-GNU.ttf"
mv "BPG 2017 DejaVuSerifCondensed-Italic.ttf" "BPG_DejaVu_SerifCondensed_Italic_2017_GPL-GNU.ttf"

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0644 -p BPG_Classic_*.otf BPG_Irubaqidze*.otf BPG_Mikhail_Stephan*.otf BPG_Ucnobi*.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-algeti.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-chveulebrivi.conf
install -m 0644 -p %{SOURCE3} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-courier.conf
install -m 0644 -p %{SOURCE4} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-courier-s.conf
install -m 0644 -p %{SOURCE5} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-elite.conf
install -m 0644 -p %{SOURCE6} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-glaho.conf
install -m 0644 -p %{SOURCE7} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-ingiri.conf
install -m 0644 -p %{SOURCE8} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nino-medium.conf
install -m 0644 -p %{SOURCE9} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nino-medium-cond.conf
install -m 0644 -p %{SOURCE10} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE11} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-medium.conf
install -m 0644 -p %{SOURCE12} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-modern.conf
install -m 0644 -p %{SOURCE13} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-regular.conf
install -m 0644 -p %{SOURCE14} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif.conf
install -m 0644 -p %{SOURCE15} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif-modern.conf
install -m 0644 -p %{SOURCE17} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-excelsior.conf
install -m 0644 -p %{SOURCE18} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-classic.conf
install -m 0644 -p %{SOURCE19} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-excelsior-caps.conf
install -m 0644 -p %{SOURCE20} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-excelsior-condenced.conf
install -m 0644 -p %{SOURCE21} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gorda.conf
install -m 0644 -p %{SOURCE22} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-irubaqidze.conf
install -m 0644 -p %{SOURCE23} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mikhail-stephan.conf
install -m 0644 -p %{SOURCE24} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mrgvlovani.conf
install	-m 0644	-p %{SOURCE25} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mrgvlovani-caps.conf
install -m 0644 -p %{SOURCE26} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nateli.conf
install -m 0644 -p %{SOURCE27} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nateli-caps.conf
install -m 0644 -p %{SOURCE28} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nateli-condenced.conf
install -m 0644 -p %{SOURCE29} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-ucnobi.conf
install	-m 0644 -p %{SOURCE30} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-dedaena-block.conf
install -m 0644 -p %{SOURCE31} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-bpg-dejavu-sans.conf
install -m 0644 -p %{SOURCE87} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-bpg-dejavu-sans-mono.conf
install -m 0644 -p %{SOURCE89} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-bpg-dejavu-serif.conf

for fontconf in %{fontconf}-algeti.conf %{fontconf}-chveulebrivi.conf %{fontconf}-courier.conf %{fontconf}-courier-s.conf\
		%{fontconf}-elite.conf %{fontconf}-glaho.conf %{fontconf}-ingiri.conf %{fontconf}-nino-medium.conf\
		%{fontconf}-nino-medium-cond.conf %{fontconf}-sans.conf %{fontconf}-sans-medium.conf %{fontconf}-sans-modern.conf\
		%{fontconf}-sans-regular.conf %{fontconf}-serif.conf %{fontconf}-serif-modern.conf %{fontconf}-excelsior.conf\
		%{fontconf}-classic.conf %{fontconf}-excelsior-caps.conf %{fontconf}-excelsior-condenced.conf \
		%{fontconf}-gorda.conf %{fontconf}-irubaqidze.conf %{fontconf}-mikhail-stephan.conf %{fontconf}-mrgvlovani.conf \
		%{fontconf}-mrgvlovani-caps.conf %{fontconf}-nateli.conf %{fontconf}-nateli-caps.conf %{fontconf}-nateli-condenced.conf \
		%{fontconf}-ucnobi.conf %{fontconf}-dedaena-block.conf %{fontconf}-bpg-dejavu-sans.conf %{fontconf}-bpg-dejavu-sans-mono.conf %{fontconf}-bpg-dejavu-serif.conf
do
	ln -s %{_fontconfig_templatedir}/$fontconf %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE51} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-algeti.metainfo.xml
install -Dm 0644 -p %{SOURCE52} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-chveulebrivi.metainfo.xml
install -Dm 0644 -p %{SOURCE53} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-classic.metainfo.xml
install -Dm 0644 -p %{SOURCE54} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-courier.metainfo.xml
install -Dm 0644 -p %{SOURCE55} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-courier-s.metainfo.xml
install -Dm 0644 -p %{SOURCE56} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-dedaena-block.metainfo.xml
install -Dm 0644 -p %{SOURCE57} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-dejavu-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE58} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-elite.metainfo.xml
install -Dm 0644 -p %{SOURCE59} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-excelsior.metainfo.xml
install -Dm 0644 -p %{SOURCE60} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-excelsior-caps.metainfo.xml
install -Dm 0644 -p %{SOURCE61} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-excelsior-condenced.metainfo.xml
install -Dm 0644 -p %{SOURCE62} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-glaho.metainfo.xml
install -Dm 0644 -p %{SOURCE63} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-gorda.metainfo.xml
install -Dm 0644 -p %{SOURCE64} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-ingiri.metainfo.xml
install -Dm 0644 -p %{SOURCE65} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-irubaqidze.metainfo.xml
install -Dm 0644 -p %{SOURCE66} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-mikhail-stephan.metainfo.xml
install -Dm 0644 -p %{SOURCE67} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-mrgvlovani.metainfo.xml
install -Dm 0644 -p %{SOURCE68} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-mrgvlovani-caps.metainfo.xml
install -Dm 0644 -p %{SOURCE69} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-nateli.metainfo.xml
install -Dm 0644 -p %{SOURCE70} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-nateli-caps.metainfo.xml
install -Dm 0644 -p %{SOURCE71} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-nateli-condenced.metainfo.xml
install -Dm 0644 -p %{SOURCE72} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-nino-medium.metainfo.xml
install -Dm 0644 -p %{SOURCE73} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-nino-medium-cond.metainfo.xml
install -Dm 0644 -p %{SOURCE74} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE75} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans-medium.metainfo.xml
install -Dm 0644 -p %{SOURCE76} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans-modern.metainfo.xml
install -Dm 0644 -p %{SOURCE77} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans-regular.metainfo.xml
install -Dm 0644 -p %{SOURCE78} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-serif.metainfo.xml
install -Dm 0644 -p %{SOURCE79} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-serif-modern.metainfo.xml
install -Dm 0644 -p %{SOURCE80} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-ucnobi.metainfo.xml
install -Dm 0644 -p %{SOURCE86} \
	%{buildroot}%{_datadir}/appdata/%{fontname}-dejavu-sans-mono.metainfo.xml
install -Dm 0644 -p %{SOURCE88} \
	%{buildroot}%{_datadir}/appdata/%{fontname}-dejavu-serif.metainfo.xml
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

%files -n fonts-ttf-bpg-common
%doc Docs/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1:20120413-alt5_14
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1:20120413-alt5_9
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1:20120413-alt5_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1:20120413-alt5_6
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1:20120413-alt5_5
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:20120413-alt5_4
- bugfix: fixed subpackage name

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1:20120413-alt4_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1:20120413-alt4_3
- update to new release by fcimport

* Tue Feb 05 2013 Igor Vlasenko <viy@altlinux.ru> 1:20120413-alt4_2
- update to new release by fcimport

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 1:20120413-alt4_1
- new version

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20090205-alt3_10
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20090205-alt3_9
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 20090205-alt2_9
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20090205-alt2_8
- rebuild with new rpm-build-fonts

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 20090205-alt1_8
- initial release by fcimport

