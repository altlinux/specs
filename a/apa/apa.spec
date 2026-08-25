%define _unpackaged_files_terminate_build 1

Name: apa
Version: 0.2
Release: alt1

Summary: An assistant for working with packages in your ALT distros
License: GPL-3.0-or-later
Group: System/Configuration/Packaging
Url: https://altlinux.space/alt-gnome/apa
VCS: https://altlinux.space/alt-gnome/apa.git

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(libapi-base-7)

%description
An assistant for working with packages in your ALT distros.

Use `apa help` for more information.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name

%changelog
* Tue Aug 25 2026 Vladimir Romanov <rirusha@altlinux.org> 0.2-alt1
- New version 0.2.
- Dropped everything except search-file command.

* Fri Sep 05 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.1.8.alpha-alt2
- Fixed build with newer libapi-base version

* Tue Feb 4 2025 Alexey Volkov <qualimock@altlinux.org> 0.1.8.alpha-alt1
- New version 0.1.8.alpha (closes: #52652, #52654)

* Fri Jan 3 2025 Alexey Volkov <qualimock@altlinux.org> 0.1.7.alpha-alt1
- New version 0.1.7.alpha (closes: #52430, #52499, #52555, #52566)

* Tue Dec 17 2024 Alexey Volkov <qualimock@altlinux.org> 0.1.4.alpha-alt1
- New version 0.1.4.alpha (closes: #52447)

* Sat Dec 14 2024 Alexey Volkov <qualimock@altlinux.org> 0.1.0.alpha-alt1
- Initial build for ALT
