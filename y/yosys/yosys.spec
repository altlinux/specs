Name: yosys
Version: 0.7
Release: alt1

Summary: Yosys Open SYnthesis Suite
License: ISC
Group: Engineering
Url: http://www.clifford.at/yosys/

Source: %name-%version.tar
Patch0: explicit-git-revision.patch
Patch1: makefile-cxxflags.patch

# Automatically added by buildreq on Mon Jan 23 2017
# optimized out: libstdc++-devel pkg-config python-base python3 tcl
BuildRequires: flex gcc-c++ libffi-devel libreadline-devel python3-base tcl-devel

BuildPreReq: /proc

Requires: alanmi-abc

%description
Yosys is a framework for RTL synthesis tools. It currently has extensive
Verilog-2005 support and provides a basic set of synthesis algorithms for
various application domains.

Yosys can be adapted to perform any synthesis job by combining the existing
passes (algorithms) using synthesis scripts and adding additional passes as
needed by extending the yosys C++ code base.

%package -n yosys-devel
Summary: Yosys Open SYnthesis Suite - headers for plugin development
Group: Engineering

%description -n yosys-devel
Yosys is a framework for RTL synthesis tools. This package contains the headers
and programs needed to build yosys plugins.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
make config-gcc
echo "CXXFLAGS += %optflags" >> Makefile.conf
%make_build ABCEXTERNAL=abc PRETTY=0 PREFIX=%prefix

%install
%makeinstall_std PREFIX=%prefix ABCEXTERNAL=abc
mkdir -p %buildroot/%_man1dir/ %buildroot/%_includedir/
install -m 644 %{name}*.1 %buildroot/%_man1dir/
mv %buildroot%_datadir/%name/include/ %buildroot%_includedir/%name

%files -n yosys
%_bindir/%name
%_bindir/%name-filterlib
%_bindir/%name-smtbmc
%_datadir/%name
%_man1dir/%name.1*
%_man1dir/%name-filterlib.1*
%_man1dir/%name-smtbmc.1*

%files -n yosys-devel
%_bindir/%name-config
%_includedir/%name
%_man1dir/%name-config.1*

%changelog
* Mon Jan 23 2017 Elvira Khabirova <lineprinter@altlinux.org> 0.7-alt1
- Initial build
