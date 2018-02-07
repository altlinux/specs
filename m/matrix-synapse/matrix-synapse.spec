Name: matrix-synapse
Version: 0.26.0
Release: alt1

Summary: Synapse: Matrix reference homeserver
License: Apache 2.0
Group: Communications

Url: http://matrix.org

# Source-url: https://github.com/matrix-org/synapse/archive/v%version.tar.gz
Source: %name-%version.tar

# python-pip python-setuptools sqlite3 python-virtualenv
# python-devel libffi-devel libopenssl-devel libjpeg-devel

BuildRequires: python-module-twisted-core >= 16.0.0
BuildRequires: python-module-mock
BuildRequires: python-module-setuptools
BuildRequires: python-module-unpaddedbase64 >= 1.1.0
BuildRequires: python-module-canonicaljson >= 1.0.0
BuildRequires: python-module-signedjson >= 1.0.0
BuildRequires: python-module-matrix-angular-sdk >= 0.6.8
BuildRequires: python-module-service-identity >= 1.0.0
BuildRequires: python-module-OpenSSL >= 0.14
BuildRequires: python-module-yaml
BuildRequires: python-module-pyasn1
BuildRequires: python-module-pynacl >= 0.3.0
BuildRequires: python-module-daemonize
BuildRequires: python-module-bcrypt
BuildRequires: python-module-frozendict >= 0.4
BuildRequires: python-module-Pillow
BuildRequires: python-module-pydenticon
BuildRequires: python-module-ujson
BuildRequires: python-module-blist
BuildRequires: python-module-pysaml2 >= 3.0.0
BuildRequires: python-module-pysaml2 < 4.0.0
BuildRequires: python-module-pymacaroons-pynacl
BuildRequires: python-module-bleach >= 1.4.2
BuildRequires: python-module-netaddr >= 0.7.18
BuildRequires: python-module-jinja2 >= 2.8
#BuildRequires: python-module-matrix-synapse-ldap3 >= 0.1
BuildRequires: python-module-psutil >= 2.0.0
BuildRequires: python-module-lxml
BuildRequires: python-module-msgpack
BuildRequires: python-module-jsonschema >= 2.5.1
BuildRequires: python-module-phonenumbers >= 8.2.0

Requires: python-module-twisted-conch >= 17.5.0
Requires: python-module-twisted-names >= 17.5.0
Requires: python-module-twisted-web >= 17.5.0
Requires: python-module-service-identity >= 1.0.0
Requires: python-module-pysaml2 >= 3.0.0
Requires: python-module-pysaml2 < 4.0.0

# python-modules-sqlite3
Requires: python-module-matrix-angular-sdk

BuildArch: noarch

%description
Matrix is an ambitious new ecosystem for open federated Instant Messaging and VoIP.

Synapse is the reference python/twisted Matrix homeserver implementation.

%prep
%setup
%__subst "s|nacl==0.3.0|nacl>=0.3.0|g" synapse/python_dependencies.py

%build
%python_build

%install
%python_install --install-scripts=%_libexecdir/%name/
mkdir -p %buildroot/etc/synapse
cp contrib/systemd/log_config.yaml %buildroot/etc/synapse/
# TODO
echo >%buildroot/etc/synapse/homeserver.yaml
install -m644 -D contrib/systemd/synapse.service %buildroot%_unitdir/synapse.service
subst "s|=synapse|=_synapse|g" %buildroot%_unitdir/synapse.service
mkdir -p %buildroot/var/{run,lib,log}/synapse
mkdir -p %buildroot%_sbindir/
ln -sr %buildroot%_libexecdir/%name/synctl %buildroot%_sbindir/synctl
mkdir -p %buildroot%_tmpfilesdir/
echo "D /var/run/synapse 0710 _synapse _synapse -" >%buildroot%_tmpfilesdir/%name.conf

%pre
/usr/sbin/groupadd -r -f _synapse
/usr/sbin/useradd -r -g _synapse -d /var/lib/synapse -s /dev/null -c 'Synapse user' _synapse >/dev/null 2>&1 ||:
if [ $1 -gt 1 ]; then
        /usr/sbin/usermod -d /var/lib/synapse _synapse
fi


%files
%doc README.rst UPGRADE.rst CHANGES.rst AUTHORS.rst docs/
%dir %_libexecdir/%name/
%_libexecdir/%name/hash_password
%_libexecdir/%name/register_new_matrix_user
%_libexecdir/%name/synapse_port_db
%_libexecdir/%name/synctl
%_sbindir/synctl
%_unitdir/synapse.service
%_tmpfilesdir/%name.conf
%python_sitelibdir_noarch/*
%dir /etc/synapse/
%attr(0640,root,_synapse) %config(noreplace) /etc/synapse/*
%attr(0710,_synapse,_synapse) /var/run/synapse/
%attr(0710,_synapse,_synapse) /var/lib/synapse/
%attr(0750,_synapse,_synapse) /var/log/synapse/

%changelog
* Wed Feb 07 2018 Vitaly Lipatov <lav@altlinux.ru> 0.26.0-alt1
- new version 0.26.0 (with rpmrb script)

* Sat Oct 07 2017 Vitaly Lipatov <lav@altlinux.ru> 0.23.1-alt1
- new version 0.23.1 (with rpmrb script)

* Mon Jul 17 2017 Vitaly Lipatov <lav@altlinux.ru> 0.22.1-alt1
- new version 0.22.1 (with rpmrb script)

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.21.0-alt1
- initial build for ALT Sisyphus
