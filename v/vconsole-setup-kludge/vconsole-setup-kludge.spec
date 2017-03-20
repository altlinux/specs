Name: vconsole-setup-kludge
Version: 0.1
Release: alt1
Summary: Setup virtual console after getty start
License: %gpl2plus
Group: System/Configuration/Boot and Init
Source0: vconsole-setup-kludge@.service
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

Requires: systemd

%description
Seems like with some video drivers the font is not set properly.
For example it causes a problem with Cyrillic.
This package contains the systemd service which setup virtual
console once more after getty is started on tty.

%install
install -Dm0644 %SOURCE0 %buildroot%_unitdir/vconsole-setup-kludge@.service
mkdir -p %buildroot%_unitdir/getty@.service.wants/
touch %buildroot%_unitdir/getty@.service.wants/vconsole-setup-kludge@.service

%post
# We can't enable template service for all getty@ instances by systemctl.
# So statically enable it.
if [ "$1" -eq 1 ]; then
	mkdir -p %_unitdir/getty@.service.wants/
	ln -s %_unitdir/vconsole-setup-kludge@.service %_unitdir/getty@.service.wants/vconsole-setup-kludge@.service
fi
systemctl daemon-reload ||:

%preun
if [ "$1" -eq 0 ]; then
	rm -f %_unitdir/getty@.service.wants/vconsole-setup-kludge@.service
fi

%files
%_unitdir/vconsole-setup-kludge@.service
%ghost %_unitdir/getty@.service.wants/vconsole-setup-kludge@.service

%changelog
* Mon Mar 20 2017 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initital build.

