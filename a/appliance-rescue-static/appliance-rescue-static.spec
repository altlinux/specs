Url: http://www.altlinux.org/Appliances
Name: appliance-rescue-static
Summary: Virtual package that requires useful static-linked utilites
BuildArch: noarch
Version: 4.0.1
Release: alt3
License: GPL
Group: System/Base

Requires: ash-static
Requires: find-static
Requires: cpio-static
Requires: lvm2-static

%description
%summary
If you broke your system by remove or modify core system libraries,
this packages can help you in fixing your system.
Recommended to install in all non-virtual servers

%files

%changelog
* Wed Sep 07 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.1-alt3
- Dropped R: rpm-static.

* Sun Jun 16 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt2
- add Url tag

* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

