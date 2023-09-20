%global import_path github.com/gokcehan/lf
%define lf_ver 31
Name:     lf
Version:  r%lf_ver
Release:  alt1

Summary:  Terminal file manager
License:  MIT
Group:    File tools
Url:      https://github.com/gokcehan/lf

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
lf (as in "list files") is a terminal file manager written in Go. It is
heavily inspired by ranger with some missing and extra features. Some of the
missing features are deliberately omitted since they are better handled by
external tools.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="${LDFLAGS:-} -X main.gVersion=%lf_ver"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -D -m644 etc/lf.bash \
	%buildroot%_datadir/bash-completion/completions/%name
install -D -m644 etc/lf.fish \
	%buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -D -m644 etc/lf.zsh \
	%buildroot%_datadir/zsh/site-functions/_%name

%files
%_bindir/*
%doc *.md
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%changelog
* Wed Sep 20 2023 Ilya Demyanov <turbid@altlinux.org> r31-alt1
- New upstream version r31
- Add shell-complection files

* Fri May 26 2023 Ilya Demyanov <turbid@altlinux.org> r30-alt1
- New upstream version r30

* Wed May 03 2023 Ilya Demyanov <turbid@altlinux.org> r29-alt1
- New upstream version r29

* Thu Feb 02 2023 Ilya Demyanov <turbid@altlinux.org> r28-alt1
- New upstream version r28

* Tue Feb 09 2021 Nikita Ermakov <arei@altlinux.org> r20-alt1
- Update to r20
- Fix a '-version' option

* Tue Jan 26 2021 Nikita Ermakov <arei@altlinux.org> r19-alt1
- Initial build for Sisyphus
