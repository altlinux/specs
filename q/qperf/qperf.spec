Name: qperf
Summary: Measure socket and RDMA performance
Version: 0.4.6
Release: alt1
Group: Networking/Other
License: %gpl2only
Url: http://www.openfabrics.org
Source: %name-%version.tar
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
Buildrequires: librdmacm-devel perl-devel

%description
Measure socket and RDMA performance.


%prep
%setup


%build
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
