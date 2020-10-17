Name: coz
Version: 0.2.2
Release: alt1

Packager: %packager

Summary: Coz: Finding Code that Counts with Causal Profiling
License: GPL
Group: Development/C
URL: https://github.com/plasma-umass/coz

Source: %name-%version.tar

# Automatically added by buildreq on Sun Oct 18 2020
BuildRequires: gcc-c++ libelfin-devel python3-module-mpl_toolkits python3-module-yieldfrom selinux-policy-alt python-module-docutils

%description
Coz is a new kind of profiler that unlocks optimization opportunities
missed by traditional profilers. Coz employs a novel technique we call
causal profiling that measures optimization potential. This measurement
matches developers' assumptions about profilers: that optimizing highly-ranked
code will have the greatest impact on performance.

%prep
%setup

%build
%make prefix=%_exec_prefix bindir=%_bindir MANPREFIX=%_mandir

%install
%define docdir %_docdir/%name-%version

%makeinstall LIBDIR=%buildroot%_libdir prefix=%buildroot%_exec_prefix MANPREFIX=%_mandir pkglibdir=%buildroot%_libdir/coz-profiler

mkdir -p %buildroot%docdir
install -pm644 README.md %buildroot%docdir/
install -pm644 LICENSE.md %buildroot%docdir/
cp -R benchmark.mk %buildroot%docdir/
cp -R common.mk %buildroot%docdir/
cp -R benchmarks %buildroot%docdir/

%find_lang %name

%files
%_bindir/*
%_includedir/*
%_libdir/coz-profiler/*
%_man1dir/*

%dir %docdir
%docdir/*

%changelog
* Sat Oct 17 2020 Andrey Bergman <vkni@altlinux.org> 0.2.2-alt1
- Initial release for Sisyphus.
