%define        _unpackaged_files_terminate_build 1
%define        pypiname google_auth_oauthlib
%define        modname google_auth_oauthlib
%define        distname google_auth_oauthlib
%def_enable    check


Name:          python3-module-%pypiname
Version:       1.0.0
Release:       alt1
Summary:       Google Authentication Library
License:       Apache-2.0
Group:         Development/Python3
Url:           https://github.com/googleapis/google-auth-library-python-oauthlib
Vcs:           https://github.com/googleapis/google-auth-library-python-oauthlib.git
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(wheel)
%if_enabled check
BuildRequires: python3(pytest)
BuildRequires: python3(mock)
BuildRequires: python3(requests)
BuildRequires: python3(click)
BuildRequires: python3-module-google-api-core
BuildRequires: python3(requests_oauthlib)
%endif

%description
This library provides oauthlib integration with google-auth.


%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md docs/*rst
%_bindir/google-oauthlib-tool
%python3_sitelibdir/%{distname}
%python3_sitelibdir/%{modname}-%{version}.dist-info


%changelog
* Fri Mar 01 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Initial build v1.0.0 for Sisyphus.
