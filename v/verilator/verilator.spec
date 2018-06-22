Name: verilator
Version: 3.924
Release: alt1
Summary: A fast and free Verilog HDL simulator

Group: Engineering
License: LGPLv3 or Perl Artistic 2.0
Url: https://www.veripool.org/wiki/verilator
Source: %name-%version.tar
# Version string in pkg-config files can not contain whitespace
Patch0: pkg-config-version-fix.patch

BuildRequires: flex gcc-c++ perl-Pod-LaTeX texlive

%description
Verilator is the fastest free Verilog HDL simulator, and beats most commercial
simulators. It compiles synthesizable Verilog, plus some PSL, SystemVerilog and
Synthesis assertions into C++ or SystemC code. It is designed for large projects
where fast simulation performance is of primary concern, and is especially well
suited to generate executable models of CPUs for embedded software design teams.

%package -n %name-doc
Summary: A fast and free Verilog HDL simulator - documentation and examples
Group: Engineering
BuildArch: noarch

%description -n %name-doc
Verilator is the fastest free Verilog HDL simulator, and beats most commercial
simulators. This package contains documentation and examples.

%define docfiles README README.html README.pdf internals.txt internals.html internals.pdf verilator.txt verilator.html verilator.pdf

%prep
%setup
%patch0 -p1

%build
autoconf
%configure
%make_build all %docfiles

%check
%make test

%install
%makeinstall_std
mkdir -p %buildroot%_pkgconfigdir/
mv %buildroot%_datadir/pkgconfig/%name.pc %buildroot%_pkgconfigdir/%name.pc
mkdir -p %buildroot%_docdir/%name/
mv %buildroot%_datadir/%name/examples %buildroot%_docdir/%name/

%files -n %name
%_bindir/*
%_datadir/%name/
%_man1dir/*
%_pkgconfigdir/%name.pc

%files -n %name-doc
%doc %docfiles
%_docdir/%name/

%changelog
* Tue Jun 19 2018 Elvira Khabirova <lineprinter@altlinux.org> 3.924-alt1
- Initial build
