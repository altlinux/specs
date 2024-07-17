%global import_path github.com/ansible-semaphore/semaphore
Name:     semaphore
Version:  2.10.18
Release:  alt1

Summary:  Open Source alternative to Ansible Tower
License:  MIT
Group:    Other
Url:      https://github.com/ansible-semaphore/semaphore

ExclusiveArch: %go_arches

Source:   %name-%version.tar

Patch1:   semaphore-2.20.18-alt-show-just-version.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup
%patch1 -p1

# next commands need to prepare sources
# apt-get install go-task packr
# go mod vendor
# task deps:fe
# task build:fe
%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="${LDFLAGS:-} -X github.com/ansible-semaphore/semaphore/util.Ver=%version"
export LDFLAGS="${LDFLAGS:-} -X github.com/ansible-semaphore/semaphore/util.Commit="
export LDFLAGS="${LDFLAGS:-} -X github.com/ansible-semaphore/semaphore/util.Date="

%golang_prepare

cd .build/src/%import_path
%golang_build cli

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
mv %buildroot%_bindir/{cli,%name}

mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%name
mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%_bindir/%name
%doc README.ALT
%doc *.md
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Wed Jul 17 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.10.18-alt1
- Update to 2.10.18 (Closes: 50935)

* Tue May 16 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.8.90-alt1
- Update to 2.8.90

* Tue Sep 03 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.5.1-alt2
- Set ExclusiveArch to %%go_arches

* Sat Mar 16 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.5.1-alt1
- Update to 2.5.1

* Thu May 10 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.4.1-alt1
- Initial build for Sisyphus
