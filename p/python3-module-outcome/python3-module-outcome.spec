%define  modulename outcome

Name:    python3-module-%modulename
Version: 1.0.0
Release: alt1

Summary: Capture the outcome of Python function calls
License: MIT or Apache-2.0
Group:   Development/Python
URL:     https://github.com/python-trio/outcome

Packager: Evgeny Sinelnikov <sin@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Capture the outcome of Python function calls. Extracted from the Trio project.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md *.rst


%changelog
* Tue Jan 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
