# BEGIN SourceDeps(oneline):
BuildRequires: libncurses-devel
# END SourceDeps(oneline)
Name: pspg
Version: 5.8.16
Release: alt1

Summary: A unix pager optimized for psql

License: BSD-2-Clause
Group: Development/Tools
Url: https://github.com/okbob/pspg

Source: %name-%version.tar

BuildRequires: libncursesw-devel
BuildRequires: libreadline-devel
BuildRequires: libpq-devel

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
* Wed May 06 2026 Alexei Takaseev <taf@altlinux.org> 5.8.16-alt1
- 5.8.16
- Change BR postgresql-devel -> libpq-devel

* Fri Aug 25 2023 Igor Vlasenko <viy@altlinux.org> 3.0.4-alt2
- NMU: fixed build

* Wed Apr 15 2020 Maxim Knyazev <mattaku@altlinux.org> 3.0.4-alt1
- Initial build to Sisyphus
