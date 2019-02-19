Group: System/Fonts/True type
%define oldname aftertheflood-sparks-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname aftertheflood-sparks
%global fontconf 66-%{fontname}
%global desc After the Flood Sparks is a font that allows for the combination of text and \
visual data to show an idea and evidence in one headline. This builds on the \
principle of Sparklines defined by Edward Tufte and makes them easier to use. \
Sparklines are currently available as plugins or javascript elements. By  \
installing the Sparks font you can use them immediately without the need for \
custom code. \
\
Sparks data needs to be formatted as comma-separated values, with curly brackets \
at both ends of the set, e.g., {30,60,90}. You can also have numbers at the \
beginning and end of the set, which are useful for providing the start and \
end points, e.g., 123{30,60,90}456 a.. Sparks has numerals built in.


Name:       fonts-otf-aftertheflood-sparks
Version:    2.0
Release:    alt1_3
Summary:    After the Flood Sparks, a font to display charts within text
License:    OFL
URL:        https://aftertheflood.co/projects/sparks/
Source0:    https://github.com/aftertheflood/sparks/archive/v%{version}/%{oldname}-%{version}.tar.gz
Source1:    66-%{fontname}-bar.conf
Source2:    66-%{fontname}-dot.conf
Source3:    66-%{fontname}-dot-line.conf
Source4:    %{fontname}.metainfo.xml
Source5:    %{fontname}-bar.metainfo.xml
Source6:    %{fontname}-dot.metainfo.xml
Source7:    %{fontname}-dot-line.metainfo.xml

BuildArch:      noarch

BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Source44: import.info



%description
%{desc}


%package -n fonts-otf-aftertheflood-sparks-common
Group: System/Fonts/True type
Summary: Common files for After the Flood Sparks

%description -n fonts-otf-aftertheflood-sparks-common
%{desc}

Common files for After the Flood Sparks.


%package -n fonts-otf-aftertheflood-sparks-bar
Group: System/Fonts/True type
Summary: After the Flood Sparks Bar fonts
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-otf-aftertheflood-sparks-bar
%{desc}

This package provides the Bar family.


%package -n fonts-otf-aftertheflood-sparks-dot
Group: System/Fonts/True type
Summary: After the Flood Sparks Dot fonts
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-otf-aftertheflood-sparks-dot
%{desc}

This package provides the Dot family.


%package -n fonts-otf-aftertheflood-sparks-dot-line
Group: System/Fonts/True type
Summary: After the Flood Sparks Dot-line fonts
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-otf-aftertheflood-sparks-dot-line
%{desc}

This package provides the Dot-line family.


%prep
%setup -q -n sparks-%{version}



%build
# Nothing to do


%install
# install fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 output/otf/*.otf %{buildroot}%{_fontdir}

# install fontconfig files
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-bar.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-dot.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-dot-line.conf

for fconf in %{fontconf}-bar.conf %{fontconf}-dot.conf %{fontconf}-dot-line.conf; do
    ln -s %{_fontconfig_templatedir}/$fconf \
          %{buildroot}%{_fontconfig_confdir}/$fconf
done

# install appdata
install -m 0755 -d %{buildroot}%{_datadir}/metainfo
install -m 0644 -p %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} \
        %{buildroot}%{_datadir}/metainfo

appstream-util validate-relax --nonet \
               %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
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

               
%files -n fonts-otf-aftertheflood-sparks-common
%doc --no-dereference OFL.txt
%doc AUTHORS.txt CONTRIBUTORS.txt FONTLOG.txt README.md 
%{_datadir}/metainfo/%{fontname}.metainfo.xml


%files -n fonts-otf-aftertheflood-sparks-bar
%{_fontconfig_templatedir}/%{fontconf}-bar.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-bar.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Sparks-Bar-*.otf
%{_datadir}/metainfo/%{fontname}-bar.metainfo.xml


%files -n fonts-otf-aftertheflood-sparks-dot
%{_fontconfig_templatedir}/%{fontconf}-dot.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-dot.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Sparks-Dot-*.otf
%{_datadir}/metainfo/%{fontname}-dot.metainfo.xml


%files -n fonts-otf-aftertheflood-sparks-dot-line
%{_fontconfig_templatedir}/%{fontconf}-dot-line.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-dot-line.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Sparks-Dotline-*.otf
%{_datadir}/metainfo/%{fontname}-dot-line.metainfo.xml


%changelog
* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_3
- new version

