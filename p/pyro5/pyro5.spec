#%%def_disable check
%define modulename Pyro5

Name: pyro5
Version: 5.15
Release: alt1
Summary: Distributed object middleware for Python (RPC)
License: MIT
Group: Development/Python3
Url: https://github.com/irmen/Pyro5
# Source-url: https://files.pythonhosted.org/packages/source/P/Pyro5/Pyro5-%version.tar.gz

Source: %modulename-%version.tar

BuildArch: noarch

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_disabled check
%else
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-cloudpickle
BuildRequires: python3-module-dill
BuildRequires: python3-module-msgpack
BuildRequires: python3-module-pytest
BuildRequires: python3-module-serpent >= 1.41
BuildRequires: ca-certificates
%endif

%description
Pyro means PYthon Remote Objects.

It is a library for building applications in which objects can talk
to each other over the network. One can use normal Python method
calls, with almost every possible parameter and return value type,
and Pyro takes care of locating the right object on the right system
to execute the method. It also provides a set of features that enable
building distributed applications. Pyro is a pure Python library and
runs on many different platforms and Python versions.

%package -n python3-module-%modulename
Summary: Distributed object middleware for Python (RPC)
Group: Development/Python3

%description -n python3-module-%modulename
Pyro means PYthon Remote Objects.

It is a library for building applications in which objects can talk
to each other over the network. One can use normal Python method
calls, with almost every possible parameter and return value type,
and Pyro takes care of locating the right object on the right system
to execute the method. It also provides a set of features that enable
building distributed applications. Pyro is a pure Python library and
runs on many different platforms and Python versions.

%prep
%setup -n %modulename-%version
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -m "not network"

%files
%_bindir/%name-*

%files -n python3-module-%modulename
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Mon Oct 23 2023 Anton Midyukov <antohami@altlinux.org> 5.15-alt1
- new version (5.15) with rpmgs script

* Sat Apr 15 2023 Anton Midyukov <antohami@altlinux.org> 5.14-alt1
- initial build
