Name: nnn
Version: 3.3
Release: alt1

Summary: A full-featured terminal file manager.
License: BSD-2-Clause and BSD-3-Clause
Group: File tools

Packager: Andrew A. Vasilyev <andy@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: libreadline-devel libncurses-devel libncursesw-devel

%description
nnn (or n^3) is a full-featured terminal file manager.
It's tiny and nearly 0-config with an incredible performance.

%prep
%setup

%build
%make_build

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
%_datadir/bash-completion/completions/%name

%changelog
* Tue Jul 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.3-alt1
- 3.2 -> 3.3

* Tue Jun 09 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.2-alt2
- Install desktop file.
- Change application group.
- Install bash completions.

* Mon Jun 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.2-alt1
- Initial build fot ALT.

