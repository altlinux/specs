Name: appliance-base-compress-all
Summary: Virtual package that require all compress-related utilites
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

Requires: appliance-base-compress-minimal

# Archive
Requires: cpio

# Copmression
Requires: zip unzip
Requires: xz

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

