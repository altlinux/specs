%def_with check

Name: sshuttle
Version: 1.3.2
Release: alt1

Summary: Transparent proxy server that works as a poor man's VPN
License: LGPL-2.1
Group: Other
URL: https://sshuttle.readthedocs.org
VCS: https://github.com/sshuttle/sshuttle

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: makeinfo
%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-flake8
BuildRequires: python3-module-editables
%endif

BuildArch: noarch

Source: %name-%version.tar

# cmdline_options python module is automaticall generated during execution
%add_python3_req_skip sshuttle.cmdline_options

%description
As far as I know, sshuttle is the only program that solves the following
common case:
- Your client machine (or router) is Linux, FreeBSD, MacOS or Windows.
- You have access to a remote network via ssh.
- You don't necessarily have admin access on the remote network.
- The remote network has no VPN, or only stupid/complex VPN protocols
(IPsec, PPTP, etc). Or maybe you are the admin and you just got frustrated
with the awful state of VPN tools.
- You don't want to create an ssh port forward for every single host/port on
the remote network.
- You hate openssh's port forwarding because it's randomly slow and/or stupid.
- You can't use openssh's PermitTunnel feature because it's disabled by
default on openssh servers; plus it does TCP-over-TCP, which has terrible
performance.


%prep
%setup -n %name-%version

%build
%pyproject_build

pushd docs
make man
make info
popd

%install
%pyproject_install

pushd docs
install -pD -m0644 _build/man/sshuttle.1 %buildroot%_man1dir/sshuttle.1
install -pD -m0644 _build/texinfo/sshuttle.info %buildroot%_infodir/sshuttle.info
popd

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}
%_man1dir/sshuttle.1*
%_infodir/sshuttle.info*

%changelog
* Wed Nov 19 2025 Alexander Stepchenko <geochip@altlinux.org> 1.3.2-alt1
- Initial build.
