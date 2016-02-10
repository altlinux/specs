Name: hdu
Version: 0.2.2.5
Release: alt1
Summary: Human-friendly summary of disk usage

Group: File tools
License: GPLv3+
Url: https://bitbucket.org/norok2/hdu

Source: %name-%version.tar
Patch: %name-%version-alt.patch
Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch
BuildRequires: python-module-setuptools

%description
Human-friendly summary of disk usage.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/%name
%python_sitelibdir/%{name}*
%doc README

%changelog
* Wed Feb 10 2016 Terechkov Evgenii <evg@altlinux.org> 0.2.2.5-alt1
- Initial build for ALT Linux Sisyphus
