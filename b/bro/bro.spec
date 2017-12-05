Name: bro
Version: 2.3.1
Release: alt8

Summary: A Network Intrusion Detection System and Analysis Framework

Group: Networking/Other
License: BSD
Url: http://bro.org

Source0: http://www.bro.org/downloads/release/%name-%version.tar
Source1: bro.service
Source3: bro.init
Source2: bro-logrotate.conf

# Fix for the usage of configure with cmake. This is Fedora specific.
Patch0: bro-2.3-configure.patch
# The aux tools are separate packages. No need to build them.
Patch1: bro-2.3-broctl-disable-aux.patch
# Adjust the paths
Patch2: bro-2.3-broctl-path.patch
# commit 36bc7ba5b5 Handle guess_lexer exceptions in pygments reST directive
Patch3: bro-2.3-pygments-reST-alt.patch

Provides: /var/spool/bro/broctl-config.sh

BuildRequires: rpm-macros-intro-conflicts

BuildRequires: cmake
BuildRequires: libpcap-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel
BuildRequires: ncurses-devel
BuildRequires: curl-devel
BuildRequires: libtool
BuildRequires: byacc
BuildRequires: swig
BuildRequires: bison
BuildRequires: flex
BuildRequires: libmagic-devel
BuildRequires: libxml2-devel
BuildRequires: readline-devel
BuildRequires: gperftools-devel
BuildRequires: bind-devel
BuildRequires: libjemalloc-devel
BuildRequires: python-dev
BuildRequires: python-tools-scripts
BuildRequires: libGeoIP-devel
BuildRequires: systemd
BuildRequires: gcc-c++
# Unfortunately there is check for sendmail during prep
#BuildRequires:    sendmail

BuildRequires: python-module-pysubnettree
#BuildRequires: trace-summary
#BuildRequires: capstats

%description
Bro is an open-source, Unix-based Network Intrusion Detection System (NIDS)
that passively monitors network traffic and looks for suspicious activity.
Bro detects intrusions by first parsing network traffic to extract is
application-level semantics and then executing event-oriented analyzers that
compare the activity with patterns deemed troublesome. Its analysis includes
detection of specific attacks (including those defined by signatures, but also
those defined in terms of events) and unusual activities (e.g., certain hosts
connecting to certain services, or patterns of failed connection attempts).

%package -n binpac
Summary: A language for protocol parsers
Group: Networking/Other

%description -n binpac
BinPAC is a high level language for describing protocol parsers and generates
C++ code. It is currently maintained and distributed with the Bro Network
Security Monitor distribution, however, the generated parsers may be used
with other programs besides Bro.

%package -n binpac-devel
Summary: Development file for binpac
Requires: binpac = %version-%release
Provides: binpac-static = %version-%release
Group: Networking/Other

%description -n binpac-devel
This package contains the header files for binpac.

%package -n broctl
Summary: A control tool for bro
Group: Networking/Other

%description -n broctl
BroControl is an interactive interface for managing a Bro installation which
allows you to, e.g., start/stop the monitoring or update its configuration.

%package -n broccoli
Summary: The bro client communication library
Group: Networking/Other

Requires: %name = %version-%release

%description -n broccoli
Broccoli is the "Bro client communications library". It allows you to create
client sensors for the Bro intrusion detection system. Broccoli can speak a
good subset of the Bro communication protocol, in particular, it can receive
Bro IDs, send and receive Bro events, and send and receive event requests
to/from peering Bros. You can currently create and receive values of pure
types like integers, counters, timestamps, IP addresses, port numbers,
booleans, and strings.

%package -n broccoli-devel
Summary: Development file for broccoli
Group: Networking/Other
Requires: %name = %version-%release
Requires: pkgconfig

%description -n broccoli-devel
This package contains the header files for broccoli.

%package -n python-module-broccoli
Summary: Python bindings for bro
Group: Networking/Other
Requires: %name = %version-%release
Requires: python-module-pysubnettree
Requires: trace-summary
Requires: capstats

%description -n python-module-broccoli
This Python module provides bindings for Broccoli, Bro client communication
library.

%package doc
Summary: Documentation for bro
Group: Documentation
BuildArch: noarch
BuildRequires: python-module-sphinx
BuildRequires: doxygen
BuildRequires: rsync

%description doc
This package contains the documentation for bro.

%prep
%setup
%patch0 -p1 -b .configure
%patch1 -p1 -b .cmake
%patch2 -p1 -b .path
%patch3 -p1

# Paths for broctl broctl/bin/broctl.in
sed -ibak "s|/lib/broctl|%python_sitelibdir/BroControl|g" aux/broctl/BroControl/options.py
sed -ibak "s|/lib|%_libdir/bro|g" aux/broctl/BroControl/options.py

# Shebang
sed -i -e '1i#! /bin/bash' aux/broctl/bin/set-bro-path
sed -i -e '1i#! /bin/awk' aux/broctl/bin/helpers/to-bytes.awk

%build
./configure \
    --prefix=%prefix \
    --libdir=%_libdir \
    --conf-files-dir=%_sysconfdir/bro \
    --python-install-dir=%python_sitelibdir \
    --disable-rpath \
    --enable-debug \
    --enable-mobile-ipv6 \
    --enable-jemalloc \
    --enable-binpac
%make
%make doc

# Fix doc related rpmlint issues
rm -rf %_builddir/%name-%version/build/doc/sphinx_output/html/.tmp
rm -rf %_builddir/%name-%version/build/doc/sphinx_output/html/.buildinfo
rm -rf %_builddir/%name-%version/build/doc/sphinx_output/html/_static/broxygen-extra.js
find %_builddir/%name-%version/build/doc/ -size 0 -delete
#sed -i "s|\r||g" %_builddir/%name-%version/build/doc/sphinx_output/html/objects.inv
#f="%_builddir/%name-%version/build/doc/sphinx_output/html/objects.inv"
#iconv --from=ISO-8859-1 --to=UTF-8 $f > $f.new && \
#touch -r $f $f.new && \
#mv $f.new $f

%install
%makeinstall DESTDIR=%buildroot INSTALL="install -p"

# Install service file
install -D -c -m 644 %SOURCE1 %buildroot%_unitdir/bro.service
install -pD -m755 %SOURCE3 %buildroot%_initdir/%name

# Install config
install -d -m 755 %buildroot%_sysconfdir/bro

# Create runtime dir
install -d -m 755 %buildroot%_localstatedir/run/bro

# Create log dirs
install -D -m 0644 -p %SOURCE2 %buildroot%_sysconfdir/logrotate.d/bro
install -d -m 755 %buildroot%_localstatedir/log/bro
install -d -m 755 %buildroot%_localstatedir/log/bro/archive
install -d -m 755 %buildroot%_localstatedir/log/bro/sorted-logs
install -d -m 755 %buildroot%_localstatedir/log/bro/stats

# Create spool dir
%__install -d -m 755 %buildroot%_localstatedir/spool/bro
%__install -d -m 755 %buildroot%_localstatedir/spool/bro/tmp

# Install scripts
pushd scripts
%__install -d -m 755 %buildroot%_datadir/bro/scripts
popd

# The signature samples should go into a seperate sub-package if possible
# Install example signatures, site policy
%__install -D -d -m 755 %buildroot%_localstatedir/lib/bro/site
%__install -D -d -m 755 %buildroot%_localstatedir/lib/bro/host

# Fix broctl python location
mv %buildroot/usr/lib/broctl/BroControl/ %buildroot%python_sitelibdir/BroControl/
mv %buildroot/usr/lib/broctl/plugins %buildroot%python_sitelibdir/BroControl/plugins

# Move static library to default location
%if %_arch == "x86_64"
mkdir -p %buildroot%_libdir
mv %buildroot/usr/lib/libbinpac.a %buildroot%_libdir/libbinpac.a
%endif

# Remove devel, junk, and zero length files
find "%buildroot%prefix" -iname "*.la" -delete;
#find "%buildroot%prefix" -iname "*.[ha]" -delete;
find "%buildroot" -iname "*.log" -delete;
rm -rf %buildroot%_includedir/binpac.h.in

%preun
%preun_service %name
# the last version of a package is erased
if [ $1 = 0 ]; then
 rm -f "%_spooldir/bro/broctl-config.sh"
fi

%post
# first version of a package is installed
if [ $1 = 1 ]; then
if ! [ -e "%_spooldir/bro/broctl-config.sh" ]; then
broctl install
fi
fi
%post_service %name

%files
%doc CHANGES COPYING NEWS README VERSION
%_bindir/bro
%_bindir/bro-cut
%config(noreplace) %_sysconfdir/bro/networks.cfg
%config(noreplace) %_sysconfdir/bro/node.cfg
%_unitdir/bro.service
%_initdir/%name
%_datadir/bro/

%config(noreplace) %_sysconfdir/logrotate.d/bro
#%ghost %_localstatedir/run/bro
%ghost %_localstatedir/log/bro
%ghost %_localstatedir/lib/bro
%ghost %_localstatedir/spool/bro

%files -n binpac
%doc CHANGES COPYING README
%_bindir/binpac

%files -n binpac-devel
%_includedir/binpac*.h
%_libdir/libbinpac.a

%files -n broctl
%config(noreplace) %_sysconfdir/bro/broctl.cfg
%_bindir/broctl
%python_sitelibdir/BroControl
%_datadir/broctl/

%files -n broccoli
%config(noreplace) %_sysconfdir/bro/broccoli.conf
%_libdir/libbroccoli.so.*

%files -n broccoli-devel
%_bindir/broccoli-config
%_libdir/libbroccoli.so
%_includedir/broccoli.h
%exclude %_libdir/libbroccoli.a

%files -n python-module-broccoli
%python_sitelibdir/*broccoli*

%files doc
%doc doc/LICENSE doc/README
%doc build/doc/sphinx_output/html

%changelog
* Tue Dec 05 2017 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt8
- replace rpm-build-intro with rpm-macros-intro-conflicts

* Sun Oct 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt7
- add BuildRequires: rpm-build-intro (ALT bug 34025)

* Thu Jan 29 2015 Andriy Stepanov <stanv@altlinux.ru> 2.3.1-alt6
- noarch for documentation package

* Thu Jan 29 2015 Andriy Stepanov <stanv@altlinux.ru> 2.3.1-alt5
- Add services script
  Call broctl install

* Wed Jan 28 2015 Andriy Stepanov <stanv@altlinux.ru> 2.3.1-alt3
- Provides /var/spool/bro/broctl-config.sh

* Wed Jan 28 2015 Andriy Stepanov <stanv@altlinux.ru> 2.3.1-alt2
- Build with documentation

* Fri Dec 26 2014 Anton Farygin <rider@altlinux.ru> 2.3.1-alt1
- first build for ALT Linux Sisyphus
