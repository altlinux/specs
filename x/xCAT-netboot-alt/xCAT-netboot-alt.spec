%define user _mknetboot
%define xcatprof %_datadir/xcat/netboot/alt

Name: xCAT-netboot-alt
Summary: Tools for build kernel & initrd, for xCAT netboot
Version: 2.5.1
Release: alt0.4
License: GPL
Group: System/Servers
Packager: Andriy Stepanov <stanv@altlinux.ru>
BuildArch: noarch

Prereq: hasher-priv
Requires: mkimage libshell
AutoReq: yes, noshell

Source: %name.tar

BuildRequires: perl-Template perl-File-Copy-Recursive perl-xCAT
BuildRequires: xCAT-server

%description
xCAT requires to boot unknown stations via net.
All unknow nodes booted using genereal kernel and initrd.
This package provide tools for build such kernel and attendant initrd

OS images for Diskless/Statelite nodes generated with special tools.
This package contains tools to build such images.

# Skip Req/Prov checks for mkimage profile
%add_findreq_skiplist %_localstatedir/%user/mkimage-profile-netboot/image-scripts.d/*/*
%add_findprov_skiplist %_localstatedir/%user/mkimage-profile-netboot/image-scripts.d/*/*

%add_findreq_skiplist %_localstatedir/%user/mkimage-profile-diskless/image-scripts.d/*/*
%add_findprov_skiplist %_localstatedir/%user/mkimage-profile-diskless/image-scripts.d/*/*

%prep
%setup -q -n %name

%install

# Create home directory
install -m 755 -d %buildroot%_localstatedir/%user

# Create directory for mkimage profile configuration files
install -m 755 -d %buildroot%_sysconfdir/xcat/alt
install -D -pm 644 config/* %buildroot%_sysconfdir/xcat/alt

# Install binares
install -d -pm 755 %{buildroot}%{_bindir}
install -D -pm 755 bin/nbcreate %{buildroot}%{_bindir}

# Install netboot mkimage profile
cp -a mkimage-profile-netboot %{buildroot}%{_localstatedir}/%{user}

# Install diskless/statelite mkimage profile
cp -a mkimage-profile-diskless %{buildroot}%{_localstatedir}/%{user}

# Follow xCAT conventions and put to special directory tools for build Diskless/Statelite images
install -m 755 -d %buildroot%xcatprof
install -D -pm 755 bin/genimage %buildroot%xcatprof

# Copy xCAT profiles for Diskless / Statelite images
install -D -pm 644 xCAT-profiles/* %buildroot%xcatprof


%pre
%_sbindir/groupadd -r -f %user
%_sbindir/useradd -r -g %user -d %_localstatedir/%user -s /dev/null -n %user > /dev/null 2>&1
if ! getent group hashman |cut -d: -f4 |tr , '\n' |fgrep -qsx %user; then
    hasher-useradd %user &&
    printf '%%s\n%%s\n' 'allow_ttydev=YES' 'allowed_mountpoints=/dev/pts' \
        >> /etc/hasher-priv/user.d/%user
fi

%files
%_bindir/nbcreate
%_sysconfdir/xcat/alt/*
%xcatprof/*
%attr(-,%user,%user) %_localstatedir/%user

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
- Update from upstream SVN: trunk@7759.

* Fri Sep 17 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.2
- Update from upstream SVN: trunk@7490.

* Fri Sep 10 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.1
- Update from upstream SVN: trunk@7385.

* Sun Jun 27 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.3-alt0.1
- Update from upstream SVN: trunk@6611.

* Mon Jun 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.3
- Update from upstream SVN: trunk@6560.

* Tue Jun 08 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.2
- update genimage to expand macrosses in packages lists

* Wed Jun 02 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.1
- Update from upstream SVN: trunk@6312.

* Thu May 20 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.4
- Add profile for build Diskless/Statelite images

* Thu May 13 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.3
- Rewrite script in Perl

* Thu Apr 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.2
- Update from upstream SVN: trunk@5831.

* Thu Mar 18 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.1
- Update from upstream SVN: trunk@5517.

* Tue Mar 02 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.5
- Update from upstream SVN: trunk@5320.

* Fri Feb 05 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.4
- Update from upstream SVN.

* Thu Jan 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.3
- Update from upstream SVN: trunk@5004.

* Tue Jan 19 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.2
- Update from upstream SVN: trunk@4978.

* Mon Jan 11 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.1
- Update from upstream SVN.

* Fri Dec 11 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3.2-alt0.1
- Update from upstream SVN.

* Wed Nov 18 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3-alt0.1
- ALT: initial build

