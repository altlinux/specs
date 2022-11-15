%define modname tablib

Name:		python3-module-%modname
Version:	0.12.1
Release:	alt2.1
Summary:	Format agnostic tabular data library (XLS, JSON, YAML, CSV)

Group:		Development/Python3
License:	MIT
URL:		http://github.com/kennethreitz/tablib
Source0:	%name-%version.tar

BuildArch:	noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-html5lib python3-module-pbr python3-module-yaml

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%modname/packages/dbfpy3/utils.py

%description
Tablib is a format-agnostic tabular dataset library, written in Python.

Output formats supported:

 - Excel (Sets + Books)
 - JSON (Sets + Books)
 - YAML (Sets + Books)
 - HTML (Sets)
 - TSV (Sets)
 - CSV (Sets)

%add_python3_req_skip UserDict
%add_python3_req_skip odf

%prep
%setup
pushd tablib/packages/dbfpy/
sed -i '/print.*/ s/$/)/' dbfnew.py | sed 's/print/print(/' > dbfnew.py
popd

%build
%python3_build

%install
%python3_install

%files
%doc README.rst AUTHORS LICENSE
%python3_sitelibdir/*


%changelog
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
