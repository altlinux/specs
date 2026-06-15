Name:     telemt-panel
Version:  0.6.0
Release:  alt2

Summary:  Control web panel for TeleMT proxy
License:  MIT
Group:    Networking/WWW
Url:      https://github.com/amirotin/telemt_panel
VCS:      https://github.com/amirotin/telemt_panel.git

Packager: Alexei Mezin <alexvm@altlinux.org>
Source:   %name-%version.tar.gz

Summary(ru_RU.UTF-8): Web-панель управления для Telemt MTProxy


#ExclusiveArch: %nodejs_arches
ExclusiveArch: x86_64

BuildRequires(pre): sed
BuildRequires(pre): rpm-macros-golang
BuildRequires(pre): rpm-macros-nodejs
BuildRequires: golang
BuildRequires: npm

%description
Control web panel for TeleMT proxy. You can monitor server state, manage users, control security settings and observe server statistics.

%description -l ru_RU.UTF-8
Web-панель управления для Telemt MTProxy. Позволяет мониторить состояние сервера, управлять пользователями, отслеживать безопасность и просматривать статистику.


%prep
%setup

%build
# Prevent npm from removing vendor files
sed -i 's/&& npm ci//' Makefile
%make_build

%install
install -Dp %name %buildroot/%_bindir/%name
# Fix binary path
sed -i 's/local\///' %name.service
install -D -m 0644 %name.service $RPM_BUILD_ROOT/%_unitdir/%name.service
install -D -m 0644 config.example.toml $RPM_BUILD_ROOT/%_sysconfdir/%name/config.example.toml
install -D -m 0644 docs/CONFIG.md -t %buildroot/%_docdir/%name

%pre
%_sbindir/groupadd -r %name &>/dev/null ||:
%_sbindir/useradd -r -n -M -g %name -d %_localstatedir/%name -s /dev/null %name  &>/dev/null ||:



%files
%_sysconfdir/%name/*
%_bindir/*
%_unitdir/*
%doc %_docdir/%name/*


%changelog
* Tue Jun 16 2026 Alexei Mezin <alexvm@altlinux.org> 0.6.0-alt2
- Build only for x86_64 due to npm vendoring problems

* Mon Jun 15 2026 Alexei Mezin <alexvm@altlinux.org> 0.6.0-alt1
- Initial build


