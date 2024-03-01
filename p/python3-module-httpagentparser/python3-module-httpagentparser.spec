%define        _unpackaged_files_terminate_build 1
%define        pypiname httpagentparser
%define        modname httpagentparser
%define        distname httpagentparser

Name:          python3-module-%pypiname
Version:       1.9.5
Release:       alt1
Summary:       Python HTTP Agent Parser
License:       MIT
Group:         Development/Python3
Url:           https://github.com/shon/httpagentparser
Vcs:           https://github.com/shon/httpagentparser.git
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(wheel)


%description
Python HTTP Agent Parser.

Features:
* Fast
* Detects OS and Browser. Does not aim to be a full featured agent parser
* Will not turn into django-httpagentparser ;)


%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/%{distname}
%python3_sitelibdir/%{modname}*/METADATA

%changelog
* Fri Mar 01 2024 Pavel Skrylev <majioa@altlinux.org> 1.9.5-alt1
- Initial build v1.9.5 for Sisyphus.
