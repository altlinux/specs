Name: xCATsn
Summary: Metapackage for a common, default xCAT service node setup
Version: 2.5.1
Release: alt0.4
License: EPL
Group: System/Servers
Packager: Andriy Stepanov <stanv@altlinux.ru>
BuildArch: noarch

Source0: %name-%version.tar
Source1: xcat.conf

Provides: xCATsn = %version
Conflicts: xCAT

# xCAT stuff:
Requires: perl-xCAT   >= %version
Requires: xCAT-client >= %version
Requires: xCAT-server >= %version
Requires: xnba-undi
Requires: xCAT-netboot-alt
Requires: xCAT-nbroot-core-x86 xCAT-nbroot-core-x86_64 xCAT-nbroot-core-ppc64

# Perl modules:
Requires: perl-Template
Requires: perl-File-Copy-Recursive
Requires: perl-XML-Parser

# Services that can hold Service Node:
Requires: dhcp-server dhcp-omshell
Requires: atftp
Requires: httpd
Requires: bind
Requires: nfs-utils nfs-server
Requires: vsftpd

# Necessary tools:
Requires: expect nmap fping ipmitool
Requires: conserver perl-Net-Telnet
Requires: syslinux

BuildRequires: perl-Curses perl-Net-SSLeay

%description
xCATsn is a service node management package intended for at-scale management,
including hardware management and software management.

%prep
%setup -q

%build

%install

# Service Node distinction:
install -d -pm 755 %buildroot%_datadir/xcat
install -d -pm 755 %buildroot%_sysconfdir
install -D -pm 644 xCATSN %buildroot%_sysconfdir

# Apache2 configuration
install -d -pm 755 %buildroot%_sysconfdir/httpd2/conf/extra-available
install -D -pm 644 %SOURCE1 %buildroot%_sysconfdir/httpd2/conf/extra-available/

# Docs
install -d -pm 755 %buildroot%_docdir/%name-%version
install -D -pm 644 LICENSE.html %buildroot%_docdir/%name-%version

%post

# Install xCAT configs for Apache2
if [ -x "/usr/sbin/a2enextra" ]; then
    /usr/sbin/a2enextra xcat
fi

%files
%_docdir/%name-%version
%_sysconfdir/httpd2/conf/extra-available/xcat.conf
%_sysconfdir/xCATSN
%dir %_datadir/xcat

%changelog
* Wed Nov 24 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.4
- Update from upstream: trunk@8256.

* Mon Nov 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.3
- Update from upstream: trunk@8225.

* Mon Nov 15 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.2
- Update from upstream: trunk@8159.

* Thu Oct 28 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.1
- Update from upstream: trunk@7954.

* Mon Oct 25 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.4
- Update from upstream: trunk@7912.

* Wed Oct 06 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.3
- Update from upstream: trunk@7759.

* Fri Sep 17 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.2
- Update from upstream: trunk@7490.

* Mon Sep 13 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.1
- Update from upstream: trunk@7385.

* Sun Jun 27 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.3-alt0.1
- Update from upstream: trunk@6611.

* Mon Jun 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.2
- Update from upstream: trunk@6560.

* Wed Jun 02 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.1
- Update from upstream: trunk@6312.

* Tue May 25 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.4
- Update from upstream: trunk@6208.

* Thu Apr 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.3
- Initial build Service Node package. trunk@5831.

* Tue Mar 30 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.2
- Go away from unnecessary dependencies

* Tue Mar 23 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.1
- Initial build Service Node package. trunk@5541.
