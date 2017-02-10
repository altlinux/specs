%define modulename migen

Name: python3-module-%modulename
Version: 0.4.0.56.gd594c71
Release: alt1

Summary: A Python toolbox for building complex digital hardware
License: %bsdstyle
Group: Engineering
Url: https://github.com/m-labs/migen
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses rpm-build-python3
# Automatically added by buildreq on Tue Jan 24 2017
# optimized out: python-base python3 python3-base
BuildRequires: python3-dev python3-module-setuptools

%description
Despite being faster than schematics entry, hardware design with Verilog and
VHDL remains tedious and inefficient for several reasons. The event-driven model
introduces issues and manual coding that are unnecessary for synchronous
circuits, which represent the lion's share of today's logic designs. Counter-
intuitive arithmetic rules result in steeper learning curves and provide a
fertile ground for subtle bugs in designs. Finally, support for procedural
generation of logic (metaprogramming) through "generate" statements is very
limited and restricts the ways code can be made generic, reused and organized.

The Migen FHDL library replaces the event-driven paradigm with the notions
of combinatorial and synchronous statements, has arithmetic rules that make
integers always behave like mathematical integers, and most importantly allows
the design's logic to be constructed by a Python program. This last point
enables hardware designers to take advantage of the richness of
the Python language - object oriented programming, function parameters,
generators, operator overloading, libraries, etc. - to build well organized,
reusable and elegant designs.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Fri Feb 10 2017 Elvira Khabirova <lineprinter@altlinux.org> 0.4.0.56.gd594c71-alt1
- Initial build
