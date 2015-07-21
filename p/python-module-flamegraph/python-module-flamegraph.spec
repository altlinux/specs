Name: python-module-flamegraph
Version: 0.1
Release: alt1
Summary: Statistical profiler which outputs in format suitable for FlameGraph

Group: Monitoring
License: Public Domain
Url: https://github.com/evanhempel/python-flamegraph
Source0: %name-%version.tar
BuildRequires: python-module-setuptools
BuildArch: noarch

%description
A simple statistical profiler which outputs in format suitable for
FlameGraph.

%prep
%setup

%build
python setup.py build

%install
python setup.py install --root %buildroot

%files
%python_sitelibdir/flamegraph
%python_sitelibdir/flamegraph-%{version}*
%doc README.rst docs/*
 
%changelog
* Tue Jul 21 2015 Terechkov Evgenii <evg@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus
- git-20150721
