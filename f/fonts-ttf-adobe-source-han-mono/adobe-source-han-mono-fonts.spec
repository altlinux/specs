Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
%define oldname adobe-source-han-mono-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.002
%global fontname adobe-source-han-mono
%global fontconf 68-%{fontname}.conf
%global archivename source-han-mono-%{version}R

Name:		fonts-ttf-adobe-source-han-mono
Version:	1.002
Release:	alt1_9
Summary:	Adobe OpenType monospaced font for mixed Latin and CJK text

License:	OFL
URL:		https://github.com/adobe-fonts/source-han-mono/
Source0:	https://github.com/adobe-fonts/source-han-mono/releases/download/%{version}/SourceHanMono.ttc
Source1:	https://raw.githubusercontent.com/adobe-fonts/source-han-mono/%{version}/LICENSE.md
Source2:	https://raw.githubusercontent.com/adobe-fonts/source-han-mono/%{version}/README.md
Source10:	%{oldname}-fontconfig.conf
Source11:	%{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel libappstream-glib libappstream-glib-gir
Source44: import.info

%description
Source Han Mono, which is derived from Source Han Sans and Source Code Pro,
is an OpenType/CFF Collection (OTC) that includes 70 font instancesa..consisting
of seven weights, five languages, and two stylesa..and is a Pan-CJK version
of Source Han Code JP.

%prep
%setup -n %{oldname}-%{version} -q -c -T

cp -a %{SOURCE0} .
cp -a %{SOURCE1} .
cp -a %{SOURCE2} .

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_metainfodir}
install -m 0644 -p %{SOURCE11} %{buildroot}%{_metainfodir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s	%{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc woff woff2 WOFF WOFF2 otb OTB pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*|otb|OTB) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
	woff|WOFF) type=woff;;
	woff2|WOFF2) type=woff2;;
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
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%dir %{_fontsdir}/*/%{_fontstem}/
%{_fontsdir}/*/%{_fontstem}/*.ttc

%doc --no-dereference LICENSE.md
%doc README.md
%{_metainfodir}/%{fontname}.metainfo.xml

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 1.002-alt1_9
- new version

