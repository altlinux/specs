%define _unpackaged_files_terminate_build 1
%define oname bowler
%def_with check

Name: python3-module-%oname
Version: 0.9.0
Release: alt1

Summary: Safe code refactoring for modern Python
License: MIT
Group: Development/Python3
BuildArch: noarch

Url: https://github.com/facebookincubator/Bowler
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)

%if_with check
BuildRequires: python3-module-attrs
BuildRequires: python3-module-click
BuildRequires: python3-module-fissix
BuildRequires: python3-module-moreorless
%endif

%description
Safe code refactoring for modern Python projects.

%prep
%setup
%patch0 -p1

%build
%python3_build

%install
%python3_install

%check
%__python3 -m bowler.tests -v

%files
%doc LICENSE README.md
%_bindir/%oname
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Wed Dec 29 2021 Ivan Alekseev <qwetwe@altlinux.org> 0.9.0-alt1
- 0.9.0

