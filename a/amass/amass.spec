%define _unpackaged_files_terminate_build 1
%global import_path github.com/owasp-amass/amass

Name: amass
Version: 4.2.0
Release: alt1
Summary: In-depth attack surface mapping and asset discovery.
License: Apache-2.0
Group: Networking/Other
Url: https://owasp.org/www-project-amass/
Vcs: https://github.com/owasp-amass/amass

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch
ExclusiveArch:  x86_64

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
The OWASP Amass tool suite obtains subdomain names by scraping data
sources, recursive brute forcing, crawling web archives,
permuting/altering names and reverse DNS sweeping. Additionally, Amass
uses the IP addresses obtained during resolution to discover associated
netblocks and ASNs. All the information is then used to build maps of the
target networks.
Amass ships with a set of wordlist (to be used with the amass -w flag)
that are found under the wordlists output.

%prep
%setup -a 1
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build cmd/%name/

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md
%_bindir/%name

%changelog
* Sat Nov 02 2024 Pavel Shilov <zerospirit@altlinux.org> 4.2.0-alt1
- initial build for Sisyphus
