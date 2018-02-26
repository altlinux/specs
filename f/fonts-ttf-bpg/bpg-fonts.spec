# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname bpg-fonts
%define fontname bpg
%define fontconf 64-%{fontname}.conf
%define common_ver 20090205

%define common_desc BPG Fonts are a set of GPL licensed Georgian Unicode fonts.


Name:		fonts-ttf-bpg
Summary: 	Georgian Unicode fonts
Version:	%{common_ver}
Release:	alt3_9
# Font exception
# See: http://groups.google.com/group/bpg-fonts/web/gpl-gnu-license
# No version of the GPL is specified.
License:	GPL+ with exceptions
Group:		System/Fonts/True type
# Source is actually http://bpg-fonts.googlegroups.com/web/BPG_GPL%26GNU_Fonts.zip
# but it is buried in Google Groups. Barf.
# Also, it has a & in its name, which confuses all sorts of things. 
# I renamed the zip file to replace & with _and_
Source0:	BPG_GPL_and_GNU_Fonts.zip
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
Source16:	BPG_Excelsior_GPL_and_GNU.zip
Source17:	%{oldname}-excelsior-fontconfig.conf
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
Version:	2.025
Group:		System/Fonts/True type
Requires:	%{name}-common = %{common_ver}-%{release}
License:	Bitstream Vera

%description -n fonts-ttf-bpg-excelsior
%common_desc

This package contains the Excelsior font family.

%files -n fonts-ttf-bpg-excelsior
%{_fontconfig_templatedir}/%{fontconf}-excelsior.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-excelsior.conf
%{_fontbasedir}/*/%{_fontstem}/"BPG_Excelsior*.ttf"

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

%prep
%setup -q -c -n %{oldname}
%{__unzip} -qqo "%{SOURCE0}"
%{__unzip} -qqo "%{SOURCE16}"
# correct end-of-line encoding
sed -i 's/\r//' "Docs/BPG_GPL&GNU_Fonts.txt"

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
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

for fontconf in %{fontconf}-algeti.conf %{fontconf}-chveulebrivi.conf %{fontconf}-courier.conf %{fontconf}-courier-s.conf\
		%{fontconf}-elite.conf %{fontconf}-glaho.conf %{fontconf}-ingiri.conf %{fontconf}-nino-medium.conf\
		%{fontconf}-nino-medium-cond.conf %{fontconf}-sans.conf %{fontconf}-sans-medium.conf %{fontconf}-sans-modern.conf\
		%{fontconf}-sans-regular.conf %{fontconf}-serif.conf %{fontconf}-serif-modern.conf %{fontconf}-excelsior.conf
do
	ln -s %{_fontconfig_templatedir}/$fontconf %{buildroot}%{_fontconfig_confdir}/$fontconf
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
%doc Docs/*
%dir %{_fontbasedir}/*/%{_fontstem}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20090205-alt3_9
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 20090205-alt2_9
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20090205-alt2_8
- rebuild with new rpm-build-fonts

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 20090205-alt1_8
- initial release by fcimport

