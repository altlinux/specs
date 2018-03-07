Name: ipt-so
Version: 1.0
Release: alt1

Summary: Iptables match for Security Options (IPSO) Labels
License: GPLv2
Group: System/Kernel and hardware
Requires: iptables

Url: https://github.com/vt-alt/ipt-so
Source0: %name-%version.tar

BuildPreReq: rpm-build-kernel
BuildRequires: libiptables-devel

%description
Iptables match for Security Options (IPSO) Labels (userspace part).

%package -n kernel-source-%name
Summary: Iptables match for Security Options (IPSO) Labels (source)
Group: Development/Kernel
BuildArch: noarch
%description -n kernel-source-%name
Iptables match for Security Options (IPSO) Labels (source).

%prep
%setup -q

%build
make libxt_so.so VERSION=%version

%install
make install-lib DESTDIR=%buildroot
install -pDm0644 %_sourcedir/%name-%version.tar %kernel_srcdir/kernel-source-%name-%version.tar

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/kernel-source-%name-%version.tar

%files
%doc README.md
/%_lib/iptables/*.so

%changelog
* Wed Mar 07 2018 Vitaly Chikunov <vt@altlinux.ru> 1.0-alt1
- Sisyphus package.
