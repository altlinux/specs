Name: hass
Version: 0.104.3
Release: alt1

Summary: Home automation platform
License: APL
Group: System/Servers
Url: https://www.home-assistant.io/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%package core
Summary: Home automation platform
Group: System/Servers
Requires: python3-module-hass-frontend >= 20200108.2

%package -n python3-module-hass
Summary: Home automation platform
Group: System/Servers
AutoReq: no

%define desc Home Assistant is a home automation platform running on Python 3.\
It is able to track and control all devices at home and offer a platform \
for automating control.

%description
%desc

%description core
%desc
This package contains core modules only.

%description -n python3-module-hass
%desc
This package contains most of Home Assistant modules.

%prep
%setup

%build
%python3_build

%install
%python3_install
install -pm0644 -D hass.service %buildroot%_unitdir/hass.service
install -pm0644 -D hass.sysconfig %buildroot%_sysconfdir/sysconfig/hass
mkdir -p %buildroot%_localstatedir/hass

find %buildroot%python3_sitelibdir/homeassistant/components -type f -name manifest.json |\
	fgrep -vf precious |sed -re 's,^%buildroot(/.+)/manifest.json,%exclude \1,' > core.files
sed -re 's,%exclude ,,' < core.files > rest.files

%pre core
%_sbindir/groupadd -r -f _hass &> /dev/null
%_sbindir/useradd -r -g _hass -d %_localstatedir/hass -s /dev/null \
	-c 'Home Assistant' -n _hass &> /dev/null ||:

%set_python3_req_method strict
# optional
%add_python3_req_skip av
%add_python3_req_skip colorlog colorlog.escape_codes
%add_python3_req_skip custom_components
%add_python3_req_skip hbmqtt.broker

%files core -f core.files
%_sysconfdir/sysconfig/hass
%_unitdir/hass.service
%_bindir/hass

%python3_sitelibdir/homeassistant
%python3_sitelibdir/homeassistant-%version-*-info

%dir %attr(0770,root,_hass) %_localstatedir/hass

%files -n python3-module-hass -f rest.files

%changelog
* Wed Jan 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.104.3-alt1
- 0.104.3 released

* Mon Jan 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.104.2-alt1
- 0.104.2 released

* Fri Jan 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.104.1-alt1
- 0.104.1 released

* Thu Jan 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.104.0-alt1
- 0.104.0 released

* Sat Jan 11 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.103.6-alt1
- 0.103.6 released

* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.102.2-alt1
- initial
