%global pypi_name livereload
%def_with python3

Name:           python-module-%pypi_name
Version:        2.5.1
Release:        alt2.1
Summary:        Utility for starting a server in a directory
License:        BSD
URL:            https://github.com/lepture/python-livereload
Group:          Development/Python
Source0:        %name-%version.tar
BuildArch:      noarch

BuildRequires:  python-module-setuptools python-module-setuptools
BuildRequires:  python-devel
BuildRequires:  python-module-six
BuildRequires:  python-module-tornado
BuildRequires:  python-module-certifi
BuildRequires:  python-module-backports_abc
BuildRequires:  python-module-backports.ssl_match_hostname
BuildRequires:  python-module-django
BuildRequires:  python-module-pytest
BuildRequires:  python3-module-pytest

Requires:       python-module-backports.ssl_match_hostname
Requires:       python-module-tornado
Requires:       python-module-six

%description
LiveReload provides a command line utility, livereload, for starting
a server in a directory. By default, it will listen to port 35729,
the common port for LiveReload browser extensions. LiveReload is designed
for web developers who know Python. 

%if_with python3
%package -n python3-module-%pypi_name

Summary:        Command line utility for starting a server in a directory
Group:          Development/Documentation

BuildRequires:  python3-module-setuptools python3-module-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-module-six
BuildRequires:  python3-module-tornado
BuildRequires:  python3-module-certifi
BuildRequires:  python3-module-backports_abc
BuildRequires:  python3-module-django

Requires:       python3-module-tornado
Requires:       python3-module-six

%description -n python3-module-%pypi_name
Python3 LiveReload provides a command line utility, livereload, for
starting a server in a directory. By default, it will listen to port
35729, the common port for LiveReload browser extensions. LiveReload
is designed for web developers who know Python.
%endif

%package docs

Summary:        Documentation for %name
Group:          Development/Python

%description docs
LiveReload documentation and examples.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
py.test
%if_with python3
pushd ../python3
py.test3
popd
%endif

%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst CHANGES.rst LICENSE
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version-py?.?.egg-info
%endif

%files -n python-module-%pypi_name
%doc README.rst CHANGES.rst LICENSE
%python_sitelibdir/%pypi_name
%python_sitelibdir/%pypi_name-%version-py?.?.egg-info

%files docs
%doc docs example LICENSE

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.5.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.1-alt2
- Fixed build.

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 2.5.1-alt1
- Initial build for ALT (based on 2.5.1-2.fc26.src)

