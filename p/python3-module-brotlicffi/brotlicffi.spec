%define pypi_name brotlicffi

Name: python3-module-%pypi_name
Version: 1.1.0.0
Release: alt1

Summary: Library contains Python bindings for the reference Brotli
License: MIT
Group: Development/Python3
Url: https://github.com/python-hyper/brotlicffi/

Source: %pypi_name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject

BuildRequires: python3(pytest-cov)
BuildRequires: python3(hypothesis)
BuildRequires: python3-module-sphinx

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check

%description
This library contains Python bindings for the reference Brotli 
encoder/decoder, available here. This allows Python software to 
use the Brotli compression algorithm directly from Python code.

%package docs
Summary: Documentation for %name
Group: Development/Documentation

BuildArch: noarch

%description docs
This library contains Python bindings for the reference Brotli 
encoder/decoder, available here. This allows Python software to 
use the Brotli compression algorithm directly from Python code.

This package contains documentation for %name

%prep
%setup -n %pypi_name-%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

export PYTHONPATH=$PWD
%make SPHINXBUILD="sphinx-build-3" -C docs man

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.rst
%python3_sitelibdir/*

%files docs
%doc docs/build/*

%changelog
* Sun Oct 22 2023 Andrey Limachko <liannnix@altlinux.org> 1.1.0.0-alt1
- Version 1.1.0.0
- Rename package to brotlicffi. brotli provide replaced with python3-module-brotli

* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt3
- Drop python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2.qa1
- NMU: applied repocop patch

* Mon Apr 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt2
- (NMU) Rebuilt with python-3.6.4.

* Fri Mar 30 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.7.0-alt1
- Version 0.7.0
