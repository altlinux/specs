Group: System/Fonts/True type
%define oldname polarsys-b612-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname polarsys-b612
%global fontconf 64-%{fontname}
%global gitcommit bd14fde2544566e620eab106eb8d6f2b7fb1347e
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})

%global common_desc \
Commissioned by Airbus and designed by Intactile Design, B612 is a \
digital font intended to be used in an aeronautical context. B612 is \
built with legibility as its core: every character is designed to be \
highly recognizable even in critical reading conditions. B612 drawing \
has been optimized for screen display, and full hinting has been added \
to all sizes of alpha numeric characters.


Name:           fonts-ttf-polarsys-b612
Version:        1.003
Release:        alt1_5.20171129git%{gitshortcommit}
Summary:        A typeface designed for reading comfort and safety in aeroplane cockpits

# README.md explains, "This program and the accompanying materials are
# made available under the terms of the Eclipse Public License v1.0 and
# Eclipse Distribution License v1.0 which accompanies this
# distribution."
License:        EPL and BSD

URL:            https://www.polarsys.org/projects/polarsys.b612
Source0:        https://git.polarsys.org/c/b612/b612.git/snapshot/b612-%{gitcommit}.tar.xz
Source1:        %{fontname}-sans.conf
Source2:        %{fontname}-mono.conf
Source3:        %{fontname}-sans.metainfo.xml
Source4:        %{fontname}-mono.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info


%description
%common_desc



%package -n fonts-ttf-polarsys-b612-common
Group: System/Fonts/True type
Summary:        Common files of B612

%description -n fonts-ttf-polarsys-b612-common
%common_desc

This package consists of files used by other %{oldname} packages.


%files -n fonts-ttf-polarsys-b612-common
%doc README.md
%doc edl-v10.html
%doc epl-v10.html



%package doc
Group: System/Fonts/True type
Summary:        Documentation for B612
BuildArch: noarch

%description doc
%common_desc

This package contains a leaflet explaining the design and production of
the fonts.


%files doc
%doc Goodies/B612-Leaflet.pdf



%package -n fonts-ttf-polarsys-b612-sans
Group: System/Fonts/True type
Summary:        Sans-serif fonts designed for reading comfort and safety in aeroplane cockpits

Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-polarsys-b612-sans
%common_desc

This packages contains a sans serif font family.


%files -n fonts-ttf-polarsys-b612-sans
%{_fontconfig_templatedir}/%{fontconf}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/B612-*.ttf
%{_datadir}/metainfo/org.polarsys.B612-sans.metainfo.xml
# in mono
%exclude %_ttffontsdir/%{_fontstem}/B612-Mono-*.ttf



%package -n fonts-ttf-polarsys-b612-mono
Group: System/Fonts/True type
Summary:        Monospace fonts designed for reading comfort and safety in aeroplane cockpits
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-polarsys-b612-mono
%common_desc

This packages contains a monospace font family.


%files -n fonts-ttf-polarsys-b612-mono
%{_fontconfig_templatedir}/%{fontconf}-mono.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-mono.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/B612-Mono-*.ttf
%{_datadir}/metainfo/org.polarsys.B612-mono.metainfo.xml



%prep
%setup -q -n b612-%{gitcommit}

cd TTF/
for ttf in *\ *.ttf; do
    mv "$ttf" `echo "$ttf" | sed 's/ /-/'`
done
cd -


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p TTF/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir} \
                   %{buildroot}%{_datadir}/metainfo

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mono.conf

for fconf in %{fontconf}-sans.conf \
             %{fontconf}-mono.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/metainfo/org.polarsys.B612-sans.metainfo.xml
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/metainfo/org.polarsys.B612-mono.metainfo.xml
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


%changelog
* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1_5.20171129gitbd14fde
- new version

