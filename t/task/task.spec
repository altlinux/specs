Name:           task
Version:        2.5.1
Release:        alt1
Summary:        A command-line todo list manager

Group:          Office
License:        GPLv2+
URL:            http://taskwarrior.org
Source0:        %name-%version.tar
Packager:	Kirill Maslinsky <kirill@altlinux.org>
Patch0:		%name-%version-%release.patch

Requires: zsh-completion-%name = %version-%release %name-core = %version-%release
# TODO Requires: vim-plugin-syntax

BuildRequires(pre): rpm-macros-cmake
BuildRequires:  gcc-c++ libncurses-devel cmake libuuid-devel perl-devel libgnutls-devel python-devel

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
Group:		Office
Summary:	Core distribution of taskwarrior
%description core
Task is a command-line todo list manager. It has
support for GTD functionality and includes the
following features: tags, colorful tabular output,
reports and graphs, lots of manipulation commands,
low-level API, abbreviations for all commands and
options, multiuser file locking, recurring tasks.

%package -n zsh-completion-task
Group:		Shells
BuildArch:	noarch
Summary: Zsh completion for taskwarrior
%description -n zsh-completion-task
Zsh completion for taskwarrior

%prep
%setup -q
%patch0 -p1

%build
%cmake_insource

%install
%makeinstall_std
%find_lang %name
install -Dm 644 -T scripts/bash/task.sh %buildroot%_sysconfdir/bash_completion.d/task
install -D scripts/zsh/_task %buildroot%_datadir/zsh/Completion/Unix/_task

%check
make test

%files
%_sysconfdir/bash_completion.d/%name

%files core
%doc %_docdir/%name/*
%_bindir/task
%_man1dir/*
%_man5dir/*

%files -n zsh-completion-task
%_datadir/zsh/Completion/Unix/_task

%changelog
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

