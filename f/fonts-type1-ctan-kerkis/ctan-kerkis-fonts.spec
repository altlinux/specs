# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-texmf
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname ctan-kerkis-fonts
%global foundryname  ctan
%global fontpkg      kerkis
%global fontname     %{foundryname}-%{fontpkg}
%global fontconf     64-%{fontname}
%global ctan_date    20090115
%global texfonts     %{_texmfmain}/fonts
%global texfontpath  %{fontpkg}

# Common description
%global common_desc Kerkis type 1 fonts for LaTeX.  These fonts are particularly useful \
for typesetting Greek. The Greek repertoire includes full support for \
polytonic Greek, Greek numerals, and double forms of several letters \
that occur in variant forms.


Name:           fonts-type1-ctan-kerkis
Version:        2.0
Release:        alt2_25
Summary:        Kerkis Type 1 fonts
Group:          Publishing
License:        LPPL
URL:            http://www.ctan.org/tex-archive/help/Catalogue/entries/kerkis.html
Source0:        kerkis-%{ctan_date}.zip
# upstream source - unversioned zip file
# ftp://tug.ctan.org/pub/tex-archive/fonts/greek/kerkis.zip
Source1:        %{fontname}-fontconfig.tar.gz
# Tarball of fontconfig files for each font
BuildArch:      noarch
BuildRequires:  fontpackages-devel texlive-generic-recommended
Source44: import.info
%description
%{common_desc}


%package common
Summary:  Kerkis Type 1 fonts, common files (documentationa..)
Group:    System/Fonts/True type
%description common
%common_desc
This package consists of files used by other %{fontname} packages.


%global seriffonts %{fontname}-serif-fonts
%package -n fonts-type1-ctan-kerkis-serif
Summary:  Kerkis serif Type1 fonts
Group:    System/Fonts/True type
Requires:  %{name}-common = %{version}-%{release}
%description -n fonts-type1-ctan-kerkis-serif
%{common_desc}
This package contains the Kerkis font family. It is based on the URW Bookman
font and extends it with Greek characters and math support.

%files -n fonts-type1-ctan-kerkis-serif
%{_fontconfig_templatedir}/%{fontconf}-serif.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-serif.conf
%{_fontbasedir}/*/%{_fontstem}/Kerkis.*
%{_fontbasedir}/*/%{_fontstem}/Kerkis-*Bold.*
%{_fontbasedir}/*/%{_fontstem}/Kerkis-*Italic.*
%{_fontbasedir}/*/%{_fontstem}/Kerkis-*SmallCaps*


%global sansfonts %{fontname}-sans-fonts
%package -n fonts-type1-ctan-kerkis-sans
Summary:  KerkisSans Type1 fonts
Group:    System/Fonts/True type
Requires:  %{name}-common = %{version}-%{release}
%description -n fonts-type1-ctan-kerkis-sans
%{common_desc}
This package contains the KerkisSans font family, based on a free version
of the AvantGardURW Bookman font.

%files -n fonts-type1-ctan-kerkis-sans
%{_fontconfig_templatedir}/%{fontconf}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans.conf
%{_fontbasedir}/*/%{_fontstem}/KerkisSans*


%global calligraphicfonts %{fontname}-calligraphic-fonts
%package -n fonts-type1-ctan-kerkis-calligraphic
Summary:  Kerkis Calligraphic Type1 fonts
Group:    System/Fonts/True type
Requires:  %{name}-common = %{version}-%{release}
%description -n fonts-type1-ctan-kerkis-calligraphic
%{common_desc}
This package contains the Kerkis-Calligraphic font family, a calligraphic font 
family of Kerkis, based on URW Bookman.

%files -n fonts-type1-ctan-kerkis-calligraphic
%{_fontconfig_templatedir}/%{fontconf}-calligraphic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-calligraphic.conf
%{_fontbasedir}/*/%{_fontstem}/Kerkis-Calligraphic*
%{_fontbasedir}/*/%{_fontstem}/ktsy.*


%global texfontpkg tex-kerkis
%package -n texmf-fonts-kerkis
Summary:  Kerkis Type1 fonts, TeX support files
Group:    System/Fonts/True type
Requires: fonts-type1-ctan-kerkis-serif = %{version}-%{release} fonts-type1-ctan-kerkis-sans = %{version}-%{release}
Requires: /usr/bin/latex texlive-latex-recommended
Provides: tetex-font-kerkis = %{version}-%{release}
Obsoletes: tetex-font-kerkis < 2.0-17

%description -n texmf-fonts-kerkis
%{common_desc}
TeX support files.


%prep
%setup -q -a1 -n %{fontpkg}


%build


%install

mkdir -p %{buildroot}%{_texmfmain}/tex/latex/%{fontpkg}
mkdir -p %{buildroot}%{texfonts}/{afm,tfm,type1,vf}/%{texfontpath}
mkdir -p %{buildroot}%{texfonts}/{map,enc}/dvips/%{fontpkg}

install -p -m 644 tex/{*.sty,*.fd} %{buildroot}%{_texmfmain}/tex/latex/%{fontpkg}/
install -p -m 644 tfm/*.tfm %{buildroot}%{texfonts}/tfm/%{texfontpath}/
install -p -m 644 vf/*.vf %{buildroot}%{texfonts}/vf/%{texfontpath}/
install -p -m 644 dvips/*.map %{buildroot}%{texfonts}/map/dvips/%{fontpkg}/
install -p -m 644 dvips/*.enc %{buildroot}%{texfonts}/enc/dvips/%{fontpkg}/

#install .pfb and .afm files in %{_fontdir} as per the fedora font guidelines
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p type1/* %{buildroot}%{_fontdir}
install -m 0644 -p afm/* %{buildroot}%{_fontdir}

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

install -m 0644 -p fontconfig/%{fontname}-serif.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif.conf
install -m 0644 -p fontconfig/%{fontname}-sans.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p fontconfig/%{fontname}-calligraphic.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-calligraphic.conf


for fconf in %{fontconf}-serif.conf \
             %{fontconf}-sans.conf \
             %{fontconf}-calligraphic.conf ; do
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
%doc License.txt README.html
%dir %{_fontbasedir}/*/%{_fontstem}


%files -n texmf-fonts-kerkis
%{_texmfmain}/tex/latex/%{fontpkg}
%{texfonts}/afm/%{texfontpath}
%{texfonts}/tfm/%{texfontpath}
%{texfonts}/type1/%{texfontpath}
%{texfonts}/vf/%{texfontpath}
%{texfonts}/map/dvips/%{fontpkg}
%{texfonts}/enc/dvips/%{fontpkg}



%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_25
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_25
- update to new release by fcimport

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_24
- initial release by fcimport

