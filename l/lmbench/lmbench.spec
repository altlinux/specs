%define _unpackaged_files_terminate_build 1

Name: lmbench
Version: 3.0a9
Release: alt1
Summary: Suite of simple, portable benchmarks

License: GPL-2.0-or-later
Group: System/Kernel and hardware
Url: http://www.bitmover.com/lmbench
#URL: http://sourceforge.net/projects/lmbench

Source: %name-%version.tar

# patchs from https://github.com/intel/lmbench
Patch0: 0003-config-run-set-OUTPUT-as-dev-null.patch
Patch1: 0004-Fix-errors-of-fstat-stat-open-in-lat_syscall.patch
Patch2: 0008-Create-s.ChangeSet.patch
Patch3: lmbench-3.0a9-alt-add-libtirpc-support.patch

BuildRequires: libtirpc-devel

%description
Bandwidth benchmarks: cached file read, memory copy (bcopy), memory read,
memory write, pipe, TCP; Latency benchmarks: context switching, connection
establishment, pipe, TCP, UDP, RPC hot potato, file system creates and
deletes, process creation, signal handling, system call overhead,  memory
read latency; Miscellanious Processor clock rate calculation.

%description -l ru_RU.UTF-8
Набор программ для тестирования производительности.
Измерение пропускной способности:
cached file read, memory copy (bcopy),
memory read, memory write, pipe, TCP;
Измерение задержек:
context switching, connection establishment, pipe, TCP, UDP,
RPC hot potato, file system creates and deletes, process
creation, signal handling, system call overhead, memory
read latency; Miscellanious Processor clock rate calculation.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p2

%build
%make_build 

%install
install -d -m0755 %buildroot%_sbindir
install -d -m0755 %buildroot%_mandir/{man1,man3,man8}/ \

%ifarch %arm %ix86 x86_64
pushd bin/*-linux-gnu
%else
pushd bin
%endif

install -p -m0755 bw_* %buildroot%_sbindir
install -p -m0755 cache %buildroot%_sbindir
install -p -m0755 disk %buildroot%_sbindir
install -p -m0755 enough %buildroot%_sbindir
install -p -m0755 flushdisk %buildroot%_sbindir
install -p -m0755 hello %buildroot%_sbindir
install -p -m0755 lat_* %buildroot%_sbindir
install -p -m0755 line %buildroot%_sbindir
install -p -m0755 lmdd %buildroot%_sbindir
install -p -m0755 lmhttp %buildroot%_sbindir
install -p -m0755 loop_o %buildroot%_sbindir
install -p -m0755 memsize %buildroot%_sbindir
install -p -m0755 mhz %buildroot%_sbindir
install -p -m0755 msleep %buildroot%_sbindir
install -p -m0755 par_* %buildroot%_sbindir
install -p -m0755 stream %buildroot%_sbindir
install -p -m0755 timing_o %buildroot%_sbindir
install -p -m0755 tlb %buildroot%_sbindir
popd

install -p -m0644 doc/*.1 %buildroot%_man1dir/
install -p -m0644 doc/*.3 %buildroot%_man3dir/
install -p -m0644 doc/*.8 %buildroot%_man8dir/

%files
%doc ACKNOWLEDGEMENTS CHANGES COPYING COPYING-2 README hbench-REBUTTAL doc/*.ms
%doc %_mandir/man?/*
%_sbindir/*

%changelog
* Tue Apr 20 2021 Egor Ignatov <egori@altlinux.org> 3.0a9-alt1
- Cleanup spec
- Update .gear/rules
- Remove unneeded patch files
- Fix build with glibc-2.26 and newer
  + Add support for libtirpc

* Sat May 02 2020 Anton Midyukov <antohami@altlinux.org> 3.0-alt3
- Cleanup spec
- Added patches from https://github.com/intel/lmbench

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.0-alt2.qa1
- NMU: rebuilt for debuginfo.

* Tue Jan 09 2007 Dmitri Kuzishchin <dim@altlinux.ru> 3.0-alt2
- Change path from /usr/bin to %_sbindir.

* Sat May 13 2006 Dmitri Kuzishchin <dim@altlinux.ru> 3.0-alt1
- Initial package.
