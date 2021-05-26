%define git 3f9c625

Name: acpilight
Version: 1.2
Release: alt1.g%{git}

Summary: Replacement for xbacklight that uses the ACPI interface to set brightness
License: GPL-3.0+
Group: System/Kernel and hardware
URL: https://gitlab.com/wavexx/acpilight/
Patch0: %name-%version-%release.patch
Source0: https://gitlab.com/wavexx/acpilight/-/archive/v%{version}/%{name}-%{version}.tar.gz

Conflicts: xbacklight

BuildRequires: rpm-build-python3
BuildArch: noarch

%description
Replacement for xbacklight that uses the ACPI interface to set brightness

%prep
%setup -q -n %name-%version

%build

%install
mkdir -p %buildroot{%_bindir,%_udevrulesdir,%_man1dir}
install -m755 xbacklight %buildroot%{_bindir}/
install -m644 xbacklight.1 %buildroot%{_man1dir}/
install -m644 90-backlight.rules %buildroot%{_udevrulesdir}/

%post
echo 'To use the xbacklight binary as a regular user, you must be a part of the video group'

%files
%doc README.rst NEWS.rst
%_bindir/*
%_man1dir/*
%_udevrulesdir/*.rules

%changelog
* Wed May 26 2021 L.A. Kostis <lakostis@altlinux.ru> 1.2-alt1.g3f9c625
- v1.2-4-g3f9c625
- Don't obsolete xbacklight yet as it might be something which
  still depends on it.
- Initial build for ALTLinux.
