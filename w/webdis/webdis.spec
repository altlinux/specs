# vim: set ft=spec: -*- rpm-spec -*-
Name:          webdis
Version:       0.1.20
Release:       alt1
Summary:       A Redis HTTP interface with JSON output
Group:         Networking/Other
License:       BSD-2-Clause
Url:           https://webd.is
Vcs:           https://github.com/nicolasff/webdis.git

Source:        %name-%version.tar
BuildRequires: libevent-devel
BuildRequires: libssl-devel
Source1:       %name.service


%description
A very simple web server providing an HTTP interface to Redis. It uses hiredis,
jansson, libevent, and http-parser.

To build Webdis with support for encrypted connections to Redis, see Building
Webdis with SSL support.


%package       -n %name-devel
Summary:       A Redis HTTP interface with JSON output development package
Summary(ru_RU.UTF-8): Файлы для разработки пакета webdis
Group:         Development/C
BuildArch:     noarch

Requires:      %name = %EVR
Requires:      libevent-devel
Requires:      libssl-devel

%description   -n %name-devel
A Redis HTTP interface with JSON output development package.

A very simple web server providing an HTTP interface to Redis. It uses hiredis,
jansson, libevent, and http-parser.

To build Webdis with support for encrypted connections to Redis, see Building
Webdis with SSL support.

%description   -n %name-devel -l ru_RU.UTF-8
Файлы для разработки пакета webdis.


%prep
%setup

%build
%make_build SSL=1

%install
%makeinstall_std PREFIX=%_prefix

install -Dm 0644 %SOURCE1 %buildroot%_unitdir/%name.service


%files
%_bindir/%name
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/%name.prod.json

%files         -n %name-devel

%changelog
* Mon Feb 13 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.20-alt1
- Initial build in Sisyphus with version 0.1.20
