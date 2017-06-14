%define modname ethtool
%def_with man
%def_disable python3

Name: python-module-%modname
Version: 0.13
Release: alt1

Summary: Ethernet settings python bindings
Group: Development/Python
License: GPLv2
Url: https://pypi.python.org/pypi/%modname/

Source: https://pypi.io/packages/source/e/%modname/%modname-%version.tar.gz

BuildRequires: python-devel python-module-setuptools libnl-devel
%{?_enable_python3:BuildRequires: rpm-build-python3 python3-devel python3-module-setuptools}
%{?_with_man:BuildRequires: asciidoc-a2x >= 8.6.8}

%description
Python bindings for the ethtool kernel interface, that allows querying
and changing of Ethernet card settings, such as speed, port,
auto-negotiation, and PCI locations.

%package -n python3-module-%modname
Summary: Ethernet settings python3 bindings
Group: Development/Python3

%description -n python3-module-%modname
Python3 bindings for the ethtool kernel interface, that allows querying
and changing of Ethernet card settings, such as speed, port,
auto-negotiation, and PCI locations.


%prep
%setup -n %modname-%version -a0
mv %modname-%version py3build

%build
%python_build
%if_with man
a2x -d manpage -f manpage man/pethtool.8.asciidoc
a2x -d manpage -f manpage man/pifconfig.8.asciidoc
%endif

%if_enabled python3
pushd py3build
%python3_build
popd
%endif

%install
%python_install --install-scripts=%_sbindir
%if_with man
mkdir -p %buildroot%_man8dir
install -m644 man/pethtool.8 %buildroot%_man8dir/pethtool.8
install -m644 man/pifconfig.8 %buildroot%_man8dir/pifconfig.8
%endif

%if_enabled python3
pushd py3build
%python3_install --install-scripts=%_sbindir
popd
%endif

%files
%_sbindir/pethtool
%_sbindir/pifconfig
%python_sitelibdir/ethtool.so
%python_sitelibdir/*.egg-info
%{?_with_man:%_man8dir/*}
%doc README.rst CHANGES.rst

%changelog
* Wed Jun 14 2017 Yuri N. Sedunov <aris@altlinux.org> 0.13-alt1
- 0.13 (new url)

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- 0.12

* Tue Feb 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1.1
- fixed build

* Fri Jun 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- 0.11

* Sat Jan 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Wed Oct 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt1
- first build for Sisyphus
- wait for asciidoc >= 8.6.8 to build mans

