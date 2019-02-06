Name: matrix-synapse
Version: 0.99.0
Release: alt1

Summary: Synapse: Matrix reference homeserver
License: Apache 2.0
Group: Communications

Url: http://matrix.org

# Source-url: https://github.com/matrix-org/synapse/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name.service

# python-pip python-setuptools sqlite3 python-virtualenv
# python-devel libffi-devel libopenssl-devel libjpeg-devel

BuildRequires(pre): rpm-build-intro >= 2.1.9

%py_use setuptools
%py_use matrix-angular-sdk >= 0.6.8


# Note: update from synapse/python_dependencies.py
%py_use jsonschema >= 2.5.1
%py_use frozendict >= 1
%py_use unpaddedbase64 >= 1.1.0
%py_use canonicaljson >= 1.1.3
%py_use signedjson >= 1.0.0
%py_use pynacl >= 1.2.1
%py_use service_identity >= 16.0.0
# logcontext handling relies on the ability to cancel inlineCallbacks
# (https://twistedmatrix.com/trac/ticket/4632) which landed in Twisted 18.7.
%py_use twisted-core >= 18.7.0
%py_use treq >= 15.1
# Twisted has required pyopenssl 16.0 since about Twisted 16.6.
%py_use OpenSSL >= 16.0.0
%py_use yaml >= 3.11
%py_use pyasn1 >= 0.1.9
%py_use pyasn1-modules >= 0.0.7
%py_use daemonize >= 2.3.1
%py_use bcrypt >= 3.1.0
%py_use Pillow >= 3.1.2
%py_use sortedcontainers >= 1.4.4
%py_use psutil >= 2.0.0
%py_use pymacaroons-pynacl >= 0.13.0
%py_use msgpack >= 0.5.0
%py_use phonenumbers >= 8.2.0
%py_use six >= 1.10
# prometheus_client 0.4.0 changed the format of counter metrics
# (cf https://github.com/matrix-org/synapse/issues/4001)
%py_use prometheus_client >= 0.0.18
%py_use prometheus_client < 0.4.0
# we use attr.s(slots), which arrived in 16.0.0
%py_use attrs >= 17.4.0
%py_use netaddr >= 0.7.18

# Conditional
#py_use matrix-synapse-ldap3 >= 0.1
# "email.enable_notifs"
%py_use jinja2 >= 2.9
%py_use bleach >= 1.4.2
# "acme": ["txacme>=0.9.2"],

%py_use pysaml2 >= 4.5.0
# "url_preview"
%py_use lxml >= 3.5.0
# "test"
%py_use mock >= 2.0



# for /usr/lib/matrix-synapse/sync_room_to_group.pl
BuildRequires: perl-CPAN
BuildRequires: perl-JSON-XS

Requires: python-module-twisted-conch >= 17.5.0
Requires: python-module-twisted-names >= 17.5.0
Requires: python-module-twisted-web >= 17.5.0
#Requires: python-module-service-identity >= 1.0.0
Requires: python-module-twisted-mail >= 17.5.0
#Requires: python-module-pysaml2 >= 3.0.0
#Requires: python-module-pysaml2 < 4.0.0

# python-modules-sqlite3
#Requires: python-module-matrix-angular-sdk

BuildArch: noarch

%description
Matrix is an ambitious new ecosystem for open federated Instant Messaging and VoIP.

Synapse is the reference python/twisted Matrix homeserver implementation.

%prep
%setup
#__subst "s|nacl==0.3.0|nacl>=0.3.0|g" synapse/python_dependencies.py

%build
%python_build

%install
%python_install --install-scripts=%_libexecdir/%name/
mkdir -p %buildroot/etc/synapse
cp contrib/systemd/log_config.yaml %buildroot/etc/synapse/
# TODO
echo >%buildroot/etc/synapse/homeserver.yaml
install -m644 -D %SOURCE1 %buildroot%_unitdir/matrix-synapse.service
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
%doc README.rst UPGRADE.rst CHANGES.md AUTHORS.rst docs/
%dir %_libexecdir/%name/
%_libexecdir/%name/hash_password
%_libexecdir/%name/register_new_matrix_user
%_libexecdir/%name/synapse_port_db
%_libexecdir/%name/synctl
%_libexecdir/%name/move_remote_media_to_new_store.py
%_libexecdir/%name/sync_room_to_group.pl
%_libexecdir/%name/generate_config
%_sbindir/synctl
%_unitdir/matrix-synapse.service
%_tmpfilesdir/%name.conf
%python_sitelibdir_noarch/*
%dir /etc/synapse/
%attr(0640,root,_synapse) %config(noreplace) /etc/synapse/*
%attr(0710,_synapse,_synapse) /var/run/synapse/
%attr(0710,_synapse,_synapse) /var/lib/synapse/
%attr(0750,_synapse,_synapse) /var/log/synapse/

%changelog
* Wed Feb 06 2019 Vitaly Lipatov <lav@altlinux.ru> 0.99.0-alt1
- new version 0.99.0 (with rpmrb script)
- update requires

* Tue Jan 22 2019 Vitaly Lipatov <lav@altlinux.ru> 0.34.1.1-alt1
- new version 0.34.1.1 (with rpmrb script)
- update build and install python module requires
- rename service to matrix-synapse

* Wed Dec 19 2018 Alexey Shabalin <shaba@altlinux.org> 0.33.9-alt2
- no longer require a specific version of saml2 since v0.27.0-rc1

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 0.33.9-alt1
- new version 0.33.9 (with rpmrb script)

* Sun Nov 18 2018 Vitaly Lipatov <lav@altlinux.ru> 0.33.8-alt1
- new version 0.33.8 (with rpmrb script)

* Wed Sep 26 2018 Vitaly Lipatov <lav@altlinux.ru> 0.33.5.1-alt1
- new version 0.33.5.1 (with rpmrb script)

* Wed Aug 15 2018 Vitaly Lipatov <lav@altlinux.ru> 0.33.1-alt1
- new version 0.33.1 (with rpmrb script)

* Tue Jul 03 2018 Vitaly Lipatov <lav@altlinux.ru> 0.31.2-alt1
- new version 0.31.2 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.29.1-alt1
- new version 0.29.1 (with rpmrb script)

* Wed Feb 07 2018 Vitaly Lipatov <lav@altlinux.ru> 0.26.0-alt1
- new version 0.26.0 (with rpmrb script)

* Sat Oct 07 2017 Vitaly Lipatov <lav@altlinux.ru> 0.23.1-alt1
- new version 0.23.1 (with rpmrb script)

* Mon Jul 17 2017 Vitaly Lipatov <lav@altlinux.ru> 0.22.1-alt1
- new version 0.22.1 (with rpmrb script)

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.21.0-alt1
- initial build for ALT Sisyphus
