Name:     leaf
Version:  1.21.0
Release:  alt1

Summary:  Terminal Markdown previewer - GUI-like experience
License:  MIT
Group:    File tools
Url:      https://github.com/RivoLink/leaf
VCS:      https://github.com/RivoLink/leaf.git

Packager: Alexei Mezin <alexvm@altlinux.org>
Source:   %name-%version.tar.gz
Source1:  README.alt.md

Summary(ru_RU.UTF8): Консольная программа для просмотра markdown-файлов

BuildRequires(pre): rpm-build-rust

%description
leaf lets you read Markdown files directly in the terminal with a clean, focused interface. Designed for developers, CLI users, and AI-assisted workflows.

%description -l ru_RU.UTF-8
leaf позволяет просматривать файлы Markdown непосредственно в терминале, предоставляя простой интерфейс. Создан для разработчиков, пользователей командной строки и интеграци с ИИ.


%prep
%setup
%rust_prep

%build
%rust_build

%install
install -Dp target/release/%name -t %buildroot/%_bindir
install -D -m 0644 config.toml -t %buildroot/%_docdir/%name
install -D -m 0644 README.md -t %buildroot/%_docdir/%name
install -D -m 0644 TESTING.md -t %buildroot/%_docdir/%name
install -D -m 0644 %SOURCE1 -t %buildroot/%_docdir/%name


%files
%_bindir/*
%doc %_docdir/%name/*

%changelog
* Mon May 11 2026 Alexei Mezin <alexvm@altlinux.org> 1.21.0-alt1
- Initial build

