Name: qperf
Summary: Measure socket and RDMA performance
Version: 0.4.11
Release: alt2
Group: Networking/Other
License: %gpl2only
Url: https://github.com/linux-rdma/qperf
Source: %name-%version.tar
BuildRequires(pre): rpm-build-licenses
Buildrequires: librdmacm-devel perl-devel perl-diagnostics

%description
Measure socket and RDMA performance.

%prep
%setup

%build
touch NEWS README ChangeLog
%autoreconf
%configure
%make_build

%install
install -D -m 0755 {src,%buildroot%_bindir}/%name
install -D -m 0644 {src,%buildroot%_man1dir}/%name.1

%files
%doc AUTHORS
%_bindir/*
%_man1dir/*

%changelog
* Sun Apr 28 2024 Anton Farygin <rider@altlinux.ru> 0.4.11-alt2
- fixed FTBFS

* Fri Aug 20 2021 Anton Farygin <rider@altlinux.ru> 0.4.11-alt1
- new version

* Wed Feb 04 2015 Anton Farygin <rider@altlinux.ru> 0.4.9-alt1
- new version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.6-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Aug 18 2010 Andriy Stepanov <stanv@altlinux.ru> 0.4.6-alt1
- 0.4.6 (OFED 1.5.1)

* Mon Jun 08 2009 Led <led@altlinux.ru> 0.4.4-alt1
- 0.4.4

* Wed Apr 15 2009 Led <led@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Tue Oct 28 2008 Led <led@altlinux.ru> 0.4.1-alt1
- initial build for ALTLinux

* Sat Oct 20 2007 - johann@georgex.org
- Initial package
