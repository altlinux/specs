Name: istioctl
Version: 1.30.2
Release: alt1

Summary: CLI for the istio service mesh in Kubernetes

License: Apache-2.0
Group: System/Configuration/Other
Url: https://github.com/istio/istio
Vcs: https://github.com/istio/istio
# NOTE: See https://istio.io/latest/news/releases for CVEs.

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source0: %name-%version.tar
# cd istio/ && go mod vendor -o ../vendor && cd ../
Source1: vendor.tar
Patch: %name-%version-%release.patch

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
%autopatch -p1
sed '/buildVersion/s|"unknown"|"%version"|' \
   -i pkg/version/version.go

%build
go build -x \
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
* Thu Jun 25 2026 Leontiy Volodin <lvol@altlinux.org> 1.30.2-alt1
- New version 1.30.2 (Fixes: CVE-2026-47692, CVE-2026-47207,
  CVE-2026-47205, CVE-2026-47220, CVE-2026-47221, CVE-2026-48044,
  CVE-2026-48090, CVE-2026-47778, CVE-2026-47204, CVE-2026-48497,
  CVE-2026-48706, CVE-2026-48743, CVE-2026-47775, CVE-2026-48042,
  GHSA-p7c7-7c47-pwch).

* Fri Jun 05 2026 Leontiy Volodin <lvol@altlinux.org> 1.30.1-alt1
- New version 1.30.1 (Fixes: CVE-2026-47774).

* Mon Jun 01 2026 Leontiy Volodin <lvol@altlinux.org> 1.30.0-alt1
- New version 1.30.0.

* Mon Jun 01 2026 Leontiy Volodin <lvol@altlinux.org> 1.29.3-alt1
- New version 1.29.3.

* Tue Apr 14 2026 Leontiy Volodin <lvol@altlinux.org> 1.29.2-alt1
- New version 1.29.2.

* Wed Mar 11 2026 Leontiy Volodin <lvol@altlinux.org> 1.29.1-alt1
- New version 1.29.1 (Fixes: CVE-2026-31837, CVE-2026-31838).

* Tue Feb 17 2026 Leontiy Volodin <lvol@altlinux.org> 1.29.0-alt1
- New version 1.29.0.

* Wed Jan 21 2026 Leontiy Volodin <lvol@altlinux.org> 1.28.3-alt1
- New version 1.28.3.

* Tue Dec 23 2025 Leontiy Volodin <lvol@altlinux.org> 1.28.2-alt1
- New version 1.28.2.

* Thu Dec 04 2025 Leontiy Volodin <lvol@altlinux.org> 1.28.1-alt1
- New version 1.28.1.

* Thu Nov 06 2025 Leontiy Volodin <lvol@altlinux.org> 1.28.0-alt1
- New version 1.28.0.

* Tue Oct 21 2025 Leontiy Volodin <lvol@altlinux.org> 1.27.3-alt1
- New version 1.27.3.

* Tue Oct 14 2025 Leontiy Volodin <lvol@altlinux.org> 1.27.2-alt1
- New version 1.27.2.

* Thu Sep 04 2025 Leontiy Volodin <lvol@altlinux.org> 1.27.1-alt1
- New version 1.27.1.

* Wed Aug 13 2025 Leontiy Volodin <lvol@altlinux.org> 1.27.0-alt1
- New version 1.27.0.

* Wed Jul 30 2025 Leontiy Volodin <lvol@altlinux.org> 1.26.3-alt1
- New version 1.26.3.

* Mon Jun 23 2025 Leontiy Volodin <lvol@altlinux.org> 1.26.2-alt1
- New version 1.26.2.

* Tue Jun 03 2025 Leontiy Volodin <lvol@altlinux.org> 1.26.1-alt1
- New version 1.26.1.

* Wed May 28 2025 Leontiy Volodin <lvol@altlinux.org> 1.26.0-alt1
- New version 1.26.0.

* Tue Apr 15 2025 Leontiy Volodin <lvol@altlinux.org> 1.25.2-alt1
- New version 1.25.2.

* Tue Apr 01 2025 Leontiy Volodin <lvol@altlinux.org> 1.25.1-alt1
- New version 1.25.1.

* Mon Mar 24 2025 Leontiy Volodin <lvol@altlinux.org> 1.25.0-alt2
- Fixed istioctl version (ALT #53401).

* Tue Mar 04 2025 Leontiy Volodin <lvol@altlinux.org> 1.25.0-alt1
- New version 1.25.0.

* Fri Feb 28 2025 Leontiy Volodin <lvol@altlinux.org> 1.24.3-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).

