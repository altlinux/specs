%global modname docker-squash

Name: docker-squash
Version: 1.2.2
Release: alt1

Summary: Docker layer squashing tool

License: MIT
Group: File tools
Url: https://github.com/goldmann/docker-squash

# Source-url: https://github.com/goldmann/docker-squash/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Tool to squash layers in Docker images.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%doc LICENSE
%_bindir/docker-squash
%python3_sitelibdir/docker_squash/
%python3_sitelibdir/docker_squash-*.dist-info/

%changelog
* Mon Feb 10 2025 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Mon Feb 10 2025 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Sisyphus (thanks, Fedora!)
