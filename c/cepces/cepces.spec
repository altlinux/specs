%define _libexecdir /usr/libexec

Name:           cepces
Version:        0.3.7
Release:        alt1
Summary:        Certificate Enrollment through CEP/CES
Group:          System/Configuration/Other
BuildArch:      noarch

License:        GPLv3+
URL:            https://github.com/openSUSE/%{name}

# Sources:      https://github.com/openSUSE/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source:         %name-%version.tar
Patch:          %name-%version-alt.patch

BuildRequires:  rpm-build-python3
Requires:       python3-module-%name = %version-%release

%description
cepces is an application for enrolling certificates through CEP and CES.
It requires certmonger to operate.

Only simple deployments using Microsoft Active Directory Certificate Services
have been tested.

%package -n python3-module-%name
Summary:        Python part of %name
Group:          Development/Python3
BuildArch:      noarch

BuildRequires:  python3(setuptools)
BuildRequires:  python3(cryptography)
BuildRequires:  python3(requests)
BuildRequires:  python3(gssapi)
BuildRequires:  python3(requests-gssapi)

%description -n python3-module-%name
%name is an application for enrolling certificates through CEP and CES.
This package provides the Python part for CEP and CES interaction.

%package certmonger
Summary:        certmonger integration for %name
Requires:       %name = %version-%release
Requires:       certmonger
Group:          System/Configuration/Other
BuildArch:      noarch

%description certmonger
Installing %name-certmonger adds %name as a CA configuration.
Uninstall revert the action.

%prep
%setup -q
%patch -p1

%build
%python3_build

%install
%python3_install

install -d  %buildroot%_logdir/%name

# Configuration files
install -d -m 0755 %buildroot%_sysconfdir/%name/
install -m 644 conf/cepces.conf.dist %buildroot%_sysconfdir/%name/cepces.conf
install -m 644 conf/logging.conf.dist %buildroot%_sysconfdir/%name/logging.conf

# Default logrotate file
install -d -m 0755 %buildroot%_sysconfdir/logrotate.d
cat <<EOF>%buildroot%_sysconfdir/logrotate.d/%name
/var/log/%name/*.log {
    compress
    delaycompress
    missingok
    rotate 4
}
EOF

%check
# Create a symlink so test can locate cepces_test
ln -s tests/cepces_test .
%__python3 setup.py test

%post certmonger
# Install the CA into certmonger.
if [[ "$1" == "1" ]]; then
  getcert add-ca -c %name \
    -e %_libexecdir/certmonger/%name-submit >/dev/null || :
fi

%preun certmonger
# Remove the CA from certmonger, unless it's an upgrade.
if [[ "$1" == "0" ]]; then
  getcert remove-ca -c %name >/dev/null || :
fi

%files
%doc README.rst
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_sysconfdir/%name/logging.conf
%attr(0700,-,-) %dir %_logdir/%name
%config(noreplace) %_sysconfdir/logrotate.d/%name

%files -n python3-module-%name
%doc LICENSE
%python3_sitelibdir/%name
%python3_sitelibdir/*.egg-info

%files certmonger
%_libexecdir/certmonger/%name-submit

%changelog
* Tue Mar 21 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.3.7-alt1
- Add support the openssl security level

* Wed Nov 30 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.3.6-alt1
- Update to latest release

* Sat Sep 17 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.3.5-alt1
- Initial build for sisyphus

