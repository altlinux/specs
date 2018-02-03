Group: System/Fonts/True type
%define oldname motoya-lcedar-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global	priority	70
%global	fontname	motoya-lcedar
%global	archivedate	20110406
%global	fontconf	%{priority}-%{fontname}.conf
%global	download_root	http://android.git.kernel.org/?p=platform/frameworks/base.git;a=blob_plain;f=data/fonts/

Name:		fonts-ttf-motoya-lcedar
Version:	1.00
Release:	alt3_0.15.%{archivedate}git
Summary:	Japanese Gothic-typeface TrueType fonts by MOTOYA Co,LTD

License:	ASL 2.0
URL:		http://android.git.kernel.org/?p=platform/frameworks/base.git;a=tree;f=data/fonts
Source0:	%{download_root}MTLc3m.ttf
Source1:	%{download_root}NOTICE
Source2:	%{download_root}README.txt
Source10:	%{fontname}-fontconfig.conf
Source11:       %{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Source44: import.info

%description
Motoya font was created in 1950s, it aims beauty and readability.
"MotoyaLCedar W3 mono", Gothic-typeface font was contributed by
MOTOYA Co,LTD. for Android platform.

%prep
%setup -n %{oldname}-%{version} -q -c -T
install -m 0644 -p %{SOURCE1} notice.txt
install -m 0644 -p %{SOURCE2} readme.txt


%build


%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p %{SOURCE0} $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d	$RPM_BUILD_ROOT%{_fontconfig_templatedir}	\
			$RPM_BUILD_ROOT%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE10} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} $RPM_BUILD_ROOT%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
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
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/*.ttf
%doc readme.txt
%doc --no-dereference notice.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_0.15.20110406git
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_0.14.20110406git
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_0.10.20110406git
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_0.9.20110406git
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_0.7.20110406git
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_0.6.20110406git
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_0.5.20110406git
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_0.4.20110406git
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2_0.4.20110406git
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2_0.3.20110406git
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_0.3.20110406git
- initial release by fcimport

