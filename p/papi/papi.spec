%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
# appio.c directly calls non-LFS functions.
%set_verify_elf_method strict,lfs=relaxed
%define optflags_lto %nil
%def_without doc

Name: papi
Version: 6.0.0
Release: alt8

Summary: Performance Application Programming Interface

License: BSD-3-Clause
Group: Development/Tools
Url: https://icl.utk.edu/exa-papi/
Vcs: https://github.com/icl-utk-edu/papi

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%define tagversion %(echo "%version" | sed -e "s|\\.|-|g")
# Source-url: https://bitbucket.org/icl/papi/get/papi-%tagversion-t.tar.bz2
Source: %name-%version.tar

Patch1: papi-6.0.0-alt-fix-mips-warning.patch
Patch4: papi-config.patch
Patch5: papi-nostatic.patch
Patch6: papi-init_thread.patch
Patch2000: papi-e2k.patch

Requires: lib%name = %EVR

BuildRequires: /proc
BuildRequires: rpm-build-python3
BuildRequires: libncurses-devel gcc-fortran libsensors3-devel libgomp-devel
BuildRequires: doxygen
%if_with doc
BuildRequires: graphviz
%endif
BuildRequires: libpfm-devel

BuildRequires: chrpath

%description
PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter hardware
found in most major microprocessors. PAPI enables software engineers to see, in
near real time, the relation between software performance and processor events.

%package -n lib%name
Summary: Shared libraries of PAPI (Performance Application Programming Interface)
Group: System/Libraries

%description -n lib%name
PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter hardware
found in most major microprocessors. PAPI enables software engineers to see, in
near real time, the relation between software performance and processor events.

This package contains shared libraries of PAPI.

%package -n lib%name-devel
Summary: Development files of Performance Application Programming Interface
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter hardware
found in most major microprocessors. PAPI enables software engineers to see, in
near real time, the relation between software performance and processor events.

This package contains development files of PAPI.

%package doc
Summary: Documentation for Performance Application Programming Interface
Group: Documentation
#BuildArch: noarch

%description doc
PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter hardware
found in most major microprocessors. PAPI enables software engineers to see, in
near real time, the relation between software performance and processor events.

This package contains documentation for PAPI.

%prep
%setup

%patch1 -p2
%patch4 -p1
%patch5 -p1
%patch6 -p1
%ifarch %e2k
%patch2000 -p2
%endif
rm -rf src/libpfm*

#rm -fR src/perfctr-*
#cp -f src/Rules.pfm src/Rules.perfctr
#cp -f src/Rules.pfm src/Rules.perfctr-pfm

#__subst 's|-Xlinker "-rpath" -Xlinker "\$(LIBDIR)"||' src/configure.in

%build
cd src

# TODO: fix build with static-lib=no
%add_optflags %optflags_shared %(getconf LFS_CFLAGS)
%autoreconf
%configure \
	--with-ffsll \
	--with-static-lib=no \
	--with-shlib \
	--with-shared-lib=yes \
	--with-shlib-tools=yes \
	--with-virtualtimer=clock_thread_cputime_id \
	--with-perf-events \
	--with-pfm-incdir=%_includedir --with-pfm-libdir=%_libdir \
	--with-components="appio coretemp lmsensors mx net rapl stealtime"
#cp -f Makefile.inc.bak Makefile.inc
#make libpapi.a
%make_build
%if_with doc
%make -C ../doc html
%endif
%make -C ../doc man

%install
cd src
%makeinstall_std
%make_install DESTDIR=%buildroot install-man

%__subst "s|/usr/bin/python|/usr/bin/env python3|" %buildroot%_bindir/papi_hl_output_writer.py

chrpath --delete %buildroot%_libdir/*.so*
rm -rf %buildroot%_libdir/*.a

%if_with doc
install -d %buildroot%_docdir/%name
cp -fR ../doc/html/* %buildroot%_docdir/%name/
%endif

#ln -s libpapi.so %buildroot%_libdir/libpapi64.so
#ln -s libpfm.so %buildroot%_libdir/libpfm64.so

rm -f %buildroot%_libdir/*.a

%check
export LD_LIBRARY_PATH=%buildroot%_libdir PATH=%buildroot%_bindir:$PATH
papi_version
papi_component_avail
cd src
ctests/version
set +x
# Only selected fast and reliable ctests.
for i in \
	attach2 attach3 attach_cpu attach_cpu_sys_validate attach_cpu_validate	\
	attach_target attach_validate byte_profile				\
	clockres_pthreads cmpinfo code2name data_range				\
	disable_component dmem_info earprofile eventname exec exec2		\
	failed_events first fork fork2 forkexec forkexec2 forkexec3 forkexec4	\
	get_event_component inherit locks_pthreads low-level			\
	memory overflow overflow_index						\
	overflow_one_and_read							\
	p4_lst_ins pthrtough							\
	pthrtough2 remove_events reset reset_multiplex version zero		\
	zero_flip zero_fork zero_omp zero_pthreads zero_shmem zero_smp
do
	if ctests/$i >.out 2>&1; then
		echo "$i OK"
	else
		echo "$i FAILED!"
		sed 's/^/\t/' .out
		> .failed
	fi
done
test -e .failed && exit 1
set -x

%files
%doc *.txt README.md
%_bindir/*
%_man1dir/*
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_man3dir/*
%_pkgconfigdir/*.pc

%if_with doc
%files doc
%_docdir/%name
%endif

%changelog
* Tue Oct 31 2023 Vitaly Chikunov <vt@altlinux.org> 6.0.0-alt8
- spec: Update Url and Vcs links.
- spec: Remove BR on libltdl-devel.

* Fri May 26 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 6.0.0-alt7.1
- Fixed build for Elbrus.

* Fri May 26 2023 Vitaly Chikunov <vt@altlinux.org> 6.0.0-alt7
- Fix rebuild due to "Couldn't open hw_instructions".

* Wed Jan 05 2022 Vitaly Chikunov <vt@altlinux.org> 6.0.0-alt6
- Unbundle libpfm.
- Update License tag.
- Add some testing in %%check.
- Do not build huge papi-doc package.

* Tue Aug 31 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 6.0.0-alt5
- disabled LTO because of build errors

* Tue Aug 31 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 6.0.0-alt4
- added patch for Elbrus

* Tue Aug 10 2021 Ivan A. Melnikov <iv@altlinux.org> 6.0.0-alt3
- fix build on mipsel

* Sat May 15 2021 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt2
- add BR: rpm-build-python3

* Sat Oct 10 2020 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt1
- new version 6.0.0 (with rpmrb script)

* Tue Mar 26 2019 Vitaly Lipatov <lav@altlinux.ru> 5.7.0-alt1
- new version (5.7.0) with rpmgs script
- cleanup spec, change upstream source url

* Wed May 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.0-alt1
- Version 5.3.0

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2.0-alt1
- Version 5.2.0

* Thu Jul 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.1-alt1
- Version 5.1.1

* Fri Feb 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.0.2-alt1
- Version 5.1.0.2

* Thu Nov 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.1-alt1
- Version 5.0.1

* Wed Sep 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt1
- Version 5.0.0

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt2
- Fixed build with new glibc

* Fri Mar 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1
- Version 4.2.1

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt2
- Removed setting of RPATH

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1
- Version 4.2.0

* Mon Aug 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1
- Version 4.1.3

* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2.1-alt1
- Version 4.1.2.1
- Disabled devel-static subpackage

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt3
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt2
- Rebuilt for soname set-versions

* Fri Jul 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0
- Built with PerfCtr 2.6.41

* Sat Jan 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt6
- Rebuild with PerfCtr 2.6.40

* Thu Jun 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt5
- Rebuild with PerfCtr 2.6.39

* Fri Jun 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt4
- Rebuild with PIC

* Thu Jun 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt3
- Add links libpapi64.*

* Fri May 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt2
- Rebuild with PerfCtr 2.6.38

* Tue May 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1
- Initial build for Sisyphus

