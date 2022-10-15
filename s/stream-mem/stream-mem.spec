%def_with fortran
%add_debuginfo_skiplist %_bindir

Name: stream-mem
Version: 5.10
Release: alt3

Summary: STREAM: Sustainable Memory Bandwidth in High Performance Computers
License: distributable
Group: Monitoring

Url: http://www.cs.virginia.edu/stream/
Source: stream-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libgomp-devel
%if_with fortran
BuildRequires: gcc-fortran
%endif

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

%make CFLAGS="-O%_optlevel -fopenmp -D_OPENMP" stream_c.exe
%if_with fortran
%make FFLAGS="-O%_optlevel" stream_f.exe
%endif

cat > README.ALT << EOF
Multiprocessor runs (find out the optimal factor by experimenting):

OMP_NUM_THREADS=4 stream_c

See also http://www.cs.virginia.edu/stream/ref.html#runrules
EOF

%install
install -pDm755 stream_c.exe %buildroot%_bindir/stream_c
%if_with fortran
install -pDm755 stream_f.exe %buildroot%_bindir/stream_f
%endif

%files
%_bindir/*
%doc HISTORY.txt LICENSE.txt READ.ME TO_DO
%doc README.ALT 

# TODO: cover MPI version as well

%changelog
* Sat Oct 15 2022 Michael Shigorin <mike@altlinux.org> 5.10-alt3
- fixed License:, dang!

* Sat Oct 15 2022 Michael Shigorin <mike@altlinux.org> 5.10-alt2
- fixed effective optlevel
- added the missing docs
- fixed fortran knob

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

