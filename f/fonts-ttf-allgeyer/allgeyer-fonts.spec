Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname allgeyer-fonts
%global fontname allgeyer

%global common_desc \
Robert Allgeyer's MusiQwik and MusiSync are a set of original True Type fonts \
that depict musical notation. Each music font may be used within a word \
processing document without the need for special music publishing software, or\
embedded in PDF files.

Name:		fonts-ttf-allgeyer
Summary: 	Musical Notation True Type Fonts
Version:	5.002
Release:	alt3_13
License:	OFL
# The source was originally downloaded from:
# http://www.icogitate.com/~ergosum/fonts/musiqwik_musisync_y6.zip
# But the website is gone now.
Source0:	musiqwik_musisync_y6.zip
Source1:       %{fontname}.metainfo.xml
Source2:       %{fontname}-musisync.metainfo.xml
Source3:       %{fontname}-musiqwik.metainfo.xml

# This website is gone. :(
URL:		http://www.icogitate.com/~ergosum/fonts/musicfonts.htm
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	%{name}-common = %{version}-%{release}
Source44: import.info

%description
%common_desc

%package -n fonts-ttf-allgeyer-common
Group: System/Fonts/True type
Summary:	Common files for MusiSync and MusiQwik fonts (documentation...)

%description -n fonts-ttf-allgeyer-common
%common_desc

This package consists of files used by other Allgeyer font packages.

%package -n fonts-ttf-allgeyer-musisync
Group: System/Fonts/True type
Summary:	A musical notation font family that provides general musical decorations
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-allgeyer-musisync
%common_desc

This font family provides a collection of general musical decorations.

%files -n fonts-ttf-allgeyer-musisync
%{_fontbasedir}/*/%{_fontstem}/MusiSync*.ttf
%{_datadir}/appdata/%{fontname}-musisync.metainfo.xml

%package -n fonts-ttf-allgeyer-musiqwik
Group: System/Fonts/True type
Summary:	A musical notation font family intended for writing lines of actual music
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-allgeyer-musiqwik
%common_desc

This font family is intended for writing lines of actual music.

%files -n fonts-ttf-allgeyer-musiqwik
%{_fontbasedir}/*/%{_fontstem}/MusiQwik*.ttf
%{_datadir}/appdata/%{fontname}-musiqwik.metainfo.xml

%prep
%setup -q -c -n %{oldname}

# correct end-of-line encoding
for i in OFL-FAQ.txt FONTLOG.txt SOURCE.txt README_MusiQwik_MusiSync.txt LICENSE_OFL.txt; do
	sed -i 's/\r//' $i
done

# Convert to UTF-8
iconv -f iso-8859-1 -t utf-8 -o README_MusiQwik_MusiSync.txt{.utf8,}
mv README_MusiQwik_MusiSync.txt{.utf8,}

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-musisync.metainfo.xml
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-musiqwik.metainfo.xml
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

%files -n fonts-ttf-allgeyer-common
%doc FONTLOG.txt LICENSE_OFL.txt MusiQwik_character_map.htm musiqwik_demo.png 
%doc MusiSync_character_map.htm musisync_demo.png MusiSync-README.htm OFL-FAQ.txt 
%doc README_MusiQwik_MusiSync.txt SOURCE.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 5.002-alt3_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 5.002-alt3_12
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 5.002-alt3_11
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 5.002-alt3_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 5.002-alt3_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 5.002-alt3_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 5.002-alt3_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.002-alt3_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.002-alt2_6
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 5.002-alt2_5
- rebuild with new rpm-build-fonts

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 5.002-alt1_5
- initial release by fcimport

