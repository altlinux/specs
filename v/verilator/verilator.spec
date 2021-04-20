# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/git tex(dehypht.tex)
# END SourceDeps(oneline)

%define _unpackaged_files_terminate_build 1

Name: verilator
Version: 4.200
Release: alt1
Summary: A fast and free Verilog HDL simulator

Group: Engineering
License: LGPLv3 or Perl Artistic 2.0
Url: https://www.veripool.org/wiki/verilator
Source: %name-%version.tar

BuildRequires: flex gcc-c++ perl-Pod-LaTeX texlive
BuildRequires: /usr/bin/pod2html

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

%define docfiles verilator.txt verilator.html verilator.pdf

%prep
%setup

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
* Tue Apr 20 2021 Egor Ignatov <egori@altlinux.org> 4.200-alt1
- new version
- remove pkg-config-version-fix patch

* Sat Apr 18 2020 Michael Shigorin <mike@altlinux.org> 3.924-alt1.2
- added missing BR: /usr/bin/pod2html

* Fri Apr 03 2020 Igor Vlasenko <viy@altlinux.ru> 3.924-alt1.1
- NMU: applied logoved fixes

* Tue Jun 19 2018 Elvira Khabirova <lineprinter@altlinux.org> 3.924-alt1
- Initial build
