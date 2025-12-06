
%define family Iosevka
%define variant TermSS18
%define descr   Input Mono style, Term spacing

%define fname %family%variant
%define dist_dir dist/%fname/TTF
%define src_version %{get_version %family-source}
%define src_release %{get_release %family-source}


Name:    fonts-ttf-%fname
Version: %src_version
Release: %src_release

Summary: Versatile typeface for code -- %descr
License: OFL-1.1
Group:   System/Fonts/True type
URL:     https://typeof.net/Iosevka/
Vcs:     https://github.com/be5invis/Iosevka.git

Packager: Ivan A. Melnikov <iv@altlinux.org>

BuildArch: noarch

# building on one primary architecture is enough
ExcludeArch: %ix86 aarch64

BuildRequires(pre): rpm-macros-fonts >= 0.4
BuildRequires(pre): Iosevka-source

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
%setup -cT
tar --strip-components 1 -xvf %_usrsrc/%family/%family-%src_version.tar
tar -xvf  %_usrsrc/%family/node_modules.tar
patch -p1 < %_usrsrc/%family/%family-%src_version-%src_release.patch

%build
(sleep 3500s; echo -e "\nplease wait...\n") &

npm run build -- ttf::%fname

%install
pushd %dist_dir
%ttf_fonts_install %fname
popd

%files -f %dist_dir/%fname.files

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- %src_version

* Thu Dec 04 2025 Ivan A. Melnikov <iv@altlinux.org> 33.3.5-alt0.1
- Build from a separated source package

* Wed Sep 17 2025 Ivan A. Melnikov <iv@altlinux.org> 33.3.0-alt1
- Initial build for Sisyphus
