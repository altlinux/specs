Name: esptool
Version: 5.3.1
Release: alt1

Summary: Flasher for Espressif ESP8266 & ESP32 chips
License: GPLv2
Group: Development/Other
URL: https://docs.espressif.com/projects/esptool
VCS: https://github.com/espressif/esptool

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

%description
A Python-based, open source, platform independent, utility to communicate with
the ROM bootloader in Espressif ESP8266 & ESP32 chips.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
for f in %buildroot%_bindir/*.py;
	do mv -vf $f ${f%%.py*}
done

%files
%doc LICENSE README.md
%_bindir/espefuse
%_bindir/espsecure
%_bindir/esptool
%_bindir/esp_rfc2217_server
%python3_sitelibdir/esp_rfc2217_server
%python3_sitelibdir/espefuse
%python3_sitelibdir/espsecure
%python3_sitelibdir/esptool
%python3_sitelibdir/esptool-%version.dist-info

%changelog
* Mon Jul 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 5.3.1-alt1
- 5.3.1 released

* Tue Jun 02 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 5.3.0-alt1
- 5.3.0 released

* Thu Feb 19 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 5.2.0-alt1
- 5.2.0 released

* Tue Sep 16 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 5.1.0-alt1
- 5.1.0 released

* Fri Sep 05 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 5.0.2-alt1
- 5.0.2 released

* Fri Jun 20 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 4.9.0-alt1
- 4.9.0 released

* Thu Sep 26 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 4.8.1-alt1
- 4.8.1 released

* Tue Sep 17 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 4.8.0-alt1
- 4.8.0 released

* Thu Dec 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.7.0-alt1
- 4.7.0 released

* Tue Jun 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.6.2-alt1
- 4.6.2 released

* Fri Jun 02 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.6.1-alt1
- 4.6.1 released

* Tue May 30 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.6-alt1
- 4.6 released

* Wed Mar 01 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.5.1-alt1
- 4.5.1 released

* Mon Feb 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.5-alt1
- 4.5 released

* Wed Nov 23 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4-alt1
- 4.4 released

* Fri Sep 23 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.3-alt1
- 4.3 released

* Tue Aug 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2-alt1
- 4.2 released

* Tue May 31 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1-alt1
- 4.1 released

* Fri May 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0-alt1
- 4.0 released

* Mon Apr 25 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.3-alt1
- 3.3 released

* Wed Oct 27 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.2-alt1
- 3.2 released

* Fri Jul 23 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1-alt1
- 3.1 released

* Mon Dec 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt1
- 3.0 released

* Sat Nov 09 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8-alt1
- initial
