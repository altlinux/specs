# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname woodardworks-laconic-fonts
%global fontname woodardworks-laconic
%global fontconf 60-%{fontname}

Name:		fonts-otf-woodardworks-laconic
Summary:	An artistic and minimal sans-serif font family
Version:	001.001
Release:	alt3_6
License:	OFL
Group:		System/Fonts/True type
Source0:	http://www.woodardworks.com/laconic.zip
Source1:	%{oldname}-fontconfig.conf
Source2:	%{fontname}-shadow-fonts-fontconfig.conf
URL:		http://www.woodardworks.com/type13.html
BuildRequires:	fontpackages-devel
BuildArch:	noarch
Source44: import.info

%description
Laconic is a typeface font design meant to be dry without quite seeming 
parched. Curves and diagonals are kept to a bare minimum without sacrificing
legibility. What it lacks in design features are more than made up for in 
OpenType features. All the weights contain small caps, proportial figures,
old style figures, tabular figures, ligatures and stylistic alternates.

%package -n fonts-otf-woodardworks-laconic-shadow
Summary:	A shadowed version of the Laconic sans-serif font family
Group:		System/Fonts/True type

%description -n fonts-otf-woodardworks-laconic-shadow
Laconic is a typeface font design meant to be dry without quite seeming
parched. Curves and diagonals are kept to a bare minimum without sacrificing
legibility. What it lacks in design features are more than made up for in
OpenType features. All the weights contain small caps, proportial figures,
old style figures, tabular figures, ligatures and stylistic alternates.
This package contains the Laconic Shadow font face.

%prep
%setup -q -c -T -n laconic
# We have to do this to avoid leaving a stray __MACOSX dir in the buildroot
unzip -j -L -q %{SOURCE0}
# Get rid of junk files
rm -rf ._*

%build
# Nothing to do here, already in OTF.

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-shadow.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}.conf %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}-shadow.conf %{buildroot}%{_fontconfig_confdir}/%{fontconf}-shadow.conf
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
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/Laconic_Bold.otf
%{_fontbasedir}/*/%{_fontstem}/Laconic_Light.otf
%{_fontbasedir}/*/%{_fontstem}/Laconic_Regular.otf
%doc laconic_eula.pdf

%files -n fonts-otf-woodardworks-laconic-shadow
%{_fontconfig_templatedir}/%{fontconf}-shadow.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-shadow.conf
%{_fontbasedir}/*/%{_fontstem}/Laconic_Shadow.otf
%doc laconic_eula.pdf

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 001.001-alt3_6
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 001.001-alt2_6
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 001.001-alt2_5
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 001.001-alt1_5
- initial release by fcimport

