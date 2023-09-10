# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

#%%def_disable check

Name: chirp
Version: 20230906
Release: alt1
Summary: A tool for programming two-way radio equipment

Group: Communications
License: GPLv3+
Url: https://github.com/kk7ds/chirp

Source: %name-%version.tar
Patch: %name-%version-alt.diff

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_disabled check
%else
BuildRequires: python3(future)
BuildRequires: python3(libxml2)
BuildRequires: python3(requests)
BuildRequires: python3(serial)
BuildRequires: python3(suds)
BuildRequires: python3(wx)
BuildRequires: python3(yattag)
%endif

# for Radio -> Query Source
%py3_requires suds

# for build translations
BuildRequires: /proc

%description
Chirp is a tool for programming two-way radio equipment
It provides a generic user interface to the programming
data and process that can drive many radio models under
the hood.

%prep
%setup
%patch -p1

%build
%pyproject_build

# build translations
pushd chirp/locale/
make
popd

%install
%pyproject_install

# Desktop file
mkdir -p %buildroot%_datadir/applications

cat>%buildroot%_datadir/applications/%name.desktop<<EOF
[Desktop Entry]
Name=Chirp
GenericName=chirp
Exec=chirp
Icon=chirp
Terminal=false
Type=Application
Categories=AudioVideo;Audio;HamRadio;
Comment=CHIRP Radio Programming Tool
EOF

# Icon
mkdir -p %buildroot/%_iconsdir/hicolor/scalable/apps
cp -f chirp/share/chirp.svg %buildroot/%_iconsdir/hicolor/scalable/apps/chirp.svg

# Install translations
mkdir -p %buildroot/%_datadir/locale
find chirp/locale -type d -mindepth 1 -maxdepth 1 -exec cp -r {} %buildroot/%_datadir/locale \;
%find_lang CHIRP

%check
%tox_check

%files -f CHIRP.lang
%doc README.md
%_bindir/*
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-0.dist-info/
%_datadir/applications/%name.desktop
%_iconsdir/hicolor/scalable/apps/chirp.svg

%changelog
* Thu Sep 07 2023 Anton Midyukov <antohami@altlinux.org> 20230906-alt1
- new snapshot
- echable check
- fix localedir
- do not require importlib-resources

* Wed May 24 2023 Anton Midyukov <antohami@altlinux.org> 20230514-alt2
- Add desktop file and icon
- Add translations

* Wed May 24 2023 Anton Midyukov <antohami@altlinux.org> 20230514-alt1
- new snapshot

* Thu Feb 09 2023 Stanislav Levin <slev@altlinux.org> 20221229-alt2
- Fixed FTBFS (setuptools 66).

* Thu Dec 29 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 20221229-alt1
- revived chirp (from upstream py3 branch snapshot)

* Mon Jul 30 2018 Anton Midyukov <antohami@altlinux.org> 20180707-alt1
- new version (20180707) with rpmgs script

* Tue Nov 14 2017 Anton Midyukov <antohami@altlinux.org> 20171104-alt1
- Initial build for ALT Sisyphus.
