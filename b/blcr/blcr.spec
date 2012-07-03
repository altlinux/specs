%def_disable debug
%def_disable tracing
%def_enable shared
%def_enable static
%def_disable multilib
%def_enable testsuite
%def_disable restore_ids
%def_disable all_static
%def_disable info
%def_without ftb
#-------------------------------------------------------------
%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

%if "%_lib" != "lib64"
%set_disable multilib
%endif

Name: blcr
%define Name BLCR
%define lname lib%name
Version: 0.8.3
Release: alt1
Summary: Berkeley Lab Checkpoint/Restart for Linux
Group: System/Base
License: %gpl2plus
Url: https://ftg.lbl.gov/CheckpointRestart/CheckpointRestart.shtml
Source: https://ftg.lbl.gov/CheckpointRestart/downloads/%name-%version.tar
Source1: init.info
# Kernel and asm support only ported to certain architectures
# i386 is omitted because it lacks required atomic instructions
ExclusiveArch: %ix86 x86_64 %arm ppc ppc64
ExclusiveOs: Linux
Requires: %lname = %version-%release
%{?_enable_shared:Requires: %lname = %version-%release}
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses rpm-build-kernel
BuildRequires: gcc-c++
%{?_with_ftb:BuildRequires: libftb-devel}

%description
Berkeley Lab Checkpoint/Restart for Linux (%Name).
This package implements system-level checkpointing of scientific
applications in a manner suitable for implementing preemption,
migration and fault recovery by a batch scheduler.
%Name includes documented interfaces for a cooperating applications or
libraries to implement extensions to the checkpoint system, such as
consistent checkpointing of distributed MPI applications.
Using this package with an appropriate MPI implementation, the vast
majority of scientific applications which use MPI for communication on
Linux clusters are checkpointable without any modifications to the
application source code.


%package doc
Summary: Berkeley Lab Checkpoint/Restart for Linux documentation
Group: Documentation
BuildArch: noarch

%description doc
Berkeley Lab Checkpoint/Restart for Linux documentation.


%if_enabled shared
%package -n %lname
Summary: Libraries for Berkeley Lab Checkpoint/Restart for Linux
Group: System/Libraries
License: %lgpl2plus

%description -n %lname
Runtime libraries for Berkeley Lab Checkpoint/Restart for Linux (%Name).
%endif


%package -n %lname-devel
Summary: Header and object files for Berkeley Lab Checkpoint/Restart for Linux
Group: Development/C
License: %lgpl2plus
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release
%{?_disable_shared:BuildArch: noarch}

%description -n %lname-devel
Header and object files for Berkeley Lab Checkpoint/Restart for Linux.


%if_enabled static
%package -n %lname-devel-static
Summary: Static libraries for Berkeley Lab Checkpoint/Restart for Linux
Group: Development/C
License: %lgpl2plus
Requires: %lname = %version-%release

%description -n %lname-devel-static
Static libraries for Berkeley Lab Checkpoint/Restart for Linux.
%endif


%if_enabled testsuite
%package testsuite
Summary: Test suite for Berkeley Lab Checkpoint/Restart for Linux
Group: System/Base
License: %gpl2plus
Requires: %name = %version-%release

%description testsuite
This package includes tests for Berkeley Lab Checkpoint/Restart for
Linux.
%endif


%package -n kernel-source-%name
Summary: %Name sources for kernel development
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
%Name sources for kernel development.


%prep
%setup
install -m644 %SOURCE1 .


%build
install -d -m 0755 kernel-source-%name-%version
cp -r -L -t ./kernel-source-%name-%version Makefile* a* %{name}_* config* cr_module include vmadump4
for i in {doc,etc,rpm}/*.in; do
    install -D -m 0644 /dev/null ./kernel-source-%name-%version/$i
done
%configure  \
    --enable-init-script \
    --with-installed-modules \
    %{subst_enable debug} \
    %{subst_enable_to tracing libcr-tracing} \
    %{subst_enable shared} \
    %{subst_enable static} \
    %{subst_enable multilib} \
    %{subst_enable testsuite} \
    %{subst_enable_to restore_ids restore-ids} \
    %{subst_enable_to all_static all-static} \
    %{subst_enable_to info cr-info} \
    %{subst_with ftb} \
    --without-bug2524 \
    --with-gnu-ld \
    --disable-config-report
%make_build
bzip2 -9kf NEWS


%install
%make_install DESTDIR=%buildroot install
install -d -m 0755 $(dirname "%buildroot%_initdir") %buildroot%kernel_src
mv %buildroot{%_sysconfdir/init.d,%_initdir}
install -d -m 0755 %buildroot%_docdir/%name-%version/html
install -m 0644 LICENSE.txt NEWS.* %{?_with_ftb:README.FTB} doc/README util/license.txt %buildroot%_docdir/%name-%version/
install -m 0644 doc/html/*  %buildroot%_docdir/%name-%version/html/
tar -cj kernel-source-%name-%version > %buildroot%kernel_src/kernel-source-%name-%version.tar.bz2

sed -i -e '3rinit.info' \
	-e 's/^\(\ *reload\)/\1 | condrestart/' \
	-e 's/^\(\ *stop\)/\1 | condstop/' \
	%buildroot%_initdir/blcr

%post
[ "$RPM_INSTALL_ARG1" -ne 1 ] || /sbin/chkconfig --add %name ||:

%preun
[ "$RPM_INSTALL_ARG1" -ne 0 ] || /sbin/chkconfig --del %name ||:


%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/*.txt
%doc %_docdir/%name-%version/README
%{?_with_ftb:%doc %_docdir/%name-%version/README.FTB}
%_bindir/*
%_man1dir/*
%_initdir/*


%files doc
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/html
%doc %_docdir/%name-%version/NEWS.*


%if_enabled shared
%files -n %lname
%doc libcr/license.txt
%_libdir/*.so.*
%{?_enable_multilib:%_prefix/lib/*.so.*}
%endif



%files -n %lname-devel
%doc README.devel
%_includedir/*
%if_enabled shared
%_libdir/*.so
%{?_enable_multilib:%_prefix/lib/*.so}
%else
%doc libcr/license.txt
%endif


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%{?_enable_multilib:%_prefix/lib/*.a}
%endif


%if_enabled testsuite
%files testsuite
%doc tests/license.txt
%_libexecdir/%name-testsuite
%endif


%files -n kernel-source-%name
%kernel_src/*


%changelog
* Thu Oct 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1
- Version 0.8.3

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt3
- Rebuilt for debuginfo

* Thu Oct 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt2
- Rebuilt for soname set-versions

* Mon Jul 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1
- Version 0.8.2

* Tue Jun 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt3.1
- Build for Sisyphus

* Mon Jun 29 2009 Led <led@altlinux.ru> 0.8.1-alt3
- cleaned up post scripts

* Fri Jun 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.2
- Fix init script

* Fri Jun 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.1
- Build for Sisyphus

* Mon Jun 01 2009 Led <led@altlinux.ru> 0.8.1-alt2
- cleaned up BuildRequires

* Mon May 11 2009 Led <led@altlinux.ru> 0.8.1-alt1
- initial build
