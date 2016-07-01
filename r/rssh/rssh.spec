Name: rssh
Version: 2.3.4
Release: alt2

Summary: Restricted shell for scp or sftp

License: BSD
Group: Shells
Url: http://www.pizzashack.org/rssh/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/rssh/%name-%version.tar

Patch1: 0001-Fix-invalid-option-error.patch
Patch2: 0002-Honor-CFLAGS-CPPFLAGS-passed-to-configure.patch
Patch3: 0003-Fix-buffer-allocation-buffer-for-fail-message.patch
Patch4: 0004-Lower-syslog-priority-to-debug.patch
Patch7: 0007-Handle-rsync-v3-e-protocol-option.patch

# Automatically added by buildreq on Tue Dec 20 2005
BuildRequires: openssh-clients cvs openssh-server rsync

%description
rssh is a restricted shell for use with ssh, which allows the system
administrator to restrict a user's access to a system via scp or sftp, or
both.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch7 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
# since rssh 2.3.4, default config is installed as rssh.conf.default,
# rename it for packaging in rpm
mv %buildroot/%_sysconfdir/rssh.conf{.default,}

%files
%doc AUTHORS ChangeLog CHROOT COPYING README SECURITY TODO conf_convert.sh mkchroot.sh
%_bindir/rssh
%attr(4711, root, root) %_libexecdir/rssh_chroot_helper
%_man1dir/*
%_man5dir/*
%config(noreplace) %_sysconfdir/rssh.conf


%changelog
* Fri Jul 01 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.4-alt2
- really update sources to 2.3.4 fixes (CVE-2012-3478 and CVE-2012-2252)
- add patch for rsync3 compat

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 2.3.4-alt1
- new version 2.3.4 (with rpmrb script)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.3.2-alt0.1.qa1
- NMU: rebuilt for debuginfo.

* Sat Jan 07 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt0.1
- new version
- add Packager, some fixes in files section

* Tue Dec 20 2005 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt0.1
- initial build for ALT Linux Sisyphus
