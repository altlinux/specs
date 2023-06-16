# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define modulename filetype

#%%def_disable check

Name:    python3-module-%modulename
Version: 1.2.0
Release: alt1

Summary: Infer file type and MIME type of any file/buffer
License: MIT
Group:   Development/Python3
URL:     https://github.com/h2non/filetype.py

# Source-url: https://github.com/h2non/filetype.py/archive/v%version/%modulename-%version.tar.gz
Source: %modulename-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_disabled check
%else
BuildRequires: pytest3
%endif

BuildArch: noarch

%description
Small and dependency free Python package to infer file type and MIME type
checking the magic numbers signature of a file or buffer.

%prep
%setup -n %modulename-%version
sed -i -e '/^#!\//, 1d' examples/*.py
rm -rf examples/__init__.py

%build
%pyproject_build

%install
%pyproject_install

rm %buildroot/%_bindir/filetype

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
pytest3 -v tests --ignore tests/test_benchmark.py

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info
%doc README.rst History.md examples

%changelog
* Fri Jun 16 2023 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- new version (1.2.0) with rpmgs script

* Fri Jun 16 2023 Anton Midyukov <antohami@altlinux.org> 1.0.7-alt2
- Migration to PEP517

* Thu Jul 29 2021 Anton Midyukov <antohami@altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus
