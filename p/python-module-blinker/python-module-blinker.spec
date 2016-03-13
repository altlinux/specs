%define module_name blinker

%def_with python3

Name: python-module-%module_name
Version: 1.3
Release: alt1.git20130703.1.1
Group: Development/Python
License: MIT License
Summary: Fast, simple object-to-object and broadcast signaling
URL: http://discorporate.us/projects/Blinker/
# https://github.com/jek/blinker.git
Source: %module_name-%version.tar.gz
BuildArch: noarch

#BuildPreReq: python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv rpm-build-python3 time

%description
Blinker provides a fast dispatching system that allows any number of
interested parties to subscribe to events, or "signals".

Signal receivers can subscribe to specific senders or receive signals
sent by any sender.

%package -n python3-module-%module_name
Summary: Fast, simple object-to-object and broadcast signaling
Group: Development/Python3

%description -n python3-module-%module_name
Blinker provides a fast dispatching system that allows any number of
interested parties to subscribe to events, or "signals".

Signal receivers can subscribe to specific senders or receive signals
sent by any sender.

%prep
%setup -n %module_name-%version

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs/source html

%files
%doc AUTHORS CHANGES LICENSE README docs/html
%python_sitelibdir/%{module_name}*

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS CHANGES LICENSE README docs/html
%python3_sitelibdir/%{module_name}*
%endif

%changelog
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
