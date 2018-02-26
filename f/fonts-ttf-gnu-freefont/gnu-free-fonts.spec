# BEGIN SourceDeps(oneline):
BuildRequires: python
# END SourceDeps(oneline)
%define oldname gnu-free-fonts
%global fontname gnu-free
%global fontconf 67-%{fontname}

Name:      fonts-ttf-gnu-freefont
Version:   20100919
Release:   alt3_5
Summary:   Free UCS Outline Fonts
Group:     System/Fonts/True type
# Standard font exception
License:   GPLv3+ with special font exception
URL:       http://www.gnu.org/software/freefont/
Source0:   http://savannah.nongnu.org/download/freefont/freefont-sfd-%{version}.tar.gz
Source1:   gnu-free-fonts-buildscript
Source2:   %{fontconf}-mono.conf
Source3:   %{fontconf}-sans.conf
Source4:   %{fontconf}-serif.conf
BuildArch: noarch
BuildRequires: fontpackages-devel fontforge

%global common_desc \
Gnu FreeFont is a free family of scalable outline fonts, suitable for general \
use on computers and for desktop publishing. It is Unicode-encoded for \
compatibility with all modern operating systems. \
 \
Besides a full set of characters for writing systems based on the Latin \
alphabet, FreeFont contains large selection of characters from other writing \
systems some of which are hard to find elsewhere. \
 \
FreeFont also contains a large set of symbol characters, both technical and \
decorative. We are especially pleased with the Mathematical Operators range, \
with which most of the glyphs used in LaTeX can be displayed.
Source44: import.info

%description
%common_desc


%package common
Group: System/Fonts/True type
Summary:  Common files for freefont (documentationa..)

%description common
%common_desc

This package consists of files used by other %{oldname} packages.


%package -n fonts-ttf-gnu-freefont-mono
Group: System/Fonts/True type
Summary:  GNU FreeFont Monospaced Font
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-gnu-freefont-mono
%common_desc

This package contains the GNU FreeFont monospaced font.


%package -n fonts-ttf-gnu-freefont-sans
Group: System/Fonts/True type
Summary:  GNU FreeFont Sans-Serif Font
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-gnu-freefont-sans
%common_desc

This package contains the GNU FreeFont sans-serif font.


%package -n fonts-ttf-gnu-freefont-serif
Group: System/Fonts/True type
Summary:  GNU FreeFont Serif Font
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-gnu-freefont-serif
%common_desc

This package contains the GNU FreeFont serif font.


%package compat
Group: System/Fonts/True type
Summary: GNU freefont compatibility package
Obsoletes: freefont < 20090104-4
Requires:  fonts-ttf-gnu-freefont-mono = %{version}-%{release}
Requires:  fonts-ttf-gnu-freefont-sans = %{version}-%{release}
Requires:  fonts-ttf-gnu-freefont-serif = %{version}-%{release}

%description compat
This package only exists to help transition pre 20090104-4 freefont users to \
the new package split. It will be removed after one distribution release \
cycle, please do not reference it or depend on it in any way.\
\
It can be safely uninstalled.


%prep
%setup -qn freefont-%{version}


%build
fontforge -lang=ff -script %{SOURCE1} *.sfd

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -p -m 644 *.ttf  %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mono.conf

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf

install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif.conf


for fconf in %{fontconf}-mono.conf \
                %{fontconf}-sans.conf \
                %{fontconf}-serif.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

rm %{buildroot}%{_datadir}/fonts/gnu-free/Untitled1.ttf
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

%files -n fonts-ttf-gnu-freefont-mono
%{_fontconfig_templatedir}/%{fontconf}-mono.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-mono.conf
%{_fontbasedir}/*/%{_fontstem}/FreeMono*.ttf
%files -n fonts-ttf-gnu-freefont-sans
%{_fontconfig_templatedir}/%{fontconf}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans.conf
%{_fontbasedir}/*/%{_fontstem}/FreeSans*.ttf
%files -n fonts-ttf-gnu-freefont-serif
%{_fontconfig_templatedir}/%{fontconf}-serif.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-serif.conf
%{_fontbasedir}/*/%{_fontstem}/FreeSerif*.ttf

%files common
%doc AUTHORS ChangeLog CREDITS COPYING README Untitled1.ttf

%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 20100919-alt3_5
- rebuild for fontlang provides

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100919-alt2_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100919-alt1_5
- update to new release by fcimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 20100919-alt1_4
- initial release by fedoraimport

