%define _unpackaged_files_terminate_build 1
%define import_path github.com/Gu1llaum-3/sshm

Name:       sshm
Version:    1.11.0
Release:    alt1

License:    MIT
Group:      Networking/Remote access
Summary:    TUI tool for managing SSH connections

Url:        https://github.com/Gu1llaum-3/sshm
Source:     %name-%version.tar
Source1:    vendor.tar

Patch1:     sshm-1.11.0-disable_check_for_updates.patch
Patch2:     sshm-1.11.0-fix_output_service_completions.patch

BuildRequires(pre): rpm-build-golang

ExclusiveArch: %go_arches

%description
SSHM is a beautiful command-line tool that transforms
how you manage and connect to your SSH hosts.
Built with Go and featuring an intuitive TUI interface,
it makes SSH connection management effortless and enjoyable.

%prep
%setup -a 1 -q
%patch1 -p1
%patch2 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-mod=vendor"
export GOROOT="%_libexecdir/golang"
export LDFLAGS="$LDFLAGS -X github.com/Gu1llaum-3/sshm/cmd.AppVersion=%version"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
export GOROOT="%_libexecdir/golang"

%golang_install

mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/zsh/site-functions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d

%buildroot%_bindir/%name completion bash \
    > %buildroot%_datadir/bash-completion/completions/%name
%buildroot%_bindir/%name completion zsh \
    > %buildroot%_datadir/zsh/site-functions/_%name
%buildroot%_bindir/%name completion fish \
    > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%doc LICENSE README.*
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Wed Apr 08 2026 Sergey Savelev <medovi@altlinux.org> 1.11.0-alt1
- New version 1.11.0.

* Mon Jan 12 2026 Sergey Savelev <medovi@altlinux.org> 1.10.0-alt1
- New version 1.10.0.

* Fri Nov 28 2025 Sergey Savelev <medovi@altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus.
