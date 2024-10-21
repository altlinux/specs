%define	 modulename axolotl

Name:	 python3-module-axolotl
Version: 0.2.3
Release: alt2

Summary: python port of libsignal-protocol-java

License: GPL-3.0-only
Group:	 Development/Python3
Url:	 https://github.com/tgalal/python-axolotl

Source:	 python-%modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev

BuildArch: noarch

%description
This is a Python port of libsignal-protocol-java, originally written by Moxie
Marlinspike.

%prep
%setup -n python-%modulename-%version

%build
%python3_build

%install
%python3_install

%check
# upstream uses unmaintained nose

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/python_%modulename-%version-py*.egg-info/
%exclude %python3_sitelibdir/%modulename/tests

%changelog
* Mon Oct 21 2024 Stanislav Levin <slev@altlinux.org> 0.2.3-alt2
- Disabled check (see #50996).

* Sun Oct 18 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.2.3-alt1
- Initial build for ALT Sisyphus.

