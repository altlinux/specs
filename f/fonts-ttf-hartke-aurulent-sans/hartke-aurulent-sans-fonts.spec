%define oldname hartke-aurulent-sans-fonts
%define fontname hartke-aurulent-sans
%define fontconf 63-%{fontname}-fonts-fontconfig.conf
%define fontconfmono 64-%{fontname}-fonts-fontconfig.conf
%define archivename AurulentSans-20070504

%define common_desc \
Aurulent Sans is a sans-serif font developed for use as the primary interface\
font on X Windows on GNU/Linux. It includes the latin alphabet, digits, and\
punctuation, as well as some accents. It is created by Stephen G. Hartke.

Name:           fonts-ttf-hartke-aurulent-sans
Version:        20070504
Release:        alt3_5
Summary:        A sans-serif font for use as primary interface font

Group:          System/Fonts/True type
License:        OFL
URL:            http://www.geocities.com/hartke01/
Source0:        %{url}%{archivename}.tgz
Source1:        %{fontname}-fonts-fontconfig.conf
Source2:        %{fontname}-mono-fonts-fontconfig.conf
Source3:        %{archivename}.pdf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       %{name}-common = %{version}-%{release}
Source44: import.info

%description
%common_desc
This package includes the Aurulent Sans font family.

%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/AurulentSans-*.otf

%package common
Summary:        Common files of the Aurulent font family
Group:          System/Fonts/True type

%description common
%common_desc

This package consists of files used by other
%{oldname} packages.

%package -n fonts-ttf-hartke-aurulent-sans-mono
Summary:        Aurulent Sans Mono font family
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-hartke-aurulent-sans-mono
%common_desc
This package includes the Aurulent Sans Mono font family.

%files -n fonts-ttf-hartke-aurulent-sans-mono
%{_fontconfig_templatedir}/%{fontconfmono}
%config(noreplace) %{_fontconfig_confdir}/%{fontconfmono}
%{_fontbasedir}/*/%{_fontstem}/AurulentSansMono-*.otf


%prep
%setup -q -c
install -m 0644 -p %{SOURCE3} .


%build
#Nothing to do yet. Asked upstream for sources on Feb 01 2009.

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconfmono}

for fconf in %{fontconf}\
             %{fontconfmono}; do
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
%doc README *.pdf

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070504-alt3_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070504-alt2_5
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20070504-alt2_4
- rebuild with new rpm-build-fonts

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 20070504-alt1_4
- initial release by fcimport

