%define brand alt
%define Brand ALT
%define theme container
%define Theme Container
%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch sisyphus
%endif
%define status %nil
%define status_en %nil
%define flavour %brand-%theme

%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

%define data_cur_dir %_datadir/branding-data-current

%define _unpackaged_files_terminate_build 1

Name: branding-%flavour
Version: 11
Release: alt1
Url: https://packages.altlinux.org/en/sisyphus/srpms/branding-alt-container/

BuildRequires(pre): rpm-macros-branding
BuildRequires: libalternatives-devel
#BuildRequires: qt5-base-devel

BuildRequires: ImageMagick fontconfig bc

BuildRequires: distro-licenses >= 1.3.7

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPL-2.0-or-later

%define distro_name ALT Container
%define distro_name_ru Альт Контейнер

%description
Distro-specific packages with design and texts for %distro_name.

%description -l ru_RU.UTF-8
Пакеты оформления для дистрибутива %distro_name_ru.

%package graphics
Summary: Design for %distro_name
Summary(ru_RU.UTF-8): Тема для дистрибутива %distro_name_ru
License: Different licenses
Group: Graphics
BuildArch: noarch
Provides: design-graphics-%theme  branding-alt-%theme-graphics
Obsoletes: design-graphics-%theme
Provides: design-graphics = %design_graphics_abi_major.%design_graphics_abi_minor.%design_graphics_abi_bugfix

Requires(post,preun): alternatives >= 0.2
%branding_add_conflicts %flavour graphics

%description graphics
This package contains some graphics for %distro_name design.

%description graphics -l ru_RU.UTF-8
В данном пакете находится необходимые графические элементы для дистрибутива 
%distro_name_ru.

%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release

%package release
BuildArch: noarch
Summary:  %distro_name release file
Summary(ru_RU.UTF-8): Описание дистрибутива %distro_name_ru
License:  GPL-2.0-or-later
Group:    System/Configuration/Other
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release
Obsoletes: %obsolete_list
%branding_add_conflicts %flavour release
Conflicts: altlinux-release-%altbranch
Requires: alt-os-release

%description release
%distro_name release file.

%description release -l ru_RU.UTF-8
В данном пакете находится описание дистрибутива %distro_name_ru.

%package notes
BuildArch: noarch
Provides:  alt-license-theme = %version alt-notes-%theme
Obsoletes: alt-license-%theme alt-notes-%theme
Summary:   Distribution license and release notes
Summary(ru_RU.UTF-8): Лицензия и дополнительные сведения для дистрибутива %distro_name_ru
License:   Distributable
Group:     Documentation
%branding_add_conflicts %flavour notes

%description notes
Distribution license and release notes

%description notes -l ru_RU.UTF-8
В данном пакете находится лицензия и дополнительные сведения
для дистрибутива %distro_name_ru.

%prep
%setup -n branding
mkdir -p notes
cp /usr/share/distro-licenses/ALT_Container_License/license.all.html notes/license.all.html.in
cp /usr/share/distro-licenses/ALT_Container_License/license.ru.html notes/license.ru.html.in

%build
autoconf
THEME=%theme NAME='%Brand %Theme' BRAND_FNAME='%brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME_RU='%distro_name_ru' PRODUCT_NAME='%distro_name' BRANCH='%altbranch' ./configure
make

%install
%makeinstall
find %buildroot -name \*.in -delete

#notes
%post notes
if ! [ -e %_datadir/alt-notes/license.all.html ]; then
	cp -a %data_cur_dir/alt-notes/license.*.html %_datadir/alt-notes/
fi

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design
#_iconsdir/hicolor/*/apps/alt-%theme.png

%files release
%_sysconfdir/buildreqs/packages/ignore.d/*
%_sysconfdir/*-release
%prefix/lib/os-release

%files notes
%dir %data_cur_dir
%data_cur_dir/alt-notes
%ghost %config(noreplace) %_datadir/alt-notes/license.*.html

%changelog
* Tue Oct 22 2024 Anton Midyukov <antohami@altlinux.org> 11-alt1
- bump version

* Tue Sep 17 2024 Anton Midyukov <antohami@altlinux.org> 10-alt1
- Initial build
