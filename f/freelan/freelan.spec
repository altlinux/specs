Name: freelan
Version: 2.3
Release: alt3

Summary: Peer-to-peer virtual private network daemon
License: GPLv3+
Group: Networking/Other

Url: http://www.freelan.org
# repacked https://github.com/freelan-developers/freelan/archive/refs/tags/%version.tar.gz
Source0: %name-%version.tar
Source1: %name@.service
Source2: %name.init
Source3: %name.sysconfig
Source4: %name.tmpfiles

# Build errors: help2man: can't get `--help' info from build/release/bin/freelan
ExcludeArch: %arm

BuildRequires: libssl-devel
BuildRequires: boost-complete
BuildRequires: libcurl-devel
BuildRequires: libminiupnpc-devel
BuildRequires: help2man
BuildRequires: scons
Requires: openssl

%description
Freelan is an application to create secure ethernet tunnels over a
single UDP port. It can be used to create virtual LANs ("Local
Area Network"), hence the name: "freelan".

Freelan may create peer-to-peer tunnel connections or rely on a
more classic client/server layout. The virtual network can be
shaped to fit exactly the bandwidth or topology constraints,
providing an optimal virtual private network.

Freelan is particularly useful for remote sites interconnection and
gaming.

%prep
%setup

%build
%ifarch %e2k
# build/release/libs/asiotap/src/posix/posix_tap_adapter.cpp:135
%add_optflags -Wno-error=unused-function
%endif
CXXFLAGS="%optflags" \
scons %_smp_mflags \
	--mode=release apps prefix=/ bin_prefix=%_usr \
	--upnp=yes \
	--mongoose=no \
	#

%install
install -pDm755 build/release/bin/freelan %buildroot/%_bindir/%name
install -pDm755 apps/freelan/config/freelan.cfg \
	%buildroot/%_sysconfdir/%name/%name.cfg
install -pDm644 build/release/man/freelan.1 %buildroot/%_man1dir/%name.1
install -pDm644 %SOURCE1 %buildroot/%_unitdir/%name@.service
install -pDm755 %SOURCE2 %buildroot/%_initdir/%name
install -pDm640 %SOURCE3 %buildroot/%_sysconfdir/sysconfig/%name
install -pDm644 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf
install -pdm755 %buildroot%_runtimedir/%name

%pre
if [ $1 == 1 ]; then
#Add the "freelan" user and grop
	%_sbindir/groupadd -r -f %name 2>/dev/null ||:
	%_sbindir/useradd  -r -g %name -c 'Freelan daemon' \
		-s /dev/null -d /dev/null %name 2>/dev/null ||:
fi

%files
%_bindir/%name
%_man1dir/*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.cfg
%_unitdir/%name@.service
%_initdir/%name
%_tmpfilesdir/%name.conf
%_sysconfdir/sysconfig/%name
%attr(2770,root,%name) %ghost %dir %_runtimedir/%name

%preun
%preun_service %name

%changelog
* Thu Oct 14 2021 Nikolay Burykin <bne@altlinux.org> 2.3-alt3
- Added instances to init script
- Added tmpfiles.d config and user "freelan"
- Added ExcludeArch %arm to spec due to build errors

* Wed Jun 23 2021 Michael Shigorin <mike@altlinux.org> 2.3-alt2
- E2K: ftbfs workaround

* Thu Dec 17 2020 Nikolay Burykin <bne@altlinux.org> 2.3-alt1
- Initial build for ALT

* Tue May 7 2019  <sebastien.vincent@freelan.org> 2.2-1
- Version 2.2.

* Fri Aug 11 2017  <sebastien.vincent@freelan.org> 2.1-1
- First RPM version.
