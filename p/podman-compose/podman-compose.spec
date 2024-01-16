%define name podman-compose
Name: %name
Version: 1.0.6
Release: alt1
Summary: An implementation of Docker Compose Spec with Podman backend
BuildArch: noarch

License: GPL-2.0-only
Group: Development/Python3
Url: https://github.com/containers/podman-compose

Source: %name-%version.tar

BuildRequires: rpm-build-python3

Requires: podman >= 4.8.3-alt2

%description
An implementation of Docker Compose Spec
(https://github.com/compose-spec/compose-spec/blob/master/spec.md)
with Podman backend.
Compose is a tool for defining and running multi-container applications
with Docker or Podman.
With Compose, you define a multi-container application in a
single file, then spin your application up in a single command which does
everything that needs to be done to get it running.
Using podman-compose you can migrate the docker-compose solution to kubernetes.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE README.md
%_bindir/%name
%python3_sitelibdir/*

%changelog
* Mon Jan 15 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.6-alt1
- 1.0.6


