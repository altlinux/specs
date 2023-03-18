%define pypi_name pysyncobj

Name:    python3-module-%pypi_name
Version: 0.3.12
Release: alt1

Summary: A library for replicating your python class between multiple servers, based on raft protocol
License: MIT
Group:   Development/Python3
URL:     https://github.com/bakwc/PySyncObj

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
PySyncObj is a python library for building fault-tolerant distributed systems.
It provides the ability to replicate your application data between multiple
servers. It has following features:

* raft protocol for leader election and log replication
* Log compaction - it use fork for copy-on-write while serializing data on disk
* Dynamic membership changes - you can do it with syncobj_admin utility
  or directly from your code
* Zero downtime deploy - no need to stop cluster to update nodes
* In-memory and on-disk serialization - you can use in-memory mode for small
  data and on-disk for big one
* Encryption - you can set password and use it in external network
* Python2 and Python3 on linux, macos and windows - no dependencies required
  (only optional one, eg. cryptography)
* Configurable event loop - it can works in separate thread with it's own event
  loop - or you can call onTick function inside your own one
* Convenient interface - you can easily transform arbitrary class into a
  replicated one (see example below).

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Mar 18 2023 Andrey Cherepanov <cas@altlinux.org> 0.3.12-alt1
- Initial build for Sisyphus
