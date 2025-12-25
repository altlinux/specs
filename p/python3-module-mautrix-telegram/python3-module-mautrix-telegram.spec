%define oname mautrix_telegram

Name: python3-module-mautrix-telegram
Version: 0.15.3
Release: alt1

Summary: A Matrix-Telegram hybrid puppeting/relaybot bridge
Url: https://pypi.org/project/mautrix-telegram
License: AGPL-3.0-or-later
Group: Development/Python3

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

Source1: mautrix-telegram.service

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

mkdir -p %buildroot%_sysusersdir %buildroot%_libexecdir/tmpfiles.d/
echo 'u mautrix-telegram - "Matrix Telegram puppeting bridge" /var/lib/mautrix-telegram' > %buildroot%_sysusersdir/mautrix-telegram.conf

cat << EOF > %buildroot%_libexecdir/tmpfiles.d/mautrix-telegram.conf
z /etc/mautrix-telegram/* 640 mautrix-telegram mautrix-telegram
d /var/lib/mautrix-telegram/ 700 mautrix-telegram mautrix-telegram
EOF

install -Dm644 %SOURCE1 %buildroot%_unitdir/mautrix-telegram.service
install -Dm644 %buildroot/usr/example-config.yaml %buildroot/etc/mautrix-telegram/example-config.yaml

rm -v %buildroot/usr/example-config.yaml

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version+*.dist-info/METADATA
%_unitdir/mautrix-telegram.service
%_sysusersdir/mautrix-telegram.conf
%_tmpfilesdir/mautrix-telegram.conf
%_sysconfdir/mautrix-telegram/example-config.yaml

%changelog
* Wed Nov 26 2025 Ivan Mazhukin <vanomj@altlinux.org> 0.15.3-alt1
- Initial build for ALT Sisyphus

