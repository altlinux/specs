Name:     ch57x-keyboard-tool
Version:  1.5.4
Release:  alt1

Summary:  This keyboard configuration utility is for programming small keyboards.
License:  MIT
Group:    Development/Tools
Url:      https://github.com/kriomant/ch57x-keyboard-tool
VCS:      https://github.com/kriomant/ch57x-keyboard-tool.git

Packager: Alexei Mezin <alexvm@altlinux.org>
Source:   %name-%version.tar
Source1:  README.alt

Summary(ru_RU.UTF8): Утилита для настройки программируемых мини-клавиатур.
BuildRequires(pre): rpm-build-rust

%description
This keyboard configuration utility is for programming small keyboards. Such macro keyboards 
are popular on AliExpress. Keyboard with following vendor/product IDs are supported: 
1189:8890, 1189:8840, 1189:8842

%description -l ru_RU.UTF8
Утилита для настройки программируемых клавиатур, популярных на Алиэкспресс. Поддерживаются устройства
со следующими идентификаторами:
1189:8890, 1189:8840, 1189:8842



%prep
%setup
%rust_prep

%build
%rust_build

%install
install -Dp target/release/%name -t %buildroot/%_bindir
install -D -m 0644 example-mapping.yaml -t %buildroot/%_docdir/%name
install -D -m 0644 README.md -t %buildroot/%_docdir/%name
install -D -m 0644 %SOURCE1 -t %buildroot/%_docdir/%name


%files
%_bindir/*
%doc %_docdir/%name/*

%changelog
* Fri Nov 07 2025 Alexei Mezin <alexvm@altlinux.org> 1.5.4-alt1
- Initial build

