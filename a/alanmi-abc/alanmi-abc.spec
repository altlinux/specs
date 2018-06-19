Name: alanmi-abc
Version: 20180617.0.g28a1307
Release: alt1

Summary: System for Sequential Logic Synthesis and Formal Verification
License: %bsdstyle
Group: Engineering

Url: https://people.eecs.berkeley.edu/~alanmi/abc/
Source: %name-%version.tar

# https://bitbucket.org/alanmi/abc/issues/27/assertion-failure-in-write_pla-command
Patch0: trivial-functions-fix-assert.patch
Patch1: use-external-bzlib-zlib.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Jun 19 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libstdc++-devel python-base
BuildRequires: gcc-c++ libreadline-devel

Provides: berkeley-abc

%description
ABC is a growing software system for synthesis and verification of binary
sequential logic circuits appearing in synchronous hardware designs. ABC
combines scalable logic optimization based on And-Inverter Graphs (AIGs),
optimal-delay DAG-based technology mapping for look-up tables and standard
cells, and innovative algorithms for sequential synthesis and verification.

ABC provides an experimental implementation of these algorithms and a
programming environment for building similar applications. Future development
will focus on improving the algorithms and making most of the packages
stand-alone. This will allow the user to customize ABC for their needs as if it
were a tool-box rather than a complete tool.

%prep
%setup

%build
%make_build OPTFLAGS='%optflags' ABC_MAKE_VERBOSE=1

%install
mkdir -p %buildroot/%_bindir/
install -p -m 755 abc %buildroot/%_bindir/

%files -n alanmi-abc
%doc copyright.txt README.md
%_bindir/abc

%changelog
* Tue Jun 19 2018 Elvira Khabirova <lineprinter@altlinux.org> 20180617.0.g28a1307-alt1
- New version
- Upstream moved to github

* Fri Feb 10 2017 Elvira Khabirova <lineprinter@altlinux.org> 20160717.196.5d42a91ef6fb-alt1
- Initial build
