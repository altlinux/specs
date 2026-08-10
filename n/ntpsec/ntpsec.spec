Name: ntpsec
Version: 1.2.5
Release: alt1
Summary: NTP daemon and utilities
Group: System/Servers

%define privuser  %name
%define privgroup %name
%define privpath  %_localstatedir/ntp
# build endianess check fails with LTO
%global optflags_lto %nil

License: NTP AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND ISC AND Apache-2.0 AND Beerware
Url: https://www.ntpsec.org/
Source0: https://ftp.ntpsec.org/pub/releases/ntpsec-%version.tar
Source3: ntp.conf

Patch: %name-alt-dns_sd.patch

BuildRequires: bison
BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: libbsd-devel
BuildRequires: libcap-devel
BuildRequires: m4
BuildRequires: openssl-devel
BuildRequires: pps-tools-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-modules-curses
BuildRequires: asciidoctor
BuildRequires: libsystemd-devel
BuildRequires: waf
# optional but nice to hve
BuildRequires: libavahi-devel
BuildRequires: python3-module-gps

Conflicts: ntp ntpd perl-NTP-Util ntpdate openntpd ntpq
Provides: python3-module-%name = %EVR

Requires: logrotate

# self-provides
%filter_from_requires /\/usr\/%_lib\/libntpc\.so.*/d

%description
NTPsec is a more secure and improved implementation of the Network Time
Protocol derived from the original NTP project.

%prep
%setup
%patch -p1

# Fix egg info to use a shorter version which will work as an rpm provide
sed -i 's|NTPSEC_VERSION_EXTENDED|NTPSEC_VERSION|' pylib/ntp-in.egg-info

# Modify compiled-in statsdir
sed -i 's|/var/NTP|/var/log/ntpstats|' \
        docs/includes/ntpd-body.adoc ntpd/ntp_util.c

# Disable failing test
sed -i 's|c cprogram test|c cprogram|' libaes_siv/wscript

# Use systemctl kill in logrotate postrotate script
sed -i 's|killall -HUP ntpd$|systemctl kill --signal=HUP --kill-whom=main ntpd.service 2>/dev/null \|\| true|' \
        etc/logrotate-config.ntpd

# Make sure we use the system waf instead of the one bundled with ntpsec
rm -f waf
%global waf waf

%build
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"
export PYTHONDIR=%python3_sitelibdir

%waf configure \
	--pyshebang=%__python3 \
        --enable-debug \
        --disable-doc \
        --refclock=all \
        --prefix=%prefix \
        --exec-prefix=%_exec_prefix \
        --bindir=%_bindir \
        --sbindir=%_sbindir \
        --sysconfdir=%_sysconfdir \
        --datadir=%_datadir \
        --includedir=%_includedir \
        --libdir=%_libdir \
        --libexecdir=%_libexecdir \
        --localstatedir=/var \
        --sharedstatedir=%_sharedstatedir \
        --mandir=%_mandir \
        ;

%waf build

%install
%waf --destdir=%buildroot install

install -p -m755 attic/ntpdate %buildroot%_sbindir/ntpdate
mkdir -p %buildroot%_sysconfdir/logrotate.d
install -p -m644 etc/logrotate-config.ntpd \
        %buildroot%_sysconfdir/logrotate.d/ntpsec.conf

rm -rf %buildroot%_docdir

pushd %buildroot

install -pm640 %SOURCE3 .%_sysconfdir/ntp.conf
subst 's,VARNTP,%_localstatedir/ntp,' .%_sysconfdir/ntp.conf

# Move ntpq to sbin for better compatibility with ntp package
mv .%_bindir/ntpq .%_sbindir/ntpq

mkdir -p ./var/{lib/ntp,log/ntpstats}
touch .%_localstatedir/ntp/ntp.drift

mkdir -p .%_systemd_dir/ntp-units.d
echo 'ntpd.service' > .%_systemd_dir/ntp-units.d/60-ntpd.list
subst 's,-u\ ntp:ntp,-u %privuser:%privgroup,g' .%_unitdir/ntpd.service

# Create a sysusers.d config file (UID/GID is inherited from the ntp package)
mkdir -p .%{_sysusersdir}
cat > .%{_sysusersdir}/ntpsec.conf <<EOF
u %privuser %privgroup - /var/lib/ntp -
EOF

popd

%check
%waf check

%pre
/usr/sbin/groupadd -r -f %privgroup
/usr/sbin/useradd -r -s /dev/null -g %privgroup -d %privpath -c 'NTPSec daemon' %privuser >/dev/null 2>&1 ||:

%post
%post_systemd ntpd.service ntp-wait.service

%preun
%preun_systemd ntpd.service ntp-wait.service
%global service_save_file /run/ntp-ntpsec.upgrade.services

%triggerin -- ntp
[ $1 = 0 ] || exit 0
# Save enabled ntp services and configuration (before our post)
for s in ntpd ntp-wait; do
        systemctl is-enabled -q "$s".service 2> /dev/null &&
                echo "$s" 2> /dev/null >> %service_save_file
done
rm -rf %_sysconfdir/ntp.ntpsec
cp -r --preserve=all %_sysconfdir/ntp %_sysconfdir/ntp.ntpsec 2> /dev/null
:

%triggerpostun -- ntp
[ $2 = 0 ] || exit 0
# Restore the services and configuration from ntp (after its preun)
for s in ntpd ntp-wait; do
        grep -q "^$s$" %service_save_file 2> /dev/null &&
                systemctl enable -q "$s".service 2> /dev/null
done
rm -f %service_save_file
mv -f -T --backup=numbered %_sysconfdir/ntp.ntpsec %_sysconfdir/ntp
# Remove unsupported restrictions
sed -i.bak -E '/^restrict/s/no(e?peer|trap)//g' %_sysconfdir/ntp.conf
:

%files
%doc LICENSES/*
%doc NEWS.adoc README.adoc
%config(noreplace) %attr(640, %privuser,%privgroup) %_sysconfdir/ntp.conf
%config(noreplace) %_sysconfdir/logrotate.d/ntpsec.conf
%_bindir/ntp*
%_sbindir/ntp*
%_libdir/libntpc.so*
%_mandir/man?/ntp*.*
%_unitdir/ntp*.service
%_unitdir/ntp*.timer
%dir %_systemd_dir/ntp-units.d
%_systemd_dir/ntp-units.d/*ntpd.list
%dir %attr(750,%privuser,%privgroup) %_localstatedir/ntp
%ghost %attr(644,%privuser,%privgroup) %_localstatedir/ntp/ntp.drift
%dir %attr(750,%privuser,%privgroup) %_logdir/ntpstats
%_sysusersdir/ntpsec.conf
%python3_sitelibdir/ntp-*.egg-info
%python3_sitelibdir/ntp

%changelog
* Mon Aug 10 2026 L.A. Kostis <lakostis@altlinux.ru> 1.2.5-alt1
- 1.2.5.
- Security fixes: CVE-2026-18321.
- BR: added libavahi (for dns_sd) and python3-module-gps.

* Sat Jul 25 2026 L.A. Kostis <lakostis@altlinux.ru> 1.2.4-alt1
- Initial build for ALTLinux.

