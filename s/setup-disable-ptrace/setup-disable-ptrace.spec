Name: setup-disable-ptrace
Version: 0.1
Release: alt2

Summary: disable kernel ptrace()
License: public domain
Group: System/Configuration/Other

BuildArch: noarch
AutoReqProv: no

%set_verify_elf_method none
%define sysctldir %_sysconfdir/sysctl.d
%define sysstring kernel.yama.ptrace_scope = 3
%define procknob /proc/sys/kernel/yama/ptrace_scope

%description
%summary as a hardening measure

%install
mkdir -p %buildroot%sysctldir
echo "%sysstring" > %buildroot%sysctldir/50-ptrace.conf

%post
if [ ! -f %procknob ]; then
        echo "setup-disable-ptrace: need CONFIG_SECURITY_YAMA=y and /proc" >&2
	exit 0
fi
if ! grep -Fqsx 3 "%procknob"; then
        echo "setup-disable-ptrace: %sysstring" >&2
        echo 3 > %procknob
fi

%files
%config(noreplace) %sysctldir/50-ptrace.conf

%changelog
* Fri Aug 15 2025 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- safeguard against missing /proc bits (or altogether)

* Fri Mar 01 2019 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (thx bircoph@)

