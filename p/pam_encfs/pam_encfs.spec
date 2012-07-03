Name: pam_encfs
Version: 0.1.4.4
Release: alt1

Summary: Mount fuse-encfs partitions when login
License: GPL
Group: System/Base

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar.gz

BuildRequires(pre): libpam-devel

Patch: %name.patch
Patch2: %name.stack-protector.patch

%set_pam_name %name

%package -n %pam_name
Summary: Mount fuse-encfs partitions when login
License: GPL
Group: System/Base
Requires(post): coreutils
Provides: %name = %version-%release
Obsoletes: %name

%description
Mount fuse-encfs partitions when login

%description -n %pam_name
Mount fuse-encfs partitions when login

%prep
%setup -q
%patch -p2
%patch2 -p2

%build
%make_build

%install
%make_install install \
	DESTDIR=%buildroot \
	PAM_LIB_DIR=%buildroot/%_lib/security

install -D -m600 pam_encfs.conf %buildroot%_sysconfdir/security/pam_encfs.conf
%files -n %pam_name
/%_lib/security/*
%config(noreplace) %_sysconfdir/security/pam_encfs.conf
%doc README

%changelog
* Tue Sep 28 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.4.4-alt1
- new version

* Fri Feb 06 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1.3-alt7
- not replace pam_encfs.conf after update (#18470)

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 0.1.3-alt6
- cleanup spec

* Wed Oct 18 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1.3-alt5
- package pam_encfs.conf (9940)

* Sun Oct 15 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1.3-alt4
- fix building

* Sun Oct 15 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1.3-alt3
- fix x86_64 build

* Fri Oct 13 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1.3-alt2
- fix build with stack-protector

* Sat Mar 25 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1.3-alt1
- fist build for Sisyphus

