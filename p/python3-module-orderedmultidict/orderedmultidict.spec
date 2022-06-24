%define  oname orderedmultidict

%def_with check

Name:    python3-module-%oname
Version: 1.0.1
Release: alt1

Summary: Ordered Multivalue Dictionary. Helps power furl.

License: Unlicense
Group:   Development/Python3
URL:     https://github.com/gruns/orderedmultidict

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-six
BuildRequires: python3-module-flake8
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
A multivalue dictionary is a dictionary that can store multiple values for the
same key. An ordered multivalue dictionary is a multivalue dictionary that
retains the order of insertions and deletions.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%doc *.md

%changelog
* Fri Jun 24 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
