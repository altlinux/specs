Name: eepm-apt
Version: 3.60.0
Release: alt1

Summary: APT like frontend via Etersoft EPM package manager

License: AGPL-3.0+
Group: System/Configuration/Packaging
Url: http://wiki.etersoft.ru/EPM

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Etersoft/eepm-apt/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArchitectures: noarch

BuildRequires: eepm >= 3.60.0
Requires: eepm >= 3.60.0

AutoProv:no
AutoReq:no

# Conflicts: /usr/bin/apt

# all requires in eepm package
# Requires: grep

%description
This package contains APT like frontend for Etersoft EPM package manager.

Etersoft EPM is the package manager for any platform
and any platform version. It provides
universal interface to any package manager.
Can be useful for system administrators working
with various distros.

See detailed description here: http://wiki.etersoft.ru/EPM

%prep
%setup

%install
# install to datadir and so on
# do not use uncommon makeinstall_std here
%make_install install DESTDIR=%buildroot \
	datadir=%_datadir bindir=%_bindir mandir=%_mandir \
	sysconfdir=%_sysconfdir version=%version-%release

%files
# not for apt based system
%_bindir/apt

%changelog
* Tue Apr 02 2024 Vitaly Lipatov <lav@altlinux.ru> 3.60.0-alt1
- initial build for ALT Sisyphus
