Group: System/Fonts/True type
%define oldname paktype-naskh-basic-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global priority 65-0
%global fontname paktype-naskh-basic
%global fontconf %{priority}-%{fontname}

Name:		fonts-ttf-paktype-naskh-basic
Version:	6.0
Release:	alt1_3
Summary:	Fonts for Arabic, Farsi, Urdu and Sindhi from PakType
License:	GPLv2 with exceptions
URL:		https://sourceforge.net/projects/paktype/
Source0:	https://sourceforge.net/p/paktype/code/HEAD/tree/Fonts/Release/PakType-Naskh-Basic-%{version}.tar.gz?format=raw#/%{oldname}-%{version}.tar.gz
Source1:	%{oldname}.conf
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Source44: import.info

%description
The paktype-naskh-basic-fonts package contains fonts for the display of \
Arabic, Farsi, Urdu and Sindhi from PakType by Lateef Sagar.

%prep
%setup -n %{oldname}-%{version} -q -c
rm -rf Code

# get rid of the white space (' ')
mv PakType\ Naskh\ Basic\ License.txt PakType_Naskh_Basic_License.txt
mv PakType\ Naskh\ Basic\ Features.pdf PakTypeNaskhBasicFeatures.pdf

sed -i 's/\r//' PakType_Naskh_Basic_License.txt
chmod a-x PakType_Naskh_Basic_License.txt PakTypeNaskhBasicFeatures.pdf


%build
echo "Nothing to do in Build."

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p PakTypeNaskhBasic.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf
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
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%dir %{_fontsdir}/*/%{_fontstem}/
%{_fontsdir}/*/%{_fontstem}/PakTypeNaskhBasic.ttf

%doc PakType_Naskh_Basic_License.txt PakTypeNaskhBasicFeatures.pdf

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 6.0-alt1_3
- update to new release by fcimport

* Mon Mar 30 2020 Igor Vlasenko <viy@altlinux.ru> 5.0-alt1_2
- update

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_8
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_4
- update to new release by fcimport

* Wed Feb 06 2013 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_2
- update to new release by fcimport

* Sun Nov 25 2012 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_1
- update to new release by fcimport

* Mon Sep 10 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 3.0-alt3_11
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.0-alt3_10
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 3.0-alt2_10
- update to new release by fcimport

* Thu Aug 25 2011 Igor Vlasenko <viy@altlinux.ru> 3.0-alt2_9
- rebuild woth new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_9
- initial release by fcimport

