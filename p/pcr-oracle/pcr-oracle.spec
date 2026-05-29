%define _unpackaged_files_terminate_build 1

%def_with check

%ifarch aarch64
%global swtpm_device tpm-tis-device
%else
%global swtpm_device tpm-tis
%endif

Name: pcr-oracle
Version: 0.6.3
Release: alt1

Summary: Predict TPM PCR values for future boot
License: GPL-2.0
Group: System/Configuration/Boot and Init

Url: https://github.com/openSUSE/pcr-oracle
VCS: https://github.com/openSUSE/pcr-oracle
Source: %name-%version.tar

BuildRequires: libelf-devel
BuildRequires: libssl-devel
BuildRequires: libfdisk-devel
BuildRequires: libjson-c-devel
BuildRequires: libtpm2-tss-devel

%if_with check
BuildRequires: swtpm
BuildRequires: openssl
BuildRequires: tpm2-tools
BuildRequires: rpm-build-vm
%endif

%description
This tool tries to predict TPM PCR  values for future boot, based on the current
state of the system it runs in.

The top objective in creating this tool  is to support full disk encryption, and
be able to have the TPM unseal  the encryption key that is protecting the system
partition. Of course, as  changes are made to the system,  the PCR values during
boot will change, making it necessary to adjust the policy that's protecting the
SRK. Examples include updates of the shim and/or boot loader, or changes made to
the GPT of the hard disk that EFI is booting from.

The primary mode of  operation uses the TPM event log to  replay the sequence of
PCR Extend operations. However, instead of hashing the event as contained in the
event log,  it will use the  current values of EFI  variables, boot applications
and files etc as found in the running system.

%prep
%setup

# fix libjson pkgname
sed -i '/uc_pkg_config_check_package/ s/json/json-c/' ./microconf/stage3/05-json
sed -i 's/JSON/JSON_C/g' ./Makefile.in

# fix bindir
sed -i 's|/bin|%_bindir|' ./Makefile.in

%build

./configure \
    --mandir=%_mandir \
    --with-os-vendor=altlinux \
    --with-libjson \
    --enable-manpages

%make_build

%install
%makeinstall_std

%check
mkdir -p $TMPDIR/swtpm
swtpm socket --tpm2 --tpmstate dir=$TMPDIR/swtpm \
      --ctrl type=unixio,path=$TMPDIR/swtpm/swtpm-sock &

vm-run --sbin --udevd --kvm=cond \
       -chardev socket,id=chrtpm,path=$TMPDIR/swtpm/swtpm-sock \
       -tpmdev emulator,id=tpm0,chardev=chrtpm \
       -device %swtpm_device,tpmdev=tpm0 \
       --heredoc <<EOF
set -eux
for test in ./test*.sh; do
    \$test
done
EOF

%files
%doc README.md LICENSE
%_bindir/pcr-oracle
%_man8dir/pcr-oracle.*

%changelog
* Thu May 28 2026 Egor Ignatov <egori@altlinux.org> 0.6.3-alt1
- New version 0.6.3.

* Fri Apr 24 2026 Egor Ignatov <egori@altlinux.org> 0.6.0-alt1
- New version 0.6.0.

* Mon Apr 20 2026 Egor Ignatov <egori@altlinux.org> 0.5.4-alt1
- First build for ALT.
