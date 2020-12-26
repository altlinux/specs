Group: System/Fonts/True type
%define oldname smc-suruma-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname smc-suruma
%global fontconf 67-%{fontname}.conf

Name:		fonts-ttf-smc-suruma
Version:	3.2.4
Release:	alt1_1
Epoch:		1
Summary:	Open Type Fonts for Malayalam script 
License:	GPLv3+ with exceptions
URL:		https://gitlab.com/smc/fonts/suruma
Source0:	%{url}/-/archive/Version%{version}/suruma-Version%{version}.tar.gz
Source1:	%{fontname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
BuildRequires:	fontforge libfontforge python3-module-fontforge
Obsoletes:	fonts-ttf-smc-common < 6.1-alt1_9
Source44: import.info

%description
Suruma-3.2.1 is a rehash of earlier releases. 
The earlier idea of akhand conjuncts for *RA *LA forms is revisited and 
implemented again with the new opentype specs. The new specs do away 
with statically-assigned character properties (by the shaping engine) 
for consonants. Instead, they are font dependent. i.e., post-base forms,
below-base forms etc. are all decided by the the font itself. 
This concept was also used in the initial version of suruma font.

%prep
%setup -q -n suruma-Version%{version}


%build
make

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p build/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
	%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

install -Dm 0644 -p %{SOURCE2} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

ln -s %{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}
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

%check
appstream-util validate-relax --nonet \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/*.ttf
%doc README.md
%doc --no-dereference COPYING
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 1:3.2.4-alt1_1
- update to new release by fcimport

* Wed Feb 26 2020 Igor Vlasenko <viy@altlinux.ru> 1:3.2.3-alt1_1
- update to new release by fcimport

* Wed Aug 07 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.2.2-alt1_3
- update to new release by fcimport

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.2.1-alt1_3
- new version

