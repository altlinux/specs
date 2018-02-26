Name: appliance-devel-alt
Summary: Virtual package that require ALT-specific devel packages
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: Development/Other

Requires: appliance-devel-base
Requires: appliance-devel-debug
Requires: appliance-devel-distro

Requires: gear git tig
Requires: hasher

Requires: rpm-utils

Requires: rpm-build
Requires: rpm-build-intro
Requires: rpm-build-perl
Requires: rpm-build-python
Requires: rpm-build-tcl

Requires: cpan2rpm

Requires: srpmcmp qa-robot

# C programming
Requires: indent

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

