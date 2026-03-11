Name: hddfancontrol
Version: 2.1.0
Release: alt1

Summary: Control system fan speed by monitoring hard drive temperature

License: GPL-3.0-only
Group: Monitoring
Url: https://github.com/desbma/hddfancontrol

# Source-url: https://github.com/desbma/hddfancontrol.git
Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc

%description
HDD Fan control is a command line tool to dynamically control fan speed
according to hard drive temperature on Linux.

%prep
%setup -n %name-%version
tar -xf %{SOURCE1}

mkdir -p .cargo
cat >> .cargo/config <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_sysconfdir/sysconfig
cp -a systemd/hddfancontrol.service %buildroot%_unitdir/
cp -a systemd/hddfancontrol.conf %buildroot%_sysconfdir/sysconfig/hddfancontrol
sed -i 's|/etc/conf.d/|/etc/sysconfig/|' %buildroot%_unitdir/hddfancontrol.service

%files
%doc LICENSE README.md
%_bindir/hddfancontrol
%_unitdir/hddfancontrol.service
%config(noreplace) %_sysconfdir/sysconfig/hddfancontrol

%changelog
* Wed Mar 11 2026 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version (2.1.0) via gear-uupdate
- rewrite spec for Rust build system (upstream switched from Python to Rust)
- move config from /etc/conf.d to /etc/sysconfig

* Mon Dec 09 2024 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- new version 1.6.2 (with rpmrb script)

* Mon Dec 25 2023 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- new version 1.6.0 (with rpmrb script)

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
