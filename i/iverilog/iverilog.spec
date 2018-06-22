Name: iverilog
Version: 10.2
Release: alt1
Summary: Verilog simulation and synthesis tool

Group: Engineering
License: %lgpl21only
Url: http://iverilog.icarus.com
Source: %name-%version.tar

# Automatically added by buildreq on Sun Jun 17 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libstdc++-devel perl python-base
BuildRequires: flex gcc-c++ gperf libreadline-devel
BuildRequires(pre): rpm-build-licenses
Provides: verilog

%description
Icarus Verilog is a Verilog simulation and synthesis tool. It operates
as a compiler, compiling source code written in Verilog (IEEE-1364)
into some target format. For batch simulation, the compiler can generate
an intermediate form called vvp assembly. This intermediate form is
executed by the ``vvp'' command. For synthesis, the compiler generates
netlists in the desired format. It supports the 1995, 2001 and 2005
versions of the standard, portions of SystemVerilog, and some extensions.

# Some binaries are in fact loadable code generators
# See developer-quick-start.txt
%set_verify_elf_method unresolved=relaxed

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
%exclude %_docdir/%name-%version/macosx.txt
%exclude %_docdir/%name-%version/mingw.txt

%changelog
* Sat Jun 16 2018 Elvira Khabirova <lineprinter@altlinux.org> 10.2-alt1
- Initial build
