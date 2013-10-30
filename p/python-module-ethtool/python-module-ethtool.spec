%define _name python-ethtool
%def_without man

Name: python-module-ethtool
Version: 0.8
Release: alt1

Summary: Ethernet settings python bindings
Group: Development/Python
License: GPLv2
Url: http://git.fedorahosted.org/cgit/%_name.git

Source: https://fedorahosted.org/releases/p/y/%_name/%_name-%version.tar.bz2

BuildRequires: python-devel libnl1-devel
%{?_with_man:BuildRequires: asciidoc >= 8.6.8}

%description
Python bindings for the ethtool kernel interface, that allows querying
and changing of Ethernet card settings, such as speed, port,
auto-negotiation, and PCI locations.

%prep
%setup -n %_name-%version

%build
%python_build
%if_with man
a2x -d manpage -f manpage man/pethtool.8.asciidoc
a2x -d manpage -f manpage man/pifconfig.8.asciidoc
%endif

%install
%python_install
mkdir -p %buildroot{%_sbindir,%_man8dir}
install -m755 pethtool.py %buildroot%_sbindir/pethtool
install -m755 pifconfig.py %buildroot%_sbindir/pifconfig
%if_with man
install -m644 man/pethtool.8 %buildroot%_man8dir/pethtool.8
install -m644 man/pifconfig.8 %buildroot%_man8dir/pifconfig.8
%endif

%files
%_sbindir/pethtool
%_sbindir/pifconfig
%python_sitelibdir/ethtool.so
%python_sitelibdir/*.egg-info
%{?_with_man:%_man8dir/*}

%changelog
* Wed Oct 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt1
- first build for Sisyphus
- wait for asciidoc >= 8.6.8 to build mans

