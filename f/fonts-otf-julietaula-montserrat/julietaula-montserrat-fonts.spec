Group: System/Fonts/True type
%define oldname julietaula-montserrat-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname julietaula-montserrat
%global fontconf 61-%{fontname}
%global common_desc \
A typeface inspired by signs around the Montserrat area \
of Buenos Aires, Argentina

Name:		fonts-otf-julietaula-montserrat
Version:	7.210
Release:	alt1_1
# Override versioning to sync with upstream
Epoch:		1
Summary:	Sans-serif typeface inspired from Montserrat area

License:	OFL
URL:		https://github.com/JulietaUla/Montserrat
Source0:	%{url}/releases/download/v%{version}/Montserrat-%{version}.tar.gz
Source1:	%{oldname}-fontconfig.conf
Source2:	%{oldname}-alternates-fontconfig.conf
Source3:	%{fontname}.metainfo.xml
Source4:	%{fontname}-alternates.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib

# Reset the old date based versioning
Obsoletes:	%{oldname} < 1:%{version}-%{release}
Source44: import.info


%description
%common_desc

%package -n fonts-otf-julietaula-montserrat-common
Group: System/Fonts/True type
Summary:  Common files for %{oldname}

%description -n fonts-otf-julietaula-montserrat-common
%common_desc
This package consists of files used by other %{oldname} packages.

%package	-n %{fontname}
Group: System/Fonts/True type
Summary:	Base version of the Montserrat area inspired typeface
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description	-n %{fontname}
%common_desc

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Montserrat-*.otf
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%package 	-n fonts-otf-julietaula-montserrat-alternates
Group: System/Fonts/True type
Summary:	A Montserrat area inspired typeface family alternate version
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description	-n fonts-otf-julietaula-montserrat-alternates
%common_desc

%files -n fonts-otf-julietaula-montserrat-alternates
%{_fontconfig_templatedir}/%{fontconf}-alternates.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-alternates.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MontserratAlternates-*.otf
%{_datadir}/metainfo/%{fontname}-alternates.metainfo.xml

%prep
%setup -n %{oldname}-%{version} -q -c


%build


%install
install -Dpm 0644 Montserrat-%{version}/fonts/otf/*.otf -t %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

# Install Montserrat fonts
install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

# Install MontserratAlternates fonts
install -m 0644 -p %{SOURCE2} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-alternates.conf

for fconf in %{fontconf}.conf \
	     %{fontconf}-alternates.conf ; do
	ln -s %{_fontconfig_templatedir}/$fconf \
		%{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata file, Repeat for every font family
install -Dm 0644 -p %{SOURCE3} \
		%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
		%{buildroot}%{_datadir}/metainfo/%{fontname}-alternates.metainfo.xml
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

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{fontname}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{fontname}-alternates.metainfo.xml

%files -n fonts-otf-julietaula-montserrat-common
%doc --no-dereference Montserrat-%{version}/OFL.txt
%doc Montserrat-%{version}/README.md 

%changelog
* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 1:7.210-alt1_1
- update to new release by fcimport

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 1:7.200-alt1_5
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1:7.200-alt1_3
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1:7.200-alt1_2
- update to new release by fcimport

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:7.200-alt1_1
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:6.002-alt1_3
- new version

