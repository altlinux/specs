Name: pspg
Version: 3.0.4
Release: alt1

Summary: A unix pager optimized for psql

License: BSD-2-Clause
Group: Development/Tools
Url: https://github.com/okbob/pspg

Packager: Maxim Knyazev <mattaku@altlinux.org>

Source: %name-%version.tar

BuildRequires: libncursesw-devel
BuildRequires: libreadline-devel
BuildRequires: postgresql-devel

%description
pspg is a unix pager optimized for psql. It can freeze rows, freeze
columns, and lot of color themes are included.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc README.md LICENSE
%_bindir/*

%changelog
* Wed Apr 15 2020 Maxim Knyazev <mattaku@altlinux.org> 3.0.4-alt1
- Initial build to Sisyphus
