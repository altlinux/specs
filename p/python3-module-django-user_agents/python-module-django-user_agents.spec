%global pypi_name user_agents

Name:           python3-module-django-%pypi_name
Version:        0.4.0
Release:        alt1

Summary:        A django package that allows easy identification of visitors information
License:        MIT
Group:          Development/Python3
URL:            https://pypi.org/project/django-user-agents
BuildArch:      noarch

# Source0-url: %__pypi_url django-user_agents
Source0:        %name-%version.tar
Patch0:         django-user_agents-tests-django4-urls.patch
Patch1:         django-user_agents-tests-templates.patch

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3(setuptools)
BuildRequires:  python3(wheel)

%if_disabled check
%else
BuildRequires:  python3(django)
BuildRequires:  python3-module-django-dbbackend-sqlite3
BuildRequires:  python3(user_agents)
%endif


%description
A django package that allows easy identification of visitor's browser,
OS and device information, including whether the visitor uses a mobile phone,
tablet or a touch capable device. Under the hood, it uses user-agents.

%package tests
Summary: Tests for %name
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
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
export DJANGO_SETTINGS_MODULE=django_user_agents.tests.settings
%__python3 -m django test django_user_agents.tests -v 2

%files
%doc README.rst LICENSE.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/django_%pypi_name/tests

%files tests
%python3_sitelibdir/django_%pypi_name/tests


%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- new version 0.4.0
- drop fix-import.patch (use system user_agents module)
- switch to pyproject build
- enable tests (fix test urls for Django 4+, add missing test templates)

* Sun Jul 18 2021 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt3
- drop unneeded BR: python3-module-django-formtools

* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.0-alt2
- build for python2 disabled

* Fri May 26 2017 Lenar Shakirov <snejok@altlinux.ru> 0.3.0-alt1
- Initial build for ALT


