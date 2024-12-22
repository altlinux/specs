%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
# appio.c directly calls non-LFS functions.
%set_verify_elf_method strict,lfs=relaxed
%define optflags_lto %nil

Name: papi
Version: 7.1.0
Release: alt1
Summary: Performance Application Programming Interface
License: BSD-3-Clause
Group: Development/Tools
Url: https://icl.utk.edu/exa-papi/
Vcs: https://github.com/icl-utk-edu/papi
Requires: libpapi = %EVR

Source: %name-%version.tar
Patch2000: papi-e2k.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: chrpath
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: gcc-fortran
BuildRequires: libgomp-devel
BuildRequires: libncurses-devel
BuildRequires: libpfm-devel
BuildRequires: libsensors3-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: /proc
}}

%description
PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter hardware
found in most major microprocessors. PAPI enables software engineers to see, in
near real time, the relation between software performance and processor events.

%package -n libpapi
Summary: Shared libraries of PAPI (Performance Application Programming Interface)
Group: System/Libraries

%description -n libpapi
PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter hardware
found in most major microprocessors. PAPI enables software engineers to see, in
near real time, the relation between software performance and processor events.

This package contains shared libraries of PAPI.

%package -n libpapi-devel
Summary: Development files of Performance Application Programming Interface
Group: Development/C
Requires: libpapi = %EVR

%description -n libpapi-devel
PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter hardware
found in most major microprocessors. PAPI enables software engineers to see, in
near real time, the relation between software performance and processor events.

This package contains development files of PAPI.

%prep
%setup
%ifarch %e2k
%patch2000 -p2
%endif

%build
cd src
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure \
	--with-components="appio coretemp infiniband io lmsensors net powercap rapl sde stealtime" \
	--with-perf-events \
	--with-pfm-incdir=%_includedir \
	--with-pfm-libdir=%_libdir \
	--with-shared-lib=yes \
	--with-shlib \
	--with-shlib-tools=yes \
	--with-static-lib=no \
	%nil
%make_build
%make -C ../doc man

%install
cd src
%makeinstall_std
%make_install DESTDIR=%buildroot install-man
sed -i "1s|/usr/bin/python.*|%__python3|" %buildroot%_bindir/papi_hl_output_writer.py
find %buildroot -type f | xargs file4 -N | grep ELF | cut -d: -f1 |
	xargs -t chrpath --delete

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
%doc ChangeLog*.txt LICENSE.txt README.md RELEASENOTES.txt
%_bindir/papi_*
%_man1dir/PAPI_*.1*
%_man1dir/papi_*.1*
%_datadir/papi

%files -n libpapi
%_libdir/*.so.*

%files -n libpapi-devel
%_libdir/*.so
%_includedir/*.h*
%_man3dir/PAPI*.3*
%_pkgconfigdir/*.pc

%changelog
* Sun Dec 22 2024 Vitaly Chikunov <vt@altlinux.org> 7.1.0-alt1
- Update to papi-7-1-0-t (2023-12-20).
- spec: Change packaging from tar import to git.
- spec: Enable more components (including sde).

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

