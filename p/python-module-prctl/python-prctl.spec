Name: python-module-prctl
Version: 1.7
Release: alt1
Group: Development/Python
License: GPL
Summary: Interface to the linux prctl syscall
Url: https://pypi.python.org/pypi/python-prctl
Source: python-prctl-%version.tar.gz

%setup_python_module prctl

# Automatically added by buildreq on Thu Sep 25 2014
# optimized out: libcloog-isl4 python-base python-devel python-module-BeautifulSoup python-module-PyStemmer python-module-Pygments python-module-docutils python-module-html5lib python-module-jinja2 python-module-markupsafe python-module-setuptools python-module-six python-module-snowballstemmer python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest
BuildRequires: ctags libcap-devel python-module-sphinx-pickles python-module-sphinx time

%description
Control process attributes through prctl

The linux prctl function allows you to control specific characteristics
of a process' behaviour. Usage of the function is fairly messy though,
due to limitations in C and linux. This module provides a nice non-messy
python(ic) interface.

Besides prctl, this library also wraps libcap for complete capability
handling and allows you to set the process name as seen in ps and top.

%prep
%setup -n python-prctl-%version

%build
%python_build
make -C docs html

%install
%python_install

%files
%doc docs/_build/html/*
%python_sitelibdir/*

%changelog
* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 1.7-alt1
- Autobuild version bump to 1.7

* Wed Feb 11 2015 Fr. Br. George <george@altlinux.ru> 1.6.1-alt1
- Autobuild version bump to 1.6.1

* Thu Sep 25 2014 Fr. Br. George <george@altlinux.ru> 1.5.0-alt1
- Autobuild version bump to 1.5.0

* Thu Sep 25 2014 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1
- Initial build

