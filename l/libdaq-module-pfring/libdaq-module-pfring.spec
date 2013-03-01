%def_disable static

Name: libdaq-module-pfring
Version: 0.1
Release: alt2

Summary: PF_RING support of snort DAQ
License: GPLv2
Group: System/Libraries
Url: http://www.ntop.org/PF_RING.html

Source: %name-%version.tar

Requires: libpfring1.0 >= 1.0.0
BuildRequires: libpfring-devel >= 1.0.0
BuildRequires: libdaq-devel

%description
PF_RING is a high speed packet capture library that turns a commodity PC into an efficient and cheap
network measurement box suitable for both packet and active traffic analysis and manipulation.
Moreover, PF_RING opens totally new markets as it enables the creation of efficient application such as
traffic balancers or packet filters in a matter of lines of codes.

PF_RING support of snort DAQ

%prep
%setup -q

%build
autoreconf -ifv
%configure
%make_build

%install
%makeinstall_std

%files
%_libdir/daq/*.so

%changelog
* Fri Mar 01 2013 Timur Aitov <timonbl4@altlinux.org> 0.1-alt2
- fix requires

* Fri Mar 01 2013 Timur Aitov <timonbl4@altlinux.org> 0.1-alt1
- initial build
