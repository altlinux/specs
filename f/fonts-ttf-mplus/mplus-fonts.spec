%define oldname mplus-fonts
###############################################################################
# Definitions
###############################################################################
%define fixed_desc() \
The combination of fixed-fullwidth M+ %2 for Japanese and fixed-halfwidth \
%1 %2 %3 for alphabets. They are 5 weights from Thin to Bold.   

%define proportional_desc() \
The combination of fixed-fullwidth M+ %2 for Japanese and proportional  \
%1 %2 %3 for alphabets. They are 7 weights from Thin to Black.         

%define common_desc() \
The Mplus fonts are 7 families of fonts, of which 4 are combinations \
of proportional font families,variations of fixed-fullwidth fonts, \
variations of fixed-halfwidth fonts and each have between 5 - 7 \
different weights.

%define summary_p M+ P is aimed as sophisticated and relaxed design

%define summary_c M+ C is optimized to be proportioned and has two variations

%define summary_m M+ M emphasize the balance of natural letterform and high legibility


%define fontname mplus

###############################################################################
# Header
###############################################################################

Name:       fonts-ttf-mplus
Version:    028 
Release:    alt3_3
Summary:    The Mplus fonts is a superfamily of fonts designed by Coji Morishita

Group:      System/Fonts/True type
License:    mplus
URL:        http://%{fontname}-fonts.sourceforge.jp/%{fontname}-outline-fonts/index-en.html
Source0:    http://downloads.sourceforge.jp/%{fontname}-fonts/6650/%{fontname}-TESTFLIGHT-%{version}.tar.gz

BuildArch: noarch  
BuildRequires:   fontpackages-devel
Source44: import.info

%description
%common_desc

###############################################################################
# Package section
###############################################################################

%package common
Group: System/Fonts/True type
Summary:  Mplus, common files (documentationa..)

%description common
%common_desc

This package consists of files used by other %{oldname} packages.


# 1p
%package -n fonts-ttf-mplus-1p
Group: System/Fonts/True type
Summary: %summary_p
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-mplus-1p
%proportional_desc M+ 1P Type-1

%files -n fonts-ttf-mplus-1p
%{_fontbasedir}/*/%{_fontstem}/%{fontname}-1p-*.ttf

# 2p
%package -n fonts-ttf-mplus-2p
Group: System/Fonts/True type
Summary: %summary_p
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-mplus-2p
%proportional_desc M+ 2P Type-2

%files -n fonts-ttf-mplus-2p
%{_fontbasedir}/*/%{_fontstem}/%{fontname}-2p-*.ttf

# 1c
%package -n fonts-ttf-mplus-1c
Group: System/Fonts/True type
Summary: %summary_c
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-mplus-1c
%proportional_desc M+ 1C Type-1

%files -n fonts-ttf-mplus-1c
%{_fontbasedir}/*/%{_fontstem}/%{fontname}-1c-*.ttf

# 2c
%package -n fonts-ttf-mplus-2c
Group: System/Fonts/True type
Summary: %summary_c
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-mplus-2c
%proportional_desc M+ 2C Type-2

%files -n fonts-ttf-mplus-2c
%{_fontbasedir}/*/%{_fontstem}/%{fontname}-2c-*.ttf

# 1m
%package -n fonts-ttf-mplus-1m
Group: System/Fonts/True type
Summary: %summary_m
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-mplus-1m
%fixed_desc M+ 1M Type-1

%files -n fonts-ttf-mplus-1m
%{_fontbasedir}/*/%{_fontstem}/%{fontname}-1m-*.ttf

# 2m
%package -n fonts-ttf-mplus-2m
Group: System/Fonts/True type
Summary: %summary_m
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-mplus-2m
%fixed_desc M+ 2M Type-2

%files -n fonts-ttf-mplus-2m
%{_fontbasedir}/*/%{_fontstem}/%{fontname}-2m-*.ttf

# 1mn
%package -n fonts-ttf-mplus-1mn
Group: System/Fonts/True type
Summary: %summary_m
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-mplus-1mn
%fixed_desc M+ 1MN Type-1

%files -n fonts-ttf-mplus-1mn
%{_fontbasedir}/*/%{_fontstem}/%{fontname}-1mn-*.ttf

###############################################################################
# Files
###############################################################################
%prep
%setup -q -n %{fontname}-TESTFLIGHT-%{version}

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
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
%doc LICENSE_{E,J} README_{E,J}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 028-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 028-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 028-alt2_2
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 028-alt1_2
- initial release by fcimport

