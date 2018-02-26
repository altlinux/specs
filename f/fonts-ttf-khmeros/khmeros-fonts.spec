# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname khmeros-fonts
%define version 5.0
%define name khmeros-fonts
%global fontname khmeros
%global archivename All_KhmerOS_%{version}

%global fontconf 65-0-%{fontname}

%global common_desc \
The Khmer OS fonts include Khmer and Latin alphabets, and they have equivalent \
sizes for Khmer and English alphabets, so that when texts mix both it is not \
necessary to have different point sizes for the text in each language. \
\
They were created by Danh Hong of the Cambodian Open Institute.


Name:           fonts-ttf-khmeros
Version:        5.0
Release:        alt3_12
Summary:        Khmer font set created by Danh Hong of the Cambodian Open Institute

Group:          System/Fonts/True type
License:        LGPLv2+
URL:            http://www.khmeros.info/drupal/?q=en/download/fonts
Source0:        http://downloads.sourceforge.net/khmer/%{archivename}.zip
Source1:        65-0-khmeros-battambang.conf
Source2:        65-0-khmeros-bokor.conf
Source3:        65-0-khmeros-handwritten.conf
Source4:        65-0-khmeros-base.conf
Source5:        65-0-khmeros-metal-chrieng.conf
Source6:        65-0-khmeros-muol.conf
Source7:        65-0-khmeros-siemreap.conf
Source8:        License.txt

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
%common_desc


%package common
Summary:        Common files of %{oldname}
Group:          System/Fonts/True type

%description common
%common_desc

This package consists of files used by other %{oldname} packages.


%package -n fonts-ttf-khmeros-base
Summary:        Base KhmerOS font
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}
Obsoletes:      khmeros-fonts-base < 5.0-4

%description -n fonts-ttf-khmeros-base
%common_desc

Base KhmerOS fonts.

%files -n fonts-ttf-khmeros-base
%{_fontconfig_templatedir}/65-0-khmeros-base.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-khmeros-base.conf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS.ttf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_content.ttf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_sys.ttf

%package -n fonts-ttf-khmeros-battambang
Summary:        Battambang font
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}
Obsoletes:      khmeros-fonts-battambang < 5.0-4

%description -n fonts-ttf-khmeros-battambang
%common_desc

Battambang font.

%files -n fonts-ttf-khmeros-battambang
%{_fontconfig_templatedir}/65-0-khmeros-battambang.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-khmeros-battambang.conf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_battambang.ttf

%package -n fonts-ttf-khmeros-bokor
Summary:        Bokor font
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}
Obsoletes:      khmeros-fonts-bokor < 5.0-4

%description -n fonts-ttf-khmeros-bokor
%common_desc

Bokor font.

%files -n fonts-ttf-khmeros-bokor
%{_fontconfig_templatedir}/65-0-khmeros-bokor.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-khmeros-bokor.conf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_bokor.ttf

%package -n fonts-ttf-khmeros-handwritten
Summary:        Freehand and fasthand fonts
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}
Obsoletes:      khmeros-fonts-handwritten < 5.0-4

%description -n fonts-ttf-khmeros-handwritten
%common_desc

Freehand and fasthand - handwritten fonts.

%files -n fonts-ttf-khmeros-handwritten
%{_fontconfig_templatedir}/65-0-khmeros-handwritten.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-khmeros-handwritten.conf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_freehand.ttf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_fasthand.ttf

%package -n fonts-ttf-khmeros-metal-chrieng
Summary:        Metal Chrieng font
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}
Obsoletes:      khmeros-fonts-metalchrieng < 5.0-4

%description -n fonts-ttf-khmeros-metal-chrieng
%common_desc

Metal Chrieng font.

%files -n fonts-ttf-khmeros-metal-chrieng
%{_fontconfig_templatedir}/65-0-khmeros-metal-chrieng.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-khmeros-metal-chrieng.conf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_metalchrieng.ttf

%package -n fonts-ttf-khmeros-muol
Summary:        Muol fonts - normal, light and Pali
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}
Obsoletes:      khmeros-fonts-muol < 5.0-4

%description -n fonts-ttf-khmeros-muol
%common_desc

Muol fonts - normal, light and Pali.

%files -n fonts-ttf-khmeros-muol
%{_fontconfig_templatedir}/65-0-khmeros-muol.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-khmeros-muol.conf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_muol.ttf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_muollight.ttf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_muolpali.ttf

%package -n fonts-ttf-khmeros-siemreap
Summary:        Siemreap font
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}
Obsoletes:      khmeros-fonts-siemreap < 5.0-4

%description -n fonts-ttf-khmeros-siemreap
%common_desc

Siemreap font.

%files -n fonts-ttf-khmeros-siemreap
%{_fontconfig_templatedir}/65-0-khmeros-siemreap.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-khmeros-siemreap.conf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_siemreap.ttf


%prep
%setup -q -n %{archivename}
install -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .
install -p %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} .


%build
#nothing

%install
# get rid of the white space (' ')
mv 'KhmerOS .ttf' KhmerOS.ttf

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

for conffile in *.conf ; do
install -m 0644 -p $conffile %{buildroot}%{_fontconfig_templatedir}/${conffile}
ln -s %{_fontconfig_templatedir}/$conffile \
      %{buildroot}%{_fontconfig_confdir}/$conffile
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
%doc License.txt


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.0-alt3_12
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.0-alt2_12
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 5.0-alt2_11
- rebuild with new rpm-build-fonts

* Sun Aug 07 2011 Igor Vlasenko <viy@altlinux.ru> 5.0-alt1_11
- initial release by fcimport

