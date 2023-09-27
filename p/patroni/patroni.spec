Name:    patroni
Version: 3.1.2
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

# From requirements.txt
Requires: python3-module-urllib3 >= 1.19.1
Requires: python3(boto3)
Requires: python3(yaml)
Requires: python3-module-kazoo >= 1.3.1
Requires: python3-module-etcd >= 0.4.3
Requires: python3-module-consul >= 0.7.1
Requires: python3-module-click >= 4.1
Requires: python3-module-prettytable >= 0.7
Requires: python3-module-pysyncobj >= 0.3.8
Requires: python3-module-cryptography >= 1.4
Requires: python3-module-psutil >= 2.0.0
Requires: python3-module-ydiff >= 1.2

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
* Wed Sep 27 2023 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt1
- New version.

* Wed Sep 20 2023 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- New version.

* Fri Aug 04 2023 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version.

* Fri Jul 14 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.4-alt1
- New version.

* Sat Jun 24 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.3-alt1
- New version.

* Sat Apr 08 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt3
- Set Python module requirements from requirements.txt.

* Fri Apr 07 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt2
- Required python3(ydiff) (ALT #45744).

* Sun Mar 26 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version.

* Sat Mar 18 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus
