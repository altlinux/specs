Summary: Suite of simple, portable benchmarks 
Name: lmbench
Version: 3.0
Release: alt2
License: GPL
Group: System/Kernel and hardware
URL: http://www.bitmover.com/lmbench
#URL: http://sourceforge.net/projects/lmbench
Source: lmbench-%{version}-a5.tgz

%description
Bandwidth benchmarks: cached file read, memory copy (bcopy), memory read,
memory write, pipe, TCP; Latency benchmarks: context switching, connection
establishment, pipe, TCP, UDP, RPC hot potato, file system creates and
deletes, process creation, signal handling, system call overhead,  memory
read latency; Miscellanious Processor clock rate calculation.

%description -l ru_RU.KOI8-R
Набор программ для тестирования производительности.
Измерение пропускной способности:cached file read, memory copy (bcopy), memory read,
memory write, pipe, TCP; Имерение задержек: context switching, connection
establishment, pipe, TCP, UDP, RPC hot potato, file system creates and
deletes, process creation, signal handling, system call overhead,  memory
read latency; Miscellanious Processor clock rate calculation.

%prep
%setup -n %{name}-%{version}-a5

%build
%{__make} %{?_smp_mflags}

%install
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -d -m0755 %{buildroot}/usr/sbin
%{__install} -d -m0755 %{buildroot}%{_mandir}/{man1,man3,man8}/ \

cd bin/*-linux-gnu
%{__install} -p -m0755 bw_* %{buildroot}/usr/sbin
%{__install} -p -m0755 cache %{buildroot}/usr/sbin
%{__install} -p -m0755 disk %{buildroot}/usr/sbin
%{__install} -p -m0755 enough %{buildroot}/usr/sbin
%{__install} -p -m0755 flushdisk %{buildroot}/usr/sbin
%{__install} -p -m0755 hello %{buildroot}/usr/sbin
%{__install} -p -m0755 lat_* %{buildroot}/usr/sbin
%{__install} -p -m0755 line %{buildroot}/usr/sbin
%{__install} -p -m0755 lmdd %{buildroot}/usr/sbin
%{__install} -p -m0755 lmhttp %{buildroot}/usr/sbin
%{__install} -p -m0755 loop_o %{buildroot}/usr/sbin
%{__install} -p -m0755 memsize %{buildroot}/usr/sbin
%{__install} -p -m0755 mhz %{buildroot}/usr/sbin
%{__install} -p -m0755 msleep %{buildroot}/usr/sbin
%{__install} -p -m0755 par_* %{buildroot}/usr/sbin
%{__install} -p -m0755 stream %{buildroot}/usr/sbin
%{__install} -p -m0755 timing_o %{buildroot}/usr/sbin
%{__install} -p -m0755 tlb %{buildroot}/usr/sbin
cd -

%{__install} -p -m0644 doc/*.1 %{buildroot}%{_mandir}/man1/
%{__install} -p -m0644 doc/*.3 %{buildroot}%{_mandir}/man3/
%{__install} -p -m0644 doc/*.8 %{buildroot}%{_mandir}/man8/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGEMENTS CHANGES COPYING COPYING-2 README hbench-REBUTTAL doc/*.ms
%doc %{_mandir}/man?/*
/usr/sbin/*

%changelog
* Tue Jan 09 2007 Dmitri Kuzishchin <dim@altlinux.ru> 3.0-alt2
- Change path from /usr/bin to /usr/sbin.

* Sat May 13 2006 Dmitri Kuzishchin <dim@altlinux.ru> 3.0-alt1
- Initial package.
