# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/runtest gcc-c++ libICE-devel libSM-devel libX11-devel unzip
# END SourceDeps(oneline)
%define oldname paktype-tehreer-fonts
%global fontname paktype-tehreer
%global fontconf 67-paktype

Name:	fonts-ttf-paktype-tehreer
Version:     4.0
Release:     alt1_2
Summary:     Fonts for Arabic from PakType
Group:		System/Fonts/True type
License:     GPLv2 with exceptions
URL:		https://sourceforge.net/projects/paktype/
Source0:     http://downloads.sourceforge.net/paktype/Individual-Release/PakType-Tehreer-%{version}.tar.gz
Source1:	%{fontconf}-tehreer.conf
BuildArch:   noarch
BuildRequires:	fontpackages-devel
Obsoletes: paktype-fonts-common < %{version}i-%{release}
Source44: import.info

%description 
The paktype-tehreer-fonts package contains fonts for the display of \
Arabic from the PakType by Lateef Sagar.

%prep
%setup -q -c
rm -rf Code
# get rid of the white space (' ')
mv PakType\ Tehreer.ttf PakType_Tehreer.ttf
mv PakType\ Tehreer\ License.txt PakType_Tehreer_License.txt
mv PakType\ Tehreer\ Features.pdf PakType_Tehreer_Features.pdf

%{__sed} -i 's/\r//' PakType_Tehreer_License.txt
chmod a-x PakType_Tehreer.ttf PakType_Tehreer_License.txt PakType_Tehreer_Features.pdf


%build
echo "Nothing to do in Build."

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p PakType_Tehreer.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-tehreer.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}-tehreer.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}-tehreer.conf
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

%files
%{_fontconfig_templatedir}/%{fontconf}-tehreer.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-tehreer.conf
%{_fontbasedir}/*/%{_fontstem}/PakType_Tehreer.ttf

%doc PakType_Tehreer_License.txt PakType_Tehreer_Features.pdf

%changelog
* Sun Nov 25 2012 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_2
- update to new release by fcimport

* Wed Nov 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_1
- update to new release by fcimport

* Mon Sep 10 2012 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_13
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_12
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_12
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_11
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_11
- initial release by fcimport

