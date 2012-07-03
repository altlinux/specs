Name: xCAT
Summary: Meta-package for a common, default xCAT setup
Version: 2.5.1
Release: alt0.4
License: EPL
Group: System/Servers
Packager: Andriy Stepanov <stanv@altlinux.ru>
BuildArch: noarch

%define installdir %{_localstatedir}/xcat
%define tftpdir %{_localstatedir}/tftpboot

Source1: xcat.conf
Source2: postscripts.tar
Source3: templates.tar
Source4: prescripts.tar
Source5: postscripts-alt.tar
Source6: xCATMN

Requires: xCAT-server xCAT-client
Requires: xCAT-netboot-alt

Requires: atftp dhcp-server apache2 nfs-utils expect nmap fping bind vsftpd
Requires: dhcp-omshell
Requires: syslinux
Requires: ipmitool >= 1.8.9
Requires: xnba-undi
Requires: conserver
Requires: nfs-server
Requires: make
Requires: ntp-server

Requires: perl-DBD-SQLite
Requires: perl-IO-Stty
Requires: perl-Net-Telnet
Requires: perl-XML-Parser

Requires: qemu-system
Requires: qemu-user

# All versions of the nb rpms are pulled in so an x86 MN can manage nodes of any arch.
# The nb rpms are used for dhcp-based discovery, and flashing, so for now we do not need them on a ppc MN.
# Requires: xCAT-nbroot-oss-x86 xCAT-nbkernel-x86 xCAT-nbroot-oss-x86_64 xCAT-nbkernel-x86_64 xCAT-nbroot-oss-ppc64 xCAT-nbkernel-ppc64 syslinux

Requires: xCAT-nbroot-core-x86
Requires: xCAT-nbroot-core-x86_64
Requires: xCAT-nbroot-core-ppc64

%description
xCAT is a server management package intended for at-scale management,
including hardware management and software management.

%define nbuser _mknetboot

# XXX: Files from postscripts dir usually executed at remote machines, doesnt are ?
%add_findreq_skiplist %installdir/postscripts/*

%build

%install

# Apache2 config
install -d -pm 755 %{buildroot}%{_sysconfdir}/httpd2/conf/extra-available
install -D -pm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd2/conf/extra-available/

# Make this node as Managment Node
install -D -pm 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/

# Prescripts && postscripts
install -d -pm 755 %{buildroot}/%{installdir}
tar xf %{SOURCE2} -C %{buildroot}/%{installdir}
tar --strip-components 1 -xf %{SOURCE5} -C %{buildroot}/%{installdir}/postscripts
tar xf %{SOURCE4} -C %{buildroot}/%{installdir}
chmod 755 %{buildroot}/%{installdir}/postscripts/*

# Templates
install -d -pm 755 %{buildroot}%{_datadir}/xcat
tar xf %{SOURCE3} -C %{buildroot}%{_datadir}/xcat

%post
# Install xCAT configs for Apache2
if [ -x "/usr/sbin/a2enextra" ]; then
    /usr/sbin/a2enextra xcat
fi

if [ -f /etc/profile.d/xcat.sh ]; then
  . /etc/profile.d/xcat.sh
fi
if [ "$1" = "1" ]; then #Only if installing for the first time..
  %{_sbindir}/xcatconfig --initinstall --database --installdir=%{installdir} --tftpdir=%{tftpdir}
else
  %{_sbindir}/xcatconfig --updateinstall --installdir=%{installdir} --tftpdir=%{tftpdir}
fi
# Allow %nbuser lookup xCAT tables
XCATBYBASS=1 chtab priority="6.2" policy.name=%nbuser policy.commands="gettab" policy.rule="allow"

%files
%{_datadir}/xcat/*
%{_sysconfdir}/httpd2/conf/extra-available/xcat.conf
%{_sysconfdir}/xCATMN
%{installdir}/postscripts
%{installdir}/prescripts

%changelog
* Wed Nov 24 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.4
- Update from upstream SVN: trunk@8256.

* Mon Nov 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.3
- Update from upstream SVN: trunk@8225.

* Mon Nov 15 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.2
- Update from upstream SVN: trunk@8159.

* Thu Oct 28 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.1
- Update from upstream SVN: trunk@7954.

* Mon Oct 25 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.4
- Update from upstream SVN: trunk@7912.

* Wed Oct 06 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.3
- Update from upstream SVN: trunk@7760.

* Fri Sep 17 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.2
- Update from upstream SVN: trunk@7490.

* Mon Sep 13 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.1
- Update from upstream SVN: trunk@7385.

* Sun Jun 27 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.3-alt0.1
- Update from upstream SVN: trunk@6611.

* Mon Jun 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.4
- Update from upstream SVN: trunk@6560.

* Tue Jun 08 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.3
- Init xCAT DataBase at firsttime installation

* Mon Jun 07 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.2
- Add Requires to make

* Wed Jun 02 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.1
- Update from upstream SVN: trunk@6312.

* Tue May 25 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.3
- Update from upstream SVN: trunk@6208.

* Thu Apr 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.2
- Update from upstream SVN: trunk@5831.

* Thu Mar 18 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.1
- Update from upstream SVN: trunk@5517.

* Tue Mar 02 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.8
- Update from upstream SVN: trunk@5320.

* Wed Feb 10 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.7
- Move directories to std locations

* Tue Jan 26 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.6
- Use netcat in postscripts.

* Thu Jan 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.5
- Update from upstream SVN: trunk@5004.

* Tue Jan 19 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.4
- Update from upstream SVN: trunk@4978.

* Mon Jan 11 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.3
- Update from upstream SVN repository

* Fri Dec 18 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3.2-alt0.3
- Allow _mknetboot user lookup xCAT tables

* Mon Dec 14 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3.2-alt0.2
- Requires xCAT-netboot-alt

* Fri Dec 11 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3.2-alt0.1
- Update from upstream SVN repository

* Thu Nov 12 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3-alt0.2
- Update from upstream SVN repository

