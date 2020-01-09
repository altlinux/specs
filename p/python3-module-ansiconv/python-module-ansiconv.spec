%define oname ansiconv

Name: python3-module-%oname
Version: 1.0.0
Release: alt2

Summary: A Python module for converting ANSI coded text and converts it to either plain text or HTML
License: MIT
Group: Text tools
Url: https://bitbucket.org/dhrrgn/ansiconv
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
A Python module for converting ANSI coded text and converts it to either plain text or HTML.

Documentation: http://pythonhosted.org/ansiconv/

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/ansiconv*
%python3_sitelibdir/__pycache__/
%doc README.md


%changelog
* Thu Jan 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt2
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 21 2015 Terechkov Evgenii <evg@altlinux.org> 1.0.0-alt1
- v1.0.0-3-g8a7d68e
