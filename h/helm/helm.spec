%define _unpackaged_files_terminate_build 1
%global import_path k8s.io/helm
Name:     helm
Version:  2.11.0
Release:  alt1

Summary:  The Kubernetes Package Manager
License:  Apache-2.0
Group:    Development/Tools
Url:      https://github.com/helm/helm

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Helm is a tool for managing Kubernetes charts. Charts are packages of
pre-configured Kubernetes resources.

%package -n tiller
Summary: The server side of helm
Group:    Development/Tools

%description -n tiller
%summary.

%prep
%setup

%build
export BUILDDIR="$PWD/.go"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="\
    -X k8s.io/helm/pkg/version.Version=%version \
    -X k8s.io/helm/pkg/version.BuildMetadata= \
    -X k8s.io/helm/pkg/version.GitCommit=2e55dbe1fdb5fdb96b75ff144a339489417b146b \
    -X k8s.io/helm/pkg/version.GitTreeState=clean \
    $LDFLAGS \
"

#%%golang_prepare

pushd "$BUILDDIR"/src/%import_path
%golang_build cmd/helm cmd/tiller
popd
"$BUILDDIR"/bin/helm completion bash > helm-bash-completion
"$BUILDDIR"/bin/helm completion zsh > helm-zsh-completion

%install
export BUILDDIR="$PWD/.go"
export IGNORE_SOURCES=1

%golang_install

install -Dm 644 helm-zsh-completion %buildroot/%_datadir/zsh/site-functions/_%name
install -Dm 644 helm-bash-completion %buildroot/%_sysconfdir/bash_completion.d/%name
for man_dir in docs/man/man*; do
    n="${man_dir#docs/man/man}"
    for man_file in "$man_dir"/*."$n"; do
        install -Dm 644 "$man_file" -t %buildroot/%_mandir/"man$n"
        # install -Dm 644 "$man_file" -t %buildroot/%_mandir/"man$n"/"$(basename "$m")"
    done
done
rm -r docs/man

%files
%doc README.md
%doc docs
%doc %_man1dir/%{name}*
%_bindir/%name
%_datadir/zsh/site-functions/_%name
%_sysconfdir/bash_completion.d/%name

%files -n tiller
%_bindir/tiller

%changelog
* Wed Oct 03 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.11.0-alt1
- Initial build for Sisyphus
