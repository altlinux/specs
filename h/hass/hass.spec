Name: hass
Version: 2023.3.3
Release: alt1

Summary: Home automation platform
License: APL
Group: System/Servers
Url: https://www.home-assistant.io/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildRequires: python3(atomicwrites)
BuildRequires: python3(awesomeversion)
BuildRequires: python3(black)
BuildRequires: python3(ciso8601)
BuildRequires: python3(jinja2)
BuildRequires: python3(orjson)
BuildRequires: python3(slugify)
BuildRequires: python3(tqdm)
BuildRequires: python3(typing_extensions)
BuildRequires: python3(voluptuous)
BuildRequires: python3(voluptuous_serialize)
BuildRequires: python3(yaml)

%package core
Summary: Home automation platform
Group: System/Servers
Requires: python3-module-aiohttp >= 3.8.1
Requires: python3-module-astral >= 2.2
Requires: python3-module-httpcore >= 0.14.5
Requires: python3-module-pip >= 21.0
Requires: python3-module-async-timeout >= 4.0.2
Requires: python3-module-text-unidecode >= 1.3
Requires: python3-module-voluptuous >= 0.13.1
Requires: python3-module-websocket-client >= 0.56.0
Requires: python3-module-yaml >= 6.0
Requires: python3-module-hass-frontend >= 20230110.0

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
> .coveragerc
find homeassistant/components -type f -name manifest.json |\
	fgrep -vf precious |sed -r 's,[^/]+$,,' |xargs rm -rv
python3 -m script.hassfest
tar x --wildcards --strip-components=1 --file %SOURCE0 '*/homeassistant/components'
python3 -m script.translations develop --all

%build
%pyproject_build

%install
%pyproject_install
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
%add_python3_req_skip custom_components
# optional
%add_python3_req_skip av
%add_python3_req_skip colorlog colorlog.escape_codes
# stdlib
%add_python3_req_skip deque

%files core -f core.files
%_sysconfdir/sysconfig/hass
%_unitdir/hass.service
%_bindir/hass

%python3_sitelibdir/homeassistant
%python3_sitelibdir/homeassistant-%version.dist-info

%dir %attr(0770,root,_hass) %_localstatedir/hass

%files -n python3-module-hass -f rest.files

%changelog
* Fri Mar 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.3.3-alt1
- 2023.3.3 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.1.7-alt1
- 2023.1.7 released

* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2022.11.2-alt1.1
- NMU: used %%add_python3_req_skip because Sisyphus does not provide debugpy.

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.11.2-alt1
- 2022.11.2 released

* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.9.4-alt1
- 2022.9.4 released

* Wed Jul 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.7.5-alt1
- 2022.7.5 released

* Thu Jul 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.7.0-alt1
- 2022.7.0 released

* Thu May 19 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.5.5-alt1
- 2022.5.5 released

* Tue Mar 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.3.7-alt1
- 2022.3.7

* Thu Feb 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.2.5-alt1
- 2022.2.5 released

* Tue Oct 12 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.10.4-alt1
- 2021.10.4 released

* Thu Oct 07 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.10.0-alt1
- 2021.10.0 released

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.8.2-alt1
- 2021.8.2 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.6.6-alt1
- 2021.6.6 released

* Wed Apr 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.4.6-alt1
- 2021.4.6 released

* Tue Apr 13 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.4.4-alt1
- 2021.4.4 released

* Fri Apr 09 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.4.1-alt1
- 2021.4.1 released

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.3.4-alt1
- 2021.3.4 released

* Thu Feb 25 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.2.3-alt3
- get rid of deprecated zwave dependency

* Thu Feb 25 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.2.3-alt2
- interdependencies corrected

* Fri Feb 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.2.3-alt1
- 2021.2.3 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.1.5-alt1
- 2021.1.5-alt1 released

* Mon Nov 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.118.2-alt1
- 0.118.2 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.117.2-alt1
- 0.117.2 released

* Fri Oct 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.116.4-alt1
- 0.116.4 released

* Wed Sep 30 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.115.6-alt1
- 0.115.6 released

* Mon Sep 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.115.2-alt1
- 0.115.2 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.114.2-alt1
- 0.114.2 released

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.112.5-alt1
- 0.112.5 released

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.112.1-alt1
- 0.112.1-alt1 released

* Mon May 04 2020 Stanislav Levin <slev@altlinux.org> 0.106.5-alt2
- Dropped runtime dependency on importlib_metadata.

* Wed Mar 04 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.106.5-alt1
- 0.106.5 released

* Wed Feb 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.105.3-alt1
- 0.105.3 released

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
