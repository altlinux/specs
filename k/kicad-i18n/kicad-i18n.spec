Summary: Translations for kicad
Name: kicad-i18n
Version: 4.0.5
Release: alt1
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
License: GPLv2+
Group: Sciences/Computer science
Url: https://github.com/KiCad/kicad-i18n
BuildArch: noarch
BuildRequires(pre): cmake rpm-macros-cmake

%description
Translations for kicad

%prep
%setup -n %name-%version

%build
%cmake -DKICAD_I18N_UNIX_STRICT_PATH=ON ..
%make_build -C BUILD

%install
%makeinstall_std -C BUILD
%find_lang kicad

%files -f kicad.lang

%changelog
* Wed Feb 22 2017 Anton Midyukov <antohami@altlinux.org> 4.0.5-alt1
- new version 4.0.5

* Wed Aug 31 2016 Anton Midyukov <antohami@altlinux.org> 4.0.4-alt1
- New version 4.0.4

* Thu Jul 21 2016 Anton Midyukov <antohami@altlinux.org> 4.0.2-alt1
- First build for ALT Linux Sisyphus.
