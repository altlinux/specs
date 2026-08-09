%define _unpackaged_files_terminate_build 1

%define apmdodir %_prefix/lib/%name
%define actionsdir %apmdodir/actions
%define useractionsdir %_sysconfdir/%name/actions

Name: apmdo
Version: 0.5.2
Release: alt1

Summary: A tool for configuring the system with ready-made scripts
Summary(ru_RU.UTF-8): Инструмент для настройки системы готовыми сценариями
License: GPL-3.0-or-later
Group: System/Configuration/Other
URL: https://altlinux.space/alt-atomic/apmdo
VCS: https://altlinux.space/alt-atomic/apmdo.git

ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-golang
BuildRequires: golang >= 1.26.0
BuildRequires: meson

%description
apmdo is a tool for running ujust-style actions on ALT Linux (both classic and
atomic). It finds drop-in actions and applies them to a running system
using the built-in apm build engine; it features a full-screen TUI and CLI.

%description -l ru_RU.UTF-8
apmdo — инструмент для выполнения действий в стиле ujust для ALT Linux
(классических и атомарных). Находит drop-in действия и применяет их к
работающей системе встроенным движком сборки apm; есть полноэкранный TUI
и CLI.

%package actions
Summary: Bundled action catalog for apmdo
Summary(ru_RU.UTF-8): Каталог готовых действий для apmdo
Group: System/Configuration/Other
BuildArch: noarch
AutoReq: yes, noshell
Requires: %name = %EVR

%description actions
Ready-made action catalog for apmdo: gaming tweaks, brew, hasher setup,
fonts, git setup and more.

%description actions -l ru_RU.UTF-8
Каталог готовых действий для apmdo: настройки gaming, brew, hasher,
шрифты, git и другие.

%prep
%setup -a1

# Fix go vendoring build: rename "[generated]" files
find -name '*\[generated\]*' -exec rename -v '[generated]' '' {} +

%build
export GOFLAGS="-mod=vendor"
%meson
%meson_build

%install
%meson_install

%files
%_bindir/%name
%dir %apmdodir
%dir %actionsdir
%dir %_sysconfdir/%name
%dir %useractionsdir
%doc README.md README.en.md README.ru.md
%doc LICENSE
%doc examples

%files actions
%actionsdir/*

%changelog
* Sun Aug 09 2026 Dmitry Udalov <udalov@altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus.
