Name: ima-integrity-check
Version: 0.5.2
Release: alt1

Summary: IMA integrity check
License: %gpl2plus
Group: System/Base
Packager: Denis Medvedev <nbr@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: make-initrd

Requires: %name-make-initrd-integrity

Conflicts: cert-distro-updater
Conflicts: ima-evm-integrity-check

%define _unpackaged_files_terminate_build 1

%description
This package make use of the IMA  technologies from the Linux integrity
subsystem for preparation of verification of integrity of files.
This package requires kernel with corresponding config options enabled.

%package -n %name-make-initrd-integrity
Summary: Integrity check feature for make-initrd
Group: System/Base

# For put-file utility
Requires: make-initrd >= 0.7.6-alt1
Requires: keyutils ima-evm-utils
Requires: filesystem >= 2.3.13-alt1.M80C.1
Conflicts: make-initrd-integrity
Conflicts: cert-distro-updater

BuildArch: noarch

%description -n %name-make-initrd-integrity
Integrity check feature for make-initrd

%prep
%setup

%build
LIBDIRS="/%_lib %_libdir"
if [ %_lib = lib64 ]; then
	# There is some shared objects too
	LIBDIRS="$LIBDIRS /lib %_usr/lib"
fi
LIBEXECDIRS="%_usr/libexec $LIBDIRS"

sed -r -e "s;@LIBDIRS@;$LIBDIRS;" -e "s;@EXECLIBDIRS@;$LIBEXECDIRS;" integrity-sign.in >integrity-sign
chmod +x integrity-sign

%install
install -pD -m 700 integrity-sign %buildroot%_sbindir/integrity-sign
install -pD -m 700 integrity-applier %buildroot%_bindir/integrity-applier
install -pD -m 700 integrity-remover %buildroot%_bindir/integrity-remover
install -pD -m 700 utils/signing  %buildroot%_sbindir/signing
install -pD -m 700 utils/signing-utils  %buildroot%_sbindir/signing-utils
install -pD -m 700 utils/signing.utils.parse  %buildroot%_sbindir/signing.utils.parse
install -pD -m 600 units/signing.service %buildroot%_unitdir/signing.service



# make-initrd feature
mkdir -p %buildroot%_sysconfdir/integrity/
mkdir -p %buildroot%_datadir/integrity/
mkdir -p %buildroot%_datadir/make-initrd/features/integrity/
cp -a make-initrd/*.mk %buildroot%_datadir/make-initrd/features/integrity/

MI_VERSION="$(/usr/sbin/make-initrd --version | sed -n -r 's;^make-initrd version ([[:digit:]]+)\..*;\1;p')"
if [ -n "$MI_VERSION" ] && [ "$MI_VERSION" -ge 2 ]; then
	install -pD -m 755 make-initrd/integrity.init %buildroot%_datadir/make-initrd/features/integrity/data/etc/rc.d/init.d/integrity
else
	mkdir -p %buildroot%_datadir/make-initrd/features/integrity/data/lib/initrd/modules/
	cp -a make-initrd/085-integrity %buildroot%_datadir/make-initrd/features/integrity/data/lib/initrd/modules/
fi

%files
%doc policy.example
%doc README
%_bindir/integrity-applier
%_bindir/integrity-remover
%_sbindir/integrity-sign
%_sbindir/signing
%_sbindir/signing-utils
%_sbindir/signing.utils.parse
%_unitdir/signing.service




%files -n %name-make-initrd-integrity
%dir %_sysconfdir/integrity/
%dir %_datadir/integrity/
%_datadir/make-initrd/features/integrity

%changelog
* Tue Feb 13 2024 Denis Medvedev <nbr@altlinux.org> 0.5.2-alt1
- changed operations to manual signing.

* Mon Dec 25 2023 Denis Medvedev <nbr@altlinux.org> 0.5.1-alt1
- Initial release, based on ima-evm-integrity-check and parts of
cert-distro-updater
