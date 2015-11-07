Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%define oldname oxygen-fonts
%global fontname oxygen
%global fontconf 61-%{fontname}

Name:           fonts-ttf-oxygen
Version: 5.4.3
Release: alt1_1
Summary:        Oxygen fonts created by the KDE Community

# See LICENSE-GPL+FE for details about the exception
License:        OFL or GPLv3 with exceptions
URL:            http://www.kde.org
Source0:        http://download.kde.org/stable/plasma/%{version}/%{oldname}-%{version}.tar.xz
Source1:        %{fontconf}-sans.conf
Source2:        %{fontconf}-mono.conf

# essentially a noarch pkg here, no real -debuginfo needed (#1192729)
%define debug_package   %{nil}

BuildRequires: ctest cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-base-devel
BuildRequires:  fontforge
BuildRequires:  fontpackages-devel

# main (meta)package, largely for upgrade path
Requires: fonts-ttf-oxygen-mono = %{version}-%{release}
Requires: fonts-ttf-oxygen-sans = %{version}-%{release}
Source44: import.info

%description
Oxygen fonts created by the KDE Community.

%package -n fonts-ttf-oxygen-common
Group: System/Fonts/True type
Summary:        Common files for Oxygen font
BuildArch:      noarch
%description    -n fonts-ttf-oxygen-common
%{summary}.

%package -n fonts-ttf-oxygen-mono
Group: System/Fonts/True type
Summary:        Oxygen Monospaced Font
Requires:       fonts-ttf-oxygen-common = %{version}-%{release}
BuildArch:      noarch
%description    -n fonts-ttf-oxygen-mono
%{summary}.

%package -n fonts-ttf-oxygen-sans
Group: System/Fonts/True type
Summary:        Oxygen Sans-Serif Font
Requires:       fonts-ttf-oxygen-common = %{version}-%{release}
BuildArch:      noarch
%description    -n fonts-ttf-oxygen-sans
%{summary}.

%package devel
Group: System/Fonts/True type
Summary:        Development files for %{oldname}
Requires:       fonts-ttf-oxygen = %{version}-%{release}
%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.


%prep
%setup -q -n %{oldname}-%{version}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{fedora_cmake} .. %{?fontforge} -DOXYGEN_FONT_INSTALL_DIR=%{_fontdir}
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mono.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}-sans.conf \
      %{buildroot}/%{_fontconfig_confdir}/%{fontconf}-sans.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}-mono.conf \
      %{buildroot}/%{_fontconfig_confdir}/%{fontconf}-mono.conf
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

%files -n fonts-ttf-oxygen-sans
%{_fontconfig_templatedir}/%{fontconf}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans.conf
%{_fontbasedir}/*/%{_fontstem}/Oxygen-Sans*.ttf
%files -n fonts-ttf-oxygen-mono
%{_fontconfig_templatedir}/%{fontconf}-mono.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-mono.conf
%{_fontbasedir}/*/%{_fontstem}/OxygenMono*.ttf

%files
# empty metapackage

%files -n fonts-ttf-oxygen-common
%doc COPYING-GPL+FE.txt COPYING-OFL GPL.txt README.md

%files devel
%{_libdir}/cmake/OxygenFont/

%changelog
* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 5.4.3-alt1_1
- new version

