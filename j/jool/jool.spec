Name: jool
Version: 3.4.3
Release: alt1
Summary: Jool is an Open Source implementation of IPv4/IPv6 Translation on Linux.
Group: Networking/Other

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPLv3
Url: https://www.jool.mx/
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
AutoProv: yes

BuildRequires: libnl-devel
BuildPreReq: rpm-build-kernel

%description
SIIT (Stateless IP/ICMP Translation) and NAT64 ("NAT six four", not "NAT
sixty-four") are technologies meant to communicate networking nodes which
only speak IPv4 with nodes that only speak IPv6.

The idea is basically that of an "upgraded" NAT; an "IPv4/IPv6 translator"
not only replaces addresses and/or ports within packets, but also
layer 3 headers.

 * SIIT is the simpler form, and allows preconfigured 1-to-1 mappings
   between IPv4 addresses and IPv6 addresses.

 * A Stateful NAT64 (or NAT64 for short) allows several IPv6 nodes to
   dynamically share few IPv4 addresses (useful when you're a victim of
   IPv4 address exhaustion).

For historic reasons, sometimes we mess up and label SIIT as "Stateless
NAT64". Because this expression does not seem to appear in any relevant
standards, we consider it imprecise, despite the fact it makes some degree
of sense. If possible, please try to suppress it.

%package -n kernel-source-%name
Summary: Kernel module for Jool NAT64
License: GPLv3
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
Provide Jool NAT64 kernel module


%prep
%setup
%patch0 -p1
tar -cjf ../%name-%version.tar.bz2 ../%name-%version

%build
pushd usr
./autogen.sh
%configure
%make_build
popd

%install
pushd usr
%makeinstall
popd

mkdir -p %kernel_srcdir
install -pDm0644 ../%name-%version.tar.bz2 %kernel_srcdir/%name-%version.tar.bz2

%files
%doc COPYING README.md usr/README
%_bindir/*
%_mandir/man8/*

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Thu May 12 2016 Alexei Takaseev <taf@altlinux.org> 3.4.3-alt1
- 3.4.3

* Mon Nov 23 2015 Alexei Takaseev <taf@altlinux.org> 3.4.2-alt1
- 3.4.2

* Thu Nov 12 2015 Alexei Takaseev <taf@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Oct 27 2015 Alexei Takaseev <taf@altlinux.org> 3.3.5-alt1
- 3.3.5

* Tue Sep 22 2015 Alexei Takaseev <taf@altlinux.org> 3.3.4-alt1
- 3.3.4

* Wed Sep 02 2015 Alexei Takaseev <taf@altlinux.org> 3.3.3-alt1
- Initial build for ALT Linux Sisyphus
