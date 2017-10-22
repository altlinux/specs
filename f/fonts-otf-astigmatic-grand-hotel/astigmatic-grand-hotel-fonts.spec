Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname astigmatic-grand-hotel-fonts
%define fedora 26
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname astigmatic-grand-hotel
%global fontconf 61-%{fontname}.conf

Name:		fonts-otf-astigmatic-grand-hotel
Version:	1.000
Release:	alt1_5
Summary:	Script retro style fonts

License:	OFL
URL:		http://www.astigmatic.com/
Source0:	https://www.fontsquirrel.com/fonts/download/grand-hotel/grand-hotel.zip
Source1:	%{oldname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
%if 0%{?fedora} >= 21
BuildRequires:	libappstream-glib
%endif
Source44: import.info

%description
Grand Hotel finds its inspiration from the title screen of the 1937 film a.'Cafe 
Metropolea.' starring Tyrone Power. This condensed upright connecting script has 
a classic vibe to it.

It has a wonderful weight to it that feels subtly tied to Holiday and Bakery 
themed designs, even though it can work outside that genre.

%prep
%setup -n %{oldname}-%{version} -q -c



%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}

%if 0%{?fedora} >= 21
install -Dm 0644 -p %{SOURCE2} \
		%{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
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
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{fontname}.metainfo.xml
%endif

%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.otf

%doc SIL\ Open\ Font\ License.txt
%if 0%{?fedora} >= 21
%{_datadir}/appdata/%{fontname}.metainfo.xml
%endif

%changelog
* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.000-alt1_5
- new version

