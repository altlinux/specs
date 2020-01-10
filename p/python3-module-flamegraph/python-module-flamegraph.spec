%define oname flamegraph

Name: python3-module-%oname
Version: 0.1
Release: alt4

Summary: Statistical profiler which outputs in format suitable for FlameGraph
License: Public Domain
Group: Monitoring
Url: https://github.com/evanhempel/python-flamegraph
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools


%description
A simple statistical profiler which outputs in format suitable for
FlameGraph.

%prep
%setup

%build
%__python3 setup.py build

%install
%__python3 setup.py install --root %buildroot

%files
%python3_sitelibdir/flamegraph
%python3_sitelibdir/flamegraph-%{version}*
%doc README.rst docs/* example.py
 

%changelog
* Fri Jan 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt4
- porting on python3

* Wed Feb  8 2017 Terechkov Evgenii <evg@altlinux.org> 0.1-alt3
- v0.1-15-g4094399

* Sat Oct 22 2016 Terechkov Evgenii <evg@altlinux.org> 0.1-alt2
- v0.1-13-g378fd26

* Tue Jul 21 2015 Terechkov Evgenii <evg@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus
- git-20150721
