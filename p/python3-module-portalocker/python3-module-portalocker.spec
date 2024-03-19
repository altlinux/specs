%define        _unpackaged_files_terminate_build 1
%define        pypiname portalocker
%define        modname %pypiname
%define        distname %pypiname
%def_disable   check
%def_enable    doc

Name:          python3-module-%pypiname
Version:       2.7.0
Release:       alt1.1
Summary:       An easy library for Python file locking
License:       BSD-3-Clause
Group:         Development/Python3
Url:           https://portalocker.readthedocs.io
Vcs:           https://github.com/wolph/portalocker.git

BuildArch:     noarch
Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
%{?!_disable_doc:BuildRequires: python3-module-sphinx-sphinx-build-symlink}
%if_enabled check
BuildRequires: python3(pytest-cov)
BuildRequires: python3(fakeredis)
%endif

%description
Portalocker is a library to provide an easy API to file locking.

An easy library for Python file locking. It works on Windows, Linux, BSD and
Unix systems and can even perform distributed locking. Naturally it also
supports the with statement.

An important detail to note is that on Linux and Unix systems the locks are
advisory by default. By specifying the -o mand option to the mount command it is
possible to enable mandatory file locking on Linux. This is generally not
recommended however.


%prep
%setup
%autopatch -p1

%build
%pyproject_build
%{?!_disable_doc:%make -C docs html SPHINXBUILD=sphinx-build-3}

%install
%pyproject_install

%check
%pyproject_run_pytest
%pyproject_run_unittest

%files
%doc *.rst
%{?!_disable_doc:%doc docs/_build/html/*}
%python3_sitelibdir/%{distname}/
%python3_sitelibdir/%{modname}*/METADATA

%changelog
* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 2.7.0-alt1.1
- NMU: added missing build dependency on setuptools.

* Thu Aug 17 2023 Pavel Skrylev <majioa@altlinux.org> 2.7.0-alt1
- Initial build for Sisyphus.
