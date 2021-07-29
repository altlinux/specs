%define  srcname filetype

#def_disable check

Name:    python3-module-%srcname
Version: 1.0.7
Release: alt1

Summary: Infer file type and MIME type of any file/buffer
License: MIT
Group:   Development/Python3
URL:     https://github.com/h2non/filetype.py

Packager: Anton Midyukov <antohami@altlinux.org>

# Source-url: https://github.com/h2non/filetype.py/archive/v%version/%srcname-%version.tar.gz
Source: %srcname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools

%if_disabled check
%else
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

%description
Small and dependency free Python package to infer file type and MIME type
checking the magic numbers signature of a file or buffer.

%prep
%setup -n %srcname-%version
sed -i -e '/^#!\//, 1d' examples/*.py
rm -rf examples/__init__.py

%build
%python3_build
rm -rf %{buildroot}%{python3_sitelib}/examples

%install
%python3_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v tests --ignore tests/test_benchmark.py

%files
%python3_sitelibdir/*
%doc README.rst History.md examples

%changelog
* Thu Jul 29 2021 Anton Midyukov <antohami@altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus
