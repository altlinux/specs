Name: templates
Version: 1.0
Release: alt1
Summary: Standard templates for the user directory
Summary(ru_RU.UTF-8): Стандартные шаблоны для каталога пользователя
License: GPLv3
Group: Graphical desktop/Other
Url: http://git.altlinux.org/people/antohami/packages/templates
Source: %name-%version.tar
Packager: Anton Midyukov <antohami@altlinux.org>
BuildArch: noarch

%description
Standard templates for the user directory and the script for automatic
installation template, if template directory user is empty

%description -l ru_RU.UTF-8
Стандартные шаблоны для каталога пользователя и скрипт для автоматической
установки шаблонов в случае, если каталог шаблонов пользователя пуст

%prep
%setup

%build
%install
install -D -m755 templates.sh %buildroot/%_sysconfdir/profile.d/templates.sh
install -d -m755 %buildroot/%_sysconfdir/xdg/autostart/
install -m644 update_templates.desktop.desktop %buildroot/%_sysconfdir/xdg/autostart/
install -d -m755 %buildroot/%_datadir/Templates
install -m644 Templates/* %buildroot/%_datadir/Templates


%files
%_datadir/Templates
%_sysconfdir/profile.d/templates.sh
%_sysconfdir/xdg/autostart/update_templates.desktop.desktop

%changelog
* Fri Sep 04 2015 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- Initial build for ALT Linux Sisyphus.
