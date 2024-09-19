%define _unpackaged_files_terminate_build 1

Name: alteratorctl
Version: 0.0.5
Release: alt1

Summary: CLI for alterator browser
License: GPL-2
Group: System/Configuration/Other

BuildRequires: cmake gcc glib2-devel libdbus-glib-devel libgio-devel
#BuildRequires: complgen

Source0: %name-%version.tar

%description
A command line tool for using DBus objects

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

#complgen aot --bash-script %name.bash %name.usage
#complgen aot --zsh-script  %name.zsh  %name.usage
#complgen aot --fish-script %name.fish %name.usage

%install
%cmakeinstall_std

#install -Dm 0644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
#install -Dm 0644 %name.zsh  %buildroot%_datadir/zsh/site-functions/_%name
#install -Dm 0644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%_bindir/%name
%_datadir/alteratorctl/lang/ru/LC_MESSAGES/%name.mo

#%_datadir/bash-completion/completions/%name
#%_datadir/zsh/site-functions/_%name
#%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Mon Sep 16 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.5-alt1
- implement Alterator Entry parsing
- add diag module

* Thu Aug 22 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.4-alt1
- add common method
- refactor internal client modules to check objects and interfaces
- locale fix
- add translations

* Wed Jul 31 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.3-alt1
- refactor manager module
- implement diag module

* Tue Jul 23 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.2-alt1
- implement manager, packages and components modules

* Sun Jun 02 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.1-alt1
- initial build
