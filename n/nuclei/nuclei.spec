%define _unpackaged_files_terminate_build 1
%define import_path github.com/projectdiscovery/nuclei

Name: nuclei
Version: 3.4.1
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
* Tue Apr 01 2025 Anastasia Doronina <swaggyglice@altlinux.org> 3.4.1-alt1
- Update to 3.4.1.

* Thu Mar 13 2025 Anastasia Doronina <swaggyglice@altlinux.org> 3.3.10-alt1
- Initial Build for Sisyphus.
