Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname bpg-fonts
%define fontname bpg
%define fontconf 64-%{fontname}.conf
%define common_ver 20120413

%define common_desc BPG Fonts are a set of GPL licensed Georgian Unicode fonts.

Name:		fonts-ttf-bpg
Summary: 	Georgian Unicode fonts
Version:	%{common_ver}
Release:	alt4_2
# Font exception
# See: http://groups.google.com/group/bpg-fonts/web/gpl-gnu-license
# No version of the GPL is specified.
License:	GPL+ with exceptions
Group:		System/Fonts/True type
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
# Docs
Source100:	README
Source101:	http://www.gnu.org/licenses/gpl-3.0.txt

URL:		http://groups.google.com/group/bpg-fonts
BuildRequires:	fontpackages-devel
BuildArch:	noarch
Source44: import.info

%description
%common_desc

%package common
Summary:	Common files for BPG Georgian fonts (documentation...)
Group:		System/Fonts/True type

%description common
%common_desc

This package consists of files used by other BPG font packages.

%package -n fonts-ttf-bpg-algeti
Summary:	Algeti Family of BPG Georgian Fonts
Version:	2.005
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-algeti
%common_desc

This package contains the Algeti font family.

%files -n fonts-ttf-bpg-algeti
%{_fontconfig_templatedir}/%{fontconf}-algeti.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-algeti.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Algeti*.ttf"

%package -n fonts-ttf-bpg-chveulebrivi
Summary:	Chveulebrivi family of BPG Georgian fonts
Version:	3.002
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-chveulebrivi
%common_desc

This package contains the Chveulebrivi font family.

%files -n fonts-ttf-bpg-chveulebrivi
%{_fontconfig_templatedir}/%{fontconf}-chveulebrivi.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-chveulebrivi.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Chveulebrivi_*.ttf"

%package -n %{fontname}-classic-fonts
Summary:	Classic family of BPG Georgian fonts
Version:	8.500
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-classic-fonts
%common_desc

This package contains the Classic font family.

%files -n bpg-classic-fonts
%{_fontconfig_templatedir}/%{fontconf}-classic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-classic.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Classic_*.otf"

%package -n fonts-ttf-bpg-courier
Summary:	Courier family of BPG Georgian fonts
Version:	4.002
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-courier
%common_desc

This package contains the Courier font family.

%files -n fonts-ttf-bpg-courier
%{_fontconfig_templatedir}/%{fontconf}-courier.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-courier.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Courier_GPL*.ttf"

%package -n fonts-ttf-bpg-courier-s
Summary:	Courier S family of BPG Georgian fonts
Version:	4.000
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-courier-s
%common_desc

This package contains the Courier S font family.

%files -n fonts-ttf-bpg-courier-s
%{_fontconfig_templatedir}/%{fontconf}-courier-s.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-courier-s.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Courier_S*.ttf"

%package -n %{fontname}-dedaena-block-fonts
Summary:	DedaEna Block family of BPG Georgian fonts
Version:	3.005
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-dedaena-block-fonts
%common_desc

This package contains the DedaEna Block font family.

%files -n bpg-dedaena-block-fonts
%{_fontconfig_templatedir}/%{fontconf}-dedaena-block.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-dedaena-block.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_DedEena_Block*.ttf"

%package -n %{fontname}-dejavu-sans-fonts
Summary:	DejaVu Sans with BPG Georgian changes
Version:	2.28
License:	Bitstream Vera
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-dejavu-sans-fonts
%common_desc

This package contains an improved version of DejaVu Sans with BPG Georgian 
changes.

%files -n bpg-dejavu-sans-fonts
%{_fontconfig_templatedir}/%{fontconf}-bpg-dejavu-sans.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-bpg-dejavu-sans.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_DejaVu_Sans_*.ttf"

%package -n fonts-ttf-bpg-elite
Summary:	Elite family of BPG Georgian fonts
Version:	3.000
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-elite
%common_desc

This package contains the Elite font family.

%files -n fonts-ttf-bpg-elite
%{_fontconfig_templatedir}/%{fontconf}-elite.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-elite.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Elite*.ttf"

%package -n fonts-ttf-bpg-excelsior
Summary:	Excelsior family of BPG Georgian fonts
Version:	2.03
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}
License:	Bitstream Vera

%description -n fonts-ttf-bpg-excelsior
%common_desc

This package contains the Excelsior font family.

%files -n fonts-ttf-bpg-excelsior
%{_fontconfig_templatedir}/%{fontconf}-excelsior.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-excelsior.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Excelsior_GPL*.ttf"

%package -n %{fontname}-excelsior-caps-fonts
Summary:	Excelsior Caps family of BPG Georgian fonts
Version:	2.003
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{common_ver}-%{release}
License:	Bitstream Vera

%description -n %{fontname}-excelsior-caps-fonts
%common_desc

This package contains the Excelsior Caps font family.

%files -n bpg-excelsior-caps-fonts
%{_fontconfig_templatedir}/%{fontconf}-excelsior-caps.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-excelsior-caps.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Excelsior_Caps*.ttf"

%package -n %{fontname}-excelsior-condenced-fonts
Summary:	Excelsior Condenced family of BPG Georgian fonts
Version:	2.003
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{common_ver}-%{release}
License:	Bitstream Vera

%description -n %{fontname}-excelsior-condenced-fonts
%common_desc

This package contains the Excelsior Condenced font family.

%files -n bpg-excelsior-condenced-fonts
%{_fontconfig_templatedir}/%{fontconf}-excelsior-condenced.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-excelsior-condenced.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Excelsior_Condenced*.ttf"

%package -n fonts-ttf-bpg-glaho
Summary:	Glaho family of BPG Georgian fonts
Version:	9.000
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-glaho
%common_desc

This package contains the Glaho font family.
%files -n fonts-ttf-bpg-glaho
%{_fontconfig_templatedir}/%{fontconf}-glaho.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-glaho.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Glaho*.ttf"

%package -n %{fontname}-gorda-fonts
Summary:	Gorda family of BPG Georgian fonts
Version:	2.003
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-gorda-fonts
%common_desc

This package contains the Gorda font family.

%files -n bpg-gorda-fonts
%{_fontconfig_templatedir}/%{fontconf}-gorda.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-gorda.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Gorda*.ttf"

%package -n fonts-ttf-bpg-ingiri
Summary:	Ingiri family of BPG Georgian fonts
Version:	4.000
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-ingiri
%common_desc

This package contains the Ingiri font family.

%files -n fonts-ttf-bpg-ingiri
%{_fontconfig_templatedir}/%{fontconf}-ingiri.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-ingiri.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Ingiri*.ttf"

%package -n %{fontname}-irubaqidze-fonts
Summary:	Irubaqidze family of BPG Georgian fonts
Version:	1.000
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-irubaqidze-fonts
%common_desc

This package contains the Irubaqidze font family. In 1628 Georgian printing 
types were produced for the first time, in Rome. The "Georgian-Italian 
Dictionary"  and "Georgian Prayers" were printed in Rome, 1629, by Stephano 
Paolini and Nikiphore Irbach (Irubakhidze-Cholokashvili). In 1643, in Rome, 
"Georgian Grammar" by Francisco-Maria Majio was printed, using Nuskhuri, 
Asomtavruli and Mkhedruli. Majio spent 7 years in Georgia studying Georgian 
language, scripture and grammar. Font "BPG Irubaqidze" is a modernized 
replica of this casted type. 

%files -n bpg-irubaqidze-fonts
%{_fontconfig_templatedir}/%{fontconf}-irubaqidze.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-irubaqidze.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Irubaqidze*.otf"

%package -n %{fontname}-mikhail-stephan-fonts
Summary:	Mikhail Stephan family of BPG Georgian fonts
Version:	2.500
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-mikhail-stephan-fonts
%common_desc

This package contains the Mikhail Stephan font family. This type was first 
produced in 1709, by the printing-house of King Vahtang VI. In 1712, it was
used to print "The Knight in the Panther's Skin" by Shota Rustaveli, then 
"New Testament" and "The Bible" were printed using updated types prepared 
in Tbilisi by Hungarian Master Michael Stefan Hungaro-Valakhian.

%files -n bpg-mikhail-stephan-fonts
%{_fontconfig_templatedir}/%{fontconf}-mikhail-stephan.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-mikhail-stephan.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Mikhail_Stephan*.otf"

%package -n %{fontname}-mrgvlovani-fonts
Summary:	Mrgvlovani family of BPG Georgian fonts
Version:	1.002
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-mrgvlovani-fonts
%common_desc

This package contains the Mrgvlovani font family.

%files -n bpg-mrgvlovani-fonts
%{_fontconfig_templatedir}/%{fontconf}-mrgvlovani.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-mrgvlovani.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Mrgvlovani_GPL*.ttf"

%package -n %{fontname}-mrgvlovani-caps-fonts
Summary:	Mrgvlovani Caps family of BPG Georgian fonts
Version:	1.002
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n	%{fontname}-mrgvlovani-caps-fonts
%common_desc

This package contains the Mrgvlovani Caps font family.

%files -n bpg-mrgvlovani-caps-fonts
%{_fontconfig_templatedir}/%{fontconf}-mrgvlovani-caps.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-mrgvlovani-caps.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Mrgvlovani_Caps_*.ttf"

%package -n %{fontname}-nateli-fonts
Summary:	Nateli family of BPG Georgian fonts
Version:	2.003
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-nateli-fonts
%common_desc

This package contains the Nateli font family.

%files -n bpg-nateli-fonts
%{_fontconfig_templatedir}/%{fontconf}-nateli.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-nateli.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Nateli_GPL*.ttf"

%package -n %{fontname}-nateli-caps-fonts
Summary:	Nateli Caps family of BPG Georgian fonts
Version:	2.003
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-nateli-caps-fonts
%common_desc

This package contains the Nateli Caps font family.

%files -n bpg-nateli-caps-fonts
%{_fontconfig_templatedir}/%{fontconf}-nateli-caps.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-nateli-caps.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Nateli_Caps*.ttf"

%package -n %{fontname}-nateli-condenced-fonts
Summary:	Nateli Condenced family of BPG Georgian fonts
Version:	2.003
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-nateli-condenced-fonts
%common_desc

This package contains the Nateli Condenced font family.

%files -n bpg-nateli-condenced-fonts
%{_fontconfig_templatedir}/%{fontconf}-nateli-condenced.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-nateli-condenced.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Nateli_Condenced*.ttf"

%package -n fonts-ttf-bpg-nino-medium
Summary:	Nino Medium family of BPG Georgian fonts
Version:	4.005
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-nino-medium
%common_desc

This package contains the Nino Medium font family.

%files -n fonts-ttf-bpg-nino-medium
%{_fontconfig_templatedir}/%{fontconf}-nino-medium.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-nino-medium.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Nino_Medium_GPL*.ttf"

%package -n fonts-ttf-bpg-nino-medium-cond
Summary:	Nino Medium Cond family of BPG Georgian fonts
Version:	4.005
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-nino-medium-cond
%common_desc

This package contains the Nino Medium Cond font family.

%files -n fonts-ttf-bpg-nino-medium-cond
%{_fontconfig_templatedir}/%{fontconf}-nino-medium-cond.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-nino-medium-cond.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Nino_Medium_Cond*.ttf"

%package -n fonts-ttf-bpg-sans
Summary:	Sans family of BPG Georgian fonts
Version:	1.005
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-sans
%common_desc

This package contains the Sans font family.

%files -n fonts-ttf-bpg-sans
%{_fontconfig_templatedir}/%{fontconf}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Sans_GPL*.ttf"

%package -n fonts-ttf-bpg-sans-medium
Summary:	Sans Medium family of BPG Georgian fonts
Version:	1.005
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-sans-medium
%common_desc

This package contains the Sans Medium font family.

%files -n fonts-ttf-bpg-sans-medium
%{_fontconfig_templatedir}/%{fontconf}-sans-medium.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-medium.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Sans_Medium*.ttf"

%package -n fonts-ttf-bpg-sans-modern
Summary:	Sans Modern family of BPG Georgian fonts
Version:	2.025
License:	Bitstream Vera
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-sans-modern
%common_desc

This package contains the Sans Modern font family.

%files -n fonts-ttf-bpg-sans-modern
%{_fontconfig_templatedir}/%{fontconf}-sans-modern.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-modern.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Sans_Modern*.ttf"

%package -n fonts-ttf-bpg-sans-regular
Summary:	Sans Regular family of BPG Georgian fonts
Version:	1.005
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-sans-regular
%common_desc

This package contains the Sans Regular font family.

%files -n fonts-ttf-bpg-sans-regular
%{_fontconfig_templatedir}/%{fontconf}-sans-regular.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-regular.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Sans_Regular*.ttf"

%package -n fonts-ttf-bpg-serif
Summary:	Serif family of BPG Georgian fonts
Version:	1.005
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-serif
%common_desc

This package contains the Serif font family.

%files -n fonts-ttf-bpg-serif
%{_fontconfig_templatedir}/%{fontconf}-serif.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-serif.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Serif_GPL*.ttf"

%package -n fonts-ttf-bpg-serif-modern
Summary:	Serif Modern family of BPG Georgian fonts
Version:	2.028
License:	Bitstream Vera
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n fonts-ttf-bpg-serif-modern
%common_desc

This package contains the Serif Modern font family.

%files -n fonts-ttf-bpg-serif-modern
%{_fontconfig_templatedir}/%{fontconf}-serif-modern.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-serif-modern.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Serif_Modern*.ttf"

%package -n %{fontname}-ucnobi-fonts
Summary:	Ucnobi family of BPG Georgian fonts
Version:	3.300
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-ucnobi-fonts
%common_desc

This package contains the Ucnobi font family.

%files -n bpg-ucnobi-fonts
%{_fontconfig_templatedir}/%{fontconf}-ucnobi.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-ucnobi.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Ucnobi*.otf"

%prep
%setup -q -c -n %{oldname}
mkdir -p Docs/
cp %{SOURCE100} %{SOURCE101} Docs/

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

for fontconf in %{fontconf}-algeti.conf %{fontconf}-chveulebrivi.conf %{fontconf}-courier.conf %{fontconf}-courier-s.conf\
		%{fontconf}-elite.conf %{fontconf}-glaho.conf %{fontconf}-ingiri.conf %{fontconf}-nino-medium.conf\
		%{fontconf}-nino-medium-cond.conf %{fontconf}-sans.conf %{fontconf}-sans-medium.conf %{fontconf}-sans-modern.conf\
		%{fontconf}-sans-regular.conf %{fontconf}-serif.conf %{fontconf}-serif-modern.conf %{fontconf}-excelsior.conf\
		%{fontconf}-classic.conf %{fontconf}-excelsior-caps.conf %{fontconf}-excelsior-condenced.conf \
		%{fontconf}-gorda.conf %{fontconf}-irubaqidze.conf %{fontconf}-mikhail-stephan.conf %{fontconf}-mrgvlovani.conf \
		%{fontconf}-mrgvlovani-caps.conf %{fontconf}-nateli.conf %{fontconf}-nateli-caps.conf %{fontconf}-nateli-condenced.conf \
		%{fontconf}-ucnobi.conf %{fontconf}-dedaena-block.conf %{fontconf}-bpg-dejavu-sans.conf
do
	ln -s %{_fontconfig_templatedir}/$fontconf %{buildroot}%{_fontconfig_confdir}/$fontconf
done
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

%files common
%doc Docs/*
%dir %{_fontbasedir}/*/%{_fontstem}

%changelog
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

