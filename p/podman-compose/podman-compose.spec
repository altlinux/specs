%define name podman-compose
Name: %name
Version: 1.5.0
Release: alt1
Summary: An implementation of Docker Compose Spec with Podman backend
BuildArch: noarch

License: GPL-2.0-only
Group: System/Configuration/Other
Url: https://github.com/containers/podman-compose

Source: %name-%version.tar

BuildRequires: %python3_setup_buildrequires

Requires: podman >= 4.4.2

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
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%_bindir/%name
%python3_sitelibdir/*

%changelog
* Sat Nov 15 2025 Alexey Kostarev <kaf@altlinux.org> 1.5.0-alt1
- 1.3.0 -> 1.5.0

* Fri May 23 2025 Alexey Kostarev <kaf@altlinux.org> 1.3.0-alt2
- Changed Group in podman-compose.spec

* Tue Jan 21 2025 Alexey Kostarev <kaf@altlinux.org> 1.3.0-alt1
- 1.0.6 -> 1.3.0

* Sun Feb 18 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.6-alt2
- Changed dependencies on podman version.

* Mon Jan 15 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.6-alt1
- Initial commit.


