%define _unpackaged_files_terminate_build 1
%define pypi_name requests_hawk

Name:           python3-module-requests-hawk
Version:        1.2.1
Release:        alt1

Summary:        Hawk authentication strategy for the requests python library
Group:          Development/Python3
License:        Apache-2.0
URL:            https://github.com/mozilla-services/requests-hawk

BuildArch:      noarch

Source:         %name-%version.tar
Patch:          fix-assert.patch

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-requests
BuildRequires:  python3-module-mohawk
BuildRequires:  python3-module-pytest

Requires:       python3-module-requests
Requires:       python3-module-mohawk

%description
This project allows you to use the python requests library with the hawk
authentication mechanism. Hawk itself does not provide any mechanism for
obtaining or transmitting the set of shared credentials required, but this
project proposes a scheme we use across mozilla services projects.

%prep
%setup
%patch -p0

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest %pypi_name/tests

%files
%doc README.rst CHANGES.txt LICENSE.txt
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Sep 24 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.2.1-alt1
- Initial build for ALT.

