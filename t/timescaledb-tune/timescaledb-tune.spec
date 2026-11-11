%define import_path github.com/timescale/timescaledb-tune

Name:     timescaledb-tune
Version:  0.19.1
Release:  alt1
Summary:  is a program for tuning a TimescaleDB database
License:  Apache-2.0
Group:    Databases
Url:      https://github.com/timescale/timescaledb-tune

Source:   %name-%version.tar
Patch0:   %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%name is a program for tuning a TimescaleDB database to perform
its best based on the host's resources such as memory and number of CPUs.
It parses the existing `postgresql.conf` file to ensure that the TimescaleDB
extension is appropriately installed and provides recommendations for
memory, parallelism, WAL, and other settings.

%prep
%setup
%patch0 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

cd .build/src/%import_path
%golang_build ./cmd/timescaledb-tune

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md

%changelog
* Wed Nov 11 2026 Alexei Takaseev <taf@altlinux.org> 0.19.1-alt1
- 0.19.1
- OVE-20261111-0003: Backport to c10f2 and c11f1 support new version TimescaleDB

* Tue Oct 27 2026 Alexei Takaseev <taf@altlinux.org> 0.19.0-alt2
- Added an ALT-specific path to the configuration file (ALT #61228)

* Wed Oct 21 2026 Alexei Takaseev <taf@altlinux.org> 0.19.0-alt1
- 0.19.0

* Tue Mar 01 2022 Alexei Takaseev <taf@altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus
