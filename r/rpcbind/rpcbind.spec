Name: rpcbind
Version: 0.2.1
Release: alt0.5

Summary: RPC port mapper
License: BSD
Group: Networking/Other

Source: %name-%version-%release.tar

BuildRequires: libtirpc-devel libwrap-devel

Provides: portmap = 2:%version-%release
Obsoletes: portmap
Conflicts: man-pages < 3.32-alt2

%description
%name is a server that converts RPC (Remote Procedure Call) program
numbers into DARPA protocol port numbers.  It must be running in order
to make RPC calls.

%prep
%setup

%build
[ ! -f ./autogen.sh ] || sh ./autogen.sh
%configure \
    --enable-libwrap \
    --enable-warmstarts \
    --with-statedir=%_localstatedir/rpcbind \
    --with-rpcuser=rpc \
    #
make

%install
%make_install DESTDIR=%buildroot sbindir=/sbin install
mkdir -p %buildroot%_localstatedir/rpcbind
install -pm0755 -D rpcbind.init %buildroot%_initdir/rpcbind
install -pm0755 -D rpcbind.control %buildroot%_controldir/rpcbind
install -pm0600 -D rpcbind.sysconfig %buildroot%_sysconfdir/sysconfig/rpcbind
install -pm0644 -D rpcbind.service %buildroot%systemd_unitdir/rpcbind.service

%pre
%pre_control rpcbind

%post
/usr/sbin/groupadd -r -f rpc
/usr/sbin/useradd -r -g rpc -d / -s /dev/null -c 'Portmapper RPC user' -n rpc >/dev/null 2>&1 ||:
%post_control -s local rpcbind
%post_service %name

%preun
%preun_service %name

%triggerun -- portmap
[ $2 -eq 0 ] || exit 0
/usr/sbin/control-dump portmap
if /sbin/chkconfig portmap; then
  /sbin/chkconfig rpcbind on
  [ ! -f /var/lock/subsys/portmap ] || touch /var/lock/subsys/rpcbind
fi

%triggerpostun -- portmap
[ $2 -eq 0 ] || exit 0
fi=/var/run/control/rpcbind
fo=/var/run/control/portmap
[ ! -f $fo ] || mv -f $fo $fi
/usr/sbin/control-restore rpcbind ||:
/sbin/service rpcbind condrestart

%files
%doc README

%config(noreplace) %_sysconfdir/sysconfig/rpcbind
%_controldir/rpcbind

%_initdir/%name
%systemd_unitdir/rpcbind.service

/sbin/rpcbind
%_bindir/rpcinfo

%_man8dir/rpcbind.8*
%_man8dir/rpcinfo.8*

%dir %attr(770,root,rpc) %_localstatedir/rpcbind

%changelog
* Mon Apr 25 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt0.5
- fixed rpcbind not dropping privs to `rpc' user

* Sun Apr 24 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt0.4
- rpcinfo packaged

* Fri Apr 22 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt0.3
- 0.2.1-rc3 released

* Sat Nov  6 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- 0.2.0 released

* Thu May 28 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.7-alt1
- Initial build
