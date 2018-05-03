%define modname brotlipy

Name: python-module-%modname
Version: 0.7.0
Release: alt2

Summary: Library contains Python bindings for the reference Brotli
License: MIT
Group: Development/Python
Url: https://github.com/python-hyper/brotlipy/

Source: %modname-%version.tar

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-setuptools python-dev
BuildRequires: gcc-c++ python-module-sphinx
BuildRequires: python-module-cffi 

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools python3-dev
BuildPreReq: python3-module-cffi python3-module-sphinx


%description
This library contains Python bindings for the reference Brotli 
encoder/decoder, available here. This allows Python software to 
use the Brotli compression algorithm directly from Python code.

%package -n python3-module-%modname
Summary: Library contains Python bindings for the reference Brotli
Group: Development/Python3

%description -n python3-module-%modname
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

rm -rf ../python3
cp -fR . ../python3

rm -rf *deb

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

export PYTHONPATH=$PWD
%make -C docs man

%install
%python_install

pushd ../python3
%python3_install
popd

%check
python setup.py test

pushd ../python3
python3 setup.py test
popd

%files
%doc LICENSE *.rst
%python_sitelibdir/*

%files -n python3-module-%modname
%doc LICENSE *.rst
%python3_sitelibdir/*

%files docs
%doc docs/build/*


%changelog
* Mon Apr 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt2
- (NMU) Rebuilt with python-3.6.4.

* Fri Mar 30 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.7.0-alt1
- Version 0.7.0
