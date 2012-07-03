%define nsswitch %_sysconfdir/nsswitch.conf

Name: libnss-tartarus
Version: 0.1.1
Release: alt3.2

Summary: NSS library module for Tartarus

License: %gpl2plus
URL: http://tartarus.ru/
Group: System/Libraries
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

Source: %name-%version.tar
Source1: tnscd.init.%_vendor
Patch: libnss-tartarus-0.1.1-alt-DSO.patch

Requires: libnss-role
Requires: nss-tartarus-daemon = %version-%release
Requires: libice-ssl-krb

Requires(pre): chrooted >= 0.3.5-alt1 chrooted-resolv sed
Requires(postun): chrooted >= 0.3.5-alt1 sed

BuildRequires: libdbus-c++-etersoft-devel >= 0.5.0-alt9
BuildRequires: boost-devel >= 1:1.39.0
BuildRequires: boost-devel boost-filesystem-devel
BuildRequires: libcom_err-devel libice-devel libjson_spirit-devel libkrb5user-devel
BuildRequires: gcc-c++ cmake

BuildRequires(pre): rpm-build-licenses

BuildRequires: Tartarus-SysDB-slice
BuildRequires: libice-ssl-krb-devel
BuildRequires: libkrb5user-devel >= 0.1.0

%description
NSS library module for Tartarus.

%package -n nss-tartarus-daemon
Summary: Authorization proxy and cache daemon for Tartarus
Group: System/Servers

%description -n nss-tartarus-daemon
Authorization proxy and cache daemon for Tartarus

%prep
%setup -q
%patch -p2

%build
mkdir build
cd build
cmake ../ \
        -DCMAKE_INSTALL_PREFIX=/usr \
%if %_lib == lib64
        -DLIB_SUFFIX=64 \
%endif
        -DCMAKE_BUILD_TYPE="Release"

%make_build VERBOSE=1

%install
cd build
%makeinstall DESTDIR=%buildroot

mkdir -p %buildroot%_var/run/tnscd
mkdir -p %buildroot%_initdir
cp %SOURCE1 %buildroot%_initdir/tnscd

%post
if [ "$1" = "1" ]; then
    cp %nsswitch %nsswitch.rpmorig
    grep -q '^passwd:[[:blank:]].\+tartarus' %nsswitch || \
    sed -i 's/^\(passwd:[[:blank:]].\+\)$/\1 tartarus/' %nsswitch
    if grep -q '^group:[[:blank:]].\+role' %nsswitch; then
        grep -q '^group:[[:blank:]].\+tartarus' %nsswitch || \
        sed -i 's/^\(group:[[:blank:]].\+\)\(role\)$/\1tartarus \2/' %nsswitch
    else
        grep -q '^group:[[:blank:]].\+tartarus' %nsswitch || \
        sed -i 's/^\(group:[[:blank:]].\+\)$/\1 tartarus role/' %nsswitch
    fi
fi
update_chrooted all

%postun
if [ "$1" = "0" ]; then
    sed -i -e 's/ tartarus//g' %nsswitch
fi
update_chrooted all

%post -n nss-tartarus-daemon
%post_service tnscd

%preun -n nss-tartarus-daemon
%preun_service tnscd

%files
/%_lib/libnss_*.so.*

%files -n nss-tartarus-daemon
%_sbindir/*
%_initdir/*
%_datadir/dbus-1/system-services/ru.tartarus.DBus.TNSCD.service
%_sysconfdir/dbus-1/system.d/ru.tartarus.DBus.TNSCD.conf
%config(noreplace) %_sysconfdir/Tartarus/clients/*
%dir %_var/run/tnscd

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt3.2
- Fixed build

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt3.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Fri Jul 10 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.1-alt3
- Rebuild with boost-1.39.0

* Wed Apr 29 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.1-alt2
- Fix tnscd rundir creation

* Tue Apr 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.1-alt1
- Fix communictor reinit memory leak

* Thu Apr 02 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.0-alt4
- Add tnscd runner for dbus service
- Clean code

* Thu Apr 02 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.0-alt3
- Fix problem when service call it self due authentification
- Service use anonymous mechanism only

* Tue Mar 31 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.0-alt2
- Fix problems with single thread messagebus service
- Build with new patched version of dbus-c++

* Mon Mar 02 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.0-alt1
- Replace service exchange protocol from JSON to DBus
- Replace build system from SCons to CMake

* Wed Jan 28 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.6-alt1
- Add communicator reinitialization support with kinit

* Thu Jan 22 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.5-alt2
- Add Ice timeout override for daemon

* Tue Nov 25 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.5-alt1
- Move initialization of kerberos into global getIceCommunicator() singleton

* Fri Nov 21 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.4-alt4
- Fix daemon async_accept initialization

* Fri Nov 21 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.4-alt3
- Fix daemon error code

* Fri Nov 21 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.4-alt2
- Fix mask for daemon creating unix socket
- Fix BuildRequires

* Fri Nov 21 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.4-alt1
- Add localstate directory checking and instalation
- Add signals handlers for daemon
- Add global config for unix socket

* Wed Nov 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.3-alt2
- Fix build at x86_64

* Wed Nov 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.3-alt1
- Build tnscd with alpha interface

* Wed Oct 22 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.2-alt2
- Fixed for using krb5user_set_ccname()

* Sun Sep 28 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.2-alt1
- Start to build with libkrb5user
- Fixed nsswitch.conf post/postun scripts

* Thu Sep 11 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.1-alt4
- Fixed buildrequires for new boost build
- Added genererated ice files depends
- Fixed Sconstruct

* Sat Jul 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.1-alt3
- Prerelease done

* Mon Jul 14 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.1-alt2
- Fix requires for nss module and daemon

* Fri Jul 11 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.1-alt1
- Initial rpm build for ALT Linux Sisyphus

