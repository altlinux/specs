Name: yandex-tank
Version: 1.9.10
Release: alt1

Summary: a performance measurement tool
License: LGPL-2.1
Group: Networking/Other

URL: https://github.com/yandex/yandex-tank
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: python-module-setuptools python-module-flake8 python-module-pytest-runner
Provides: python%__python_version(yandextank)

Requires: python-module-matplotlib python-module-subprocess32
Requires: python-module-pandas >= 0.20.2
Requires: python-module-future >= 0.16.0
Requires: python-module-yaml >= 3.12
Requires: python-module-influxdb >= 5.0.0
Requires: python-module-dateutil >= 2.6.0

%description
Yandex.Tank is a performance measurement and load testing automatization tool.
It uses other load generators such as JMeter, ab or phantom inside of it for
load generation and provides a common configuration system for them and
analytic tools for the results they produce.

Recommends: phantom/phantom-ssl

%prep
%setup
%patch -p1

%build
%python_build

%install
%python_install

%files
%_bindir/%{name}*
%_bindir/tank-postloader
%_bindir/tank-docs-gen
%python_sitelibdir_noarch/yandextank-%{version}*
%python_sitelibdir_noarch/yandextank
%doc README.md AUTHORS docs

%changelog
* Sat Mar 17 2018 Terechkov Evgenii <evg@altlinux.org> 1.9.10-alt1
- 1.9.10

* Sun Oct 22 2017 Terechkov Evgenii <evg@altlinux.org> 1.9.3-alt1
- 1.9.3

* Tue Oct 10 2017 Terechkov Evgenii <evg@altlinux.org> 1.9.2-alt1
- 1.9.2

* Sun Jul  2 2017 Terechkov Evgenii <evg@altlinux.org> 1.8.35-alt3
- Add requires to pull in runtime dependecies

* Sun Jul  2 2017 Terechkov Evgenii <evg@altlinux.org> 1.8.35-alt2
- Add patch to use external urllib3

* Tue Jun 20 2017 Terechkov Evgenii <evg@altlinux.org> 1.8.35-alt1
- Initialbuild for ALT Linux Sisyphus
- v1.8.35-4-g3b2b5c6
