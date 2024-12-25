Name:   python3-module-queuelib
Version:1.7.0
Release:alt1

Summary:Collection of persistent (disk-based) and non-persistent (memory-based) queues for Python
License:BSD-3-Clause
Group:  Development/Python
URL:    https://github.com/scrapy/queuelib

BuildArch: noarch
Source0:https://github.com/scrapy/queuelib/archive/refs/tags/v%version.tar.gz#/%name-%version.tar

BuildRequires:  rpm-build-python3
BuildRequires:  python3-devel python3-module-setuptools python3-module-wheel
BuildRequires:  fdupes

%description
Queuelib is a collection of persistent (disk-based) queues for Python.
Queuelib goals are speed and simplicity. It was originally part of the
`Scrapy framework`_ and stripped out on its own library.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst NEWS
%python3_sitelibdir/queuelib
%python3_sitelibdir/queuelib-%version-py*.egg-info

%changelog
* Thu Aug 08 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 1.7.0-alt1
- new version

* Tue Apr 02 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 1.6.2-alt1
- Initial build for ALT Linux

