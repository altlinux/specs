%define _unpackaged_files_terminate_build 1
%define plugin_dir %_datadir/headlamp/plugins/%name

Name: maestro
Version: 0.1.0
Release: alt1
Summary: Headlamp plugin for managing Talos cluster via UI
License: Apache-2.0
Group: System/Configuration/Other
Url: https://altlinux.space/alt-orchestra/maestro
ExcludeArch: i586
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: python3-module-setuptools

Requires: talosctl
Requires: nmap

%description
Maestro is a Headlamp plugin that adds a web interface for monitoring and
managing ALT Orchestra/Talos Kubernetes clusters instead of talosctl commands

%prep
%setup

%build
cd %{name}_api/
%pyproject_build

%install
install -pDm 644 %{name}_api/%name-api.service %buildroot%_user_unitdir/%name-api.service

pushd %{name}_api/
%pyproject_install
popd

mkdir -p $(dirname %buildroot%python3_sitelibdir)
mv \
    %buildroot%python3_sitelibdir_noarch \
    %buildroot%python3_sitelibdir

mkdir -p %buildroot%plugin_dir

cd plugin/%name
cp -rt %buildroot%plugin_dir \
    package.json \
    dist/*

%files
%_user_unitdir/%name-api.service
%_bindir/%name-api
%python3_sitelibdir/%{name}_api
%python3_sitelibdir/%{name}_api-%version.dist-info
%plugin_dir

%changelog
* Fri May 15 2026 Vladislav Tsarev <tyaplyapych@altlinux.org> 0.1.0-alt1
- initial build
