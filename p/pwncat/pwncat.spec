%define _unpackaged_files_terminate_build 1
%define pypi_name pwncat

%def_without check

Name: %pypi_name
Version: 0.1.2
Release: alt1
Summary: pwncat - netcat on steroids with Firewall   
License: MIT
Group: Networking/Other
URL: https://github.com/cytopia/pwncat
BuildArch: noarch

Source0: %name-%version.tar         
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3-dev

%if_with check
BuildRequires: python3(pytest)
%endif

%package -n python3-module-%pypi_name
Summary: %summary
Group: Development/Python3
BuildArch: noarch
%py3_provides %pypi_name

%description -n python3-module-%pypi_name
Python files for %pypi_name

%description
TCP/UDP communication suite for firewall and IDS/IPS evasion, bind and
reverse shell, self-injecting shell and port forwarding magic. pwncat is
fully scriptable with Python (PSE).

%prep
%setup
%patch -p1
# Fix build with setuptools 62.1
# https://github.com/cytopia/pwncat/issues/113
sed -i "10i packages=[]," setup.py

%build
%make_build
%pyproject_build

%install
%make_install
%pyproject_install
install -Dp -m 0644 man/%pypi_name.1 %buildroot%_man1dir/%pypi_name.1

%files
%doc README.md
%_man1dir/%pypi_name.*
%_bindir/%pypi_name

%files -n python3-module-%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Mon Dec 23 2024 Pavel Shilov <zerospirit@altlinux.org> 0.1.2-alt1
- initial build for Sisyphus
