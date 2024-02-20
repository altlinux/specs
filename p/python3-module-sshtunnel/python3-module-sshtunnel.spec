%define        _unpackaged_files_terminate_build 1
%define        pypiname sshtunnel
%define        modname sshtunnel
%define        distname sshtunnel
%def_disable   check


Name:          python3-module-%pypiname
Version:       0.4.0
Release:       alt1
Summary:       SSH tunnels to remote server
License:       MIT
Group:         Development/Python3
Url:           https://github.com/pahaz/sshtunnel
Vcs:           https://github.com/pahaz/sshtunnel.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel)
%if_enabled check
BuildRequires: python3(mock)
BuildRequires: python3(pytest)
BuildRequires: python3(paramiko)
%endif

%description
SSH tunnels to remote server.


%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest
%pyproject_run_unittest


%files
%doc *.rst docs/*rst
%_bindir/%distname
%python3_sitelibdir/%{distname}*.py
%python3_sitelibdir/%{modname}*dist-info
%python3_sitelibdir/__pycache__/%{distname}*


%changelog
* Mon Aug 14 2023 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.
