%define _unpackaged_files_terminate_build 1

%define oname pltable

Name: python3-module-%oname
Version: 1.0.2
Release: alt1
Summary: Easily displaying tabular data in a visually appealing ASCII table format

Group: Development/Python3
License: BSD
Source: %name-%version.tar
# vcs-git: https://github.com/platomav/PLTable.git
Url: https://github.com/platomav/PLTable

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
Provides: python3-module-PLTable = %EVR
Obsoletes: python3-module-PLTable < %EVR

%py3_provides %oname

%description
PLTable is a Python library designed to make it quick and easy
to represent tabular data in visually appealing ASCII tables.
PLTable is a fork of PTable which was in turn originally forked from PrettyTable.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.md LICENSE
%python3_sitelibdir/*

%changelog
* Wed Apr 07 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.2-alt1
- 1.0.2
- rename from PLTable to pltable
- do not provides and obsoletes prettytable

* Wed Mar 25 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.1-alt1
- Initial build
