Name: perftest
Summary: IB Performance tests
Version: 1.3.0
Release: alt1
License: %gpl2only
Group: Monitoring
Url: http://www.openfabrics.org
Source: %name-%version.tar
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: librdmacm-devel
BuildRequires: libibumad-devel

%description
gen2 uverbs microbenchmarks.

%prep
%setup
chmod 644 *

%build
%make_build CFLAGS="%optflags -D_GNU_SOURCE"

%install
install -d -m 0755 %buildroot%_bindir
install -m 0755 ib_{clock_test,{read,send,write}_{bw,lat},write_bw_postlist} rdma_{bw,lat} %buildroot%_bindir/

%files
%doc README COPYING runme
%_bindir/*

%changelog
* Thu Dec 16 2010 Timur Aitov <timonbl4@altlinux.org> 1.3.0-alt1
- New version

* Thu Sep 02 2010 Andriy Stepanov <stanv@altlinux.ru> 1.2.3-alt2
- Rebuild with new libibumad

* Wed Aug 18 2010 Andriy Stepanov <stanv@altlinux.ru> 1.2.3-alt1
- OFED 1.5.1

* Tue Oct 28 2008 Led <led@altlinux.ru> 1.2-alt1
- initial build for ALTLinux

* Mon Jul 09 2007 - hvogel@suse.de
- Use correct version
* Wed Jul 04 2007 - hvogel@suse.de
- Add GPL COPYING file [#289509]
* Mon Jul 02 2007 - hvogel@suse.de
- Update to the OFED 1.2 version
* Fri Jun 22 2007 - hvogel@suse.de
- Initial Package, Version 1.1
