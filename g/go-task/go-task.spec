%global import_path github.com/go-task/task
Name:     go-task
Version:  3.51.1
Release:  alt1

Summary:  A task runner / simpler Make alternative written in Go
License:  MIT
Group:    Other
Url:      https://github.com/go-task/task

Source0:   %name-%version.tar
Source1:   vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

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

install -Dm 644 completion/zsh/_task %buildroot/%_datadir/zsh/site-functions/_task

%files
%_bindir/task
%doc *.md
%_datadir/zsh/site-functions/_task

%changelog
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
