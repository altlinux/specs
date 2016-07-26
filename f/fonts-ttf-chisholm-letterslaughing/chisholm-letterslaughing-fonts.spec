Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname chisholm-letterslaughing-fonts
%global	fontname	chisholm-letterslaughing
%global	fontconf	65-%{fontname}.conf
%global archivename	lleqcdd.zip

Name:		fonts-ttf-chisholm-letterslaughing
Version:	20030323
Release:	alt3_11
Summary:	Letters Laughing is a decorative/LED sans-serif font

License:	OFL	
URL:		http://glyphobet.net/fonts/free/?font=lleqcdd
Source0:	%{archivename}
Source1:	%{oldname}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Source44: import.info

%description
Letters Laughing is a decorative/LED sans-serif font

%prep
%setup -q -n letters

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
	%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}


# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
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
%{_fontbasedir}/*/%{_fontstem}/*.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20030323-alt3_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20030323-alt3_10
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20030323-alt3_9
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20030323-alt3_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20030323-alt3_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20030323-alt3_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20030323-alt3_5
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20030323-alt3_4
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20030323-alt2_4
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20030323-alt2_3
- rebuild with new rpm-build-fonts

* Thu Aug 04 2011 Igor Vlasenko <viy@altlinux.ru> 20030323-alt1_3
- initial release by fcimport

