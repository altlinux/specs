Summary: A system performance benchmark
Name: sysbench
Version: 0.4.12
Release: alt1
Url: http://sysbench.sourceforge.net/
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: GPLv2
Group: Other

BuildRequires: gcc-c++ libmysqlclient-devel


%description
SysBench is a modular, cross-platform and multi-threaded benchmark
tool for evaluating OS parameters that are important for a system
running a database under intensive load.

The idea of this benchmark suite is to quickly get an impression about
system performance without setting up complex database benchmarks or
even without installing a database at all. Current features allow to
test the following system parameters:
- file I/O performance
- scheduler performance
- memory allocation and transfer speed
- POSIX threads implementation performance
- database server performance (OLTP benchmark)

Primarily written for MySQL server benchmarking, SysBench will be
further extended to support multiple database backends, distributed
benchmarks and third-party plug-in modules.

%prep
%setup

%build
%autoreconf
%configure
%make

%install
%makeinstall_std

%files
%_bindir/sysbench
%doc doc/manual.xml COPYING ChangeLog

%changelog
* Tue Feb 12 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.12-alt1
- Initial build

