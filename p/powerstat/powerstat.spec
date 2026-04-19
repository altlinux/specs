Name: powerstat
Version: 0.04.06
Release: alt1

Summary: A tool to measure power consumption
License: GPL-2.0-or-later
Group: Monitoring
Url: https://github.com/ColinIanKing/powerstat

Vcs: https://github.com/ColinIanKing/powerstat.git

Source: %url/archive/V%version/%name-%version.tar.gz

BuildRequires: bash-completion

# RAPL not available on other architectures
ExclusiveArch: %ix86 x86_64

%description
Powerstat  measures  the  power consumption of a computer that has a
battery power source or supports the RAPL (Running Average Power Limit)
interface. The output is like vmstat but also shows power consumption
statistics. At the end of a run, powerstat will calculate the average,
standard deviation, minimum, maximum and geometic mean of the gathered
data.

%prep
%setup
%ifarch %ix86
echo "CFLAGS += %(getconf LFS_CFLAGS)" >> Makefile
%endif

%build
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_man8dir/%name.8*
%_datadir/bash-completion/completions/%name
%doc README.md

%changelog
* Sun Apr 19 2026 Yuri N. Sedunov <aris@altlinux.org> 0.04.06-alt1
- 0.04.06

* Wed May 07 2025 Yuri N. Sedunov <aris@altlinux.org> 0.04.05-alt1
- 0.04.05

* Thu Feb 27 2025 Yuri N. Sedunov <aris@altlinux.org> 0.04.04-alt1
- 0.04.04

* Fri Feb 21 2025 Yuri N. Sedunov <aris@altlinux.org> 0.04.03-alt1
- first build for Sisyphus

