# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-texmf
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname ctan-cm-lgc-fonts
%define foundryname  ctan
%define fontpkg      cm-lgc
%define fontname     %{foundryname}-%{fontpkg}
%define fontconf     64-%{fontname}
%define ctan_date    20051007
%define texfonts     %{_texmfmain}/fonts
%define texfontpath  public/%{fontpkg}


# Common description
%define common_desc The CM-LGC PostScript Type 1 fonts are converted from the METAFONT \
sources of the Computer Modern font families. CM-LGC supports the T1, T2A, \
LGR, and TS1 encodings, i.e. Latin, Cyrillic, and Greek.


Name:           fonts-type1-ctan-cm-lgc
Version:        0.5
Release:        alt2_19
Summary:        CM-LGC Type1 fonts
Group:          Publishing
# Font exception
License:        GPLv2+ with exceptions
URL:            http://www.ctan.org/tex-archive/fonts/ps-type1/cm-lgc
Source0:        cm-lgc-%{ctan_date}.zip
# upstream source - unversioned zip file
# ftp://tug.ctan.org/pub/tex-archive/fonts/ps-type1/cm-lgc.zip
Source1:        %{fontname}-fontconfig.tar.gz
# Tarball of fontconfig files for each font
BuildRequires:  fontpackages-devel texlive-generic-recommended
BuildArch:      noarch
Source44: import.info
%description
%{common_desc} 


%package common
Summary:  CM-LGC Type 1 fonts, common files (documentationa..)
Group:    System/Fonts/True type
%description common
%common_desc
This package consists of files used by other ctan-cm-lgc-fonts packages.


%define romanfonts %{fontname}-roman-fonts
%package -n fonts-type1-ctan-cm-lgc-roman
Summary:   CM-LGC Type 1 fonts, serif font faces
Group:     System/Fonts/True type
Requires:  %{name}-common = %{version}-%{release}
%description -n fonts-type1-ctan-cm-lgc-roman
%common_desc
This package contains the CM-LGC serif typeface based on Computer Modern.

%files -n fonts-type1-ctan-cm-lgc-roman
%{_fontconfig_templatedir}/%{fontconf}-roman.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-roman.conf
%{_fontbasedir}/*/%{_fontstem}/fcm*


%define sansfonts %{fontname}-sans-fonts
%package -n fonts-type1-ctan-cm-lgc-sans
Summary:   CM-LGC Type 1 fonts, sans-serif font faces
Group:     System/Fonts/True type
Requires:  %{name}-common = %{version}-%{release}
%description -n fonts-type1-ctan-cm-lgc-sans
%common_desc
This package contains the CM-LGC sans-serif typeface based on Computer Modern.

%files -n fonts-type1-ctan-cm-lgc-sans
%{_fontconfig_templatedir}/%{fontconf}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans.conf
%{_fontbasedir}/*/%{_fontstem}/fcs*


%define typewriterfonts %{fontname}-typewriter-fonts
%package -n fonts-type1-ctan-cm-lgc-typewriter
Summary:   CM-LGC Type 1 fonts, typewriter font faces
Group:     System/Fonts/True type
Requires:  %{name}-common = %{version}-%{release}
%description -n fonts-type1-ctan-cm-lgc-typewriter
%common_desc
This package contains the CM-LGC serif typeface based on Computer Modern.

%files -n fonts-type1-ctan-cm-lgc-typewriter
%{_fontconfig_templatedir}/%{fontconf}-typewriter.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-typewriter.conf
%{_fontbasedir}/*/%{_fontstem}/fct*


%define texfontpkg tex-cm-lgc
%package -n texmf-fonts-cm-lgc
Summary:  CM-LGC Type1 fonts, TeX support files
Group:    System/Fonts/True type
Requires: fonts-type1-ctan-cm-lgc-roman = %{version}-%{release} fonts-type1-ctan-cm-lgc-sans = %{version}-%{release} fonts-type1-ctan-cm-lgc-typewriter = %{version}-%{release}
Requires: /usr/bin/latex texlive-latex-recommended
Provides: tetex-font-cm-lgc = %{version}-%{release}
Obsoletes: tetex-font-cm-lgc < 0.5-12
%description -n texmf-fonts-cm-lgc
%{common_desc}
TeX support files.


%prep
%setup -q -a1 -n %{fontpkg}


%build


%install

mkdir -p %{buildroot}%{_texmfmain}/tex/latex/%{fontpkg}
mkdir -p %{buildroot}%{texfonts}/{afm,ofm,ovf,type1,tfm,vf}/%{texfontpath}
mkdir -p %{buildroot}%{texfonts}/{enc,map}/dvips/%{fontpkg}

install -m 644 -p tex/latex/%{fontpkg}/* %{buildroot}%{_texmfmain}/tex/latex/%{fontpkg}/
install -m 644 -p fonts/ofm/%{texfontpath}/* %{buildroot}%{texfonts}/ofm/%{texfontpath}/
install -m 644 -p fonts/ovf/%{texfontpath}/* %{buildroot}%{texfonts}/ovf/%{texfontpath}/
install -m 644 -p fonts/tfm/%{texfontpath}/* %{buildroot}%{texfonts}/tfm/%{texfontpath}/
install -m 644 -p fonts/vf/%{texfontpath}/* %{buildroot}%{texfonts}/vf/%{texfontpath}/
install -m 644 -p dvips/base/* %{buildroot}%{texfonts}/enc/dvips/%{fontpkg}/
install -m 644 -p dvips/config/* %{buildroot}%{texfonts}/map/dvips/%{fontpkg}/

#install .pfb and .afm files in %{_fontdir} as per the fedora font guidelines
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/type1/%{texfontpath}/* %{buildroot}%{_fontdir}
install -m 0644 -p fonts/afm/%{texfontpath}/* %{buildroot}%{_fontdir}

pushd %{buildroot}%{_fontdir}
for pfb_file in *.pfb ;  do
    ln -s %{_fontdir}/$pfb_file %{buildroot}%{texfonts}/type1/%{texfontpath}/$pfb_file
done
for afm_file in *.afm ;  do
    ln -s %{_fontdir}/$afm_file %{buildroot}%{texfonts}/afm/%{texfontpath}/$afm_file
done
popd


# fontconfig stuff (see spectemplate-fonts-multi.spec)
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p fontconfig/%{fontname}-roman.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-roman.conf
install -m 0644 -p fontconfig/%{fontname}-sans.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p fontconfig/%{fontname}-typewriter.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-typewriter.conf

for fconf in %{fontconf}-roman.conf \
             %{fontconf}-sans.conf \
             %{fontconf}-typewriter.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done
# relink after moving
pushd %{buildroot}%{_fontdir}
for pfb_file in *.pfb ;  do
    ln -sf /usr/share/fonts/type1/%{fontname}/$pfb_file %{buildroot}%{texfonts}/type1/%{texfontpath}/$pfb_file
done
for afm_file in *.afm ;  do
    ln -sf /usr/share/fonts/type1/%{fontname}/$afm_file %{buildroot}%{texfonts}/afm/%{texfontpath}/$afm_file
done
popd
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
%doc COPYING HISTORY README
%dir %{_fontbasedir}/*/%{_fontstem}


%files -n texmf-fonts-cm-lgc
%{_texmfmain}/tex/latex/%{fontpkg}
%{texfonts}/afm/%{texfontpath}
%{texfonts}/ofm/%{texfontpath}
%{texfonts}/ovf/%{texfontpath}
%{texfonts}/tfm/%{texfontpath}
%{texfonts}/type1/%{texfontpath}
%{texfonts}/vf/%{texfontpath}
%{texfonts}/enc/dvips/%{fontpkg}
%{texfonts}/map/dvips/%{fontpkg}



%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_19
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_19
- update to new release by fcimport

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_18
- initial release by fcimport

