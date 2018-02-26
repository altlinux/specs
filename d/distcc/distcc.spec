Name: distcc
Version: 3.1
Release: alt4.1

Summary: distcc is a program to distribute builds C/C++/ Objective C/C++

License: GNU GPL
Group: Development/Tools
Url: http://distcc.org

Source0: http://distcc.googlecode.com/files/distcc-3.1.tar
Source1: distccd.init
Source2: distccd.conf

# Manually removed: python-module-z3c python-module-z3c.recipe python-module-peak  python-module-paste
# Automatically added by buildreq on Thu Jul 28 2011
# optimized out: pkg-config python-base python-devel python-modules python-modules-compiler python-modules-email
BuildRequires: libavahi-devel libpopt-devel python-devel


BuildRequires(pre): rpm-build-intro

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

Requires:   %name = %version-%release
Obsoletes: %name < 3.1

%description server
This package contains the compilation server needed to use %{name}.

%package    pump
Summary:    Include server for distributed C/C++ compilation
Group:      Development/Tools
License:    GPLv2+

Requires:   %name = %version-%release

%description pump
This package contains the include server for use %{name}.

%prep
%setup -n %name-%version

%build
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
%_man1dir/distccmon-text.*
%_sysconfdir/buildreqs/packages/ignore.d/distcc
%dir %_sysconfdir/distcc/
%_sysconfdir/distcc/hosts

%files pump
%_bindir/pump
%_man1dir/include_server*
%_man1dir/pump*
%python_sitelibdir/include_server*

%files server
%doc doc/*.txt
%_initdir/distccd
%config(noreplace) %_sysconfigdir/distccd
%_bindir/distccd
%_man1dir/distccd.*
%_sysconfdir/distcc/*allow*

%changelog
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

