%global import_path github.com/semaphoreui/semaphore
Name:     semaphore
Version:  2.18.12
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
export LDFLAGS="${LDFLAGS:-} -X %import_path/util.Ver=%version"
export LDFLAGS="${LDFLAGS:-} -X %import_path/util.Commit="
export LDFLAGS="${LDFLAGS:-} -X %import_path/util.Date="

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

%check
%buildroot%_bindir/%name version | grep -Eq '[0-9]+\.[0-9]+\.[0-9]+'

%files
%_bindir/%name
%doc README.ALT
%doc *.md
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Thu Jun 11 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.18.12-alt1
- new version 2.18.12

* Wed Jun 03 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.18.9-alt1
- new version 2.18.9

* Mon May 25 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.18.5-alt1
- new version 2.18.5

* Wed May 20 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.18.4-alt1
- new version 2.18.4

* Fri May 15 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.18.3-alt1
- new version 2.18.3

* Wed May 06 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.18.1-alt1
- new version 2.18.1

* Mon May 04 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.17.39-alt1
- new version 2.17.39

* Wed Apr 22 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.17.38-alt1
- new version 2.17.38

* Mon Mar 23 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.17.28-alt1
- new version 2.17.28

* Wed Mar 18 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.17.26-alt1
- new version 2.17.26

* Fri Mar 13 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.17.22-alt1
- new version 2.17.22

* Wed Mar 11 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.17.21-alt1
- new version 2.17.21

* Mon Mar 02 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.17.16-alt1
- new version 2.17.16

* Wed Feb 25 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.17.14-alt1
- new version 2.17.14

* Fri Feb 20 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.17.12-alt1
- new version 2.17.12

* Mon Feb 16 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.17.2-alt1
- new version 2.17.2

* Wed Jan 14 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.16.51-alt1
- new version 2.16.51

* Thu Dec 25 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.16.47-alt1
- new version 2.16.47

* Wed Dec 17 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.16.46-alt1
- new version 2.16.46

* Thu Nov 13 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.16.45-alt1
- new version 2.16.45

* Wed Nov 05 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.16.38-alt1
- new version 2.16.38

* Tue Oct 28 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.16.36-alt1
- new version 2.16.36

* Thu Oct 23 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.16.34-alt1
- new version 2.16.34

* Wed Sep 17 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.16.31-alt1
- new version 2.16.31

* Fri Sep 12 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.16.29-alt1
- new version 2.16.29

* Wed Sep 03 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.16.19-alt1
- new version 2.16.19

* Wed Aug 20 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.16.17-alt1
- new version 2.16.17

* Tue Aug 12 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.16.7-alt1
- new version 2.16.7

* Wed Jul 23 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.15.4-alt1
- new version 2.15.4

* Sat Jun 28 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.15.0-alt1
- new version 2.15.0

* Fri Jun 06 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.14.12-alt1
- new version 2.14.12

* Mon May 26 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.14.10-alt1
- new version 2.14.10

* Mon May 05 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.14.8-alt1
- new version 2.14.8

* Wed Apr 30 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.14.6-alt1
- new version 2.14.6

* Mon Apr 21 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.13.14-alt1
- new version 2.13.14

* Mon Apr 14 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.13.13-alt1
- new version 2.13.13

* Mon Mar 10 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.12.17-alt1
- new version 2.12.17

* Fri Feb 28 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.12.14-alt1
- new version 2.12.14

* Fri Feb 14 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.12.12-alt1
- new version 2.12.12

* Wed Feb 12 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.12.8-alt1
- new version 2.12.8

* Wed Feb 05 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.12.4-alt1
- new version 2.12.4

* Fri Jan 31 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.12.3-alt1
- new version 2.12.3

* Mon Jan 27 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.11.3-alt1
- new version 2.11.3

* Fri Dec 27 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.11.2-alt1
- new version 2.11.2

* Fri Nov 01 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.10.35-alt1
- new version 2.10.35

* Fri Oct 25 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.10.33-alt1
- new version 2.10.33

* Tue Sep 24 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.10.22-alt1
- new version 2.10.22

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
