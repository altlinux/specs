# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%global __find_debuginfo_files %nil
%set_verify_elf_method skip

Name: qemu-system-aarch64-core-bundle
Summary: Native qemu-system-aarch64 binary bundle
Version: 0
Release: alt1
License: BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group: Emulators

ExclusiveArch: aarch64
BuildArch: noarch
AutoReqProv: no
BuildRequires: glibc-devel-static
BuildRequires: qemu-system-aarch64-core
%define get_strict_dep() %(rpmquery --qf '%%{NAME} = %%|epoch?{%%{epoch}:}|%%{version}-%%{release}%%|disttag?{:%%{disttag}}|' %1 2>/dev/null || echo '%1 = unknown')
Requires: %{get_strict_dep qemu-system-aarch64-core}

%description
Wondrous package to run qemu-system-aarch64 on armh to access KVM.
     ,,
    /,`\
    ` | \____/\
     _(      ) \
     \-\~~~_|\  \
     `  \ `   \  `
        `     `

%prep
%setup -cT

%build
gcc %optflags -s -o kvm_ok -xc - <<'EOF'
#include <fcntl.h>
int main(void)
{
	return open("/dev/kvm", O_RDONLY) < 0;
}
EOF

%install
%define bundle %_datadir/%name
T=%buildroot%bundle
BINARY=%_bindir/qemu-system-aarch64
INTERP=$(readelf -W -l $BINARY |
        sed -ne 's,^[[:space:]]*\[Requesting program interpreter: \(/[^]]\+\)\]$,\1,p')

mkdir -p $T
cp -v -a $BINARY $INTERP kvm_ok $T/
ldd $BINARY | cut -d' ' -f 3 | grep / | xargs -i -- cp -v -p {} $T/

mkdir -p %buildroot%_bindir
%define wrapper %_bindir/qemu-system-aarch64-bundle
cat <<EOF > %buildroot%wrapper
#!/bin/sh
exec %bundle/$(basename $INTERP) --library-path %bundle %bundle/$(basename $BINARY) "\$@"
EOF
chmod a+x %buildroot%wrapper

%define kvm_ok %wrapper-kvm-ok
cat <<EOF > %buildroot%wrapper-kvm-ok
#!/bin/sh
exec %bundle/$(basename $INTERP) --library-path %bundle %bundle/kvm_ok
EOF
chmod a+x %buildroot%wrapper-kvm-ok

%files
%bundle
%wrapper
%kvm_ok

%changelog
* Wed Dec 15 2021 Vitaly Chikunov <vt@altlinux.org> 0-alt1
- Initial version.
