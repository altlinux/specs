Name: ryu
Version: 4.30
Release: alt4

Summary: Component-based Software-defined Networking Framework
License: ASL 2.0
Group: Development/Python3
Url: http://osrg.github.io/ryu/
BuildArch: noarch

Source: %name-%version.tar.gz

Requires: python3-module-%name

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr
BuildRequires: python3-module-pip
BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme
BuildRequires: python3-module-eventlet >= 0.15
BuildRequires: python3-module-msgpack >= 0.3.0
BuildRequires: python3-module-netaddr
BuildRequires: python3-module-oslo.config >= 2.5.0
BuildRequires: python3-module-routes
BuildRequires: python3-module-tinyrpc
BuildRequires: python3-module-six >= 1.4.0
BuildRequires: python3-module-webob >= 1.2
BuildRequires: python3-module-openvswitch  >= 2.6.0


%description
Ryu is a component-based software defined networking framework.

Ryu provides software components with well defined API that make it
easy for developers to create new network management and control
applications. Ryu supports various protocols for managing network
devices, such as OpenFlow, Netconf, OF-config, etc. About OpenFlow,
Ryu supports fully 1.0, 1.2, 1.3, 1.4 and Nicira Extensions.

All of the code is freely available under the Apache 2.0 license. Ryu
is fully written in Python.

%package -n python3-module-%name
Summary: Component-based Software-defined Networking Framework
Group: Development/Python3

%add_python3_req_skip neutron
%add_python3_req_skip neutron.common

%description -n python3-module-%name
Ryu is a component-based software defined networking framework.

Ryu provides software components with well defined API that make it
easy for developers to create new network management and control
applications. Ryu supports various protocols for managing network
devices, such as OpenFlow, Netconf, OF-config, etc. About OpenFlow,
Ryu supports fully 1.0, 1.2, 1.3, 1.4 and Nicira Extensions.

All of the code is freely available under the Apache 2.0 license. Ryu
is fully written in Python.

%package doc
Summary: Documentation for Software-defined Networking Framework
Group: Development/Documentation

%description doc
Documentation for Software-defined Networking Framework

%package -n python3-module-%name-tests
Group: Development/Python3
Summary: Tests for Software-defined Networking Framework

%description -n python3-module-%name-tests
Tests for Software-defined Networking Framework

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -type f \( -name '*.py' -o -name '%name' -o -name '%name-manager' \))

# drop deps in egginfo, let rpm handle them
rm tools/*-requires
rm tools/install_venv.py
# Remove non-working tests (internet connection needed)
rm -vf %name/tests/unit/test_requirements.py
# Remove pip usage (used only in test_requirements.py)
sed -i '/^from pip/d' ryu/utils.py

%build
%python3_build

# generate html docs
export PYTHONPATH="$( pwd ):$PYTHONPATH"
%__python3 setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python3_install

mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_logrotatedir
mv %buildroot/usr/etc/ryu/ryu.conf %buildroot%_sysconfdir/%name/%name.conf
install -m 644 debian/log.conf %buildroot%_logrotatedir/%name

%files
%doc README.rst
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/%name/*

%files -n python3-module-%name
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

# mininet? xml_compare?
%files -n python3-module-%name-tests
%python3_sitelibdir/*/tests

%files doc
%doc doc/build/html


%changelog
* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.30-alt4
- python shebang fixed

* Sun Oct 27 2019 Grigory Ustinov <grenka@altlinux.org> 4.30-alt3
- Build without python2.

* Thu Jan 10 2019 Alexey Shabalin <shaba@altlinux.org> 4.30-alt2
- add python3 package

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 4.30-alt1
- 4.30

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.14-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 06 2017 Alexey Shabalin <shaba@altlinux.ru> 4.14-alt1
- 4.14

* Tue Aug 30 2016 Alexey Shabalin <shaba@altlinux.ru> 4.5-alt1
- 4.5

* Fri Apr 15 2016 Alexey Shabalin <shaba@altlinux.ru> 3.30-alt1
- 3.30

* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 3.26-alt1
- 3.26

* Fri May 29 2015 Alexey Shabalin <shaba@altlinux.ru> 3.21-alt1
- 3.21

* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 3.19-alt1
- Initial release
