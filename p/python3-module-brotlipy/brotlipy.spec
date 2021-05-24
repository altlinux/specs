%define modname brotlipy

Name: python3-module-%modname
Version: 0.7.0
Release: alt3

Summary: Library contains Python bindings for the reference Brotli
License: MIT
Group: Development/Python3
Url: https://github.com/python-hyper/brotlipy/

Source: %modname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: gcc-c++ python3-module-sphinx
BuildRequires: python3-module-cffi

%description
This library contains Python bindings for the reference Brotli 
encoder/decoder, available here. This allows Python software to 
use the Brotli compression algorithm directly from Python code.

%package docs
Summary: Documentation for %name
Group: Development/Documentation

%description docs
This library contains Python bindings for the reference Brotli 
encoder/decoder, available here. This allows Python software to 
use the Brotli compression algorithm directly from Python code.

This package contains documentation for %name

%prep
%setup -n %modname-%version

rm -rf *deb

%build
%python3_build_debug

export PYTHONPATH=$PWD
%make SPHINXBUILD="sphinx-build-3" -C docs man

%install
%python3_install

%check
python3 setup.py test

%files
%doc LICENSE *.rst
%python3_sitelibdir/*

%files docs
%doc docs/build/*

%changelog
* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt3
- Drop python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2.qa1
- NMU: applied repocop patch

* Mon Apr 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt2
- (NMU) Rebuilt with python-3.6.4.

* Fri Mar 30 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.7.0-alt1
- Version 0.7.0
