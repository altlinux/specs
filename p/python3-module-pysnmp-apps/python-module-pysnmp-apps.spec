%define sname pysnmp-apps

Name: python3-module-pysnmp-apps
Version: 0.3.4
Release: alt2

Summary: PySNMP-based command-line tools
License: BSD
Group: Networking/Other
Url: http://sourceforge.net/projects/pysnmp/
BuildArch: noarch

Source: %sname-%version.tar.gz

BuildRequires(pre): rpm-build-python3


%description
PySNMP-based command-line tools, can be used for quick testing and network management purposes

%prep
%setup -n %sname-%version

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%doc README CHANGES PKG-INFO LICENSE
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.4-alt2
- python2 disabled

* Fri Nov  1 2013 Terechkov Evgenii <evg@altlinux.org> 0.3.4-alt1
- Initial build for ALT Linux Sisyphus
