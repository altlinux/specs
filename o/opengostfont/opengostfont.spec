Name: opengostfont
Version: 0.3
Release: alt4

Summary: Open-source version of the fonts by Russian standard GOST 2.304-81
License: OFL-1.1
Group: System/Fonts/True type
Url: https://bitbucket.org/fat_angel/opengostfont
Source: %name-src-%version.tar.xz
Patch: opengostfont-python3.diff

BuildArch: noarch
# Automatically added by buildreq on Tue Sep 04 2012
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings xz
BuildRequires: libfontforge-devel python3-module-fontforge

BuildRequires: rpm-build-fonts

Requires: fonts-ttf-opengost = %version, fonts-otf-opengost = %version

%description
Open-source version of the fonts by Russian standard
GOST 2.304-81 "Letters for drawings"

%package -n fonts-ttf-opengost
Group: System/Fonts/True type
Summary: True Type version of the fonts by Russian standard GOST 2.304-81
Provides: opengostfont

%description -n fonts-ttf-opengost
True Type open-source version of the fonts by Russian standard
GOST 2.304-81 "Letters for drawings"

%package -n fonts-otf-opengost
Group: System/Fonts/True type
Summary: Open Type version of the fonts by Russian standard GOST 2.304-81

%description -n fonts-otf-opengost
Open Type open-source version of the fonts by Russian standard
GOST 2.304-81 "Letters for drawings"

%prep
%setup -n %name-src-%version
%patch -p1

%build
make all

%install
( cd %name-ttf-%version && {
%ttf_fonts_install openfont
} || exit 1 )
( cd %name-otf-%version && {
%otf_fonts_install openfont
} || exit 1 )

%files -n fonts-ttf-opengost -f %name-ttf-%version/openfont.files
%doc LICENSE

%files -n fonts-otf-opengost -f %name-otf-%version/openfont.files
%doc LICENSE

%changelog
* Tue Aug 23 2022 Fr. Br. George <george@altlinux.org> 0.3-alt4
- Remove metapackage (Closes: #42464)

* Sat Apr 25 2020 Fr. Br. George <george@altlinux.ru> 0.3-alt3
- Switch to python3

* Mon Jan 13 2020 Fr. Br. George <george@altlinux.ru> 0.3-alt2
- Remove FontConfig

* Tue Sep 04 2012 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Autobuild version bump to 0.3

