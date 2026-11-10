%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: bpftop
Version: 0.9.0
Release: alt1

Summary: Dynamic real-time monitor for running eBPF programs
Summary(ru_RU.UTF-8): Динамический монитор работающих программ eBPF в реальном времени
License: Apache-2.0
Group: Monitoring
Url: https://bpftop.sh/
Vcs: https://github.com/jfernandez/bpftop
ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rustfmt
BuildRequires: clang
BuildRequires: pkg-config
BuildRequires: libelf-devel
BuildRequires: zlib-devel

%description
bpftop provides a dynamic real-time view of running eBPF programs. It displays
average runtime, events per second, and estimated CPU utilization, and offers
graphical views of these statistics over time.

%description -l ru_RU.UTF-8
bpftop предоставляет динамическое представление работающих программ eBPF в
реальном времени. Он показывает среднее время выполнения, количество событий
в секунду и оценочную загрузку процессора, а также отображает графики изменения
этих показателей во времени.

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name
%doc LICENSE README.md

%changelog
* Sat Oct 17 2026 Georgij Tsarin <crystarm@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.
