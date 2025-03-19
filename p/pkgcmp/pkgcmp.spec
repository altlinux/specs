Name:    pkgcmp
Version: 0.2.1
Release: alt1

Summary: A utility for comparing lists of RPM packages
Summary(ru_RU.UTF-8): Утилита для сравнения списков RPM пакетов
License: MIT
Group:   Development/Tools
URL:     https://github.com/username/pkgcmp

Source0: %name-%version.tar

BuildRequires: rust-cargo /proc
BuildRequires: rust >= 1.70

%description
A utility for comparing lists of RPM packages.
Shows differences in package composition and their versions.
Supports output of additional information about packages from the database.

%description -l ru_RU.UTF-8
Утилита командной строки для сравнения двух списков RPM пакетов.
Показывает различия в составе пакетов и их версиях.
Поддерживает вывод дополнительной информации о пакетах из базы данных.

%prep
%setup -q

%build
cargo build --release

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/%name
install -pm755 target/release/%name %buildroot%_bindir/
install -pm644 repo.csv %buildroot%_datadir/%name/
install -pm644 report_template.html %buildroot%_datadir/%name/

%files
%doc README.md
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/repo.csv
%_datadir/%name/report_template.html

%changelog
* Wed Mar 19 2025 Leontiy Volodin <lvol@altlinux.org> 0.2.1-alt1
- Initial build for ALT Sisyphus (by Andrey Semenow aka trefas@).

