%define _unpackaged_files_terminate_build 1

%def_with doc
%define protocols all

%define realname bird
%define _localstatedir %_var

Name: bird2
Version: 2.13.0
Release: alt1
Summary: BIRD Internet Routing Daemon

Group: Networking/Other
License: GPL-2.0-or-later
URL: http://bird.network.cz

# We conflict with bird 1 for IPv4, packaged as `bird', on purpose.
# We don't replace it for now, though.
# See also on BIRD 1 EOL:
# https://bird.network.cz/pipermail/bird-users/2023-April/016874.html
Conflicts: bird < 2.0.0

# Source-URL: https://gitlab.nic.cz/labs/bird
Source0: %realname-%version.tar
Source1: altlinux.tar

BuildRequires: libreadline-devel libncurses-devel
BuildRequires: flex glibc-kernheaders
%if_with doc
BuildRequires: linuxdoc-tools OpenSP
%endif

%description
BIRD is an Internet Routing Daemon designed to support all the routing
technologies with a clean extensible architecture allowing new routing
protocols to be easily incorporated.

This package includes BIRD version 2.

%if_with doc
%package doc
Summary: Documentation for the BIRD Internet Routing Daemon
Group: Networking/Other
BuildArch: noarch
%description doc
BIRD is an Internet Routing Daemon designed to support all the routing
technologies with a clean extensible architecture allowing new routing
protocols to be easily incorporated.

This package contains optional documentation for BIRD.
%endif

%prep
%setup -n %realname-%version -a1

%build
%configure \
	--runstatedir=/run/%realname \
	--sysconfdir=%_sysconfdir/%realname \
	--with-protocols=%protocols \
        #
%make_build

%if_with doc
# Do not build pdf documentation.
subst '/^userdocs:/s/pdf/html/' doc/Makefile
# Do not build BIRD programmer documentation.
# Contributors are going to work with the source directly anyway.
subst '/(INSTALL_DATA)/s/{bird,prog}/bird/' Makefile
%__make userdocs
%endif

%install
%makeinstall_std
install -pD -m755 distro/altlinux/init.d/%realname %buildroot%_initdir/%realname
install -pD -m755 distro/altlinux/systemd/system/%realname.service %buildroot%_unitdir/%realname.service
install -pD -m644 distro/altlinux/tmpfiles.d/bird.tmpfilesd %buildroot%_tmpfilesdir/bird.conf
mkdir -pm755 %buildroot%_sysconfdir/sysconfig
touch %buildroot%_sysconfdir/sysconfig/%realname

%pre
groupadd -r _bird ||:
useradd -r -d /dev/null -s /dev/null -g _bird _bird ||:

%post
%post_service %realname

%preun
%preun_service %realname

%files
%_initdir/%realname
%_unitdir/%realname.service
%_tmpfilesdir/%realname.conf
%config(noreplace) %_sysconfdir/%realname/%{realname}*.conf
%config(noreplace) %_sysconfdir/sysconfig/%realname
%_sbindir/%{realname}
%_sbindir/%{realname}c
%_sbindir/%{realname}cl
%doc distro/altlinux/README.instances

%if_with doc
%files doc
%doc NEWS README
%doc obj/doc/*.html
%endif

%changelog
* Mon May 08 2023 Arseny Maslennikov <arseny@altlinux.org> 2.13.0-alt1
- Initial build for ALT Sisyphus.
