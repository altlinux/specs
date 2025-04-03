Name:    the-littlest-jupyterhub
Version: 2.0.0
Release: alt1

Summary: Simple JupyterHub distribution for 1-100 users on a single server
License: BSD-3-Clause
Group:   Other
URL:     https://github.com/jupyterhub/the-littlest-jupyterhub

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar
Source1: /var/lib/jupyterhub.service

%add_python3_req_skip requests.packages.urllib3.exceptions
%py3_requires requests.packages urllib3.exceptions jupyterhub
Requires: traefik

%description
The Littlest JupyterHub (TLJH) distribution helps you provide Jupyter Notebooks
to 1-100 users on a single server.

The primary audience are people who do not consider themselves 'system
administrators' but would like to provide hosted Jupyter Notebooks for their
students or users. All users are provided with the same environment, and
administrators can easily install libraries into this environment without any
specialized knowledge.

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install
install -Dpm 0644 %SOURCE1 %buildroot%_unitdir/jupyterhub.service
mkdir -p %buildroot%_sharedstatedir/jupyterhub/{hub,user,state,config}

%files
%doc *.md
%_bindir/tljh-config
%python3_sitelibdir/tljh/
%python3_sitelibdir/%{pyproject_distinfo the_littlest_jupyterhub}
%config(noreplace) %_unitdir/jupyterhub.service
%dir %_sharedstatedir/jupyterhub
%dir %_sharedstatedir/jupyterhub/hub
%dir %_sharedstatedir/jupyterhub/user
%dir %_sharedstatedir/jupyterhub/state
%dir %_sharedstatedir/jupyterhub/config

%preun
%preun_service jupyterhub.service

%post
%post_service jupyterhub.service

%changelog
* Wed Jan 29 2025 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus.
