Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname adobe-source-han-code-jp-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.000
%global fontname adobe-source-han-code-jp
%global fontconf 65-2-%{fontname}.conf
%global archivename source-han-code-jp-%{version}R

Name:		fonts-otf-adobe-source-han-code-jp
Version:	2.000
Release:	alt1_3
Summary:	Adobe OpenType UI font for mixed Latin and Japanese text

License:	OFL
URL:		https://github.com/adobe-fonts/source-han-code-jp/
Source0:	https://github.com/adobe-fonts/source-han-code-jp/archive/%{version}R/%{archivename}.zip
Source1:	%{oldname}-fontconfig.conf

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Source44: import.info

%description
Source Han Code JP is a derivative of Source Han Sans that replaces
its proportional Latin glyphs with fixed-width 667-unit glyphs from
Source Code Pro. The Latin glyphs are scaled to match the glyphs for
Japanese kana and kanji, and their widths are adjusted to be exactly
667 units (two-thirds of an EM). Source Han Code JP is intended to be
used as a UI font for mixed Latin and Japanese text on displays,
for programming, editing HTML/CSS, viewing text or inputing to
the command line in a terminal app, and so on.

%prep
%setup -q -n %{archivename}

chmod 0644 README.md

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p OTF/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s	%{_fontconfig_templatedir}/%{fontconf} \
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

%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.otf

%doc LICENSE.txt
%doc README.md relnotes.txt

%changelog
* Wed Dec 06 2017 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1_3
- new version

