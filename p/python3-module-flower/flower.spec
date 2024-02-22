%define _unpackaged_files_terminate_build 1

Name: python3-module-flower
Version: 2.0.1
Release: alt1
Summary: Real-time monitor and web admin for Celery
License: BSD
Group: Other
Url: https://github.com/mher/flower
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Flower is an open-source web application for monitoring
and managing Celery clusters. It provides real-time
information about the status of Celery workers and tasks.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/flower
%python3_sitelibdir/%{pyproject_distinfo flower}


%changelog
* Thu Feb 22 2024 Alexander Makeenkov <amakeenk@altlinux.org> 2.0.1-alt1
- Initial build for ALT.
