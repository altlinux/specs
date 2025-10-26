%define _unpackaged_files_terminate_build 1

%def_with check

Name: bash-preexec
Version: 0.6.0
Release: alt1

Summary: preexec and precmd functions for Bash just like Zsh

License: MIT
Group: Shells

BuildArch: noarch

Url: https://github.com/rcaloras/bash-preexec

# Source-url: https://github.com/rcaloras/bash-preexec/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

%if_with check
BuildRequires: bats
# /dev/fd/63: No such file or directory
BuildRequires: /proc
%endif

%description
preexec and precmd hook functions for Bash 3.1+ in the style of Zsh. They aim to
emulate the behavior as described for}

%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/bash-preexec
install -pm 644 bash-preexec.sh %buildroot%_libexecdir/bash-preexec/

mkdir -p %buildroot%_sysconfdir/bashrc.d/
cat > %buildroot%_sysconfdir/bashrc.d/bash-preexec.sh <<EOF
# bash-preexec initialization script

# Skip non-bash shells.
[ -z "\${BASH_VERSION-}" ] && return

# Skip noninteractive shells.
[[ \$- != *i* ]] && return

source %_libexecdir/bash-preexec/bash-preexec.sh
EOF

%check
bats test

%files
%dir %_libexecdir/bash-preexec
%_libexecdir/bash-preexec/bash-preexec.sh
%config(noreplace) %_sysconfdir/bashrc.d/*
%doc LICENSE.md
%doc README.md

%changelog
* Sun Oct 26 2025 Boris Yumankulov <boria138@altlinux.org> 0.6.0-alt1
- initial build for ALT Sisyphus

