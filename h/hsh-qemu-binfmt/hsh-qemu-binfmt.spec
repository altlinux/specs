Name: hsh-qemu-binfmt
Version: 0.002
Release: alt1
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: register qemu for hasher chroot
Group: Development/Other
License: GPL2+
Url: https://www.altlinux.org/Hasher
Source: %name-%version.tar

# BuildArch: is arch, because different arches need different emulators
BuildRequires: qemu-user-static-binfmt
Requires: hasher qemu-user-static

%description
Hasher supports cross-platform package builds using qemu.
For that qemu binaries for different architectures should be registered
in binfmt_misc kernel module, and at that not on their system path in /usr/bin,
but on a special path /.host/qemu-<arch> which is relative to hasher chroot
and is created by hasher during cross-platform build.

%prep
%setup

%build
mkdir binfmt.d
for conf in /lib/binfmt.d/qemu-*.conf; do
    j=`basename $conf | sed 's,-static.conf$,,'`
    sed 's,:/usr/bin/qemu-\([a-zA-Z0-9]*\)[-\.]static:.*$,:/.host/qemu-\1:F,' $conf > binfmt.d/$j
done

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/%name/binfmt.d
for j in binfmt.d/* ; do
    install -m644 $j $RPM_BUILD_ROOT%_datadir/%name/$j
done

mkdir -p $RPM_BUILD_ROOT{%_bindir,%_sbindir}
install -m 755 bin/hsh-qemu-binfmt-status $RPM_BUILD_ROOT%_bindir/
ln -s ../bin/hsh-qemu-binfmt-status $RPM_BUILD_ROOT%_sbindir/hsh-qemu-binfmt-register
ln -s ../bin/hsh-qemu-binfmt-status $RPM_BUILD_ROOT%_sbindir/hsh-qemu-binfmt-unregister

install -D -m644 %{name}.sysconfig $RPM_BUILD_ROOT%_sysconfdir/sysconfig/%name
install -D -m644 %{name}.service $RPM_BUILD_ROOT%_unitdir/%{name}.service
install -D -m755 %{name}.init $RPM_BUILD_ROOT%_initdir/%{name}

%post
%post_service %{name}
%preun
%preun_service %{name}

%files
%dir %_datadir/%name
%_datadir/%name/binfmt.d
%_bindir/%name-*
%_sbindir/%name-*
%config(noreplace) %_sysconfdir/sysconfig/%name
%_unitdir/%{name}.service
%_initdir/%{name}

%changelog
* Thu Aug 08 2019 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- new version

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version

