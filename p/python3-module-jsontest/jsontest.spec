%define oname jsontest

Name: python3-module-%oname
Version: 1.3
Release: alt2

Summary: Automatically generate Python tests from JSON files
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/JsonTest

BuildArch: noarch

# https://github.com/Fizzadar/JsonTest.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
A tiny metaclass for autogenerating tests from JSON files.

%prep
%setup

%build
%python3_build_debug

%install
%python3_build_install

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Mon Apr 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt2
- Build for python2 disabled.

* Tue Mar 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt1
- Initial build for ALT.
