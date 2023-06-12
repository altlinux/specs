%def_disable snapshot
#%%define _unpackaged_files_terminate_build 1
%define pypi_name cachecontrol
%define modname CacheControl

%def_enable check

Name: python3-module-%pypi_name
Version: 0.13.1
Release: alt1

Summary: CacheControl is a port of the caching algorithms in httplib2
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/ionrock/cachecontrol

%if_disabled snapshot
Source: https://github.com/ionrock/cachecontrol/archive/v%version/%pypi_name-%version.tar.gz
%else
Vcs: https://github.com/ionrock/cachecontrol.git
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(flit_core)

%{?_enable_check:BuildRequires: python3(pytest)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(requests)
BuildRequires: python3(msgpack)
BuildRequires: python3(mock)
BuildRequires: python3(redis)
BuildRequires: python3(filelock)
BuildRequires: python3-module-cherrypy >= 18.8.0}

%description
CacheControl is a port of the caching algorithms in "httplib2" for use with
"requests" session object.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%_bindir/doesitcache
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Thu Jun 08 2023 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1

* Mon Jun 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0

* Mon Sep 12 2022 Yuri N. Sedunov <aris@altlinux.org> 0.12.12-alt1
- first build for Sisyphus



