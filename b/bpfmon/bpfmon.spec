%define _unpackaged_files_terminate_build 1

Name:    bpfmon
Version: 2.60
Release: alt1

Summary: Traffic monitor for BPF expression/iptables rule
License: GPL-2.0
Group:   Monitoring
Url:     https://github.com/bbonev/bpfmon

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libpcap-devel
BuildRequires: libyascreen-devel

%description
While tcpdump shows what packets are going through the
network, bpfmon will show how much in terms
of bytes per second and packets per second in a
nice pseudo-graphical terminal interface.

bpfmon also supports monitoring an iptables rule that
is selected by command line option or selected from a
menu.

%prep
%setup
%patch -p1

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std PREFIX=%buildroot%_prefix STRIP=:

%files
%doc *.md
%_sbindir/%name
%_man8dir/%name.8*


%changelog
* Mon Aug 10 2026 Pavel Shilov <zerospirit@altlinux.org> 2.60-alt1
- updated from 2.53 to 2.60

* Wed Nov 13 2024 Pavel Shilov <zerospirit@altlinux.org> 2.53-alt1
- Update version based on upstream

* Thu Feb 22 2024 Pavel Shilov <zerospirit@altlinux.org> 2.52-alt1
- Initial build for Sisyphus

