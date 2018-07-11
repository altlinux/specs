Name: livecd-qemu-arch
Version: 0.4
Release: alt1

Summary: prepare live-builder.iso for ARM/PPC/aarch64/mipsel QEMU
License: Public domain
Group: System/Configuration/Other

Url: http://www.altlinux.org/Ports
BuildArch: noarch
ExclusiveArch: x86_64 %ix86

Requires: qemu-user-binfmt_misc
AutoReqProv: no

%description
%summary

%prep

%install
mkdir -p %buildroot{%_bindir,%_sysconfdir/apt}

cat > %buildroot%_bindir/register-qemu-mipsel << EOF
#!/bin/sh
# https://www.altlinux.org/Ports/mipsel/BuildHowto
modprobe binfmt_misc
sleep 0.1
[ -d /proc/sys/fs/binfmt_misc ] || exit 1
echo ':mipsel:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x08\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/.host/qemu-mipsel:' > /proc/sys/fs/binfmt_misc/register
echo 32768 > /proc/sys/vm/mmap_min_addr
EOF

cat > %buildroot%_bindir/register-qemu-aarch64 << EOF
#!/bin/sh
# https://www.altlinux.org/Ports/aarch64
modprobe binfmt_misc
sleep 0.1
[ -d /proc/sys/fs/binfmt_misc ] || exit 1
echo ":aarch64:M::\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\xb7:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff:/.host/qemu-aarch64:" > /proc/sys/fs/binfmt_misc/register
echo 32768 > /proc/sys/vm/mmap_min_addr
EOF

cat > %buildroot%_bindir/register-qemu-armh << EOF
#!/bin/sh
# https://www.altlinux.org/Ports/arm/BuildHowto
modprobe binfmt_misc
sleep 0.1
[ -d /proc/sys/fs/binfmt_misc ] || exit 1
echo ":armh:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x28\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/.host/qemu-arm:" > /proc/sys/fs/binfmt_misc/register
echo 32768 > /proc/sys/vm/mmap_min_addr
EOF

cat > %buildroot%_bindir/register-qemu-ppc << EOF
#!/bin/sh
# https://www.altlinux.org/Ports/ppc
modprobe binfmt_misc
sleep 0.1
[ -d /proc/sys/fs/binfmt_misc ] || exit 1
echo ':ppc:M::\x7fELF\x01\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x14:\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff:/.host/qemu-ppc:' > /proc/sys/fs/binfmt_misc/register
echo 32768 > /proc/sys/vm/mmap_min_addr
EOF

cat > %buildroot%_sysconfdir/apt/apt.conf.sisyphus.mipsel << EOF
Dir::Etc::main "/dev/null";
Dir::Etc::parts "/var/empty";
Dir::Etc::SourceParts "/var/empty";
Dir::Etc::sourcelist "/etc/apt/sources.list.sisyphus.mipsel";
EOF

cat > %buildroot%_sysconfdir/apt/sources.list.sisyphus.mipsel << EOF
# https://www.altlinux.org/Ports/mipsel
rpm http://ftp.altlinux.org/pub/distributions/ALTLinux/ports/mipsel Sisyphus/mipsel classic
rpm http://ftp.altlinux.org/pub/distributions/ALTLinux/ports/mipsel Sisyphus/noarch classic
#Yandex mirror
#rpm http://mirror.yandex.ru/altlinux/ports/mipsel Sisyphus/mipsel classic
#rpm http://mirror.yandex.ru/altlinux/ports/mipsel Sisyphus/noarch classic
EOF

cat > %buildroot%_sysconfdir/apt/apt.conf.sisyphus.aarch64 << EOF
Dir::Etc::main "/dev/null";
Dir::Etc::parts "/var/empty";
Dir::Etc::SourceParts "/var/empty";
Dir::Etc::sourcelist "/etc/apt/sources.list.sisyphus.aarch64";
EOF

cat > %buildroot%_sysconfdir/apt/sources.list.sisyphus.aarch64 << EOF
# https://www.altlinux.org/Ports/aarch64
rpm http://ftp.altlinux.org/pub/distributions/ALTLinux/Sisyphus aarch64 classic
rpm http://ftp.altlinux.org/pub/distributions/ALTLinux/Sisyphus noarch classic
EOF

cat > %buildroot%_sysconfdir/apt/apt.conf.sisyphus.armh << EOF
Dir::Etc::main "/dev/null";
Dir::Etc::parts "/var/empty";
Dir::Etc::SourceParts "/var/empty";
Dir::Etc::sourcelist "/etc/apt/sources.list.sisyphus.armh";
EOF

cat > %buildroot%_sysconfdir/apt/sources.list.sisyphus.armh << EOF
# https://www.altlinux.org/Ports/arm
rpm http://ftp.altlinux.org/pub/distributions/ALTLinux/ports/armh/Sisyphus armh classic
EOF

cat > %buildroot%_sysconfdir/apt/apt.conf.4.1.ppc << EOF
Dir::Etc::main "/dev/null";
Dir::Etc::parts "/var/empty";
Dir::Etc::SourceParts "/var/empty";
Dir::Etc::sourcelist "/etc/apt/sources.list.4.1.ppc";
EOF

cat > %buildroot%_sysconfdir/apt/sources.list.4.1.ppc << EOF
# https://www.altlinux.org/Ports/ppc
rpm http://ftp.altlinux.org/pub/people/wart/repos/lioka/powerpc ppc classic
rpm http://ftp.altlinux.org/pub/people/wart/repos/lioka/powerpc ppc64 classic
rpm http://ftp.altlinux.org/pub/people/wart/repos/lioka/powerpc noarch classic
EOF

%files
%_sysconfdir/apt/apt.conf.*
%_sysconfdir/apt/sources.list.*
%attr(755,root,root) %_bindir/register-qemu-*

%changelog
* Wed Jul 11 2018 Dmitry Terekhin <jqt4@altlinux.org> 0.4-alt1
- added mipsel support

* Thu Jul 05 2018 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- fixed aarch64 support (closes: #34638); thx zorg@ for the patch
- replaced arm with armh (thx aen@ for updated repo url)
- added wiki links

* Sun Oct 08 2017 Mike Radyuk <torabora@altlinux.org> 0.2-alt1
- added aarch64 support

* Wed Aug 01 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial build
