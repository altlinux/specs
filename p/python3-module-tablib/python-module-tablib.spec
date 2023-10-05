%define modname tablib
%define release_version 3.5.0
%define commit_num .9
%define commit_id .g0f0ddf6
%def_enable check
%if_enabled check
%def_enable extra_check
%else
%def_disable extra_check
%endif
%def_enable docs

Name:		python3-module-%modname
Version:	%release_version.0%commit_num%commit_id
Release:	alt1
Summary:	Format agnostic tabular data library (XLS, JSON, YAML, CSV)

Group:		Development/Python3
License:	MIT
URL:		https://github.com/jazzband/tablib.git
Source0:	%name-%version.tar

BuildArch:	noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pyproject-installer python3(setuptools) python3(wheel)
BuildPreReq: python3-module-html5lib python3-module-pbr python3-module-yaml
%{?_enable_check:BuildRequires: python3(pytest) python3(pytest-cov) python3(openpyxl) python3(tabulate) python3(xlrd) python3(xlwt) python3(odf)}
%{?_enable_extra_check:BuildRequires: python3(pandas)}
%{?_enable_docs:BuildRequires: python3-module-sphinx python3-module-setuptools_scm}


%description
Tablib is a format-agnostic tabular dataset library, written in Python.

Output formats supported:

 - Excel (Sets + Books)
 - JSON (Sets + Books)
 - YAML (Sets + Books)
 - HTML (Sets)
 - TSV (Sets)
 - CSV (Sets)


%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%release_version
%pyproject_build

%if_enabled docs
env PYTHONPATH="$PWD/src" sphinx-build-3 docs html
env PYTHONPATH="$PWD/src" sphinx-build-3 -b man docs man
rm -rf html/.{buildinfo,doctrees}
%endif

%install
%pyproject_install
%{?_enable_docs:install -pDm 644 man/%modname.1 %buildroot%_man1dir/%modname.1}

%check
%pyproject_run_pytest -v

%files
%doc README.md AUTHORS LICENSE HISTORY.md CODE_OF_CONDUCT.md RELEASING.md
%if_enabled docs
%doc html
%_man1dir/%{modname}*
%endif
%python3_sitelibdir/%{modname}*


%changelog
* Wed Oct 04 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 3.5.0.0.9.g0f0ddf6-alt1
- Changed the upstream URL
- Updated to upstream 3.5.0-9-g0f0ddf6
- Turned on tests running and docs building

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.12.1-alt2.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Sun Aug 30 2020 Grigory Ustinov <grenka@altlinux.org> 0.12.1-alt2
- Transfer on python3.

* Fri May 18 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.12.1-alt1
- updated version to 0.12.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0
- cleanup spec
- python3 package

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 0.9.11.20120702git752443f-alt1
- Initial release for Sisyphus (based on Fedora)
