%define oname Automat

Name: python3-module-automat
Version: 20.2.0
Release: alt2

Summary: Self-service finite-state machines for the programmer on the go

Url: https://github.com/glyph/Automat
License: MIT
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools python3-module-docutils
BuildRequires: python3-module-mistune python3-module-m2r python3-module-setuptools_scm

%description
Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune
rm -rf %buildroot%python3_sitelibdir/automat/_test/
rm -f %buildroot%python3_sitelibdir/automat/_visualize.*

%files
# TODO: tools
#_bindir/automat-visualize
%python3_sitelibdir/*

%changelog
* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 20.2.0-alt2
- build python3 package separately

* Thu Mar 26 2020 Mikhail Gordeev <obirvalger@altlinux.org> 20.2.0-alt1
- new version (20.2.0) with rpmgs script

* Sun Jun 30 2019 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1.qa1
- NMU: applied repocop patch

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- initial build for ALT Sisyphus

