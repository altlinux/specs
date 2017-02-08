Name: python-module-flamegraph
Version: 0.1
Release: alt3
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
%doc README.rst docs/* example.py
 
%changelog
* Wed Feb  8 2017 Terechkov Evgenii <evg@altlinux.org> 0.1-alt3
- v0.1-15-g4094399

* Sat Oct 22 2016 Terechkov Evgenii <evg@altlinux.org> 0.1-alt2
- v0.1-13-g378fd26

* Tue Jul 21 2015 Terechkov Evgenii <evg@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus
- git-20150721
