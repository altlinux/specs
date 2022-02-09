# BEGIN SourceDeps(oneline):
BuildRequires: python3(fontforge)
# END SourceDeps(oneline)
Group: System/Fonts/True type
%define oldname smc-dyuthi-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname smc-dyuthi
%global fontconf 67-%{fontname}.conf

Name:		fonts-ttf-smc-dyuthi
Version:	3.0.2
Release:	alt1_5
Epoch:		1
Summary:	Open Type Fonts for Malayalam script
License:	OFL
URL:		https://gitlab.com/smc/fonts/dyuthi
Source0:	https://gitlab.com/smc/fonts/dyuthi}/-/archive/Version%{version}/dyuthi-Version%{version}.tar.gz
Source1:	%{fontname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib libappstream-glib-gir
BuildRequires:	libbrotli-devel
BuildRequires:	libfontforge-devel
BuildRequires:	python3
BuildRequires:	python3-module-fonttools
Obsoletes:	fonts-ttf-smc-common < 6.1-alt1_9
Source44: import.info

%description
Dyuthi is an ornamental typographic design that supports Latin and Malayalam. 
The glyph patterns are based on popular 'bulged ended' type designs 
which used to be popular in Malayalam designs. The font comes in one size 
and is thicker than usual Malayalam fonts, hence is suited for titling and 
headlines. Dyuthi can accompany Meera or Rachana as title font, 
when they are used as body text.

%prep
%setup -q -n dyuthi-Version%{version}

chmod 644 *.txt
rm -rf ttf

%build
make PY=python3

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
%dir %{_fontsdir}/*/%{_fontstem}/
%{_fontsdir}/*/%{_fontstem}/*.ttf
%doc README.md
%doc --no-dereference LICENSE.txt
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
* Wed Feb 09 2022 Igor Vlasenko <viy@altlinux.org> 1:3.0.2-alt1_5
- update to new release by fcimport

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt1_2
- new version

