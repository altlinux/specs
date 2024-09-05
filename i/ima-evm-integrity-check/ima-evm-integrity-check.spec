%define _unpackaged_files_terminate_build 1
%def_without old_make_initrd

Name: ima-evm-integrity-check
Version: 0.7.6
Release: alt1

Summary: IMA/EVM integrity check
License: %gpl2plus
Group: System/Base
Packager: Paul Wolneykien <manowar@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: bash4

BuildArch: noarch

Requires: make-initrd-integrity = %version-%release
%if_without old_make_initrd
Requires: make-initrd >= 2.0.0
%endif

Requires: /usr/bin/chattr

Conflicts: cert-distro-updater

%description
This package make use of the IMA and EVM technologies from the Linux
integrity subsystem. Basically IMA and EVM provide the following
functionality:

- measurement (hashing) of file content as it is accessed and keeping
  track of this information in an audit log;
- appraisal of files, which allows to prevent access when
  a measurement (hash) or digital signature does not match
  the expected value.

This package requires kernel with corresponding config options enabled.

%package -n make-initrd-integrity
Summary: Integrity check feature for make-initrd
Group: System/Base

# For put-file utility
Requires: make-initrd >= 0.7.6-alt1
%if_with old_make_initrd
Conflicts: make-initrd >= 2.0.0
%endif

Requires: coreutils grep kmod mount

Requires: keyutils ima-evm-utils
Requires: filesystem >= 2.3.13-alt1.M80C.1
Conflicts: cert-distro-updater

%description -n make-initrd-integrity
Integrity check feature for make-initrd

%prep
%setup

%build
%make_build libdir=%_libdir prefix=%_prefix sysconfdir=%_sysconfdir WITH_OLD_MI=%{with old_make_initrd}

%install
%makeinstall_std bindir=%_bindir sbindir=%_sbindir sysconfdir=%_sysconfdir datadir=%_datadir unitdir=%_unitdir presetdir=%_presetdir libdir=%_libdir prefix=%_prefix controldir=%_controldir mandir=%_mandir WITH_OLD_MI=%{with old_make_initrd}

%add_findreq_skiplist %_datadir/make-initrd/features/integrity/data/etc/rc.d/init.d/integrity

# For ghost:
mkdir -p %buildroot%_sysconfdir/sysconfig
touch %buildroot%_sysconfdir/sysconfig/integrity

%files
%doc README
%_sbindir/*
%_controldir/*
%_unitdir/*
%_presetdir/*
%ghost %_sysconfdir/sysconfig/integrity
%config(noreplace) %_sysconfdir/integrity/config
%_man7dir/*.7.*
%_man8dir/*.8.*

%files -n make-initrd-integrity
%dir %_sysconfdir/integrity
%_datadir/integrity
%dir %_datadir/make-initrd/features/integrity
%_datadir/make-initrd/features/integrity/*.mk
%dir %_datadir/make-initrd/features/integrity/data
%if_without old_make_initrd
%dir %_datadir/make-initrd/features/integrity/data/etc
%dir %_datadir/make-initrd/features/integrity/data/etc/rc.d
%dir %_datadir/make-initrd/features/integrity/data/etc/rc.d/init.d
%_datadir/make-initrd/features/integrity/data/etc/rc.d/init.d/integrity
%else
%dir %_datadir/make-initrd/features/integrity/data/lib
%dir %_datadir/make-initrd/features/integrity/data/lib/initrd
%dir %_datadir/make-initrd/features/integrity/data/lib/initrd/modules
%_datadir/make-initrd/features/integrity/data/lib/initrd/modules/085-integrity
%endif

%changelog
* Thu Sep 05 2024 Paul Wolneykien <manowar@altlinux.org> 0.7.6-alt1
- Make the contents of /etc/sysconfig/integrity override values
  set in /etc/integrity/config.

* Thu May 30 2024 Paul Wolneykien <manowar@altlinux.org> 0.7.5-alt1
- Use 0x80000002 as the default EVM mode.
- Automatically enable --with-evm for integrity-sign --verify if EVM
  is enabled in the kernel.
- Fix: Disable autoreq for integrity initrd script.
- Added notes about new features (README and man).
- Pass explicit EVM option via state file to Stage II.
- Fix: Reconfigure bootloader on each stage.
- Fix: Delete old /var/lib/integrity_update/default.
- Don't touch filesystem immutable bit in EVM mode.
- Added option --without-evm.
- Run make-initrd with normal log output.
- Allow to cancel loading the system if IMA policy fails to load.
- Check loading of IMA and EVM policy at system boot (ima-check.service).
- Load IMA policy at initrd stage only when ima_appraise=enforce.
- Run make-initrd with normal log output.
- Fixed OpenSSL GOST module path when copying to initrd.
- Fix: Abort on some make-initrd errors.

* Mon May 27 2024 Paul Wolneykien <manowar@altlinux.org> 0.7.4-alt1
- Fix file signing log output: stderr or file.
- Fix log of errors when signing the files.
- Write log to /var/log/integrity-sign.log by default.
- Add --log-stderr option.

* Wed May 22 2024 Paul Wolneykien <manowar@altlinux.org> 0.7.3-alt1
- Fix: Combine x509 certificate and private key in one file for
  signing.

* Fri May 17 2024 Paul Wolneykien <manowar@altlinux.org> 0.7.2-alt1
- Fixed manpage sections.
- Fix: Explicitly insert GOST kernel modules for Streebog hashes.
- Fix: Require /usr/bin/chattr.
- Added GOST_PARAMSET option (undocumented).
- Fix and secure shell code mostly related to ignoring -e option.
- Fix: Output file names to file log.
- Fixed notes about /var/log/integrity-sign.log.

* Fri May 17 2024 Paul Wolneykien <manowar@altlinux.org> 0.7.1-alt1
- Added copyright information.

* Fri May 17 2024 Paul Wolneykien <manowar@altlinux.org> 0.7.0-alt1
- Added manual pages!!!
- Add 'ima-' prefix to systemd units.
- Updated README.
- Fixed getting IMA hash from the Linux kernel command line.
- Use pipe mode (padd) when adding kmk-user with keyctl.
- Allow to run the whole cycle in automatic mode (with file signing
  log at /var/log/integrity-sign.log).
- Make integrity-applier a multitool (initialization and signing
  operations).
- integrity-sign: Make file signing error fatal.
- integrity-sign: Change verbosity.
- integrity-sign: Fixed file verification action.
- integrity-sign: Fixed EVM key symlink.
- integrity-sign: Fixed option parser.
- integrity-sign: Fixed usage.
- Setup the default policy to also check kernel modules.
- Added comments to the default config (hash algorithms and EVM).

* Tue Mar 19 2024 Paul Wolneykien <manowar@altlinux.org> 0.6.2-alt1
- Updated README.

* Tue Mar 19 2024 Paul Wolneykien <manowar@altlinux.org> 0.6.1-alt1
- Make integalert dependency optional.
- Fixed exit when integalert is disabled.

* Mon Mar 18 2024 Paul Wolneykien <manowar@altlinux.org> 0.6.0-alt2
- Fix: Own make-initrd/features/integrity/** directories.

* Mon Mar 18 2024 Paul Wolneykien <manowar@altlinux.org> 0.6.0-alt1
- signing.service: Output to tty.
- Install the default IMA policy.
- Make a configuration shorthand: /etc/integrity/config ->
  /etc/sysconfig/integrity.
- Configure modules and files for the 'integrity' make-initrd feature
  with INTEGRITY_FEATURES variable.
- Don't create /etc/noupdate.
- Use /var/lib/integrity_update directory for state files.
- Don't touch initrd from within integrity-sign script.
- Fix: Declare the missing -a short option in integrity-applier.
- Support -G | --disable-graphics option in integrity-applier.
- Rename: --hash instead of --hashalgo in integrity-sign.
- Configure the default behavior via /etc/sysconfig/integrity.
- Added two control facilities: 'ima_appraise' and 'ima_hash'.
- Read 'ima_hash=' from the kernel command line.
- Fix/improve 'usage'.
- Fix/improve some messages.
- Place temp files in integrity-sign.XXXXXXXX temp dir.
- Report error on problems with reading the certificate.
- Exit with error in case of unknown hash algo.
- Fixed 'verify' action of integrity-sign utility.
- Add support for generation of GOST keys.
- Run signing.service manually (thx Denis Medvedev).

* Tue Feb 13 2024 Denis Medvedev <nbr@altlinux.org> 0.5.2-alt1
- changed operations to manual signing.

* Mon Dec 25 2023 Denis Medvedev <nbr@altlinux.org> 0.5.1-alt1
- Initial release, based on ima-evm-integrity-check and parts of
cert-distro-updater

* Tue Apr 09 2019 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1
- integrity-sign: Fix chattr tmpdir cleanup.
- integrity-sign: Create new initrd by default.
- integrity-sign: Sign kernel modules.

* Tue Apr 02 2019 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1
- integrity-sign: Fix -i option with spaces in filenames.
- integrity-sign: Handle shared objects in /var/lib too.

* Fri Jan 25 2019 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- Package example policy.

* Fri Nov 16 2018 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- Determine make-initrd version at build time.
- Add make-initrd-2.x support.

* Thu Nov 15 2018 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.M80C.1
- New version.

* Thu Nov 01 2018 Mikhail Efremov <sem@altlinux.org> 0.2-alt0.M80C.1
- integrity-sign: Make signed files immutable.
- integrity-sign: Use single command to sign files.
