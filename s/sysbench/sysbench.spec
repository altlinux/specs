Name:     sysbench
Version:  1.0.20
Release:  alt1

Summary:  Scriptable database and system performance benchmark
License:  GPL-2.0
Group:    Other
Url:      https://github.com/akopytov/sysbench

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

BuildRequires: ck-devel
BuildRequires: docbook-style-xsl
BuildRequires: libaio-devel
BuildRequires: libtool
BuildRequires: libxslt
BuildRequires: libluajit-devel
BuildRequires: mysql-devel
BuildRequires: postgresql-devel

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
rm -r third_party/luajit/luajit/
rm -r third_party/concurrency_kit/ck/

%build
export CFLAGS="%optflags"
%autoreconf
%configure --with-mysql \
           --with-pgsql \
           --with-system-ck \
           --with-system-luajit \
           --without-gcc-arch

%make_build

%install
%makeinstall_std
mv %buildroot%_docdir/sysbench/manual.html .

%files
%doc ChangeLog COPYING README.md manual.html
%_bindir/*
%_datadir/%name

%changelog
* Wed May 20 2020 Anton Midyukov <antohami@altlinux.org> 1.0.20-alt1
- new version 1.0.20

* Tue Apr 09 2019 Anton Midyukov <antohami@altlinux.org> 1.0.17-alt1
- new version 1.0.17

* Mon Mar 04 2019 Anton Midyukov <antohami@altlinux.org> 1.0.16-alt1
- 1.0.16

* Tue Apr 02 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.12-alt2
- Dependiens zlib-devel fixed

* Tue Feb 12 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.12-alt1
- Initial build
