%define git 1e158fb

Name: xss-lock
Version: 0.3.0
Release: alt1.g%{git}
Summary: Use external locker as X screen saver

Group: Graphical desktop/Other
License: MIT
Url: https://bitbucket.org/raymonad/xss-lock
Source0: https://bitbucket.org/raymonad/%name/get/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): cmake
BuildRequires: gcc glib2-devel libgio-devel libxcb-devel python3-module-docutils 
BuildRequires: libxcbutil-devel bash-completion zsh-completions

%description
xss-lock hooks up your favorite locker to the MIT screen saver extension for
X and also to systemd's login manager.

%package -n bash-completion-%name
Summary: bash completion for %name
Group: Shells
BuildArch: noarch
Requires: %name = %EVR

%description -n bash-completion-%name
bash completion functions for %name

%package -n zsh-completion-%name
Summary: zsh completions for %name
Group: Shells
BuildArch: noarch
Requires: %name = %EVR

%description -n zsh-completion-%name
zsh completion functions for %name

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/xss-lock
%_man1dir/*
%doc NEWS LICENSE
%doc doc/dim-screen.sh
%doc doc/transfer-sleep-lock-generic-delay.sh
%doc doc/transfer-sleep-lock-i3lock.sh
%doc doc/xdg-screensaver.patch

%files -n bash-completion-%name
%_datadir/bash-completion/completions/*

%files -n zsh-completion-%name
%_datadir/zsh/site-functions/*

%changelog
* Wed Jun 02 2021 L.A. Kostis <lakostis@altlinux.ru> 0.3.0-alt1.g1e158fb
- Initial build for ALTLinux.
- .spec based on FC package.
