Name: python3-module-paho
Version: 2.1.0
Release: alt1

Summary: MQTT Python client library
License: EPL-1.0
Group: Development/Python
Url: https://pypi.org/project/paho-mqtt
VCS: https://github.com/eclipse/paho.mqtt.python

Provides: python3-module-paho-mqtt = %EVR

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_tox tox.ini testenv

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/paho
%python3_sitelibdir/paho_mqtt-%version.dist-info

%changelog
* Wed Oct 22 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.0-alt1
- 2.1.0 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.1-alt1
- 1.6.1 released

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt1
- 1.5.1 released

* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- initial
