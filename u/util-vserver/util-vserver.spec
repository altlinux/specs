%def_disable dietlibc
%def_without beecrypt
%def_enable shared
%def_disable static
%def_without doc
%def_without python

%define confdir %_sysconfdir/vservers
%define confdefaultdir %confdir/.defaults
%define vrootdir %_localstatedir/vservers

Name: util-vserver
Summary: Linux-VServer utilities
Version: 0.30.216
%define pre -pre3038
Release: alt0.3
License: GPLv2+
Group: System/Base
URL: http://savannah.nongnu.org/projects/%name/
Source0: http://people.linux-vserver.org/~dhozac/t/uv-testing/%name-%version%pre.tar
Source1: tmpfiles.conf
#Patch1: util-vserver-0.30.216-lsb.patch
AutoReq: yes,nosymlinks

BuildRequires: libe2fs-devel
BuildRequires: /bin/mount /sbin/fsck
BuildRequires: %_bindir/nohup %_bindir/ionice
BuildRequires: %_bindir/file %_bindir/strace /bin/find
BuildRequires: /sbin/ip /sbin/iptables /sbin/nameif %_bindir/vconfig
BuildRequires: /sbin/modprobe /sbin/rmmod
BuildRequires: %_bindir/wget %_bindir/rsync
BuildRequires: /bin/gzip /bin/bzip2 /bin/cpio /sbin/restore
%if_with beecrypt
BuildRequires: libbeecrypt-devel
%else
BuildRequires: libnss-devel
%endif
%{?_with_doc:BuildRequires: %_bindir/doxygen %_bindir/xsltproc}
%{?_with_python:BuildRequires: ctags python-devel}
%{?_enable_dietlibc:BuildRequires: dietlibc >= 0.25}

%description
util-vserver provides the components and a framework to setup Linux-VServers.
A virtual server runs inside a linux server. It is nevertheless highly
independent. As such, you can run various services with normal configuration.
The various vservers can't interact with each other and can't interact with
services in the main server.


%prep
%setup -q -n %name-%version%pre
#patch -p1


%build
%configure \
	--with-initrddir=%_initrddir \
	%{subst_enable shared} \
	%{subst_enable static} \
	%{subst_enable dietlibc} \
%if_with beecrypt
	--with-crypto-api=beecrypt \
%else
	--with-crypto-api=nss \
%endif
	--with-initscripts=sysv \
	--with-vrootdir=%vrootdir \
	--enable-release

%make_build all %{?_with_doc:doc}

gzip -9c ChangeLog > ChangeLog.gz


%install
%makeinstall_std install-distribution

install -d -m 0755 %buildroot%vrootdir/.{hash,pkg}
install -pD -m 0644 %SOURCE1 %buildroot/lib/tmpfiles.d/%name.conf

install -d -m 0755 %buildroot{%_cachedir/vservers,%_runtimedir/vservers.rev}
install -d -m 0755 %buildroot%_sysconfdir/{default,sysconfig}
:> %buildroot%_sysconfdir/default/vservers-default
:> %buildroot%_sysconfdir/sysconfig/vservers-default

# add symlink for mageia support
ln -s redhat %buildroot%_libdir/%name/distributions/mageia
# add symlink for altlinux support
ln -s redhat %buildroot%_libdir/%name/distributions/altlinux

%if "%vrootdir" != "/srv/vservers"
install -d -m 0755 %buildroot/srv
ln -sf %vrootdir %buildroot/srv/
%if "%vrootdir" != "%_var/vservers"
ln -sf %vrootdir %buildroot%_var/
%endif
%endif

rm -f %buildroot%_libdir/*.la

rm -rf %buildroot%_libdir/%name/distributions/{centos4,etch,{f,rh,suse9}*}
rm -rf %buildroot%_libdir/%name/distributions/legacy
rm -rf %buildroot%_libdir/%name/legacy
rm -f %buildroot{%_initddir/*-legacy,%_sysconfdir/vservers.conf}
rm -rf %buildroot%_sysconfdir/vservers/.distributions

%add_findreq_skiplist %_libdir/%name/distributions/* %_libdir/%name/vserver-init.functions


%check
%make_build check


%post
/sbin/systemd-tmpfiles --create %name.conf
[ -e %confdefaultdir/vdirbase ] || ln -s %vrootdir %confdefaultdir/vdirbase
[ -e %confdefaultdir/run.rev ] || ln -s %_runtimedir/vservers.rev %confdefaultdir/run.rev
[ -e %confdefaultdir/cachebase ] || ln -s %_cachedir/vservers %confdefaultdir/cachebase
%_sbindir/setattr --barrier %vrootdir %vrootdir/.pkg ||:
%if "%vrootdir" != "/srv/vservers"
[ -e /srv/vservers ] || ln -s "%vrootdir" /srv/
%if "%vrootdir" != "%_var/vservers"
[ -e %_var/vservers ] || ln -s "%vrootdir" %_var/
%endif
%endif


%preun
[ "$1" != 0 ] || rm -rf %_localstatedir/cache/vservers/* 2>/dev/null ||:


%postun
%if "%vrootdir" != "/srv/vservers"
[ -h /srv/vservers ] || rm -f /srv/vservers
%if "%vrootdir" != "%_var/vservers"
[ -h %_var/vservers ] || rm -f %_var/vservers
%endif
%endif


%files
%doc AUTHORS ChangeLog.* NEWS README THANKS
%_initddir/*
/sbin/*
%_sbindir/*
%_libdir/*.so.*
%_libdir/%name
%_man8dir/*
%attr(0000,root,root) %dir %vrootdir
%attr(0755,root,root) %dir %vrootdir/.pkg
%attr(0700,root,root) %dir %vrootdir/.hash
%if "%vrootdir" != "/srv/vservers"
#/srv/*
%if "%vrootdir" != "%_var/vservers"
#%_var/vservers
%endif
%endif
/lib/tmpfiles.d/*
%dir %confdir
%dir %confdefaultdir
%config(noreplace) %_sysconfdir/default/*
%config(noreplace) %_sysconfdir/sysconfig/*
%dir %_cachedir/vservers
%ghost %dir %_runtimedir/vservers.rev
%ghost %confdefaultdir/cachebase
%ghost %confdefaultdir/vdirbase
%ghost %confdefaultdir/run.rev
%exclude %_includedir/*
%exclude %_libdir/*.so
%exclude %_pkgconfigdir/*


%changelog
* Mon Oct 21 2013 Led <led@altlinux.ru> 0.30.216-alt0.3
- move %%vrootdir to %%_localstatedir/vservers

* Mon Oct 21 2013 Led <led@altlinux.ru> 0.30.216-alt0.2
- don't package dirs in /srv/ (sisyphus_check hate suchlike)

* Tue Sep 24 2013 Led <led@altlinux.ru> 0.30.216-alt0.1
- 0.30.216-pre3038
