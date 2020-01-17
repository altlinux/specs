%define oname prctl

Name: python3-module-%oname
Version: 1.7
Release: alt2

Group: Development/Python3
License: GPL
Summary: Interface to the linux prctl syscall
Url: https://pypi.python.org/pypi/python-prctl

Source: python-prctl-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: ctags libcap-devel
BuildRequires: python3-module-sphinx


%description
Control process attributes through prctl

The linux prctl function allows you to control specific characteristics
of a process' behaviour. Usage of the function is fairly messy though,
due to limitations in C and linux. This module provides a nice non-messy
python(ic) interface.

Besides prctl, this library also wraps libcap for complete capability
handling and allows you to set the process name as seen in ps and top.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
Control process attributes through prctl

The linux prctl function allows you to control specific characteristics
of a process' behaviour. Usage of the function is fairly messy though,
due to limitations in C and linux. This module provides a nice non-messy
python(ic) interface.

Besides prctl, this library also wraps libcap for complete capability
handling and allows you to set the process name as seen in ps and top.

This package contains documentation for %oname.

%prep
%setup -n python-prctl-%version

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build
make -C docs html

%install
%python3_install

%files
%doc README
%python3_sitelibdir/*

%files docs
%doc docs/_build/html/*


%changelog
* Fri Jan 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.7-alt2
- Porting on Python3.

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 1.7-alt1
- Autobuild version bump to 1.7

* Wed Feb 11 2015 Fr. Br. George <george@altlinux.ru> 1.6.1-alt1
- Autobuild version bump to 1.6.1

* Thu Sep 25 2014 Fr. Br. George <george@altlinux.ru> 1.5.0-alt1
- Autobuild version bump to 1.5.0

* Thu Sep 25 2014 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1
- Initial build

