Group: System/Fonts/True type
%define oldname gnu-free-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname gnu-free
%global fontconf 69-%{fontname}

Name:      fonts-ttf-gnu-freefont
Version:   20120503
Release:   alt1_16
Summary:   Free UCS Outline Fonts

# Standard font exception
License:   GPLv3+ with exceptions
URL:       http://www.gnu.org/software/freefont/
Source0:   http://ftp.gnu.org/gnu/freefont/freefont-src-%{version}.tar.gz
Source2:   %{fontconf}-mono.conf
Source3:   %{fontconf}-sans.conf
Source4:   %{fontconf}-serif.conf
Source5:   %{fontname}.metainfo.xml
Source6:   %{fontname}-mono.metainfo.xml
Source7:   %{fontname}-sans.metainfo.xml
Source8:   %{fontname}-serif.metainfo.xml

Patch0:    gnu-free-fonts-devanagari-rendering.patch

BuildArch: noarch
BuildRequires: fontpackages-devel fontforge libfontforge
# following is needed as we are calling /usr/bin/2to3
BuildRequires: python-tools-2to3 python3-tools

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


%package -n fonts-ttf-gnu-freefont-common
Group: System/Fonts/True type
Summary:  Common files for freefont (documentationa..)
Obsoletes: gnu-free-fonts-compat < 20120503

%description -n fonts-ttf-gnu-freefont-common
%common_desc

This package consists of files used by other %{oldname} packages.


%package -n fonts-ttf-gnu-freefont-mono
Group: System/Fonts/True type
Summary:  GNU FreeFont Monospaced Font
Requires: fonts-ttf-gnu-freefont-common = %{version}-%{release}

%description -n fonts-ttf-gnu-freefont-mono
%common_desc

This package contains the GNU FreeFont monospaced font.


%package -n fonts-ttf-gnu-freefont-sans
Group: System/Fonts/True type
Summary:  GNU FreeFont Sans-Serif Font
Requires: fonts-ttf-gnu-freefont-common = %{version}-%{release}

%description -n fonts-ttf-gnu-freefont-sans
%common_desc

This package contains the GNU FreeFont sans-serif font.


%package -n fonts-ttf-gnu-freefont-serif
Group: System/Fonts/True type
Summary:  GNU FreeFont Serif Font
Requires: fonts-ttf-gnu-freefont-common = %{version}-%{release}

%description -n fonts-ttf-gnu-freefont-serif
%common_desc

This package contains the GNU FreeFont serif font.


%prep
%setup -n %{oldname}-%{version} -qn freefont-%{version}

%patch0 -p1 -b .devanagari

# move build scripts to python3 compatible code
pushd tools
pushd generate
# Following for loop should not be used on pyc files
# better remove pre-compiled buildutils.pyc file
rm *.pyc
for item in `ls`;do
   2to3 -w $item
done
popd
popd

%build
make

%install
pushd sfd
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

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE5} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-mono.metainfo.xml
install -Dm 0644 -p %{SOURCE7} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE8} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-serif.metainfo.xml
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
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/FreeMono*.ttf
%{_datadir}/appdata/%{fontname}-mono.metainfo.xml
%files -n fonts-ttf-gnu-freefont-sans
%{_fontconfig_templatedir}/%{fontconf}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/FreeSans*.ttf
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
%files -n fonts-ttf-gnu-freefont-serif
%{_fontconfig_templatedir}/%{fontconf}-serif.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-serif.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/FreeSerif*.ttf
%{_datadir}/appdata/%{fontname}-serif.metainfo.xml

%files -n fonts-ttf-gnu-freefont-common
%doc AUTHORS ChangeLog CREDITS README
%doc --no-dereference COPYING
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 20120503-alt1_16
- update to new release by fcimport

* Tue Jan 13 2015 Igor Vlasenko <viy@altlinux.ru> 20120503-alt1_10
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20120503-alt1_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20120503-alt1_5
- update to new release by fcimport

* Thu Jan 17 2013 Igor Vlasenko <viy@altlinux.ru> 20120503-alt1_4
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 20120503-alt1_3
- update to new release by fcimport

* Wed Nov 07 2012 Igor Vlasenko <viy@altlinux.ru> 20120503-alt1_2
- update to new release by fcimport

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 20120503-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20100919-alt3_6
- update to new release by fcimport

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 20100919-alt3_5
- rebuild for fontlang provides

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100919-alt2_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100919-alt1_5
- update to new release by fcimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 20100919-alt1_4
- initial release by fedoraimport

