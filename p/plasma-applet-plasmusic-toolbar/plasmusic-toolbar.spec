%define _unpackaged_files_terminate_build 1
%define nameL plasmusic-toolbar
%define nameLC plasma_applet_plasmusic.toolbar

Name: plasma-applet-%nameL
Version: 4.2.0
Release: alt1

Summary: Plasma widget that shows playing song information and provide controls
License: GPL-3.0-only
Group: Graphical desktop/KDE

Url: https://store.kde.org/p/2128143
Vcs: https://github.com/ccatterina/plasmusic-toolbar

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: gettext-tools

%description
PlasMusic Toolbar is a widget for KDE Plasma 6 that shows currently playing song
information and provide playback controls.

%prep
%setup
mv src/translate %_builddir/%name-%version/

%build
%install
install -d %buildroot%_datadir/plasma/plasmoids/%nameL
cp -r src/* %buildroot%_datadir/plasma/plasmoids/%nameL/

for locale in translate/*.po; do
 dirname=$(basename "$locale" .po)
 mkdir -p %buildroot%_datadir/locale/${dirname}/LC_MESSAGES
 msgfmt -o "%buildroot%_datadir/locale/${dirname}/LC_MESSAGES/%name.mo" "$locale"
done

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSE *.md
%_datadir/plasma/plasmoids/%nameL

%changelog
* Sun Jun 28 2026 Aleksandr Shamaraev <shad@altlinux.org> 4.2.0-alt1
- 4.1.0 -> 4.2.0

* Mon May 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 4.1.0-alt1
- 4.0.0 -> 4.1.0

* Sun Mar 15 2026 Aleksandr Shamaraev <shad@altlinux.org> 4.0.0-alt1
- 3.7.0 -> 4.0.0

* Wed Oct 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.7.0-alt1
- 3.6.0 -> 3.7.0

* Thu Oct 09 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.6.0-alt1
- 3.5.0 -> 3.6.0

* Sat Sep 27 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.5.0-alt1
- 3.4.0 -> 3.5.0

* Fri Aug 29 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.4.0-alt1
- 3.3.0 -> 3.4.0

* Sun Aug 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.3.0-alt1
- 3.2.0 -> 3.3.0

* Wed Jul 23 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.2.0-alt1
- 3.1.0 -> 3.2.0

* Thu Jul 17 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.1.0-alt1
- 3.0.0 -> 3.1.0

* Sun Jun 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.0.0-alt1
- 2.7.0 -> 3.0.0

* Fri Jun 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.7.0-alt1
- 2.6.0 -> 2.7.0

* Sun Jun 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.6.0-alt1
- 2.5.0 -> 2.6.0

* Wed May 28 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.5.0-alt1
- Initial build for ALT Linux.
