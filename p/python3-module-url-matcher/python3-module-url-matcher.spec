%define pypi_name url_matcher
%define modname url-matcher
# online tests
%def_disable check

Name: python3-module-%modname
Version: 0.6.0
Release: alt1

Summary: URL matching rules library to connect URLs with resources
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.org/project/url-matcher/

Vcs: https://github.com/zytedata/url-matcher.git

# no tests/fixtures/ in pypi tarball
#Source: https://pypi.io/packages/source/u/%pypi_name/%pypi_name-%version.tar.gz
Source: https://github.com/zytedata/%modname/archive/%version/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools) python3(wheel)
%{?_enable_check:BuildRequires: python3(pytest)
BuildRequires: python3(tldextract)}

%description
URL matching library that relates URLs with resources. Rules are
defined using simple pattern definitions. It is simpler and faster
than using regular expressions if the rules involve many domains.

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/
%doc README* LICENSE*

%changelog
* Fri Nov 27 2026 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus


