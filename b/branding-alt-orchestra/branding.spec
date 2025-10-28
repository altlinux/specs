%define brand alt
%define Brand ALT
%define theme orchestra
%define Theme Orchestra
%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch sisyphus
%endif
%define status %nil
%define status_en %nil
%define flavour %brand-%theme

%define data_cur_dir %_datadir/branding-data-current

%define _unpackaged_files_terminate_build 1

Name: branding-%flavour
Version: 0.1
Release: alt1
Url: https://packages.altlinux.org/en/sisyphus/srpms/branding-alt-orchestra/

BuildRequires(pre): rpm-macros-branding
BuildRequires: libalternatives-devel

BuildRequires: ImageMagick fontconfig bc

BuildRequires: distro-licenses >= 1.4.0

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPL-2.0-or-later

%define distro_name ALT Orchestra

%description
Distro-specific packages with design and texts for %distro_name.

%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release

%package release
BuildArch: noarch
Summary:  %distro_name release file
License:  GPL-2.0-or-later
Group:    System/Configuration/Other
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release
Obsoletes: %obsolete_list
%branding_add_conflicts %flavour release
Conflicts: altlinux-release-%altbranch
Requires: alt-os-release

%description release
%distro_name release file.

%package notes
BuildArch: noarch
Provides:  alt-license-theme = %version alt-notes-%theme
Obsoletes: alt-license-%theme alt-notes-%theme
Summary:   Distribution license and release notes
License:   Distributable
Group:     Documentation
%branding_add_conflicts %flavour notes

%description notes
Distribution license and release notes

%prep
%setup -n branding
mkdir -p notes
cp /usr/share/distro-licenses/ALT_Orchestra_License/license.all.html.in notes/license.all.html.in
cp /usr/share/distro-licenses/ALT_Orchestra_License/license.ru.html.in notes/license.ru.html.in

%build
autoconf
THEME=%theme NAME='%Brand %Theme' BRAND_FNAME='%brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME='%distro_name' BRANCH='%altbranch' ./configure
#make

%install
%makeinstall
find %buildroot -name \*.in -delete

#notes
%post notes
if ! [ -e %_datadir/alt-notes/license.all.html ]; then
	cp -a %data_cur_dir/alt-notes/license.*.html %_datadir/alt-notes/
fi

%files release
%_sysconfdir/buildreqs/packages/ignore.d/*
%_sysconfdir/*-release
%prefix/lib/os-release

%files notes
%dir %data_cur_dir
%data_cur_dir/alt-notes
%ghost %config(noreplace) %_datadir/alt-notes/license.*.html

%changelog
* Thu Oct 23 2025 Nadezhda Fedorova <fedor@altlinux.org> 0.1-alt1
- Initial build.
