Group: System/Fonts/True type
%define oldname mgopen-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname 	mgopen
%global fontconf        61-%{fontname}
%global archivename     MgOpen
%global upstream_date   20050515

# Common description
%global common_desc The MgOpen fonts are a font family that includes Latin and Greek glyphs.\
The fonts have been released under a liberal license, similar to the\
license covering the Bitstream Vera fonts.

# Compat description
%global compat_desc \
This package only exists to help transition pre Fedora 11 MgOpen font users to\
the new package split. It will be removed after one distribution release cycle,\
please do not reference it or depend on it in any way.\
\
It can be safely uninstalled.


Name:      fonts-ttf-mgopen
Version:   0.%{upstream_date}
Release:   alt3_29
Summary:   Truetype greek fonts

License:   MgOpen
URL:       http://www.ellak.gr/fonts/mgopen/
Source0:   %{archivename}-%{upstream_date}.tar.gz
# Upstream tarball is not versioned http://www.ellak.gr/fonts/mgopen/files/%{archivename}.tar.gz
Source1:   %{archivename}-%{upstream_date}-doc.tar.gz
# Tarball of the documentation on the site http://www.ellak.gr/fonts/mgopen/
# The LICENCE file is an excerpt from the html page
Source2:   %{fontname}-fontconfig.tar.gz
# Tarball of fontconfig files for each font
Source3:   %{fontname}.metainfo.xml
Source4:   %{fontname}-canonica.metainfo.xml
Source5:   %{fontname}-cosmetica.metainfo.xml
Source6:   %{fontname}-modata.metainfo.xml
Source7:   %{fontname}-moderna.metainfo.xml

BuildArch: noarch
BuildRequires: fontpackages-devel
Source44: import.info
%description
%common_desc


%package -n fonts-ttf-mgopen-common
Group: System/Fonts/True type
Summary:  Truetype greek fonts, common files (documentationa..)
%description -n fonts-ttf-mgopen-common
%common_desc
This package consists of files used by other MgOpen packages.



%package compat
Group: System/Fonts/True type
Summary:   Truetype greek fonts, compatibility package
Obsoletes: mgopen-fonts < 0.20050515-8
Requires:  fonts-ttf-mgopen-canonica, fonts-ttf-mgopen-cosmetica
Requires:  fonts-ttf-mgopen-modata, fonts-ttf-mgopen-moderna
%description compat
%common_desc
%compat_desc



%package -n fonts-ttf-mgopen-canonica
Group: System/Fonts/True type
Summary:   Truetype variable-stroke-width serif font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n fonts-ttf-mgopen-canonica
%common_desc
This package contains the MgOpen Canonica serif variable-stroke-width typeface,
which is based on the design of Times Roman.

%files -n fonts-ttf-mgopen-canonica
%{_fontconfig_templatedir}/%{fontconf}-canonica.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-canonica.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MgOpenCanonica*.ttf
%{_datadir}/appdata/%{fontname}-canonica.metainfo.xml


%package -n fonts-ttf-mgopen-cosmetica
Summary:   Truetype variable-stroke-width sans serif font faces
Group:     System/Fonts/True type
Requires:  %{name}-common = %{version}-%{release}
%description -n fonts-ttf-mgopen-cosmetica
%common_desc
This package contains the MgOpen Cosmetica sans serif variable-stroke-width
typeface, which is  based on the design of Optima.

%files -n fonts-ttf-mgopen-cosmetica
%{_fontconfig_templatedir}/%{fontconf}-cosmetica.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-cosmetica.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MgOpenCosmetica*.ttf
%{_datadir}/appdata/%{fontname}-cosmetica.metainfo.xml


%package -n fonts-ttf-mgopen-modata
Summary:   Truetype fixed-stroke-width sans serif font faces
Group:     System/Fonts/True type
Requires:  %{name}-common = %{version}-%{release}
%description -n fonts-ttf-mgopen-modata
%common_desc
This package contains the MgOpen Modata sans serif fixed-stroke-width
which is based on the design of VAG rounded.

%files -n fonts-ttf-mgopen-modata
%{_fontconfig_templatedir}/%{fontconf}-modata.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-modata.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MgOpenModata*.ttf
%{_datadir}/appdata/%{fontname}-modata.metainfo.xml


%package -n fonts-ttf-mgopen-moderna
Summary:   Truetype fixed-stroke-width sans serif font faces
Group:     System/Fonts/True type
Requires:  %{name}-common = %{version}-%{release}
%description -n fonts-ttf-mgopen-moderna
%common_desc
This package contains the MgOpen Moderna sans serif fixed-stroke-width
typeface which is based on the design of Helvetica.

%files -n fonts-ttf-mgopen-moderna
%{_fontconfig_templatedir}/%{fontconf}-moderna.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-moderna.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MgOpenModerna*.ttf
%{_datadir}/appdata/%{fontname}-moderna.metainfo.xml


%prep
%setup -q -c -a1 -a2 -n %{archivename}-%{version}
iconv -f ISO-8859-1 -t UTF-8 LICENCE > LICENCE.tmp; mv LICENCE.tmp LICENCE

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf  %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p fontconfig/%{fontname}-canonica.conf \
	 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-canonica.conf
install -m 0644 -p fontconfig/%{fontname}-cosmetica.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-cosmetica.conf
install -m 0644 -p fontconfig/%{fontname}-modata.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-modata.conf
install -m 0644 -p fontconfig/%{fontname}-moderna.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-moderna.conf

for fconf in %{fontconf}-canonica.conf \
                %{fontconf}-cosmetica.conf \
                %{fontconf}-modata.conf \
                %{fontconf}-moderna.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-canonica.metainfo.xml
install -Dm 0644 -p %{SOURCE5} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-cosmetica.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-modata.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-moderna.metainfo.xml
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

%files -n fonts-ttf-mgopen-common
%doc LICENCE mgopen.html _files/
%{_datadir}/appdata/%{fontname}.metainfo.xml

%files compat

%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.20050515-alt3_29
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.20050515-alt3_27
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.20050515-alt3_23
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.20050515-alt3_22
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050515-alt3_20
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050515-alt3_19
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050515-alt3_18
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050515-alt2_18
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050515-alt2_17
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050515-alt1_17
- initial release by fcimport

