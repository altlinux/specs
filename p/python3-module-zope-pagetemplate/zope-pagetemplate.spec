%define _unpackaged_files_terminate_build 1
%define pypi_name zope-pagetemplate
%define ns_name zope
%define mod_name pagetemplate

%def_with check

Name: python3-module-%pypi_name
Version: 6.1
Release: alt1.1
Summary: Zope Page Templates
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope-pagetemplate
Vcs: https://github.com/zopefoundation/zope.pagetemplate
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
# switched to native namespace
Requires: python3-module-zope >= 3.3.0-alt10
# setuptools(pkg_resources) is used by namespace root which is not used in ALT

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-zope-component
BuildRequires: python3-module-zope-i18n
BuildRequires: python3-module-zope-i18nmessageid
BuildRequires: python3-module-zope-interface
BuildRequires: python3-module-zope-proxy
BuildRequires: python3-module-zope-security
BuildRequires: python3-module-zope-tal
BuildRequires: python3-module-zope-tales
BuildRequires: python3-module-zope-testing
BuildRequires: python3-module-zope-testrunner
BuildRequires: python3-module-zope-traversing
BuildRequires: python3-module-zope-untrustedpython
%endif

%description
Page Templates provide an elegant templating mechanism that achieves a clean
separation of presentation and application logic while allowing for designers to
work with templates in their visual editing tools (FrontPage, Dreamweaver,
GoLive, etc.).

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc README.*
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 6.1-alt1.1
- Demodernized packaging.

* Mon Dec 08 2025 Stanislav Levin <slev@altlinux.org> 6.1-alt1
- 5.2 -> 6.1.

* Mon Sep 08 2025 Stanislav Levin <slev@altlinux.org> 5.2-alt1
- Initial build for Sisyphus.
