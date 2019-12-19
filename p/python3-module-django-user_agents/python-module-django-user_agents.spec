%global pypi_name user_agents

Name:           python3-module-django-%pypi_name
Version:        0.3.0
Release:        alt2

Summary:        A django package that allows easy identification of visitors information
License:        MIT
Group:          Development/Python3
URL:            https://pypi.python.org/pypi/django-user_agents
BuildArch:      noarch

Source0:        %name-%version.tar
Patch0:         fix-import.patch

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-module-django python3-module-django-formtools


%description
A django package that allows easy identification of visitor's browser,
OS and device information, including whether the visitor uses a mobile phone,
tablet or a touch capable device. Under the hood, it uses user-agents.

%package tests
Summary: Tests for Theano
Group: Development/Python3
Requires: %name = %EVR

%description tests
A django package that allows easy identification of visitor's browser,
OS and device information, including whether the visitor uses a mobile phone,
tablet or a touch capable device. Under the hood, it uses user-agents.

This package contains tests for %name.

%prep
%setup
%patch0 -p1

sed -i 's|core.urlresolvers|urls|' $(find ./ -name 'tests.py')

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/django_%pypi_name/tests

%files tests
%python3_sitelibdir/django_%pypi_name/tests


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.0-alt2
- build for python2 disabled

* Fri May 26 2017 Lenar Shakirov <snejok@altlinux.ru> 0.3.0-alt1
- Initial build for ALT


