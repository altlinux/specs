# TODO: drop bundled lzo, popt

Name: distcc
Version: 3.3.5
Release: alt1

Summary: distcc is a program to distribute builds C/C++/ Objective C/C++

License: GNU GPL
Group: Development/Tools
Url: http://distcc.org

# Source-url: https://github.com/distcc/distcc/archive/v%version.tar.gz
Source: %name-%version.tar
Source1: distccd.init
Source2: distccd.conf

BuildRequires: glibc-devel-static binutils-devel
BuildRequires: libavahi-devel libpopt-devel
BuildRequires: python3-devel
BuildRequires(pre): rpm-build-python3 rpm-build-intro

%add_python3_req_skip distcc_pump_c_extensions

%description
distcc is a program to distribute builds of C, C++, Objective C
or Objective C++ code across several machines on a network.
distcc should always generate the same results as a local build,
is simple to install and use, and is often two or more
times faster than a local compile.

%package    server
Summary:    Server for distributed C/C++ compilation
Group:      Development/Tools
License:    GPLv2+

Requires:   %name = %EVR
Obsoletes: %name < 3.1

%description server
This package contains the compilation server needed to use %{name}.

%package    pump
Summary:    Include server for distributed C/C++ compilation
Group:      Development/Tools
License:    GPLv2+
Requires:   python3-module-include_server = %EVR
Requires:   %name = %EVR

%description pump
This package contains the include server for use %{name}.

%package -n python3-module-include_server
Summary: distcc include_server for Python 3
Group: Development/Python

%description -n python3-module-include_server
Python3 module distcc include_server.

%prep
%setup

%build
# FIXME: autoreconf in hasher missed CC= in Makefile
#autoreconf
./autogen.sh
%configure --disable-Werror
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sysconfigdir/ %buildroot%_initdir/
install -p -m 0755 %SOURCE1  %buildroot%_initdir/distccd
install -p -m 0644 %SOURCE2 %buildroot%_sysconfigdir/distccd

mkdir -p %buildroot%_sysconfdir/buildreqs/packages/ignore.d/
touch %buildroot%_sysconfdir/buildreqs/packages/ignore.d/distcc

rm -rf %buildroot/etc/default/
rm -rf %buildroot/%_docdir/

%pre server
%groupadd distccd || :
%useradd -g distccd -d /dev/null -c "distccd user" distccd || :

%post server
%post_service distccd

%preun server
%preun_service distccd


%files
%doc AUTHORS NEWS README README.pump TODO
%_bindir/distcc
%_bindir/lsdistcc
%_bindir/distccmon-text
%_man1dir/distcc.*
%_man1dir/lsdistcc.*
%_man1dir/distccmon-text.*
%_sysconfdir/buildreqs/packages/ignore.d/distcc
%dir %_sysconfdir/distcc/
%_sysconfdir/distcc/hosts

%files pump
%_bindir/pump
%_man1dir/include_server*
%_man1dir/pump*

%files server
%doc doc/*.txt
%_initdir/distccd
%config(noreplace) %_sysconfigdir/distccd
%_bindir/distccd
%_sbindir/update-distcc-symlinks
%_man1dir/distccd.*
%_sysconfdir/distcc/*allow*

%files -n python3-module-include_server
%python3_sitelibdir/include_server*

%changelog
* Mon Feb 01 2021 Vitaly Lipatov <lav@altlinux.ru> 3.3.5-alt1
- new version 3.3.5 (with rpmrb script)

* Mon Nov 25 2019 Vitaly Lipatov <lav@altlinux.ru> 3.3.3-alt1
- new version 3.3.3 (with rpmrb script)
- use python3

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1-alt4.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Feb 16 2012 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt4
- fix user/group add status
- fix subpackages requires, fix python buildreqs

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1-alt3.1
- Rebuild with Python-2.7

* Thu Jul 28 2011 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt3
- pack only needed docs

* Thu Jul 28 2011 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt2
- split distcc-pump to standalone package
- obsoleted old distcc package

* Thu Jul 28 2011 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt1
- new version (3.1) with rpmbs script
- split daemon part to distcc-server
- add rule for skip from distcc (ALT bug #16943)

* Fri Apr 13 2007 Lunar Child <luch@altlinux.ru> 2.18.3-alt1
- new version + fixed many bugs (#11490, #11491)

* Mon Sep 27 2004 Pavel S. Mironchik <tibor@altlinux.ru> 2.14-alt7
- bug in spec noreplace distccd.conf

* Tue Sep  21 2004 Pavel S. Mironchik <tibor@altlinux.ru> 2.14-alt6
- init script rewritten

* Tue Sep  21 2004 Pavel S. Mironchik <tibor@altlinux.ru> 2.14-alt5
- Patched for proper ACL list by LAKostis 

* Mon Jul  5 2004 Pavel S. Mironchik <tibor@altlinux.ru> 2.14-alt4
- better sample conf applied

* Mon Jul  5 2004 Pavel S. Mironchik <tibor@altlinux.ru> 2.14-alt3
- problems with findrequires

* Mon Jul  5 2004 Pavel S. Mironchik <tibor@altlinux.ru> 2.14-alt2
- fixed requires

* Mon Jul  5 2004 Pavel S. Mironchik <tibor@altlinux.ru>  2.14-alt1
- adopted for Sisyphus

