%define _unpackaged_files_terminate_build 1

Name:    bpfmon
Version: 2.52
Release: alt1

Summary: Traffic monitor for BPF expression/iptables rule
License: GPL-2.0
Group:   Monitoring
Url:     https://github.com/bbonev/bpfmon

Source: %name-%version.tar

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

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std PREFIX=%prefix STRIP=
install -p -m 644 bpfmon.8 %buildroot/%_man8dir/bpfmon.8

%files
%doc *.md
%_sbindir/%name
%_man8dir/%name.8*


%changelog
* Thu Feb 22 2024 Pavel Shilov <zerospirit@altlinux.org> 2.52-alt1
- Initial build for Sisyphus

