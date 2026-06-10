%define _unpackaged_files_terminate_build 1
%define import_path github.com/projectdiscovery/nuclei

Name: nuclei
Version: 3.9.0
Release: alt1

Summary: Nuclei is a modern vulnerability scanner built on a simple YAML-based DSL

License: MIT
Group: Development/Tools
Url: https://github.com/projectdiscovery/nuclei
VCS: https://github.com/projectdiscovery/nuclei

ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang

%description
Nuclei is a fast, customizable vulnerability scanner powered by the
global security community and built on a simple YAML-based DSL,
enabling collaboration to tackle trending vulnerabilities on the
internet. It helps you find vulnerabilities in your applications,
APIs, networks, DNS, and cloud configurations. 

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
%golang_prepare

pushd .build/src/%import_path
%golang_build cmd/nuclei
popd

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

%files
%doc LICENSE.md README.md
%_bindir/nuclei

%changelog
* Wed Jun 10 2026 Aleksandr Shamaraev <shad@altlinux.org> 3.9.0-alt1
- automatic build: 3.8.0 -> 3.9.0

* Sun Apr 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 3.8.0-alt1
- 3.7.1 -> 3.8.0

* Fri Mar 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 3.7.1-alt1
- 3.7.0 -> 3.7.1

* Sat Feb 28 2026 Aleksandr Shamaraev <shad@altlinux.org> 3.7.0-alt2
- fixed FTBFS

* Fri Jan 30 2026 Aleksandr Shamaraev <shad@altlinux.org> 3.7.0-alt1
- 3.6.2 -> 3.7.0

* Thu Jan 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 3.6.2-alt1
- 3.6.1 -> 3.6.2

* Wed Dec 17 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.6.1-alt1
- 3.6.0 -> 3.6.1
- disabled vendored-ericlagergren-decimal patch

* Fri Dec 12 2025 Ivan A. Melnikov <iv@altlinux.org> 3.6.0-alt2
- NMU: fix FTBFS on loongarch64 and riscv64

* Fri Dec 05 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.6.0-alt1
- 3.5.1 -> 3.6.0

* Fri Nov 28 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.5.1-alt2
- vendor cleanup

* Sun Nov 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.5.1-alt1
- 3.4.7 -> 3.5.1

* Tue Jul 08 2025 Anastasia Doronina <swaggyglice@altlinux.org> 3.4.7-alt1
- Update to 3.4.7

* Tue Jul 01 2025 Anastasia Doronina <swaggyglice@altlinux.org> 3.4.6-alt1
- Update to 3.4.6

* Tue Jun 24 2025 Anastasia Doronina <swaggyglice@altlinux.org> 3.4.5-alt1
- Update to 3.4.5

* Tue Apr 15 2025 Anastasia Doronina <swaggyglice@altlinux.org> 3.4.2-alt1
- Update to 3.4.2 

* Tue Apr 01 2025 Anastasia Doronina <swaggyglice@altlinux.org> 3.4.1-alt1
- Update to 3.4.1.

* Thu Mar 13 2025 Anastasia Doronina <swaggyglice@altlinux.org> 3.3.10-alt1
- Initial Build for Sisyphus.
