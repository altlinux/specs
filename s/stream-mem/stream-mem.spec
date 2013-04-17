Name: stream-mem
Version: 5.8
Release: alt2.qa1

Summary: STREAM: Sustainable Memory Bandwidth in High Performance Computers
License: GPL
Group: Monitoring

Url: http://www.cs.virginia.edu/stream/
Source0: stream-%version.tar.gz
Source1: stream-Makefile
Packager: Michael Shigorin <mike@altlinux.org>

%description
The STREAM benchmark is a simple synthetic benchmark program that
measures sustainable memory bandwidth (in MB/s) and the corresponding
computation rate for simple vector kernels.

%prep
%setup -n stream-%version
cp -a %SOURCE1 Makefile

%build
%make

%install
%makeinstall_std BIN_DIR=%_bindir

%files
%_bindir/*

%changelog
* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 5.8-alt2.qa1
- NMU: rebuilt for debuginfo.

* Thu Oct 15 2009 Michael Shigorin <mike@altlinux.org> 5.8-alt2
- built for Sisyphus

* Sat Jul 19 2008 Mikhail Yakshin <greycat@altlinux.org> 5.8-alt1
- Initial build

