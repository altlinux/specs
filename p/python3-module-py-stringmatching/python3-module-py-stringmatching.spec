%define _unpackaged_files_terminate_build 1
%define pypi_name py-stringmatching
%define mod_name py_stringmatching

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.3
Release: alt1

Summary: A comprehensive and scalable set of string tokenizers and similarity measures in Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/py-stringmatching/
Vcs: https://github.com/anhaidgroup/py_stringmatching

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: python3-module-py-stringmatching-0.4.3-alt-use-base-cython.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: libnumpy-py3-devel

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This project seeks to build a Python software package that consists of
a comprehensive and scalable set of string tokenizers (such as
alphabetical tokenizers, whitespace tokenizers) and string similarity
measures (such as edit distance, Jaccard, TF/IDF).
The package is free, open-source, and BSD-licensed.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%__mv %mod_name/tests tests && %__rm -rf %mod_name
%pyproject_run_unittest

%files
%doc LICENSE CHANGES.txt README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%mod_name/tests

%changelog
* Sat Oct 14 2023 Anton Zhukharev <ancieg@altlinux.org> 0.4.3-alt1
- Built for ALT Sisyphus.

