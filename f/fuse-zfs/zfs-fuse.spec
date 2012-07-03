# BEGIN SourceDeps(oneline):
BuildRequires: perl(IO/Handle.pm)
# END SourceDeps(oneline)
%define oldname zfs-fuse
%define _hardened_build 1
Name:             fuse-zfs
Version:          0.7.0
Release:          alt1_5
Summary:          ZFS ported to Linux FUSE
Group:            System/Base
License:          CDDL
URL:              http://zfs-fuse.net/
Source00:         http://zfs-fuse.net/releases/0.7.0/%{oldname}-%{version}.tar.bz2
Source01:         zfs-fuse.service
Source02:         zfs-fuse.scrub
Source03:         zfs-fuse.sysconfig
Source04:         zfs-fuse-helper
Patch0:           zfs-fuse-0.7.0-umem.patch
BuildRequires:    libfuse-devel libaio-devel scons zlib-devel libssl-devel libattr-devel
Requires:         fuse >= 2.7.4-1
# (2010 karsten@redhat.com) zfs-fuse doesn't have s390(x) implementations for atomic instructions
ExcludeArch:      s390
ExcludeArch:      s390x
Source44: import.info
Source45: zfs-fuse.init

%description
ZFS is an advanced modern general-purpose filesystem from Sun
Microsystems, originally designed for Solaris/OpenSolaris.

This project is a port of ZFS to the FUSE framework for the Linux
operating system.

%prep
%setup -q -n %{oldname}-%{version}

%patch0 -p0

f=LICENSE
%{__mv} $f $f.iso88591
iconv -o $f -f iso88591 -t utf8 $f.iso88591
%{__rm} -f $f.iso88591

chmod -x contrib/test-datasets
chmod -x contrib/find-binaries
chmod -x contrib/solaris/fixfiles.py
chmod -x contrib/zfsstress.py

%build
export CCFLAGS="%{optflags}"
pushd src

scons debug=1 optim='%{optflags}'

%install
pushd src
scons debug=1 install install_dir=%{buildroot}%{_bindir} man_dir=%{buildroot}%{_mandir}/man8/ cfg_dir=%{buildroot}/%{_sysconfdir}/%{oldname}
%{__install} -Dp -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{oldname}.service
%{__install} -Dp -m 0755 %{SOURCE2} %{buildroot}%{_sysconfdir}/cron.weekly/98-%{oldname}-scrub
%{__install} -Dp -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{oldname}
%{__install} -Dp -m 0755 %{SOURCE4} %{buildroot}%{_bindir}/zfs-fuse-helper

mkdir -p -m 0755 %buildroot%_initdir
install -D -m 0755 %SOURCE45 %buildroot%_initdir/zfs-fuse

%post
oldcache=/etc/zfs/zpool.cache      # this changed per 0.6.9, only needed when upgrading from earlier versions
newcache=/var/lib/zfs/zpool.cache

if [[ -f $oldcache && ! -e $newcache ]]; then
  echo "Moving existing zpool.cache to new location"
  mkdir -p $(dirname $newcache)
  mv $oldcache $newcache
else
  if [ -e $oldcache ]; then
    echo "Note: old zpool.cache present but no longer used ($oldcache)"
  fi
fi
%post_service zfs-fuse


%postun
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    echo "Removing files since we removed the last package"
    rm -rf /var/run/zfs
    rm -rf /var/lock/zfs
fi

%preun 
%preun_service zfs-fuse


%files
%doc BUGS CHANGES contrib HACKING LICENSE README 
%doc README.NFS STATUS TESTING TODO
%{_bindir}/zdb
%{_bindir}/zfs
%{_bindir}/zfs-fuse
%{_bindir}/zfs-fuse-helper
%{_bindir}/zpool
%{_bindir}/zstreamdump
%{_bindir}/ztest
%{_unitdir}/%{oldname}.service
%{_sysconfdir}/cron.weekly/98-%{oldname}-scrub
%config(noreplace) %{_sysconfdir}/sysconfig/%{oldname}
%{_sysconfdir}/%{oldname}/zfs_pool_alert
%{_mandir}/man8/zfs-fuse.8.*
%{_mandir}/man8/zdb.8.*
%{_mandir}/man8/zfs.8.*
%{_mandir}/man8/zpool.8.*
%{_mandir}/man8/zstreamdump.8.*
%config(noreplace) %_initdir/zfs-fuse

%changelog
* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_5
- resurrected from orphaned using fc import

* Thu Dec 30 2008 Sergey Ivanov <seriv@altlinux.org> 0.5.0-alt3
- fix summary, bug #18404

* Thu Oct 02 2008 Sergey Ivanov <seriv@altlinux.org> 0.5.0-alt2
- fix build problem

* Thu Oct 02 2008 Sergey Ivanov <seriv@altlinux.org> 0.5.0-alt1
- update to hg http://www.wizy.org/mercurial/zfs-fuse/trunk

* Sun May 27 2007 Sergey Ivanov <seriv@altlinux.org> 0.4.0_beta1.hg20070527-alt1
- update to hg http://www.wizy.org/mercurial/zfs-fuse/0.4.x

* Mon Mar 26 2007 Sergey Ivanov <seriv@altlinux.org> 0.4.0_beta1-alt0
- initial build for Sisyphus
