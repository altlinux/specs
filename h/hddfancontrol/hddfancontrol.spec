%def_with pandoc
%define oname hddfancontrol

Name: hddfancontrol
Version: 1.5.1
Release: alt2

Summary: Control system fan speed by monitoring hard drive temperature

License: LGPLv3
Group: Monitoring
Url: https://github.com/desbma/hddfancontrol

# The PyPI archives don't have unit tests in them anymore.
Source: https://github.com/desbma/hddfancontrol/archive/%version/%oname-%version.tar

BuildArch: noarch

BuildRequires: python3-module-setuptools
BuildRequires: python3-devel
BuildRequires: python3-module-daemon, python3-module-docutils
BuildRequires: hddtemp, hdparm
BuildRequires: udev-rules
%if_with pandoc
BuildRequires: python3-module-pypandoc
%endif

Requires: python3-module-daemon
Requires: python3-module-docutils
Requires: python3-module-setuptools

Requires: hddtemp, hdparm

%description
HDD Fan control is a command line tool to dynamically control fan speed
according to hard drive temperature on Linux.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info

%build
%python3_build

%install
%python3_install

# Remove the "tests" directory that gets installed systemwide.
rm -rf %buildroot%python3_sitelibdir/tests

# Install the systemd script and config file.
mkdir -p %buildroot%_unitdir/
mkdir -p %buildroot%_sysconfdir/

sed 's,conf.d/hddfancontrol,hddfancontrol.conf,' -i systemd/hddfancontrol.service
cp -a systemd/hddfancontrol.service %buildroot%_unitdir/
cp -a systemd/hddfancontrol.conf %buildroot%_sysconfdir/

# Run the tests.
#check
#__python3 setup.py test

%files
%doc LICENSE
%doc README.md
%_bindir/hddfancontrol
%_unitdir/hddfancontrol.service
%config(noreplace) %_sysconfdir/hddfancontrol.conf
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Mon Dec 11 2023 Michael Shigorin <mike@altlinux.org> 1.5.1-alt2
- rename doc knob to pandoc one

* Fri Jun 30 2023 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version 1.5.1 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Tue Jun 22 2021 Michael Shigorin <mike@altlinux.org> 1.4.3-alt2
- introduce doc knob (on by default): no pandoc on e2k so far

* Thu Apr 15 2021 Vitaly Lipatov <lav@altlinux.ru> 1.4.3-alt1
- new version 1.4.3 (with rpmrb script)

* Thu Apr 15 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- initial build for ALT Sisyphus

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.9

* Wed Mar 04 2020 Ben Rosser <rosser.bjr@gmail.com> - 1.3.1-1
- Update to latest upstream release.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.3.0-1
- Update to latest upstream release (#1754224).

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.10-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.2.10-1
- Update to latest upstream release, 1.2.10 (rhbz#1669729).

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.8-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.8-1
- Rebuilt for new upstream version 1.2.8, fixes rhbz #1541821

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 26 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.2.7-1
- Updated to 1.2.7, fixing a bug in hdparm error handling.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.2.6-1
- Updated to latest upstream release.
- Added systemd service file and configuration file.

* Fri Jan 13 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.2.5-1
- Updated to latest upstream release.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-2
- Rebuild for Python 3.6

* Wed Aug 24 2016 Ben Rosser <rosser.bjr@gmail.com> - 1.2.4-1
- Initial package.
