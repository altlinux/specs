%define _unpackaged_files_terminate_build 1

Name: iverilog
Version: 12.0
Release: alt1
Summary: Verilog simulation and synthesis tool

Group: Engineering
License: GPLv2
Url: http://iverilog.icarus.com
Source: %name-%version.tar

BuildRequires: /proc
BuildRequires: bzip2-devel
BuildRequires: zlib-devel
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: libreadline-devel

Provides: verilog

%description
Icarus Verilog is a Verilog simulation and synthesis tool. It operates
as a compiler, compiling source code written in Verilog (IEEE-1364)
into some target format. For batch simulation, the compiler can generate
an intermediate form called vvp assembly. This intermediate form is
executed by the ``vvp'' command. For synthesis, the compiler generates
netlists in the desired format. It supports the 1995, 2001 and 2005
versions of the standard, portions of SystemVerilog, and some extensions.

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%prep
%setup

%build
sh ./autoconf.sh
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_docdir/%name-%version/examples/
install -m644 *.txt %buildroot%_docdir/%name-%version/
install -m644 examples/* %buildroot%_docdir/%name-%version/examples/

%check
%make check

%files
%_bindir/*
%_libdir/*.a
%_libdir/ivl/
%_includedir/%name/
%_man1dir/*
%_docdir/%name-%version/
%exclude %_docdir/%name-%version/cygwin.txt
%exclude %_docdir/%name-%version/mingw.txt

%changelog
* Tue Jan 10 2023 Egor Ignatov <egori@altlinux.org> 12.0-alt1
- 12.0

* Wed Aug 25 2021 Egor Ignatov <egori@altlinux.org> 11.0-alt3
- add -ffat-lto-objects to build static libs with -flto enabled

* Thu Apr 29 2021 Egor Ignatov <egori@altlinux.org> 11.0-alt2
- Add bzip2 and zlib build dependencies (Closes: #37929)

* Sat Apr 17 2021 Egor Ignatov <egori@altlinux.org> 11.0-alt1
- New version

* Sat Jun 16 2018 Elvira Khabirova <lineprinter@altlinux.org> 10.2-alt1
- Initial build
