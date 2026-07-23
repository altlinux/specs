%define _unpackaged_files_terminate_build 1
%define prog_name samba-tool
Name: bash-completion-samba-tool
Version: 0.2
Release: alt1

Summary: Bash completion for samba-tool
License: GPLv3
Group: System/Servers
URL: https://altlinux.space/alt-domain/bash-completion-samba-tool

Provides: samba-tool-autocompletion = %version-%release
Obsoletes: samba-tool-autocompletion < %version-%release

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator

%description
Bash completion for samba-tool

%prep
%setup

%install
install -pDm 644 completions/%prog_name.completion \
     %buildroot%_datadir/bash-completion/completions/%prog_name

%files
%_datadir/bash-completion/completions/%prog_name

%changelog
* Sat Jun 13 2026 Evgenii Sozonov <arzdez@altlinux.org> 0.2-alt1
- Rename package
- Fix completion for options with values

* Tue Jun 09 2026 Evgenii Sozonov <arzdez@altlinux.org> 0.1-alt1
- Initial commit
