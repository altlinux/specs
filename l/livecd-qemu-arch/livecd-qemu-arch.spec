Name: livecd-qemu-arch
Version: 0.1
Release: alt1

Summary: prepare live-builder.iso for ARM/PPC QEMU
License: Public domain
Group: System/Configuration/Other

Url: http://www.altlinux.org/Ports/arm
BuildArch: noarch
ExclusiveArch: x86_64 %ix86

Requires: qemu-user-binfmt_misc
AutoReqProv: no

%description
%summary

%prep

%install
mkdir -p %buildroot{%_bindir,%_sysconfdir/apt}

cat > %buildroot%_bindir/register-qemu-arm << EOF
#!/bin/sh
modprobe binfmt_misc
sleep 0.1
[ -d /proc/sys/fs/binfmt_misc ] || exit 1
echo ":arm:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x28\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/.host/qemu-arm:" > /proc/sys/fs/binfmt_misc/register
echo 32768 > /proc/sys/vm/mmap_min_addr
EOF

cat > %buildroot%_bindir/register-qemu-ppc << EOF
#!/bin/sh
modprobe binfmt_misc
sleep 0.1
[ -d /proc/sys/fs/binfmt_misc ] || exit 1
echo ':ppc:M::\x7fELF\x01\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x14:\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff:/.host/qemu-ppc:' > /proc/sys/fs/binfmt_misc/register
echo 32768 > /proc/sys/vm/mmap_min_addr
EOF

cat > %buildroot%_sysconfdir/apt/apt.conf.sisyphus.arm << EOF
Dir::Etc::main "/dev/null";
Dir::Etc::parts "/var/empty";
Dir::Etc::SourceParts "/var/empty";
Dir::Etc::sourcelist "/etc/apt/sources.list.sisyphus.arm";
EOF

cat > %buildroot%_sysconfdir/apt/sources.list.sisyphus.arm << EOF
rpm http://ftp.altlinux.org/pub/distributions/ALTLinux/Sisyphus arm classic
EOF

cat > %buildroot%_sysconfdir/apt/apt.conf.4.1.ppc << EOF
Dir::Etc::main "/dev/null";
Dir::Etc::parts "/var/empty";
Dir::Etc::SourceParts "/var/empty";
Dir::Etc::sourcelist "/etc/apt/sources.list.4.1.ppc";
EOF

cat > %buildroot%_sysconfdir/apt/sources.list.4.1.ppc << EOF
rpm http://ftp.altlinux.org/pub/people/wart/repos/lioka/powerpc ppc classic
rpm http://ftp.altlinux.org/pub/people/wart/repos/lioka/powerpc noarch classic
EOF

%files
%_sysconfdir/apt/apt.conf.*
%_sysconfdir/apt/sources.list.*
%attr(755,root,root) %_bindir/register-qemu-*

%changelog
* Wed Aug 01 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial build
