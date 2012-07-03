%define oldname sil-gentium-fonts
%define fontname sil-gentium
%define archivename ttf-sil-gentium
%define common_desc \
SIL Gentium ("belonging to the nations" in Latin) is a Unicode typeface family\
designed to enable the many diverse ethnic groups around the world who use\
the Latin script to produce readable, high-quality publications. It supports\
a wide range of Latin-based alphabets.


Name:           fonts-ttf-sil-gentium
Version:        1.02
Release:        alt5_12
Summary:        SIL Gentium fonts

Group:          System/Fonts/True type
License:        OFL
URL:            http://scripts.sil.org/Gentium_linux
# Source0 can be downloaded from the above URL, search for "tar.gz"
Source0:        %{archivename}_1.0.2.tar.gz

BuildArch:      noarch
BuildRequires:  fontpackages-devel

Requires:       %{name}-common = %{version}-%{release}

# Obsoleting and providing the old RPM name
Obsoletes:      gentium-fonts < 1.02-7
Source44: import.info
Provides: fonts-ttf-gentium = %version-%release
Obsoletes: fonts-ttf-gentium <= 1.0.2-alt2


%description
%common_desc

This package consists of the main SIL Gentium family.


%files
%{_fontbasedir}/*/%{_fontstem}/Gen[RI]*.ttf


%package common
Summary:        Common files of SIL Gentium fonts
Group:          System/Fonts/True type

%description common
%common_desc

This package consists of files used by other %{oldname} packages.


%package -n fonts-ttf-sil-gentium-alt
Summary:        SIL GentiumAlt fonts
Group:          System/Fonts/True type
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-sil-gentium-alt
%common_desc

This package consists of the SIL GentiumAlt family. GentiumAlt is a
alternative version of Gentium with flatter diacratics, to make it more
suitable for languages that use stacking diacratics, like Vietnamese. There
is no problem with having both Gentium and GentiumAlt installed at the same
time.


%files -n fonts-ttf-sil-gentium-alt
%{_fontbasedir}/*/%{_fontstem}/GenA*.ttf


%prep
%setup -q -n %{archivename}-%{version}

# Convert GENTIUM-FAQ from MacRoman
iconv --from=MACINTOSH --to=UTF-8 GENTIUM-FAQ > GENTIUM-FAQ.new
touch -c -r GENTIUM-FAQ GENTIUM-FAQ.new
mv GENTIUM-FAQ.new GENTIUM-FAQ


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
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
%doc FONTLOG GENTIUM-FAQ OFL OFL-FAQ QUOTES README

%dir %{_fontbasedir}/*/%{_fontstem}


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.02-alt5_12
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.02-alt4_12
- update to new release by fcimport

* Thu Aug 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.02-alt4_11
- really added provides/obsoletes for short names

* Thu Aug 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.02-alt3_11
- added provides/obsoletes for short names

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.02-alt2_11
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_11
- initial release by fcimport

