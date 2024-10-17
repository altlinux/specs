# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

# do not forget to update Git revision in setup section

Name: yosys
Version: 0.46
Release: alt1

Summary: Yosys Open SYnthesis Suite
License: ISC
Group: Engineering
Url: https://github.com/YosysHQ/yosys

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: flex gcc-c++ libffi-devel libreadline-devel python3 tcl-devel zlib-devel

BuildPreReq: /proc

Requires: alanmi-abc

# For generating Graphviz representation of design (ALT bug 42631)
Requires: graphviz
Requires: python3-module-xdot

%add_python3_path %_datadir/%name

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
%autopatch -p1

%build
%define optflags_lto %nil
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
%_bindir/%name-witness
%_datadir/%name
%_man1dir/%name.1*
%_man1dir/%name-filterlib.1*
%_man1dir/%name-smtbmc.1*

%files -n yosys-devel
%_bindir/%name-config
%_includedir/%name
%_man1dir/%name-config.1*

%changelog
* Thu Oct 17 2024 Anton Midyukov <antohami@altlinux.org> 0.46-alt1
- New version 0.46.

* Wed Sep 04 2024 Anton Midyukov <antohami@altlinux.org> 0.45-alt1
- new version 0.45

* Tue Aug 13 2024 Anton Midyukov <antohami@altlinux.org> 0.44-alt1
- new version 0.44

* Sun Jul 28 2024 Anton Midyukov <antohami@altlinux.org> 0.43-alt1
- new version 0.43

* Tue Jun 18 2024 Anton Midyukov <antohami@altlinux.org> 0.42-alt1
- new version 0.42

* Fri May 31 2024 Anton Midyukov <antohami@altlinux.org> 0.41-alt1
- new version 0.41

* Mon Apr 15 2024 Anton Midyukov <antohami@altlinux.org> 0.40-alt1
- new version 0.40

* Mon Mar 18 2024 Anton Midyukov <antohami@altlinux.org> 0.39-alt1
- new version 0.39

* Sun Feb 18 2024 Anton Midyukov <antohami@altlinux.org> 0.38-alt1
- new version 0.38

* Mon Jan 29 2024 Anton Midyukov <antohami@altlinux.org> 0.37-alt1
- new version 0.37

* Fri Dec 29 2023 Anton Midyukov <antohami@altlinux.org> 0.36-alt1
- new version 0.36

* Sun Nov 12 2023 Anton Midyukov <antohami@altlinux.org> 0.35-alt1
- new version 0.35

* Fri Oct 06 2023 Anton Midyukov <antohami@altlinux.org> 0.34-alt1
- new version 0.34

* Mon Aug 14 2023 Anton Midyukov <antohami@altlinux.org> 0.32-alt1
- new version 0.32

* Mon Jun 12 2023 Anton Midyukov <antohami@altlinux.org> 0.30-alt1
- new version 0.30

* Sun Apr 30 2023 Anton Midyukov <antohami@altlinux.org> 0.28-alt1
- new version 0.28

* Sun Jan 15 2023 Anton Midyukov <antohami@altlinux.org> 0.25-alt1
- new version 0.25

* Sun Oct 23 2022 Anton Midyukov <antohami@altlinux.org> 0.22-alt1
- new version 0.22

* Fri Sep 09 2022 Anton Midyukov <antohami@altlinux.org> 0.21-alt1
- new version 0.21

* Thu Jul 21 2022 Anton Midyukov <antohami@altlinux.org> 0.19-alt2
- disable LTO
- cleanup spec

* Thu Jul 21 2022 Anton Midyukov <antohami@altlinux.org> 0.19-alt1
- new version 0.19

* Sun Jun 19 2022 Anton Midyukov <antohami@altlinux.org> 0.18-alt1
- New version 0.18

* Sat May 21 2022 Anton Midyukov <antohami@altlinux.org> 0.17-alt1
- New version 0.17

* Fri Apr 29 2022 Anton Midyukov <antohami@altlinux.org> 0.16-alt2
- add dependencies on graphviz, python3-module-xdot for generating Graphviz
  representation of design (Closes: 42631)

* Tue Apr 12 2022 Anton Midyukov <antohami@altlinux.org> 0.16-alt1
- New version 0.16
- Update Url

* Sat Apr 11 2021 Pavel Nakonechnyi <zorg@altlinux.org> 0.9.0.0.4052.ga58571d-alt1
- New version

* Tue Jun 19 2018 Elvira Khabirova <lineprinter@altlinux.org> 0.7.0.0.826.g626b555-alt1
- New version

* Wed Mar 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt1.qa1
- NMU: rebuild against Tcl/Tk 8.6

* Mon Jan 23 2017 Elvira Khabirova <lineprinter@altlinux.org> 0.7-alt1
- Initial build
