%define _unpackaged_files_terminate_build 1

Name:      yadm
Version:   3.2.2
Release:   alt1

Summary:   Yet Another Dotfiles Manager
License:   GPL-3.0
Group:     Development/Tools
URL:       https://yadm.io/
VCS:       https://github.com/TheLocehiliosan/yadm

Source:    %name-%version.tar

Requires:  git

BuildArch: noarch

%description
Yadm is a tool for managing a collection of files across multiple
computers, using a shared Git repository. In addition, yadm provides
a feature to select alternate versions of files based on the operation
system or host name. Lastly, yadm supplies the ability to manage a
subset of secure files, which are encrypted before they are included
in the repository.

%prep
%setup

%build

%install
install -m755 -D %name %buildroot%_bindir/%name
install -m644 -D %name.1 %buildroot%_man1dir/%name.1
install -m644 -D completion/bash/%name %buildroot%_datadir/bash-completion/completions/%name 
install -m644 -D completion/zsh/_%name %buildroot%_datadir/zsh/site-functions/_%name
install -m644 -D completion/fish/%name.fish %buildroot%_datadir/fish/completions/%name.fish

%check

%files
%doc README.md CHANGES CONTRIBUTORS contrib
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/completions/%name.fish
%_man1dir/%name.*

%changelog
* Mon Nov 06 2023 Andrey Limachko <liannnix@altlinux.org> 3.2.2-alt1
- Initial build for Sisyphus.
