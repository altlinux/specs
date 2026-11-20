%define _unpackaged_files_terminate_build 1
%global import_path github.com/go-task/task

Name:     go-task
Version:  3.54.0
Release:  alt1

Summary:  A task runner / simpler Make alternative written in Go
License:  MIT
Group:    Other
Url:      https://github.com/go-task/task

Source0:   %name-%version.tar
Source1:   %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Conflicts: task-core

%description
Task is a task runner / build tool that aims to be simpler and easier to use
than, for example, GNU Make.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/task

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -m644 -D completion/bash/task.bash  %buildroot%_datadir/bash-completion/completions/task
install -m644 -D completion/zsh/_task       %buildroot%_datadir/zsh/site-functions/_task
install -m644 -D completion/fish/task.fish  %buildroot%_datadir/fish/completions/task.fish

%files
%_bindir/task
%doc *.md
%_datadir/bash-completion/completions/task
%_datadir/zsh/site-functions/_task
%_datadir/fish/completions/task.fish

%changelog
* Fri Nov 20 2026 Maxim Slipenko <maks1ms@altlinux.org> 3.54.0-alt1
- New version 3.54.0.
- Install completion scripts for bash and fish in addition to zsh.
- Spec cleanup.

* Tue Aug 25 2026 Maxim Slipenko <maks1ms@altlinux.org> 3.53.1-alt1
- New version 3.53.1.
- Add Conflicts: task-core (closes: #60262).

* Thu Jul 09 2026 Maxim Slipenko <maks1ms@altlinux.org> 3.52.0-alt1
- New version 3.52.0.

* Wed Jun 03 2026 Maxim Slipenko <maks1ms@altlinux.org> 3.51.1-alt1
- New version 3.51.1.

* Thu May 07 2026 Maxim Slipenko <maks1ms@altlinux.org> 3.50.0-alt1
- New version 3.50.0.

* Wed Jan 28 2026 Maxim Slipenko <maks1ms@altlinux.org> 3.48.0-alt1
- 3.48.0 (closes: #57437)

* Tue Jan 10 2023 Anton Zhukharev <ancieg@altlinux.org> 3.19.1-alt1
- 3.19.1 (closes: #44593)

* Sat Mar 16 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.4.0-alt1
- Initial build for Sisyphus
