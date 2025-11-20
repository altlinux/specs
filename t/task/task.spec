%def_with check

Name: task
Version: 3.4.2
Release: alt1

Summary: A command-line todo list manager
License: GPLv2+
Group: Office

Url: https://taskwarrior.org
Vcs: https://github.com/GothenburgBitFactory/taskwarrior.git
Source: %name-%version.tar
Source1: %name-%version-src-libshared.tar
Source2: vendor.tar
Source3: config.toml

Requires: zsh-completion-%name = %version-%release %name-core = %version-%release
# TODO Requires: vim-plugin-syntax

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake libuuid-devel rust-cargo corrosion
%if_with check
BuildRequires: ctest python3
%endif

# Only those two seem to be officially supported
ExclusiveArch: x86_64 aarch64

%description
Task is a command-line todo list manager. It has
support for GTD functionality and includes the
following features: tags, colorful tabular output,
reports and graphs, lots of manipulation commands,
low-level API, abbreviations for all commands and
options, multiuser file locking, recurring tasks.

This package includes zsh completion bindings.
# TODO and new vim stuff

%package core
Group: Office
Summary: Core distribution of taskwarrior
%description core
Task is a command-line todo list manager. It has
support for GTD functionality and includes the
following features: tags, colorful tabular output,
reports and graphs, lots of manipulation commands,
low-level API, abbreviations for all commands and
options, multiuser file locking, recurring tasks.

%package -n zsh-completion-task
Group: Shells
BuildArch: noarch
Summary: Zsh completion for taskwarrior
%description -n zsh-completion-task
Zsh completion for taskwarrior

%prep
%setup -a1 -a2
install -vpD %SOURCE3 .cargo/config.toml
# Check for non-source files
find vendor \( -name '*.a' -o -name '*.lib' -o -name '*.dll' \) | grep . && exit 1

%build
export CARGO_HOME="./.cargo"
%cmake -DSYSTEM_CORROSION=ON
%cmake_build

%install
%cmake_install
%find_lang %name
install -Dm 644 -T scripts/bash/task.sh %buildroot%_sysconfdir/bash_completion.d/task

%check
%cmake_build --target test_runner
%ctest

%files
%_sysconfdir/bash_completion.d/%name

%files core
%doc %_docdir/%name/*
%_bindir/task
%_man1dir/*
%_man5dir/*

%files -n zsh-completion-task
%_datadir/zsh/site-functions/_task

%changelog
* Tue Nov 18 2025 Ilya Sorochan <k0tran@altlinux.org> 3.4.2-alt1
- Update version and return taskwarrior to sisyphus (closes #56210):
  + add libshared git submodule as tag
  + use our packaged corrosion in place of git submodule
  + enable taskchampion build
  + minor spec cleanup

* Thu Feb 01 2024 Michael Shigorin <mike@altlinux.org> 2.5.1-alt4
- NMU:
  + enable parallel build
  + minor spec cleanup

* Sat Apr 25 2020 Kirill Maslinsky <kirill@altlinux.org> 2.5.1-alt3
- fix python shebang

* Tue Mar 29 2016 Denis Medvedev <nbr@altlinux.org> 2.5.1-alt2
- NMU removed test for easter which is wrong for year 2016.

* Thu Mar 03 2016 Kirill Maslinsky <kirill@altlinux.org> 2.5.1-alt1
- 2.5.1

* Sun Jan 11 2015 Kirill Maslinsky <kirill@altlinux.org> 2.4.0-alt1
- 2.4.0

* Sun Jun 08 2014 Kirill Maslinsky <kirill@altlinux.org> 2.3.0-alt1
- 2.1.2 -> 2.3.0

* Mon Nov 12 2012 Fr. Br. George <george@altlinux.ru> 2.1.2-alt2
- Separate zsh completion file
- TODO: separate vim plugins

* Wed Sep 19 2012 Kirill Maslinsky <kirill@altlinux.org> 2.1.2-alt1
- resurrect from orphaned
- version up

* Thu Dec 03 2009 Maxim Ivanov <redbaron at altlinux.org> 1.8.4-alt1
- Version bump

* Tue Sep 15 2009 Maxim Ivanov <redbaron at altlinux.org> 1.8.2-alt1
- Initial build for ALT Linux. Fedora spec adapted.

