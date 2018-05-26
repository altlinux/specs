%define beanstalkd_user      beanstalkd
%define beanstalkd_group     %beanstalkd_user
%define beanstalkd_home      %_localstatedir/lib/beanstalkd
%define beanstalkd_binlogdir %beanstalkd_home/binlog

Name: beanstalkd
Version: 1.10
Release: alt3
Summary: A simple, fast work-queue service

Group: System/Servers
License: MIT
Url: http://kr.github.io/beanstalkd/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/kr/%name/archive/v%version.tar.gz
Source: %name-%version.tar
Source1: %name.service
Source2: %name.sysconfig

Patch1: beanstalkd-1.10-warnings.patch
Patch2: beanstalkd-1.10-mkdtemp.patch

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
#define _localstatedir %_var
BuildRequires: rpm-macros-intro-conflicts

Requires(pre):    shadow-change shadow-check shadow-convert shadow-edit shadow-groups shadow-log shadow-submap shadow-utils
Source44: import.info

%description
beanstalkd is a simple, fast work-queue service. Its interface is generic,
but was originally designed for reducing the latency of page views in
high-volume web applications by running most time-consuming tasks
asynchronously.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%make_build LDFLAGS="%{?__global_ldflags}" CFLAGS="$RPM_OPT_FLAGS"

%check
make check

%install
%make_install install PREFIX=%buildroot%prefix
install -p -D -m 0644 %SOURCE1 %buildroot%_unitdir/%name.service
install -p -D -m 0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -d -m 0755 %buildroot%beanstalkd_home
install -d -m 0755 %buildroot%beanstalkd_binlogdir
install -d -m 00755 %buildroot%_man1dir
gzip doc/%name.1
install -p -m 0644 doc/%name.1.gz %buildroot%_man1dir/

# touching all ghosts; hack for rpm 4.0.4
for rpm_404_ghost in %beanstalkd_binlogdir
do
    mkdir -p %buildroot`dirname "$rpm_404_ghost"`
    touch %buildroot"$rpm_404_ghost"
done

%pre
getent group %beanstalkd_group >/dev/null || groupadd -r %beanstalkd_group
getent passwd %beanstalkd_user >/dev/null || \
    useradd -r -g %beanstalkd_user -d %beanstalkd_home -s /sbin/nologin \
    -c "beanstalkd user" %beanstalkd_user
exit 0

%post
if [ -d %beanstalkd_home ]; then
    install -d %beanstalkd_binlogdir -m 0755 \
        -o %beanstalkd_user -g %beanstalkd_user \
%beanstalkd_binlogdir
fi

%files
%doc README LICENSE doc/protocol.txt
%_unitdir/%name.service
%_bindir/%name
%_man1dir/%name.1*
%config(noreplace) %_sysconfdir/sysconfig/%name
%attr(0755,%beanstalkd_user,%beanstalkd_group) %dir %beanstalkd_home
%ghost %attr(0755,%beanstalkd_user,%beanstalkd_group) %dir %beanstalkd_binlogdir

%changelog
* Sun Oct 01 2017 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt3
- build with rpm-build-intro
- fix quotes in sysconfig file

* Sun Oct 01 2017 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt2
- native build for ALT Sisyphus

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_5
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_3
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_2
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_4
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_2
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_1
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.6-alt1_9
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.6-alt1_8
- initial fc import

