%global modname rich

Summary: Render rich text and beautiful formatting in the terminal
Name: python3-module-%modname
Version: 6.0.0
Release: alt1
Url: https://github.com/willmcgugan/rich
# Download from https://pypi.org/project/rich
Source: %modname-%version.tar.gz
License: MIT
Group: Development/Python3

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
Rich is a Python library for rich text and beautiful formatting in the terminal.
The Rich API makes it easy to add color and style to terminal output. Rich can
also render pretty tables, progress bars, markdown, syntax highlighted source
code, tracebacks, and more - out of the box.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Sun Sep 06 2020 Alexey Shabalin <shaba@altlinux.org> 6.0.0-alt1
- Initial build.
