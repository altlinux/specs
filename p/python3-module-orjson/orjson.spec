Name: python3-module-orjson
Version: 3.10.7
Release: alt1

Summary: Fast, correct JSON library for Python
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/orjson/

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(maturin)
BuildRequires: python3(pytest)

%description
%summary

%prep
%setup
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 vendor
%else
tar xf %SOURCE1
%endif

%build
export CARGO_HOME=${PWD}/cargo
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest test

%files
%python3_sitelibdir/orjson
%python3_sitelibdir/orjson-%version.dist-info

%changelog
* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.7-alt1
- 3.10.7 released

* Fri Jul 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.6-alt1
- 3.10.6 released

* Mon May 20 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.3-alt1
- 3.10.3 released

* Tue Apr 16 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.1-alt1
- 3.10.1 released

* Fri Mar 29 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.0-alt1
- 3.10.0 released

* Tue Mar 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.15-alt1
- 3.9.15 released

* Wed Feb 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.14-alt1
- 3.9.14 released

* Wed Jan 24 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.12-alt1
- 3.9.12 relelased

* Mon Dec 18 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.10-alt1
- 3.9.10 released

* Mon Oct 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.9-alt1
- 3.9.9 released

* Fri Sep 15 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.7-alt1
- 3.9.8 released

* Fri May 05 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.8.10-alt1
- 3.8.10 released

* Wed Jan 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.8.5-alt1
- 3.8.5 released

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.8.1-alt1
- 3.8.1 released

* Wed Aug 03 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.7-alt3
- rebuilt as pyproject

* Wed Jul 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.7-alt2
- rebuilt on ppc64le

* Thu Jul 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.7-alt1
- 3.7.7 released
