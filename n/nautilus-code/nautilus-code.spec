%define _unpackaged_files_terminate_build 1
%define camel_name NautilusCode

Name: nautilus-code
Version: 0.6.alpha
Release: alt1.b6c50d93.1

Summary: Extension which adds right-click menu items to open current folder in code editors
License: AGPL-3.0
Group: Graphical desktop/GNOME
URL: https://github.com/realmazharhussain/nautilus-code
VCS: https://github.com/realmazharhussain/nautilus-code.git

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-gir
BuildRequires: meson

%description
An extension for Nautilus (GNOME Files) File Manager which adds right-click
menu options to open current/selected folder in Code Editors and IDEs like
VSCode or GNOME Builder (if they are installed).

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
%_datadir/nautilus-python/extensions/%camel_name
%_datadir/nautilus-python/extensions/%name.py

%changelog
* Sat Nov 29 2025 Vladimir Romanov <rirusha@altlinux.org> 0.6.alpha-alt1.b6c50d93.1
- Initial build.
