# -*- coding: latin-1; mode: rpm-spec -*-

Name: logwatch-smartarray
Version: 0.1
Release: alt1

Summary: Logwatch addon to show SmartArray status in output
License: GPLv3
Group: Monitoring
Url: http://git.altlinux.org/people/evg/packages/logwatch-smartarray.git
Source: %name-%version.tar
Requires: logwatch, cciss_vol_status
BuildArch: noarch

Packager: Evgenii Terechkov <evg@altlinux.org>

%description
Logwatch addon to show SmartArray status in output

Just install it and you will have cciss_vol_status output in your
everyday digest.

%prep
%setup
%build
%install
install -pD -m644 zz-smartarray.conf %buildroot%_sysconfdir/logwatch/conf/services/zz-smartarray.conf
install -pD -m755 zz-smartarray %buildroot%_sysconfdir/logwatch/scripts/services/zz-smartarray

%files
%config(noreplace) %_sysconfdir/logwatch/conf/services/zz-smartarray.conf
%_sysconfdir/logwatch/scripts/services/zz-smartarray

%changelog
* Tue Apr 12 2011 Terechkov Evgenii <evg@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisypus
