%define oldname linux-libertine-fonts
%global fontname            linux-libertine
%global prio_libertine      60
%global prio_biolinum       61
%global fontconf_libertine  %{prio_libertine}-%{fontname}-libertine.conf
%global fontconf_biolinum   %{prio_biolinum}-%{fontname}-biolinum.conf
%global archivename         LinLibertine
%define posttag             2

%define common_desc                                                     \
The Linux Libertine Open Fonts are a TrueType font family for practical \
use in documents.  They were created to provide a free alternative to   \
proprietary standard fonts.

Name:           fonts-ttf-linuxlibertine
Version:        4.7.5
Release:        alt2_2.2
Summary:        Linux Libertine Open Fonts

Group:          System/Fonts/True type
License:        GPLv2+ with exceptions or OFL
URL:            http://linuxlibertine.sf.net
Source0:        http://download.sourceforge.net/sourceforge/linuxlibertine/LinLibertineSRC-%{version}-%{posttag}.tgz
Source1:        %{oldname}-libertine-fontconfig.conf
Source2:        %{oldname}-biolinum-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge
Requires:       %{name}-common = %{version}-%{release}
Source44: import.info

%description
%common_desc

This package contains Serif fonts.

%package -n fonts-ttf-linuxlibertine-biolinum
Summary:        Sans-serif fonts from Linux Libertine Open Fonts
Requires:       %{name}-common = %{version}-%{release}
Group:          System/Fonts/True type

%description -n fonts-ttf-linuxlibertine-biolinum
%common_desc

This package contains Sans fonts.

%package common
Summary:        Common files for Linux Libertine Open Fonts
Group:          System/Fonts/True type

%description common
%common_desc

This package consists of files used by other %{oldname} packages.

%prep
%setup -q -n %{archivename}
sed -i -e 's/\r//' OFL.txt

%build
for i in $(find -name '*.sfd'); do
  (cd scripts;
   ./bailly-2.sh "../$i" ttf
  )
done
mv scripts/*.ttf .

%install
rm -fr %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf_libertine}
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf_biolinum}

for fconf in %{fontconf_libertine} %{fontconf_biolinum}; do
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
%doc Bugs.txt ChangeLog.txt GPL.txt LICENCE.txt OFL.txt Readme-TEX.txt Readme.txt

%files
%{_fontconfig_templatedir}/%{fontconf_libertine}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf_libertine}
%{_fontbasedir}/*/%{_fontstem}/LinLibertine*.ttf

%files -n fonts-ttf-linuxlibertine-biolinum
%{_fontconfig_templatedir}/%{fontconf_biolinum}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf_biolinum}
%{_fontbasedir}/*/%{_fontstem}/LinBiolinum*.ttf

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.7.5-alt2_2.2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.7.5-alt1_2.2
- update to new release by fcimport

* Thu Aug 25 2011 Igor Vlasenko <viy@altlinux.ru> 4.7.5-alt1_1.2
- added provides/obsoletes for short names

* Thu Dec 10 2009 Vitaly Lipatov <lav@altlinux.ru> 4.4.1-alt1
- new version 4.4.1 (with rpmrb script)

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 2.7.9-alt1
- new version (2.7.9)

* Fri Sep 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.6.9-alt1
- new version 2.6.9 (with rpmrb script)

* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 2.5.9-alt2
- rebuild with new rpm-build-fonts 0.3
- add require fontconfig 2.4.2

* Sun May 13 2007 Vitaly Lipatov <lav@altlinux.ru> 2.5.9-alt1
- initial build for ALT Linux Sisyphus
