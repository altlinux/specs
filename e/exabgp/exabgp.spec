%define _unpackaged_files_terminate_build 1

%def_with check

%define exabgp_user _exabgp 
%define exabgp_group _exabgp

Name: exabgp
Version: 5.0.9
Release: alt2

Summary: The BGP swiss army knife of networking
License: BSD
Group: Security/Networking
Url: https://github.com/Exa-Networks/exabgp

BuildArch: noarch

Patch: 0001-exabgp-5.0.9-python3-thread.patch

Source0: %name-%version.tar
Source1: %name.service
Source2: %name@.service

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
%if_with check
BuildRequires: /proc
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-psutil
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-benchmark
%endif

Requires: python3-module-%name

# Optional VyOS CLI/YANG parser code is not used by normal ExaBGP runtime,
# but Python autodeps treats its imports as mandatory. Skip bogus requires.
%add_python3_req_skip vyos vyos.cli vyos.cli.completer vyos.cli.validator
%add_python3_req_skip vyos.ifconfig.section vyos.modules vyos.util vyos.xml
%add_python3_req_skip yanglexer exabgp.conf.yang.tree

%description
ExaBGP allows engineers to control their network from commodity
servers. Think of it as Software Defined Networking using BGP.

It can be used to announce ipv4, ipv6, vpn or flow routes (for DDOS
protection) from its configuration file(s). ExaBGP can also transform
BGP messages into friendly plain text or JSON which can be easily
manipulate by scripts and report peer announcements.

%package -n python3-module-%name
Summary: %name python library
Group: Development/Python3

%description -n python3-module-%name
%name python library

%prep
%setup
%autopatch -p2

%build
%pyproject_build

%install
%pyproject_install

install -pDm 644 doc/man/%name.1 %buildroot%_man1dir/%name.1
install -pDm 644 doc/man/%name.conf.5 %buildroot%_man5dir/%name.conf.5

install -dm 0750 %buildroot%_sysconfdir/%name 
install -Dp -m0644 %SOURCE1 %buildroot%_unitdir/%name.service
install -Dp -m0644 %SOURCE2 %buildroot%_unitdir/%name@.service

# Delete examples
rm -rf %buildroot%_usr/etc/%name

%check
%pyproject_run_pytest --ignore=tests/fuzz

%pre
# Add the "_exabgp" user and group
getent group %exabgp_group >/dev/null || groupadd -r %exabgp_group
getent passwd %exabgp_user >/dev/null || \
    useradd -r -g %exabgp_group -d /dev/null -s /sbin/nologin \
    --no-create-home -c "ExaBGP service user"  %exabgp_user
exit 0

%post
%systemd_post %name.service

%preun
%systemd_preun %name.service

%postun
%systemd_postun %name.service

%files
%doc doc/CHANGELOG.rst CODING_STYLE.md CONTRIBUTING.md LICENCE.txt README.*
%_bindir/*
%dir %attr(0750,root,%exabgp_group) %_sysconfdir/%name
%_man1dir/*.1*
%_man5dir/*.5*
%_unitdir/%name.service
%_unitdir/%name@.service

%files -n python3-module-%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}/

%changelog
* Wed Jun 24 2026 Nikita Shmatko <nash@altlinux.org> 5.0.9-alt2
- Excluded fuzz tests from check.

* Wed Jun 03 2026 Nikita Shmatko <nash@altlinux.org> 5.0.9-alt1
- Version updated to 5.0.9.
- Specfile cleanup.
- Fixed legacy thread import.
- Turned on tests.

* Wed Mar 04 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.2.6-alt1
- Version updated to 4.2.6 (with python3 support).

* Sat Oct 29 2016 Terechkov Evgenii <evg@altlinux.org> 3.4.17-alt2
- Split exabgp library to separate subpackage

* Sat Oct 29 2016 Terechkov Evgenii <evg@altlinux.org> 3.4.17-alt1
- 3.4.17

* Sun Jul 31 2016 Terechkov Evgenii <evg@altlinux.org> 3.4.16-alt1
- Initial build for ALT Linux Sisyphus
