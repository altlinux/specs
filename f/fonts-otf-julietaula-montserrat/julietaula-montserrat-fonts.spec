Group: System/Fonts/True type
%define oldname julietaula-montserrat-fonts
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname julietaula-montserrat
%global fontconf 61-%{fontname}.conf

Name:		fonts-otf-julietaula-montserrat
Version:	7.200
Release:	alt1_1
# Override versioning to sync with upstream
Epoch:		1
Summary:	Sans-serif typeface created by Julieta Ulanovsky

License:	OFL
URL:		https://github.com/JulietaUla/Montserrat
Source0:	%{url}/archive/Montserrat/v%{version}.tar.gz#/Montserrat-%{version}.tar.gz
Source1:	%{oldname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
%if 0%{?fedora} >= 21
BuildRequires:	libappstream-glib
%endif

# Reset the old date based versioning
Obsoletes:	%{oldname} < 1:%{version}-%{release}
Source44: import.info


%description
A typeface created by Julieta Ulanovsky inspired by signs around
the Montserrat area of Buenos Aires, Argentina

%prep
%setup -n %{oldname}-%{version} -q -c


%build


%install
install -Dpm 0644 Montserrat-%{version}/fonts/ttf/*.ttf -t %{buildroot}%{_fontdir}
install -Dpm 0644 Montserrat-%{version}/fonts/otf/*.otf -t %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%if 0%{?fedora} >= 21
install -Dm 0644 -p %{SOURCE2} \
		%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml
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
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{fontname}.metainfo.xml
%endif
%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.ttf
%{_fontbasedir}/*/%{_fontstem}/*.otf
%if 0%{?fedora} >= 21
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%endif
%doc Montserrat-%{version}/OFL.txt
%doc Montserrat-%{version}/README.md 

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:7.200-alt1_1
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:6.002-alt1_3
- new version

