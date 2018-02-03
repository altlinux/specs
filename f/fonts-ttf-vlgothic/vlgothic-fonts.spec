Group: System/Fonts/True type
%define oldname vlgothic-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 20141206
%global	priority	67
%global	ppriority	66
%global	fontname	vlgothic
%global	archivename	VLGothic-%{version}
%global	fontconf	%{priority}-%{fontname}-gothic
%global	pfontconf	%{ppriority}-%{fontname}-pgothic
%global	common_desc	\
VLGothic provides Japanese TrueType fonts from the Vine Linux project.\
Most of the glyphs are taken from the M+ and Sazanami Gothic fonts,\
but some have also been improved by the project.

Name:		fonts-ttf-vlgothic
Version:	20141206
Release:	alt2_9
Summary:	Japanese TrueType font

License:	mplus and BSD
URL:		http://dicey.org/vlgothic
Source0:	http://osdn.dl.sourceforge.jp/vlgothic/62375/%{archivename}.tar.bz2
Source1:	%{oldname}-fontconfig-pgothic.conf
Source2:	%{oldname}-fontconfig-gothic.conf
Source3:        %{fontname}.metainfo.xml
Source4:        %{fontname}-proportional.metainfo.xml
Patch0:		%{oldname}-1331050.patch
Patch1:		%{oldname}-p-1331050.patch

BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	fonttools

Obsoletes:	%{oldname}-common < 20121230-2
Provides:	%{oldname}-common = %{version}-%{release}
Source44: import.info
%description
%common_desc

This package provides the monospace VLGothic font.


%package -n fonts-ttf-vlgothic-p
Group: System/Fonts/True type
Summary:	Proportional Japanese TrueType font
Obsoletes:	%{oldname}-common < 20121230-2
Provides:	%{oldname}-common = %{version}-%{release}

%description -n fonts-ttf-vlgothic-p
%common_desc

This package provides the VLGothic font with proportional glyphs for some
non-Japanese characters.

%prep
%setup -q -n VLGothic


%build
#rhbz#1331050: reassign U+23F4 and U+23F5 each other.
ttx -i -a -e VL-Gothic-Regular.ttf
ttx -i -a -e VL-PGothic-Regular.ttf
sed -ie 's/<!--.*-->//g' VL-Gothic-Regular.ttx
sed -ie 's/<!--.*-->//g' VL-PGothic-Regular.ttx
patch -b -z .1331050 VL-Gothic-Regular.ttx %{PATCH0}
patch -b -z .1331050 VL-PGothic-Regular.ttx %{PATCH1}
touch -r VL-Gothic-Regular.ttf VL-Gothic-Regular.ttx
touch -r VL-PGothic-Regular.ttf VL-PGothic-Regular.ttx
rm VL-Gothic-Regular.ttf
rm VL-PGothic-Regular.ttf
ttx -b VL-Gothic-Regular.ttx
ttx -b VL-PGothic-Regular.ttx
touch -r VL-Gothic-Regular.ttx VL-Gothic-Regular.ttf
touch -r VL-PGothic-Regular.ttx VL-PGothic-Regular.ttf

%{nil}

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p *.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d	$RPM_BUILD_ROOT%{_fontconfig_templatedir} \
			$RPM_BUILD_ROOT%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{pfontconf}.conf
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}.conf

for fconf in %{pfontconf}.conf %{fontconf}.conf; do
	ln -s %{_fontconfig_templatedir}/$fconf $RPM_BUILD_ROOT%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-proportional.metainfo.xml
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
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/VL-Gothic-Regular.ttf
%doc README*
%doc --no-dereference LICENSE*
%{_datadir}/appdata/%{fontname}.metainfo.xml

%files -n fonts-ttf-vlgothic-p
%{_fontconfig_templatedir}/%{pfontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{pfontconf}.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/VL-PGothic-Regular.ttf
%doc README*
%doc --no-dereference LICENSE*
%{_datadir}/appdata/%{fontname}-proportional.metainfo.xml

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 20141206-alt2_9
- update to new release by fcimport

* Wed Dec 06 2017 Igor Vlasenko <viy@altlinux.ru> 20141206-alt2_8
- fixed build

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 20141206-alt1_8
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 20141206-alt1_1
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20140530-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20121230-alt1_4
- update to new release by fcimport

* Thu Jan 17 2013 Igor Vlasenko <viy@altlinux.ru> 20121230-alt1_2
- update to new release by fcimport

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 20121230-alt1_1
- update to new release by fcimport

* Sun Nov 25 2012 Igor Vlasenko <viy@altlinux.ru> 20121109-alt1_2
- update to new release by fcimport

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 20121109-alt1_1
- update to new release by fcimport

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 20120928-alt1_1
- update to new release by fcimport

* Mon Sep 10 2012 Igor Vlasenko <viy@altlinux.ru> 20120905-alt1_1
- update to new release by fcimport

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 20120829-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20120629-alt1_2
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 20120629-alt1_1
- update to new release by fcimport

* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 20120618-alt1_1
- fc import

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 20120325-alt1_1
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20120130-alt2_1
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 20120130-alt1_1
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 20111122-alt2_2
- update to new release by fcimport

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 20111122-alt2_1
- updated dependencies

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 20111122-alt1_1
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20110722-alt2_1
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 20110722-alt1_1
- initial release by fcimport

