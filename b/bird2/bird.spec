%define with_doc 0
%define protocols bfd,bgp,ospf,static

%define realname bird
%define _localstatedir %_var

Name: bird2
Version: 2.0.2
Release: alt1
Summary: BIRD Internet Routing Daemon

Group: Networking/Other
License: GPL
URL: http://bird.network.cz

Provides: %{realname} = %version
Provides: %{realname}6 = %version
Obsoletes: %{realname} < %version, %{realname}6

# git clone git://git.nic.cz/bird.git
Source0: %realname.tar.xz

BuildRequires: libreadline-devel libncurses-devel
BuildRequires: flex glibc-kernheaders
%if %with_doc
BuildRequires: linuxdoc-tools OpenSP
%endif

%description
BIRD is an Internet Routing Daemon designed to support all the routing
technologies with a clean extensible architecture allowing new routing
protocols to be easily incorporated.

%if %with_doc
%package doc
Summary: Optional documentation for the BIRD Internet Routing Daemon
Group: Networking/Other
BuildArch: noarch
%description doc
%summary
%endif

%prep
%setup -n %realname

%build
autoconf
%define _configure_script ../configure

mkdir bird-ipv6
pushd bird-ipv6
  %configure	\
		--sysconfdir=%_sysconfdir/%realname \
		--enable-ipv6 --with-suffix=6 \
		--with-protocols=%protocols
  %make_build
popd

mkdir bird-ipv4
pushd bird-ipv4
  %configure	\
		--sysconfdir=%_sysconfdir/%realname \
		--with-suffix=4 \
		--with-protocols=%protocols
  %make_build
popd

%if %with_doc
pushd doc
  make prog.sgml
  ./sgml2html prog.sgml
  ./sgml2html bird.sgml
popd
%endif

%install
%makeinstall -C bird-ipv6 sysconfdir=%buildroot%_sysconfdir/%realname
%makeinstall -C bird-ipv4 sysconfdir=%buildroot%_sysconfdir/%realname
install -pD -m755 %realname.rc %buildroot%_initdir/%realname
mkdir -pm755 %buildroot%_sysconfdir/sysconfig
touch %buildroot%_sysconfdir/sysconfig/%realname

%post
%post_service %realname

%preun
%preun_service %realname

%files
%_initdir/%realname
%config(noreplace) %_sysconfdir/%realname/%{realname}*.conf
%config(noreplace) %_sysconfdir/sysconfig/%realname
%_sbindir/%{realname}*

%if %with_doc
%files doc
%doc NEWS README doc/*.html
%endif

%changelog
* Mon Apr 16 2018 Gremlin from Kremlin <gremlin@altlinux.org> 2.0.2-alt1
- first build of version 2
