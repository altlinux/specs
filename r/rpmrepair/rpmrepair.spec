Name: rpmrepair
Version: 1.1
Release: alt1

Summary: Bash script for repair broken RPM's
License: GPL-3
Group: File tools

Url: https://www.altlinux.org/RPM-repair
Source: %name-%version.tar
BuildArch: noarch
AutoReq: yes

Requires: rpm-build rsync fakeroot

Packager: Leonid Krivoshein <klark@altlinux.org>

%description
This script repacks broken RPM's for ALT-specific repo.

%prep
%setup

%install
mkdir -p -m755 %{buildroot}%_bindir
cat %name.in |sed -E                            \
	-e 's,\{\{\{NAME\}\}\},%name,g'         \
	-e 's,\{\{\{VERSION\}\}\},%version,g'   \
	-e 's,\{\{\{PACKAGER\}\}\},%packager,g' \
		> "%{buildroot}%_bindir/%name"
chmod -- 0755 "%{buildroot}%_bindir/%name"

%files
%_bindir/%name

%changelog
* Wed Aug 19 2020 Leonid Krivoshein <klark@altlinux.org> 1.1-alt1
- Add support for user-defined repair hook (*.repair).

* Sat Aug 01 2020 Leonid Krivoshein <klark@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.

