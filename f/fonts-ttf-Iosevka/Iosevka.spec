
%define family Iosevka
%define variant %nil
%define descr   monospace, default

%define fname %family%variant
%define dist_dir dist/%fname/TTF

Name:    fonts-ttf-%fname
Version: 33.3.0
Release: alt1

Summary: Versatile typeface for code -- %descr
License: OFL-1.1
Group:   System/Fonts/True type
Url:     https://github.com/be5invis/Iosevka

Packager: Ivan A. Melnikov <iv@altlinux.org>

Source:  %family-%version.tar
Source1: node_modules.tar

Patch:   %family-%version-%release.patch

BuildArch: noarch

# building on one primary architecture is enough
ExcludeArch: %ix86 aarch64

BuildRequires(pre): rpm-macros-fonts >= 0.4
BuildRequires: rpm-macros-fonts >= 0.4
BuildRequires: mkfontscale

BuildRequires: node npm /proc
BuildRequires: ttfautohint

Requires(pre): fontconfig

%description
Iosevka is an open-source multi-variant typeface family, designed
for writing code, using in terminals, and preparing technical documents.

Iosevka is completely generated from its source code.

This package contains Iosevka %variant variant (%descr).
Check out other Iosevka variants, which are packaged separately.

%prep
%setup -a1 -n %family-%version
%patch -p1

%build
(sleep 3500s; echo -e "\nplease wait...\n") &

npm run build -- contents::%fname

%install
pushd %dist_dir
%ttf_fonts_install %fname
popd

%files -f %dist_dir/%fname.files

%changelog
* Wed Sep 17 2025 Ivan A. Melnikov <iv@altlinux.org> 33.3.0-alt1
- Initial build for Sisyphus
