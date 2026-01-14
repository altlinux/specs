Name: pom2metadata
Version: 1.0.0
Release: alt1

Summary: Convert maven pom file to xmvn metadata
License: GPL-3.0+
Group: Development/Java
Url: http://altlinux.org/pom2metadata

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-python3

%description
%summary.

%prep
%setup

%install
install -Dpm0755 %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Mon Jan 12 2026 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build.
