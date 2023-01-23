%def_disable snapshot
%define pypi_name configobj
%def_disable check

Name: python3-module-%pypi_name
Version: 5.0.8
Release: alt1

Summary: a Python module for easy reading and writing of config files
License: BSD-3-Clause
Group: Development/Python3
Url: http://configobj.readthedocs.org/

%if_disabled snapshot
Source: https://pypi.python.org/packages/source/c/%pypi_name/%pypi_name-%version.tar.gz
%else
Vcs: https://github.com/DiffSK/configobj
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-wheel
%{?_enable_check:BuildRequires: python3-module-tox python3-module-flake8 python3-module-pep8}

%description
ConfigObj - a Python module for easy reading and writing of config
files.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
tox.py3 -e py%(echo %__python3_version | tr -d .) --sitepackages -o -v

%files
%python3_sitelibdir/validate/
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jan 23 2023 Yuri N. Sedunov <aris@altlinux.org> 5.0.8-alt1
- 5.0.8

* Thu Aug 05 2021 Yuri N. Sedunov <aris@altlinux.org> 5.0.6-alt2
- python3-only build

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.0.6-alt1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.0.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 11 2016 Yuri N. Sedunov <aris@altlinux.org> 5.0.6-alt1
- 5.0.6

* Thu Jul 03 2014 Yuri N. Sedunov <aris@altlinux.org> 5.0.5-alt1
- 5.0.5 (new upstream)
- new python3 subpackage

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.7.2-alt1.1
- Rebuild with Python-2.7

* Sat Oct 30 2010 Yuri N. Sedunov <aris@altlinux.org> 4.7.2-alt1
- new version (ALT #24462)

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.3-alt1.1
- Rebuilt with python 2.6

* Wed Oct 29 2008 Yuri N. Sedunov <aris@altlinux.org> 4.5.3-alt1
- first build for Sisyphus

