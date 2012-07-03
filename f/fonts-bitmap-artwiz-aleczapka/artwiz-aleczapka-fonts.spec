%define oldname artwiz-aleczapka-fonts
%global fontname artwiz-aleczapka
%global fontconf 60-%{fontname}

%define common_desc \
Artwiz is a family of very small futuristic fonts, with varying styles of \
typefaces designed at a single pixel size. The minimal nature of the \
fonts makes them popular with users of lightweight window managers. These \
fonts have been updated by Alec Zapka to be compatible with modern \
software and support an extended character set. \

Name:		fonts-bitmap-artwiz-aleczapka
Version:	1.3
Release:	alt2_12
Summary:	Very small futuristic font family
Group:		System/Fonts/True type
License:	GPLv2
URL:		http://artwizaleczapka.sourceforge.net/
Source0:	http://dl.sf.net/artwizaleczapka/artwiz-aleczapka-en-sources-1.3.tar.bz2
Source1:	http://dl.sf.net/artwizaleczapka/artwiz-aleczapka-de-sources-1.3.tar.bz2
Source2:	http://dl.sf.net/artwizaleczapka/artwiz-aleczapka-se-sources-1.3.tar.bz2
Source3:	artwiz-aleczapka-fonts-anorexia-fontconfig.conf
Source4:	artwiz-aleczapka-fonts-aqui-fontconfig.conf
Source5:	artwiz-aleczapka-fonts-cure-fontconfig.conf
Source6:	artwiz-aleczapka-fonts-drift-fontconfig.conf
Source7:	artwiz-aleczapka-fonts-edges-fontconfig.conf
Source8:	artwiz-aleczapka-fonts-fkp-fontconfig.conf
Source9:	artwiz-aleczapka-fonts-gelly-fontconfig.conf
Source10:	artwiz-aleczapka-fonts-glisp-fontconfig.conf
Source11:	artwiz-aleczapka-fonts-kates-fontconfig.conf
Source12:	artwiz-aleczapka-fonts-lime-fontconfig.conf
Source13:	artwiz-aleczapka-fonts-mints-mild-fontconfig.conf
Source14:	artwiz-aleczapka-fonts-mints-strong-fontconfig.conf
Source15:	artwiz-aleczapka-fonts-nu-fontconfig.conf
Source16:	artwiz-aleczapka-fonts-smoothansi-fontconfig.conf
Source17:	artwiz-aleczapka-fonts-snap-fontconfig.conf
Patch0:		artwiz-aleczapka-fkp-cleanups.patch
Patch1:		artwiz-aleczapka-fonts-1.3-fix-makepcf.patch
BuildArch:	noarch
BuildRequires:	xorg-font-utils fontpackages-devel
Requires:	fonts-bitmap-artwiz-aleczapka-anorexia = %{version}-%{release}
Requires:	fonts-bitmap-artwiz-aleczapka-aqui = %{version}-%{release}
Requires:	fonts-bitmap-artwiz-aleczapka-cure = %{version}-%{release}
Requires:	fonts-bitmap-artwiz-aleczapka-drift = %{version}-%{release}
Requires:	fonts-bitmap-artwiz-aleczapka-edges = %{version}-%{release}
Requires:	fonts-bitmap-artwiz-aleczapka-fkp = %{version}-%{release}
Requires:	fonts-bitmap-artwiz-aleczapka-gelly = %{version}-%{release}
Requires:	fonts-bitmap-artwiz-aleczapka-glisp = %{version}-%{release}
Requires:	fonts-bitmap-artwiz-aleczapka-kates = %{version}-%{release}
Requires:	fonts-bitmap-artwiz-aleczapka-lime = %{version}-%{release}
Requires:	fonts-bitmap-artwiz-aleczapka-mints-mild = %{version}-%{release}
Requires:	fonts-bitmap-artwiz-aleczapka-mints-strong = %{version}-%{release}
Requires:	fonts-bitmap-artwiz-aleczapka-nu = %{version}-%{release}
Requires:	fonts-bitmap-artwiz-aleczapka-smoothansi = %{version}-%{release}
Requires:	fonts-bitmap-artwiz-aleczapka-snap = %{version}-%{release}
Source44: import.info

%description
%common_desc
This is a metapackage, which pulls in all the separated fonts in this family.

%package common
Summary:	Common files for Artwiz Aleczapka fonts (documentation...)
Group:		System/Fonts/True type

%description common
%common_desc

%package -n fonts-bitmap-artwiz-aleczapka-anorexia
Summary:	Anorexia font in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-anorexia
%common_desc
This package contains the Anorexia font in three encodings, English, German, 
and Swedish.

%files -n fonts-bitmap-artwiz-aleczapka-anorexia
%{_fontconfig_templatedir}/%{fontconf}-anorexia.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-anorexia.conf
%{_fontbasedir}/*/%{_fontstem}/anorexia*.pcf

%package -n fonts-bitmap-artwiz-aleczapka-aqui
Summary:	Aqui font in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-aqui
%common_desc
This package contains the Aqui font in three encodings, English, German, and
Swedish.

%files -n fonts-bitmap-artwiz-aleczapka-aqui
%{_fontconfig_templatedir}/%{fontconf}-aqui.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-aqui.conf
%{_fontbasedir}/*/%{_fontstem}/aqui*.pcf

%package -n fonts-bitmap-artwiz-aleczapka-cure
Summary:	Cure font in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-cure
%common_desc
This package contains the Cure font in three encodings, English, German, and 
Swedish.

%files -n fonts-bitmap-artwiz-aleczapka-cure
%{_fontconfig_templatedir}/%{fontconf}-cure.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-cure.conf
%{_fontbasedir}/*/%{_fontstem}/cure*.pcf

%package -n fonts-bitmap-artwiz-aleczapka-drift
Summary:	Drift font in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-drift
%common_desc
This package contains the Drift font in three encodings, English, German,
and Swedish.

%files -n fonts-bitmap-artwiz-aleczapka-drift
%{_fontconfig_templatedir}/%{fontconf}-drift.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-drift.conf
%{_fontbasedir}/*/%{_fontstem}/drift*.pcf

%package -n fonts-bitmap-artwiz-aleczapka-edges
Summary:	Edges font in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-edges
%common_desc
This package contains the Edges font in three encodings, English, German,
and Swedish.

%files -n fonts-bitmap-artwiz-aleczapka-edges
%{_fontconfig_templatedir}/%{fontconf}-edges.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-edges.conf
%{_fontbasedir}/*/%{_fontstem}/edges*.pcf

%package -n fonts-bitmap-artwiz-aleczapka-fkp
Summary:	Fkp font in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-fkp
%common_desc
This package contains the fkp font in three encodings, English, German,
and Swedish.

%files -n fonts-bitmap-artwiz-aleczapka-fkp
%{_fontconfig_templatedir}/%{fontconf}-fkp.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-fkp.conf
%{_fontbasedir}/*/%{_fontstem}/fkp*.pcf

%package -n fonts-bitmap-artwiz-aleczapka-gelly
Summary:	Gelly font in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-gelly
%common_desc
This package contains the Gelly font in three encodings, English, German,
and Swedish.

%files -n fonts-bitmap-artwiz-aleczapka-gelly
%{_fontconfig_templatedir}/%{fontconf}-gelly.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-gelly.conf
%{_fontbasedir}/*/%{_fontstem}/gelly*.pcf

%package -n fonts-bitmap-artwiz-aleczapka-glisp
Summary:	Glisp fonts in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-glisp
%common_desc
This package contains the Glisp font in three encodings, English, German,
and Swedish. It also includes a Regular and Bold version of the font for 
each encoding.

%files -n fonts-bitmap-artwiz-aleczapka-glisp
%{_fontconfig_templatedir}/%{fontconf}-glisp.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-glisp.conf
%{_fontbasedir}/*/%{_fontstem}/glisp*.pcf

%package -n fonts-bitmap-artwiz-aleczapka-kates
Summary:	Kates font in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-kates
%common_desc
This package contains the Kates font in three encodings, English, German,
and Swedish. 

%files -n fonts-bitmap-artwiz-aleczapka-kates
%{_fontconfig_templatedir}/%{fontconf}-kates.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-kates.conf
%{_fontbasedir}/*/%{_fontstem}/kates*.pcf

%package -n fonts-bitmap-artwiz-aleczapka-lime
Summary:	Lime font in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-lime
%common_desc
This package contains the Lime font in three encodings, English, German,
and Swedish.

%files -n fonts-bitmap-artwiz-aleczapka-lime
%{_fontconfig_templatedir}/%{fontconf}-lime.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-lime.conf
%{_fontbasedir}/*/%{_fontstem}/lime*.pcf

%package -n fonts-bitmap-artwiz-aleczapka-mints-mild
Summary:	Mints Mild font in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-mints-mild
%common_desc
This package contains the Mints Mild font in three encodings, English, German,
and Swedish.

%files -n fonts-bitmap-artwiz-aleczapka-mints-mild
%{_fontconfig_templatedir}/%{fontconf}-mints-mild.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-mints-mild.conf
%{_fontbasedir}/*/%{_fontstem}/mints-mild*.pcf

%package -n fonts-bitmap-artwiz-aleczapka-mints-strong
Summary:	Mints Strong font in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-mints-strong
%common_desc
This package contains the Mints Strong font in three encodings, English, 
German, and Swedish.

%files -n fonts-bitmap-artwiz-aleczapka-mints-strong
%{_fontconfig_templatedir}/%{fontconf}-mints-strong.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-mints-strong.conf
%{_fontbasedir}/*/%{_fontstem}/mints-strong*.pcf

%package -n fonts-bitmap-artwiz-aleczapka-nu
Summary:	Nu font in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-nu
%common_desc
This package contains the Nu font in three encodings, English, German,
and Swedish.

%files -n fonts-bitmap-artwiz-aleczapka-nu
%{_fontconfig_templatedir}/%{fontconf}-nu.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-nu.conf
%{_fontbasedir}/*/%{_fontstem}/nu*.pcf

%package -n fonts-bitmap-artwiz-aleczapka-smoothansi
Summary:	Smoothansi font in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-smoothansi
%common_desc
This package contains the Smoothansi font in three encodings, English, 
German, and Swedish.

%files -n fonts-bitmap-artwiz-aleczapka-smoothansi
%{_fontconfig_templatedir}/%{fontconf}-smoothansi.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-smoothansi.conf
%{_fontbasedir}/*/%{_fontstem}/smoothansi*.pcf

%package -n fonts-bitmap-artwiz-aleczapka-snap
Summary:	Snap font in Artwiz family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-bitmap-artwiz-aleczapka-snap
%common_desc
This package contains the Snap font in three encodings, English, German,
and Swedish.

%files -n fonts-bitmap-artwiz-aleczapka-snap
%{_fontconfig_templatedir}/%{fontconf}-snap.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-snap.conf
%{_fontbasedir}/*/%{_fontstem}/snap*.pcf

%prep
%setup -q -c %{oldname}-%{version} -a1 -a2
%patch0 -p0
%patch1 -p1 -b .fix-makepcf

%build
for lang in de en se; do
    pushd %{_builddir}/%{name}-%{version}/artwiz-aleczapka-$lang-sources-%{version}
    sh makepcf.sh
    popd
done


%install
install -m 0755 -d %{buildroot}%{_fontdir}
for lang in de en se; do
    install -p -m 0644 artwiz-aleczapka-$lang-sources-%{version}/*.pcf %{buildroot}%{_fontdir}
done
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE3} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-anorexia.conf
install -m 0644 -p %{SOURCE4} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-aqui.conf
install -m 0644 -p %{SOURCE5} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-cure.conf
install -m 0644 -p %{SOURCE6} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-drift.conf
install -m 0644 -p %{SOURCE7} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-edges.conf
install -m 0644 -p %{SOURCE8} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-fkp.conf
install -m 0644 -p %{SOURCE9} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gelly.conf
install -m 0644 -p %{SOURCE10} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-glisp.conf
install -m 0644 -p %{SOURCE11} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-kates.conf
install -m 0644 -p %{SOURCE12} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-lime.conf
install -m 0644 -p %{SOURCE13} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mints-mild.conf
install -m 0644 -p %{SOURCE14} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mints-strong.conf
install -m 0644 -p %{SOURCE15} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nu.conf
install -m 0644 -p %{SOURCE16} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-smoothansi.conf
install -m 0644 -p %{SOURCE17} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-snap.conf

for fontconf in %{fontconf}-anorexia.conf %{fontconf}-aqui.conf %{fontconf}-cure.conf %{fontconf}-drift.conf %{fontconf}-edges.conf %{fontconf}-fkp.conf %{fontconf}-gelly.conf\
		%{fontconf}-glisp.conf %{fontconf}-kates.conf %{fontconf}-lime.conf %{fontconf}-mints-mild.conf %{fontconf}-mints-strong.conf %{fontconf}-nu.conf \
		%{fontconf}-smoothansi.conf %{fontconf}-snap.conf
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

%files
# This is a dummy metapackage.

%files common
# generic docs are the same for every lang (AUTHORS has all info in german dir
# so use it from german font dir)
%doc artwiz-aleczapka-de-sources-1.3/{AUTHORS,COPYING,README,VERSION}
%doc artwiz-aleczapka-de-sources-1.3/README.DE
%doc artwiz-aleczapka-se-sources-1.3/README.SE
%dir %{_fontbasedir}/*/%{_fontstem}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_12
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_12
- new fc release

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_11
- initial release by fcimport

