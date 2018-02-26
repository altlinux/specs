Name: appliance-rescue-static
Summary: Virtual package that requires useful static-linked utilites
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

Requires: ash-static
Requires: find-static
Requires: cpio-static
Requires: rpm-static
Requires: lvm2-static

%description
%summary
If you broke your system by remove or modify core system libraries,
this packages can help you in fixing your system.
Recommended to install in all non-virtual servers

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

