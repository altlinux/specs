AutoProv: no

Name: pyfetch
Version: 1.3.5
Release: alt1

Summary: a python system fetch tool

BuildArch: noarch

License: GPL-3.0-only
Group: Other

Url: https://github.com/binarylinuxx/pyfetch
Vcs: https://github.com/binarylinuxx/pyfetch

Source: %name-%version.tar

Patch: Makefile-1.3.5-alt-build.patch

BuildRequires: rpm-build-python3

%description
a python a lightweight system-fetch tool that fully
python independent from other langs

%prep
%setup

%patch -p0

subst "s|/usr/bin|%buildroot%_bindir|" Makefile
subst "s|/etc/pyfetch|%buildroot%_sysconfdir/pyfetch|" Makefile

%build
%install
%makeinstall

%files
%_bindir/*
%_sysconfdir/%name/*
%doc *.md LICENSE

%changelog
* Fri Apr 25 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.3.5-alt1
- 1.2.0 -> 1.3.5

* Mon Apr 21 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.2.0-alt1
- Initial build for ALT Linux.
