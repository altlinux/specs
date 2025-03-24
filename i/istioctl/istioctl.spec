Name: istioctl
Version: 1.25.0
Release: alt2

Summary: CLI for the istio service mesh in Kubernetes

License: Apache-2.0
Group: System/Configuration/Other
Url: https://github.com/istio/istio
Vcs: https://github.com/istio/istio.git

Source0: %url/archive/%version/%name-%version.tar.gz
# go mod vendor
Source1: vendor.tar

BuildRequires: rpm-build-golang /proc fdupes

%description
The istioctl tool is a configuration command line utility that allows service
operators to debug and diagnose their Istio service mesh deployments. The Istio
project also includes two helpful scripts for istioctl that enable
auto-completion for Bash and ZSH. Both of these scripts provide support for the
currently available istioctl commands.

%package -n bash-completion-%name
Summary: Bash Completion for %name
Group: Shells
BuildArch: noarch

%description -n bash-completion-%name
Bash command line completion support for %name.

%package -n zsh-completion-%name
Summary: Zsh Completion for %name
Group: Shells
BuildArch: noarch

%description -n zsh-completion-%name
Zsh command line completion support for %name.

%prep
%setup -a1
sed '/buildVersion/s|"unknown"|"%version"|' \
   -i pkg/version/version.go

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X istio.io/pkg/version.buildVersion=%version" \
   -o bin/%name ./istioctl/cmd/istioctl

%install
# Install the binary.
install -D -m 0755 bin/%name %buildroot%_bindir/%name

# copy the sample files
mkdir -p %buildroot%_docdir/%name
cp -vr samples %buildroot%_docdir/%name
rm -f %buildroot%_docdir/%name/samples/bookinfo/src/reviews/.gitignore
rm -f %buildroot%_docdir/%name/samples/bookinfo/src/reviews/reviews-wlpcfg/shared/.gitkeep
rm -f %buildroot%_docdir/%name/samples/wasm_modules/header_injector/.gitignore
# identify duplicate files
fdupes %buildroot%_docdir/%name/samples/

# create the bash completion file
mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name
# create the zsh completion file
mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%name

%files
%doc README.md
%doc LICENSE
%_bindir/%name
%_docdir/%name

%files -n bash-completion-%name
%_datadir/bash-completion/completions/%name

%files -n zsh-completion-%name
%_datadir/zsh/site-functions/_%name

%changelog
* Mon Mar 24 2025 Leontiy Volodin <lvol@altlinux.org> 1.25.0-alt2
- Fixed istioctl version (ALT #53401).

* Tue Mar 04 2025 Leontiy Volodin <lvol@altlinux.org> 1.25.0-alt1
- New version 1.25.0.

* Fri Feb 28 2025 Leontiy Volodin <lvol@altlinux.org> 1.24.3-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).

