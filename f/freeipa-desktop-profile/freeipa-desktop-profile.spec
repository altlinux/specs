%define _unpackaged_files_terminate_build 1

%define plugin_name desktop-profile

Name: freeipa-%plugin_name
Version: 0.0.8
Release: alt2

Summary: FleetCommander integration with FreeIPA
License: GPLv3
Group: System/Base

ExcludeArch: %ix86
Url: https://github.com/abbra/freeipa-desktop-profile
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

Requires: python3-module-freeipa-%plugin_name-server
Requires: python3-module-freeipa-%plugin_name-client
Requires: freeipa-server-common >= 4.4.1

%description
A module for FreeIPA to allow managing desktop profiles defined by the
FleetCommander.

%package common
Group: System/Base
Summary: Common package for client side FleetCommander integration with FreeIPA

%description common
A module for FreeIPA to allow managing desktop profiles defined by the
FleetCommander. This package adds common files needed by client-side packages.

%package -n python3-module-freeipa-%plugin_name-server
Summary: Server side of FleetCommander integration with FreeIPA for Python3
Group: System/Base

%description -n python3-module-freeipa-%plugin_name-server
A module for FreeIPA to allow managing desktop profiles defined by the
FleetCommander. This package adds server-side support for Python3 version of
FreeIPA.

%package -n python3-module-freeipa-%plugin_name-client
Summary: Client side of FleetCommander integration with FreeIPA for Python3
Group: System/Base
Requires: freeipa-%plugin_name-common

%description -n python3-module-freeipa-%plugin_name-client
A module for FreeIPA to allow managing desktop profiles defined by the
FleetCommander. This package adds client-side support for Python3 version of
FreeIPA.

%prep
%setup

%build

%install

mkdir -p %buildroot%_sysconfdir/ipa
cp -v plugin%_sysconfdir/ipa/fleetcommander.conf %buildroot%_sysconfdir/ipa/

mkdir -p %buildroot%_datadir/ipa/schema.d
install -p plugin/schema.d/75-deskprofile.ldif \
%buildroot/%_datadir/ipa/schema.d/

mkdir -p %buildroot%python3_sitelibdir/ipaserver/plugins
install -p plugin/ipaserver/plugins/deskprofile.py \
%buildroot%python3_sitelibdir/ipaserver/plugins/

mkdir -p %buildroot%python3_sitelibdir/ipaclient/plugins
install -p plugin/ipaclient/plugins/deskprofile.py \
%buildroot%python3_sitelibdir/ipaclient/plugins/

mkdir -p %buildroot%_datadir/ipa/updates
install -p plugin/updates/75-deskprofile.update \
%buildroot%_datadir/ipa/updates/

# Do not package web UI plugin yet
#mkdir -p %%buildroot%%_datadir/ipa/ui/js/plugins/deskprofile
# find plugin/ui/ -name '*.js' \
# -exec cp -v {} %%buildroot%%_datadir/ipa/js/plugins/ \;

%post
# launch the upgrade by freeipa-server.filetrigger
[ -d /run/ipa ] && touch /run/ipa/rpmfiletrigger_newplugin

%files
%doc COPYING plugin/Feature.mediawiki
%_datadir/ipa/schema.d/75-deskprofile.ldif
%_datadir/ipa/updates/75-deskprofile.update

%files common
%_sysconfdir/ipa/fleetcommander.conf

%files -n python3-module-freeipa-%plugin_name-client
%python3_sitelibdir/ipaclient/plugins/deskprofile.py
%python3_sitelibdir/ipaclient/plugins/__pycache__/deskprofile.*.py*

%files -n python3-module-freeipa-%plugin_name-server
%python3_sitelibdir/ipaserver/plugins/deskprofile.py
%python3_sitelibdir/ipaserver/plugins/__pycache__/deskprofile.*.py*

%changelog
* Sun Dec 30 2018 Stanislav Levin <slev@altlinux.org> 0.0.8-alt2
- Dropped build for x86 arch.

* Mon Oct 22 2018 Stanislav Levin <slev@altlinux.org> 0.0.8-alt1
- Initial build.

