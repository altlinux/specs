Group: System/Base
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ perl(IO/Handle.pm)
# END SourceDeps(oneline)
%define oldname zfs-fuse
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define _hardened_build 1
Name:             fuse-zfs
Version:          0.7.2.2
Release:          alt1_6
Summary:          ZFS ported to Linux FUSE
License:          CDDL
URL:              https://github.com/gordan-bobic/zfs-fuse
Source00:         http://github.com/gordan-bobic/zfs-fuse/archive/%{oldname}-%{version}.tar.gz
Source01:         zfs-fuse.service
Source02:         zfs-fuse.scrub
Source03:         zfs-fuse.sysconfig
Source04:         zfs-fuse-helper
Patch0:           zfs-fuse-0.7.2.2-stack.patch
BuildRequires:    libfuse-devel libaio-devel rpm-build-perl scons
BuildRequires:    zlib-devel libssl-devel libattr-devel liblzo2-devel bzlib-devel liblzma-devel
%ifnarch aarch64 ppc64le
BuildRequires:    /usr/bin/execstack
%endif
BuildRequires:    journalctl libsystemd-devel libudev-devel systemd systemd-analyze systemd-coredump systemd-networkd systemd-services systemd-utils
Requires:         fuse >= 2.7.4
# (2010 karsten@redhat.com) zfs-fuse doesn't have s390(x) implementations for atomic instructions
ExcludeArch:      s390 s390x aarch64
# For compatibility for packages expecting slightly other locations
Provides:         /sbin/zfs
Provides:         /sbin/zpool
Provides:         /sbin/zdb
Provides:         /sbin/ztest
Provides:         /sbin/zstreamdump
Provides:         /sbin/mount.zfs
Source44: import.info
Source45: zfs-fuse.init

%description
ZFS is an advanced modern general-purpose filesystem from Sun
Microsystems, originally designed for Solaris/OpenSolaris.

This project is a port of ZFS to the FUSE framework for the Linux
operating system.

%prep
%setup -n %{oldname}-%{version} -q

%patch0 -p0

f=LICENSE
mv $f $f.iso88591
iconv -o $f -f iso88591 -t utf8 $f.iso88591
rm -f $f.iso88591

chmod -x contrib/test-datasets
chmod -x contrib/find-binaries
chmod -x contrib/solaris/fixfiles.py
chmod -x contrib/zfsstress.py
# cp -f /usr/lib/rpm/config.{guess,sub} src/lib/libumem/

%build
export CCFLAGS="%{optflags}"
pushd src

scons debug=2 optim='%{optflags}'

%install
pushd src
scons debug=1 install install_dir=%{buildroot}%{_sbindir} man_dir=%{buildroot}%{_mandir}/man8/ cfg_dir=%{buildroot}/%{_sysconfdir}/%{oldname}
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{oldname}.service
install -Dp -m 0755 %{SOURCE2} %{buildroot}%{_sysconfdir}/cron.weekly/98-%{oldname}-scrub
install -Dp -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{oldname}
install -Dp -m 0755 %{SOURCE4} %{buildroot}%{_sbindir}/zfs-fuse-helper

%ifnarch aarch64 ppc64le
#set stack not executable, BZ 911150
for i in zdb zfs zfs-fuse zpool ztest; do
       /usr/bin/execstack -c %{buildroot}%{_sbindir}/$i
done
%endif

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

%preun
%preun_service zfs-fuse

%postun
echo "Removing files since we removed the last package"
rm -rf /var/run/zfs
rm -rf /var/lock/zfs

%files
%doc BUGS CHANGES contrib HACKING LICENSE README 
%doc README.NFS STATUS TESTING TODO
%{_sbindir}/zdb
%{_sbindir}/zfs
%{_sbindir}/zfs-fuse
%{_sbindir}/zfs-fuse-helper
%{_sbindir}/zpool
%{_sbindir}/zstreamdump
%{_sbindir}/ztest
%{_sbindir}/mount.zfs
%{_unitdir}/%{oldname}.service
%{_sysconfdir}/cron.weekly/98-%{oldname}-scrub
%config(noreplace) %{_sysconfdir}/sysconfig/%{oldname}
%{_sysconfdir}/%{oldname}/
%{_mandir}/man8/zfs-fuse.8*
%{_mandir}/man8/zdb.8*
%{_mandir}/man8/zfs.8*
%{_mandir}/man8/zpool.8*
%{_mandir}/man8/zstreamdump.8*
%config(noreplace) %_initdir/zfs-fuse

%changelog
* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.2.2-alt1_6
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_23
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_22
- update to new release by fcimport

* Mon Sep 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_20
- new release (closes: #30364)

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_19
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_17
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_16
- update to new release by fcimport

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_15
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_13
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_11
- update to new release by fcimport

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_10
- update to new release by fcimport

* Tue Feb 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_8
- update to new release by fcimport

* Wed Jan 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_6
- update to new release by fcimport

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
