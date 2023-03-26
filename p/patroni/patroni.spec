Name:    patroni
Version: 3.0.2
Release: alt1

Summary: A template for PostgreSQL High Availability with Etcd, Consul, ZooKeeper, or Kubernetes
License: MIT
Group:   Other
URL:     https://github.com/zalando/patroni

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-psycopg2

BuildArch: noarch

Source: %name-%version.tar

%description
Patroni is a template for you to create your own customized, high-availability
solution using Python and - for maximum accessibility - a distributed
configuration store like ZooKeeper, etcd, Consul or Kubernetes. Database
engineers, DBAs, DevOps engineers, and SREs who are looking to quickly deploy
HA PostgreSQL in the datacenter-or anywhere else-will hopefully find it useful.

We call Patroni a "template" because it is far from being a one-size-fits-all
or plug-and-play replication system. It will have its own caveats. Use wisely.

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc CODEOWNERS MAINTAINERS README.rst
%_bindir/*
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Sun Mar 26 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version.

* Sat Mar 18 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus
