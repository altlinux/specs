%define module_name blinker

Name: python3-module-%module_name
Version: 1.3
Release: alt2.git20130703
Group: Development/Python3
License: MIT License
Summary: Fast, simple object-to-object and broadcast signaling
URL: http://discorporate.us/projects/Blinker/
# https://github.com/jek/blinker.git
Source: %module_name-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx

%description
Blinker provides a fast dispatching system that allows any number of
interested parties to subscribe to events, or "signals".

Signal receivers can subscribe to specific senders or receive signals
sent by any sender.

%prep
%setup -n %module_name-%version

%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/

%build
%python3_build

%install
%python3_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make SPHINXBUILD="sphinx-build-3" -C docs/source html

%files
%doc AUTHORS CHANGES LICENSE README docs/html
%python3_sitelibdir/%{module_name}*

%changelog
* Mon Jun 07 2021 Grigory Ustinov <grenka@altlinux.org> 1.3-alt2.git20130703
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt1.git20130703.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20130703.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3-alt1.git20130703.1
- NMU: Use buildreq for BR.

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20130703
- Shapshot from git
- Added module for Python 3

* Sun Oct 20 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3-alt1
- build for ALT
