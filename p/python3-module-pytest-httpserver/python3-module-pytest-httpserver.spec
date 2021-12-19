%define modname pytest_httpserver

Name: python3-module-pytest-httpserver
Version: 1.0.3
Release: alt1

Summary: HTTP server for pytest
Group: Development/Python3
License: MIT
Url: http://pypi.python.org/pypi/%modname
Vcs: https://www.github.com/csernazs/pytest-httpserver.git

Source: http://pypi.io/packages/source/p/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%description
This library is designed to help to test http clients without contacting
the real http server. In other words, it is a fake http server which is
accessible via localhost can be started with the pre-defined expected
http requests and their responses.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc README* LICENSE

%changelog
* Sun Dec 19 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Mon Oct 18 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Fri Aug 06 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Apr 12 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus



