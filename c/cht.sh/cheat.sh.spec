%define _unpackaged_files_terminate_build 1

Name:      cht.sh
Version:   0
Release:   alt1.git571377f2

Summary:   CLI client for cheat.sh (cheat sheets repositories aggregator)
License:   MIT
Group:     Other
URL:       https://cheat.sh
VCS:       https://github.com/chubin/cheat.sh

Source:    %name-%version.tar
Patch:     %name-%version-%release-alt.patch

BuildArch: noarch

%description
Unified access to the best community driven cheat sheets repositories of the world.

%prep
%setup
%patch -p1

%build

%install
install -m755 -D share/cht.sh.txt %buildroot%_bindir/%name
install -m644 -D share/bash_completion.txt %buildroot%_datadir/bash-completion/completions/%name
install -m644 -D share/zsh.txt %buildroot%_datadir/zsh/site-functions/_%name
install -m644 -D share/fish.txt %buildroot%_datadir/fish/completions/%name.fish

%check

%files
%doc README.md
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/completions/%name.fish

%changelog
* Wed Nov 29 2023 Andrey Limachko <liannnix@altlinux.org> 0-alt1.git571377f2
- Initial build for Sisyphus.
