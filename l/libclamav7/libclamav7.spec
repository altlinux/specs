%def_without milter

%def_with ownconfdir

%if_with ownconfdir
%define clamconfdir /etc/clamav
%else
%define clamconfdir /etc
%endif

%define rctag %nil

Name: libclamav7
Version: 0.100.2
Release: alt3

Summary: Compatibility package with shared libraries of ClamAV 0.100.2
License: GPLv2 only
Group: System/Libraries

Provides: libclamav = %version-%release
Obsoletes: libclamav < %version-%release

URL: http://www.clamav.net/
%ifdef snap
Source0: http://www.clamav.net/snapshot/clamav-devel-%snap.tar.gz
%else
Source0: http://downloads.sourceforge.net/clamav/clamav-%{version}%{rctag}.tar.gz
%endif

Source1: clamav.init
Source2: clamav.sysconfig

Source4: freshclam.cron
Source5: freshclam.logrotate
Source6: clamav.logrotate

Source10: clamav-milter.init
Source11: clamav-milter.sysconfig
Source12: clamav-milter.msg
Source13: clamav-milter.whitelist
Source14: clamav-milter.conf

Source20: virusstat-perIP
Source21: virusstat-perIP-PrevHour
Source22: virusstat-total
Source23: virusstat.cron.example


Patch1: clamav-config.patch
Patch2: freshclam-config.patch

Patch20: clamav-0.99-pkgconfig.patch
Patch21: clamav-AC_SYS_LARGEFILE.patch

# postinstall uses subst utility
Requires(post): sed >= 1:3.02-alt1

# sed used by configure script
BuildRequires: sed

BuildRequires: bzlib-devel libcheck-devel libncurses-devel zlib-devel libcurl-devel libssl-devel libxml2-devel
BuildRequires: git-core graphviz groff-extra gv zip doxygen

# for compatibility libclamav7 package to avoid conflict between internal libclammspack library
BuildRequires: libmspack-devel

# ...and edited manually to separate conditional buildreqs
%{?_with_milter:BuildRequires: sendmail-devel}

# for snapshots
%{?snap: BuildRequires: automake}

%description
Compatibility package with shared libraries of ClamAV 0.98.7

%prep
%setup %{?snap: -n clamav-devel-%snap} %{?rctag: -n clamav-%{version}%{rctag}}
%patch1 -p1
%patch2 -p1

%patch20 -p1
%patch21 -p0

%build
# fixed RPATH issue (0.97.3 tarball built with wrong libtool)
%{!?snap: aclocal --force -I m4}
%{!?snap: %autoreconf}

# --disable-clamav: Disable test for clamav user/group
%configure \
        --sysconfdir=%clamconfdir \
        --enable-experimental \
        --enable-clamdtop \
        --disable-clamav \
        --with-user=mail \
        --with-group=mail \
        --with-dbdir=/var/lib/%name \
        --disable-llvm \
        --with-system-libmspack \
#


# Safety belt for IPv6 enabling. We want to build clamav with IPv6 support,
# but can not rely on configure check as it can fail if build host set up
# as IPv4 only system.
echo >> clamav-config.h
echo "#ifndef SUPPORT_IPv6" >> clamav-config.h
echo "#define SUPPORT_IPv6 1" >> clamav-config.h
echo "#endif" >> clamav-config.h

%make_build

install -m644 %_sourcedir/virusstat* .

%install
%makeinstall_std

mv %buildroot%clamconfdir/clamd.conf.sample %buildroot%clamconfdir/clamd.conf
mv %buildroot%clamconfdir/freshclam.conf.sample %buildroot%clamconfdir/freshclam.conf

%{!?_with_milter:rm -f %buildroot%_man1dir/clamav-milter*}

install -pD -m755 %_sourcedir/clamav.init %buildroot/etc/rc.d/init.d/clamd

install -pD %_sourcedir/clamav.sysconfig %buildroot/etc/sysconfig/clamd

%if_with milter
sed -e 's|@@CLAMAVCONFDIR@@|%clamconfdir|' < %_sourcedir/clamav-milter.sysconfig > %buildroot/etc/sysconfig/clamav-milter
install -m644 %_sourcedir/clamav-milter.conf %buildroot%clamconfdir/
install -m755 %_sourcedir/clamav-milter.init %buildroot/etc/rc.d/init.d/clamav-milter
#install -m644 %_sourcedir/clamav-milter.whitelist %buildroot%clamconfdir/
#install -m644 %_sourcedir/clamav-milter.msg %buildroot%clamconfdir/
%endif

install -d %buildroot%_logdir/clamav
touch %buildroot%_logdir/clamav/clamd.log
touch %buildroot%_logdir/clamav/freshclam.log

# install the logrotate stuff
install -pD -m644 %_sourcedir/freshclam.logrotate %buildroot%_sysconfdir/logrotate.d/freshclam
install -m644 %_sourcedir/clamav.logrotate %buildroot%_sysconfdir/logrotate.d/clamav

# pid file dir
install -d %buildroot/var/run/clamav

# install html docs
mkdir -p %buildroot%_defaultdocdir/clamav-manual
rm -rf docs/html/CVS
install -m644 docs/html/* %buildroot%_defaultdocdir/clamav-manual

# remove non-packaged files
rm -f %buildroot%_libdir/*.la
rm -f %buildroot%_libdir/*.a
# databases is not installing in 0.97.5
if [ -d %buildroot/var/lib/clamav ] ; then
    rm -f %buildroot/var/lib/clamav/*.cvd
else
    mkdir -p %buildroot/var/lib/clamav
fi

rm -rf %buildroot/%_bindir
rm -rf %buildroot/%_mandir
rm -rf %buildroot/%_initdir
rm -rf %buildroot/%_sysconfdir
rm -rf %buildroot/var
rm -rf %buildroot/%_defaultdocdir
rm -rf %buildroot/%_libdir/pkgconfig
rm -rf %buildroot/%_includedir

rm -f %buildroot/%_libdir/*.so
rm -f %buildroot/usr/sbin/clamd

rm -f %buildroot/%_libdir/libclammspack.so.*

%files
%_libdir/lib*.so.*

%changelog
* Fri Jan 11 2019 Sergey Y. Afonin <asy@altlinux.ru> 0.100.2-alt3
- Compatibility package with shared libraries of ClamAV 0.100.2
  (based on clamav 0.100.2-alt2 package)
