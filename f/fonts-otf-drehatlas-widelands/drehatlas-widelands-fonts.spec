# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname drehatlas-widelands-fonts
%global fontname drehatlas-widelands
%global fontconf 61-%{fontname}.conf
%global metapkgver 2010-02-06

# This is a highly-stylized titling font, so picking an ideal substitute with
# fontconfig is pointless

Name:		fonts-otf-drehatlas-widelands
Version:	1.0.3.1
Release:	alt3_7
Summary:	A Latin typeface inspired by feudal calligraphy
Group:		System/Fonts/True type
License:	OFL
URL:		http://www.drehatlas.de/
Source0:	http://downloads.sourceforge.net/project/drehatlas-fonts/Font-Packages/COMPLETE/drehatlas-fonts-%{metapkgver}.zip
Source1:	%{fontconf}
BuildArch:	noarch
BuildRequires:	fontpackages-devel fontforge
Source44: import.info

%description
This font was created by Peter Schwanemann as a logo for the Widelands project,
but has since been enhanced.  The font is decorative and not really usable for
real texts, but it looks nice for logos, banners or similar stuff.  All normal
latin glyphs and arabic numbers are included and usable.

%prep
%setup -q -c %{oldname}-%{version}
cd drehatlas-fonts-%{metapkgver}/Widelands-%{version}
# Wrap the license file at 80 chars
fold -s LICENSE > LICENSE.new
touch -r LICENSE LICENSE.new
mv LICENSE.new LICENSE

%build

%install
rm -fr %{buildroot}

cd drehatlas-fonts-%{metapkgver}/Widelands-%{version}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
	%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}
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
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.otf
%doc drehatlas-fonts-%{metapkgver}/Widelands-%{version}/LICENSE drehatlas-fonts-%{metapkgver}/Widelands-%{version}/FONTLOG

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt3_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt2_7
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt2_6
- rebuild with new rpm-build-fonts

* Thu Aug 04 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt1_6
- initial release by fcimport

