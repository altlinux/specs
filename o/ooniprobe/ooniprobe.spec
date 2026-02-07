Name: ooniprobe
Version: 3.28.0
Release: alt1

Summary: OONI Probe CLI - network interference detection tool

License: GPL-3.0
Group: Networking/Other
Url: https://ooni.org/
Vcs: https://github.com/ooni/probe-cli

# Source-url: https://github.com/ooni/probe-cli/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
OONI Probe is a free software project for measuring internet censorship
and other forms of network interference. It collects data about which
websites are blocked, whether instant messaging apps and circumvention
tools work, and whether systems are in place that could be used for
censorship and/or surveillance.

%prep
%setup -a1

%build
export CGO_ENABLED=1
%gobuild -mod=vendor ./cmd/ooniprobe

%install
install -D -p -m 755 ooniprobe %buildroot%_bindir/ooniprobe

%files
%doc Readme.md LICENSE
%_bindir/ooniprobe

%changelog
* Fri Feb 06 2026 Vitaly Lipatov <lav@altlinux.ru> 3.28.0-alt1
- initial build for ALT Sisyphus
