Name: sdpnetstat
URL: http://www.openfabrics.org
License: GPL v2 or later
Group: Networking/Other
Version: 1.60
Release: alt1
Packager: Andriy Stepanov <stanv@altlinux.ru>
Summary: netstat for SDP
Source: %name-%version.tar
Source1: config.h

%description
netstat for SDP

%prep
%setup -q
install -m0644 %SOURCE1 %_builddir/%name-%version

%build
%make netstat

%install
install -D -m 0755 netstat $RPM_BUILD_ROOT%{_bindir}/sdpnetstat

%files
%_bindir/sdpnetstat

%changelog
* Wed Aug 18 2010 Andriy Stepanov <stanv@altlinux.ru> 1.60-alt1
- OFED 1.5.1
