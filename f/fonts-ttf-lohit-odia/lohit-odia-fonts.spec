Group: System/Fonts/True type
%define oldname lohit-odia-fonts
%global fontname lohit-odia
%global fontconf0 65-0-%{fontname}.conf
%global fontconf1 30-%{fontname}.conf

Name:           fonts-ttf-lohit-odia
Version:        2.5.5
Release:        alt1_5
Summary:        Free truetype font for Odia language

License:        OFL
URL:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/%{fontname}-%{version}.tar.gz
Source1:        %{oldname}.conf
Source2:       %{fontname}.metainfo.xml
BuildArch:      noarch
BuildRequires:  fontforge >= 20080429
BuildRequires:  fontpackages-devel
Provides:       lohit-oriya-fonts = %{version}-%{release}
Obsoletes:      lohit-oriya-fonts < 2.5.4.1-4
Source44: import.info

%description
This package provides a free truetype font for Odia language.

%prep
%setup -q -n %{fontname}-%{version} 
# To make it default font for 'or' language.
mv 66-%{fontname}.conf 65-0-lohit-odia.conf


%build
make ttf %{?_smp_mflags}

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf0} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf0}
ln -s %{_fontconfig_templatedir}/%{fontconf0} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf0}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}
ln -s %{_fontconfig_templatedir}/%{fontconf1} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf1}


# Add AppStream metadata
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

%files
%{_fontconfig_templatedir}/*.conf
%config(noreplace) %{_fontconfig_confdir}/*.conf
%{_fontbasedir}/*/%{_fontstem}/*.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.5-alt1_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.5-alt1_4
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.5-alt1_3
- converted for ALT Linux by srpmconvert tools

