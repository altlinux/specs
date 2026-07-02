Name:     leaf
Version:  1.25.0
Release:  alt1

Summary:  Terminal Markdown previewer with GUI-like experience
License:  MIT
Group:    File tools
Url:      https://leaf.rivolink.mg/
VCS:      https://github.com/RivoLink/leaf.git

Packager: Alexei Mezin <alexvm@altlinux.org>
Source:   %name-%version.tar.gz
Source1:  README.alt.md

Summary(ru_RU.UTF-8): Консольная программа для просмотра markdown-файлов

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
install -Dp target/release/%name %buildroot/%_bindir/%name-markdown-viewer
install -D -m 0644 config.toml -t %buildroot/%_docdir/%name
install -D -m 0644 README.md -t %buildroot/%_docdir/%name
install -D -m 0644 TESTING.md -t %buildroot/%_docdir/%name
install -D -m 0644 %SOURCE1 -t %buildroot/%_docdir/%name
# add bash completion
mkdir -p %buildroot%_sysconfdir/bash_completion.d
sed -i 's/complete -F _leaf leaf/complete -F _leaf leaf-markdown-viewer/' completions/%name.bash
install -p -m 0644 completions/%name.bash %buildroot%_sysconfdir/bash_completion.d/%name-markdown-viewer.bash

%files
%_bindir/*
%doc %_docdir/%name/*
%_sysconfdir/bash_completion.d/*

%changelog
* Fri Jul 03 2026 Alexei Mezin <alexvm@altlinux.org> 1.25.0-alt1
- New version

* Tue Jun 16 2026 Alexei Mezin <alexvm@altlinux.org> 1.24.1-alt1
- New version

* Fri May 29 2026 Alexei Mezin <alexvm@altlinux.org> 1.23.2-alt1
- New version

* Sat May 23 2026 Alexei Mezin <alexvm@altlinux.org> 1.22.3-alt1
- New version

* Fri May 15 2026 Alexei Mezin <alexvm@altlinux.org> 1.22.0-alt2
- Rename main executable to avoid file name conflicts

* Fri May 15 2026 Alexei Mezin <alexvm@altlinux.org> 1.22.0-alt1
- New version

* Mon May 11 2026 Alexei Mezin <alexvm@altlinux.org> 1.21.0-alt1
- Initial build

