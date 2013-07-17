Name: kvm-on-demand
Version: 0.1.0
Release: alt1
Summary: Udev rules to load kvm kernel modules on demand
License: GPLv3+
Group: Emulators
Source0: %name.sh.in
Source1: %name.rules.in
Source2: blacklist-kvm.conf
Source3: kvm.conf
BuildArch: noarch

%description
Udev rules to load kvm kernel modules on demand.


%prep
install -p -m 0644 %{S:0} ./%name.sh.in
install -p -m 0644 %{S:1} ./%name.rules.in
install -p -m 0644 %{S:2} ./blacklist-kvm.conf
install -p -m 0644 %{S:3} ./kvm.conf


%build
for f in *.in; do
	sed 's/@name@/%name/' $f > $(basename $f .in)
done


%install
install -pD -m 0755 %name.sh %buildroot/lib/udev/%name
install -d -m 0755 %buildroot%_sysconfdir/{modprobe,udev/rules}.d
install -p -m 0644 *.rules %buildroot%_sysconfdir/udev/rules.d/
install -p -m 0644 *.conf %buildroot%_sysconfdir/modprobe.d/


%files
%attr(0744,root,root) /lib/udev/*
%_sysconfdir/udev/rules.d/*
%config(noreplace) %_sysconfdir/modprobe.d/*


%changelog
* Wed Jul 17 2013 Led <led@altlinux.ru> 0.1.0-alt1
- 0.1.0
