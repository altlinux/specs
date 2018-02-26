Name: lam
Version: 7.1.4
Release: alt4

%define mpi_prefix %_libexecdir/%name
%define mpi_sysconfdir %_sysconfdir/%name

Packager: Denis Pynkin <dans@altlinux.ru>

Summary: LAM/MPI (Local Area Multicomputer) programming environment
License: BSD
Group: Development/Other
Url: http://www.lam-mpi.org/
Source: http://www.lam-mpi.org/download/files/%name-%version.tar

# Automatically added by buildreq on Mon Mar 17 2003
BuildRequires: gcc-c++ gcc-g77 glibc-devel-static libg2c-devel libstdc++-devel openssh-clients

BuildPreReq: mpi-selector
Requires(post,preun): mpi-selector

%package devel
Summary: development part of %name
Group: Development/C

%description
LAM (Local Area Multicomputer) is an MPI programming environment and
development system for heterogeneous computers on a network. With
LAM/MPI, a dedicated cluster or an existing network computing
infrastructure can act as a single parallel computer.  LAM/MPI is
considered to be "cluster friendly", in that it offers daemon-based
process startup/control as well as fast client-to-client message
passing protocols.  LAM/MPI can use TCP/IP and/or shared memory for
message passing (currently, different RPMs are supplied for this --
see the main LAM web site for details).

LAM features a full implementation of MPI-1 (with the exception that
LAM does not support cancelling of sends), and much of MPI-2.
Compliant applications are source code portable between LAM/MPI and
any other implementation of MPI.  In addition to providing a
high-quality implementation of the MPI standard, LAM/MPI offers
extensive monitoring capabilities to support debugging.  Monitoring
happens on two levels.  First, LAM/MPI has the hooks to allow a
snapshot of process and message status to be taken at any time during
an application run.  This snapshot includes all aspects of
synchronization plus datatype maps/signatures, communicator group
membership, and message contents (see the XMPI application on the main
LAM web site).  On the second level, the MPI library is instrumented
to produce a cummulative record of communication, which can be
visualized either at runtime or post-mortem.

%description devel
development stuff for %name

%prep
%setup -q

%build
%autoreconf
%configure --with-rpi=tcp --with-rsh="ssh -x" \
    --prefix=%mpi_prefix \
    --sysconfdir=%mpi_sysconfdir \
    --bindir=%mpi_prefix/bin \
    --libdir=%mpi_prefix/lib \
    --datadir=%mpi_prefix/data \
    --includedir=%mpi_prefix/include \
    --mandir=%mpi_prefix/man

#NO SMP
%make all

%install

%make_install DESTDIR=%buildroot install

ln -s mpicxx.h $RPM_BUILD_ROOT/%mpi_prefix/include/mpi++.h

%__mkdir_p $RPM_BUILD_ROOT/%_docdir/%name-%version/
mv $RPM_BUILD_ROOT/%mpi_prefix/data/lam/doc/* $RPM_BUILD_ROOT/%_docdir/%name-%version/
rm -rf $RPM_BUILD_ROOT/%mpi_prefix/data

cat>%buildroot/%mpi_prefix/bin/mpivars.sh<<EOF
if ! echo \$PATH | grep -q %mpi_prefix/bin ; then
    PATH=%mpi_prefix/bin:\$PATH
    export PATH
fi

if ! echo \$LD_LIBRARY_PATH | grep -q %mpi_prefix/lib ; then
    LD_LIBRARY_PATH=%mpi_prefix/lib:\$LD_LIBRARY_PATH
    export LD_LIBRARY_PATH
fi

if ! echo \$MANPATH | grep -q %mpi_prefix/man ; then
    MANPATH=%mpi_prefix/man:\$MANPATH
    export MANPATH
fi
EOF

cat >%buildroot%mpi_prefix/bin/mpivars.csh <<EOF
if (\$?path) then
    if ( "\${path}" !~ *%mpi_prefix/bin* ) then
	set path = ( %mpi_prefix/bin \$path )
    endif
else
    set path = ( %mpi_prefix/bin )
endif

if (\$?LD_LIBRARY_PATH) then
    if ( "\$LD_LIBRARY_PATH" !~ *%mpi_prefix/lib* ) then
	setenv LD_LIBRARY_PATH %mpi_prefix/lib:\$LD_LIBRARY_PATH
    endif
else
    setenv LD_LIBRARY_PATH %mpi_prefix/lib:
endif

if (\$?MANPATH) then
    if ( "\$MANPATH" !~ *%mpi_prefix/man* ) then
	setenv MANPATH %mpi_prefix/man:\$MANPATH
    endif
else
    setenv MANPATH %mpi_prefix/man:
endif
EOF

%post
%post_mpi_selector %name %mpi_prefix/bin

%preun
%preun_mpi_selector %name

%files
%doc LICENSE HISTORY INSTALL README

%dir %mpi_prefix

%dir %mpi_prefix/bin


%mpi_prefix/bin/*

%exclude %mpi_prefix/bin/hcc
%exclude %mpi_prefix/bin/hcp
%exclude %mpi_prefix/bin/hf77
%exclude %mpi_prefix/bin/mpicc
%exclude %mpi_prefix/bin/mpiCC
%exclude %mpi_prefix/bin/mpif77


%dir %mpi_sysconfdir
%config(noreplace) %mpi_sysconfdir/*

%dir %mpi_prefix/man
%mpi_prefix/man/man1
%exclude %mpi_prefix/man/man1/hcc*
%exclude %mpi_prefix/man/man1/hcp*
%exclude %mpi_prefix/man/man1/hf77*
%exclude %mpi_prefix/man/man1/mpic*
%exclude %mpi_prefix/man/man1/mpiCC*
%exclude %mpi_prefix/man/man1/mpif77*

%mpi_prefix/man/man5
%mpi_prefix/man/man7
%mpi_prefix/man/mans

%files devel
%doc  examples
%mpi_prefix/bin/hcc
%mpi_prefix/bin/hcp
%mpi_prefix/bin/hf77
%mpi_prefix/bin/mpicc
%mpi_prefix/bin/mpiCC
%mpi_prefix/bin/mpif77
%mpi_prefix/include/*

%mpi_prefix/lib/*

%mpi_prefix/man/man1/hcc*
%mpi_prefix/man/man1/hcp*
%mpi_prefix/man/man1/hf77*
%mpi_prefix/man/man1/mpic*
%mpi_prefix/man/man1/mpiCC*
%mpi_prefix/man/man1/mpif77*

%mpi_prefix/man/man3

%changelog
* Mon May 25 2009 Denis Pynkin <dans@altlinux.ru> 7.1.4-alt4
- Fixed build for sisyphus

* Sun Oct 26 2008 Denis Pynkin <dans@altlinux.ru> 7.1.4-alt3
- Fixed configure tests for correct working with new toolchain

* Thu Sep 01 2008 Denis Pynkin <dans@altlinux.ru> 7.1.4-alt2
- Added mpi-selector support

* Sun Sep 30 2007 Denis Pynkin <dans@altlinux.ru> 7.1.4-alt1
- Bug fix release
- Link mpi++.h now points to mpicxx.h (bug 12981)

* Wed Mar 28 2007 Denis Pynkin <dans@altlinux.ru> 7.1.3-alt1
- Bug fix release
- Tar archiving without compression

* Thu Dec 07 2006 Denis Pynkin <dans@altlinux.ru> 7.1.2-alt1
- 7.1.2

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 7.0.6-alt1.1
- Rebuilt with libstdc++.so.6.

* Thu Aug 12 2004 Stanislav Ievlev <inger@altlinux.org> 7.0.6-alt1
- 7.0.6

* Thu Jun 24 2004 Stanislav Ievlev <inger@altlinux.org> 7.0.3-alt1.1
- rebuild with new glibc

* Fri Dec 05 2003 Stanislav Ievlev <inger@altlinux.org> 7.0.3-alt1
- 7.0.3

* Mon Mar 17 2003 Stanislav Ievlev <inger@altlinux.ru> 6.5.9-alt1
- 6.5.9

* Mon Oct 14 2002 Stanislav Ievlev <inger@altlinux.ru> 6.5.6-alt3
- rebuild with gcc3.

* Wed Apr 24 2002 Stanislav Ievlev <inger@altlinux.ru> 6.5.6-alt2
- added devel subpackage

* Wed Apr 03 2002 Stanislav Ievlev <inger@altlinux.ru> 6.5.6-alt1
- first build for Sisyphus
