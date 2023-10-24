%define  oname autopage
%def_with check

Name:    python3-module-%oname
Version: 0.5.2
Release: alt1

Summary: Python library to add automatic paging of CLI output

License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/autopage

# https://github.com/zaneb/autopage
Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-fixtures
BuildRequires: python3-module-pytest
BuildRequires: /dev/pts
%endif

BuildArch: noarch

%description
Autopage is a Python library to automatically display terminal output from
a program in a pager (like less) whenever you need it, and never when you don't.
And it only takes one line of code.

You know how some CLI programs like git (and a handful of others, including man
and systemctl) automatically pipe their output to less? Except not if there's
less than one screen's worth of data. And if you redirect the output to a file
or a pipe, it does the right thing instead. Colours are preserved. Don't you wish
all programs worked like that? Now at least all of your Python programs can.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
# Do not distribute tests with the package
rm -rf %buildroot%python3_sitelibdir/%oname/tests

%check
# This test is broken
rm -fv autopage/tests/test_end_to_end.py
%pyproject_run_pytest -v

%files
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Oct 24 2023 Anton Vyatkin <toni@altlinux.org> 0.5.2-alt1
- New version 0.5.2.

* Fri Sep 15 2023 Anton Vyatkin <toni@altlinux.org> 0.5.1-alt2
- Fix FTBFS.

* Wed Oct 12 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus.
