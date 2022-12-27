# hash of latest upstream commit
%define commit 73318b639f9f74ba10b7362b40db0b10311f85c8
%define commit_short %(echo %{commit} | head -c 6)

Name: linux-audit-user-run-apps
Summary: Audit which graphical user applications were started and closed by user (LAURA)
Summary(ru_RU.UTF-8): Сбор статистики, какие графические приложения запускал пользователь на Linux (LAURA)
License: GPL-3.0
Group: Graphical desktop/Other
Version: 0
Release: alt0.git%{commit_short}.1
Url: https://github.com/mikhailnov/linux-audit-user-run-apps
Source0: %name-%version.tar
BuildArch: noarch
BuildRequires: make
Requires: audit
Requires: bash
Requires: grep
Requires: procps
Provides: laura = %EVR
Provides: LAURA = %EVR

%description
Audit which graphical user applications were
started and closed by user (LAURA)

%description -l ru_RU.UTF-8
Сбор статистики, какие графические приложения
запускал пользователь на Linux (LAURA)

%prep
%setup -q

%install
%makeinstall_std

%files
%doc LICENSE README.md
%_bindir/laura-started-de
%_sbindir/laura-load-audit
%_unitdir/laura.path
%_unitdir/laura.service
%_sysconfdir/xdg/autostart/laura.desktop

%changelog
* Tue Dec 27 2022 Mikhail Novosyolov <mikhailnov@altlinux.org> 0-alt0.git73318b.1
- Initial build for Sisyphus

