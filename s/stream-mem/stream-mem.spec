%def_with fortran
%add_debuginfo_skiplist %_bindir

Name: stream-mem
Version: 5.10
Release: alt1

Summary: STREAM: Sustainable Memory Bandwidth in High Performance Computers
License: GPL
Group: Monitoring

Url: http://www.cs.virginia.edu/stream/
Source: stream-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libgomp-devel

BuildRequires: gcc-fortran

%description
The STREAM benchmark is a simple synthetic benchmark program that
measures sustainable memory bandwidth (in MB/s) and the corresponding
computation rate for simple vector kernels.

%prep
%setup -n stream-%version

%build
%ifarch %e2k
# as of lcc 1.25.23, this gives slightly better result that our default -O3
%define _optlevel 4
%endif

export CFLAGS="%optflags -fopenmp -D_OPENMP"

%make stream_c.exe
%if_with fortran
%make stream_f.exe
%endif

%install
install -pDm755 stream_c.exe %buildroot%_bindir/stream_c
%if_with fortran
install -pDm755 stream_f.exe %buildroot%_bindir/stream_f
%endif

%files
%_bindir/*

# TODO: cover MPI version as well

%changelog
* Sat Oct 15 2022 Michael Shigorin <mike@altlinux.org> 5.10-alt1
- updated to sources from 2013 (as of today)
- build with OpenMP
- build fortran version too (if enabled)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 5.8-alt2.qa1
- NMU: rebuilt for debuginfo.

* Thu Oct 15 2009 Michael Shigorin <mike@altlinux.org> 5.8-alt2
- built for Sisyphus

* Sat Jul 19 2008 Mikhail Yakshin <greycat@altlinux.org> 5.8-alt1
- Initial build

