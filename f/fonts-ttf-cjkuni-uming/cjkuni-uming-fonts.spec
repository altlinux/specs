%define oldname cjkuni-uming-fonts
%define version 0.2.20080216.1
%define name cjkuni-uming-fonts
%global fontname cjkuni-uming
%global fontconf 65-0-ttf-arphic-uming.conf
#%global fontconf2 25-ttf-arphic-uming-render.conf
%global fontconf3 90-ttf-arphic-uming-embolden.conf

%define catalogue        %{_sysconfdir}/X11/fontpath.d

%define common_desc \
CJK Unifonts are Unicode TrueType fonts derived from original fonts made \
available by Arphic Technology under "Arphic Public License" and extended by \
the CJK Unifonts project.

%define umingbuilddir %{oldname}-%{version}

Name:           fonts-ttf-cjkuni-uming
Version:        0.2.20080216.1
Release:        alt4_48
Summary:        Chinese Unicode TrueType font in Ming face

Group:          System/Fonts/True type
License:        Arphic
URL:            http://www.freedesktop.org/wiki/Software/CJKUnifonts
Source0:        http://ftp.debian.org/debian/pool/main/t/ttf-arphic-uming/ttf-arphic-uming_%{version}.orig.tar.gz
Source1:        %{oldname}-fontconfig.conf
#Source2:        %{fontconf2}
Source3:        %{fontconf3}

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Obsoletes:      cjkuni-fonts-common < 0.2.20080216.1-42
Source44: import.info

%description
%common_desc

CJK Unifonts in Ming face.

%prep
%setup -q -c -n %{oldname}-%{version}


%build
%{nil}

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttc %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


#install -m 0644 -p %{SOURCE2} \
#        %{buildroot}%{_fontconfig_templatedir}/%{fontconf2}
#ln -s %{_fontconfig_templatedir}/%{fontconf2} \
#      %{buildroot}%{_fontconfig_confdir}/%{fontconf2}

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf3}
ln -s %{_fontconfig_templatedir}/%{fontconf3} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf3}

# catalogue
install -m 0755 -d %{buildroot}%{catalogue}
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
%{_fontconfig_templatedir}/*.conf
%config(noreplace) %{_fontconfig_confdir}/*.conf
%{_fontbasedir}/*/%{_fontstem}/*.ttc

%doc ../%{umingbuilddir}/license
%doc ../%{umingbuilddir}/CONTRIBUTERS
%doc ../%{umingbuilddir}/FONTLOG
%doc ../%{umingbuilddir}/KNOWN_ISSUES
%doc ../%{umingbuilddir}/NEWS
%doc ../%{umingbuilddir}/README

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.20080216.1-alt4_48
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.20080216.1-alt3_48
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.20080216.1-alt3_47
- rebuild with new rpm-build-fonts

* Mon Aug 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.20080216.1-alt2_47
- bugfix release by fcimport

* Sun Aug 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.20080216.1-alt1_47
- initial release by fcimport

