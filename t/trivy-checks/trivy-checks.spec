%define _unpackaged_files_terminate_build 1

Name:           trivy-checks
Version:        2.2.0
Release:        alt1
Summary:        Trivy misconfiguration checks bundle

Group:          Monitoring
License:        MIT
URL:            https://github.com/aquasecurity/trivy-checks

Source:        %name-%version.tar
BuildArch:      noarch

BuildRequires(pre): rpm-macros-systemd
BuildRequires: golang

%description
%summary.

%prep
%setup

%build
%make create-bundle

%install
mkdir -p %buildroot%_sharedstatedir/trivy/policy/content
tar -xzf bundle.tar.gz -C %buildroot%_sharedstatedir/trivy/policy/content

%files
%_sharedstatedir/trivy/policy

%changelog
* Tue Mar 17 2026 Aleksandr Gamzin <gamzin@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus.
