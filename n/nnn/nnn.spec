%def_enable qsort

Name: nnn
Version: 3.5
Release: alt2

Summary: A full-featured terminal file manager
License: BSD-2-Clause and BSD-3-Clause
Group: File tools

Packager: Andrew A. Vasilyev <andy@altlinux.org>

Url: https://github.com/jarun/nnn
Vcs: https://github.com/jarun/nnn.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: libreadline-devel libncurses-devel libncursesw-devel

Requires: icon-theme-hicolor

%description
Nnn (or n^3) is a full-featured terminal file manager.
It's tiny and nearly 0-config with an incredible performance.

%prep
%setup

%build
%make_build %{?_enable_qsort:O_QSORT=1}

%install
%make_install DESTDIR=%buildroot PREFIX=/usr install install-desktop
install -D -m644 misc/auto-completion/bash/nnn-completion.bash \
    %buildroot%_datadir/bash-completion/completions/%name

%files
%doc LICENSE README.md
%_bindir/*
%_man1dir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%dir %_datadir/bash-completion
%dir %_datadir/bash-completion/completions
%_datadir/bash-completion/completions/%name

%changelog
* Sun Feb 07 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.5-alt2
- fix hicolor directories

* Tue Nov 17 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.5-alt1
- 3.4 -> 3.5
- enable Alexey Tourbin's QSORT macro

* Tue Aug 18 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.4-alt1
- 3.3 -> 3.4

* Tue Jul 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.3-alt1
- 3.2 -> 3.3

* Tue Jun 09 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.2-alt2
- Install desktop file.
- Change application group.
- Install bash completions.

* Mon Jun 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.2-alt1
- Initial build fot ALT.

