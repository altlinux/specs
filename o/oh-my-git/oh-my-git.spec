%define _unpackaged_files_terminate_build 1
%define _libexec /usr/libexec

Name: oh-my-git
Version: 0.6.5
Release: alt1

Summary: Oh My Git! is an open-source game about learning Git
License: BlueOak-1.0.0
Group: Games/Educational
Url: https://ohmygit.org
Vcs: https://github.com/git-learning-game/oh-my-git.git
ExcludeArch: aarch64

BuildRequires: godot
BuildRequires: godot-runner
BuildRequires: xvfb-run
BuildRequires: libpulseaudio
BuildRequires: libalsa

Source0: %name-%version.tar
Patch0: 0001-Remove-zip-archive-creation-alt-patch.patch 

%description
Oh My Git! is an open-source game about learning Git. Oh My Git!
visualizes the internal structures of Git repositories in realtime.
The player can immediately see the results of their actions.
To accommodate people who are new to Git, the game features a
custom-designed playing card interface! The cards help remember
newly introduced Git commands, but also contain a short description
and an icon. Therefore, they combine both action as well as
documentation.

%prep
%setup
%autopatch -p1

%define godot_version %(godot --version | sed 's/\.alt[0-9]*$//')

mkdir -p ~/.local/share/godot3/templates/%godot_version

ln -s $(which godot-runner) \
  ~/.local/share/godot3/templates/%godot_version/linux_x11_64_release

%build
LIBGL_ALWAYS_SOFTWARE=1 xvfb-run -s "+extension GLX" %make_build linux

%install
install -d %buildroot%_gamesbindir
install -d %buildroot%_desktopdir

install -Dm 755 build/oh-my-git-linux/oh-my-git \
  -t %buildroot%_libexec/oh-my-git

install -Dm 644 images/oh-my-git.png \
  -t %buildroot%_iconsdir/hicolor/48x48/apps

install -m 644 build/oh-my-git-linux/oh-my-git.pck \
  %buildroot%_libexec/oh-my-git

ln -s %_libexec/oh-my-git/oh-my-git \
  -t %buildroot%_gamesbindir

cat > %buildroot%_desktopdir/oh-my-git.desktop << EOF
[Desktop Entry]
Name=Oh My Git!
GenericName=Oh My Git!
Comment=Interactive game about learning git
Exec=%_gamesbindir/oh-my-git
Icon=oh-my-git
Terminal=false
Type=Application
Categories=Game;Educational;
EOF

%files
%doc README.md LICENSE.md
%_gamesbindir/oh-my-git
%_libexec/oh-my-git
%_iconsdir/hicolor/48x48/apps/oh-my-git.png
%_desktopdir/oh-my-git.desktop

%changelog
* Mon Sep 15 2025 Fedor Moseichuck <phobos@altlinux.org> 0.6.5-alt1
- Initial build for Alt Linux.
