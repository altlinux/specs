%global modname cliff-tablib

Name:             python3-module-%modname
Version:          2.0
Release:          alt1

Summary:          tablib formatters for cliff

Group:            Development/Python3
License:          ASL 2.0
URL:              https://pypi.python.org/pypi/cliff-tablib

Source0:          %modname-%version.tar


BuildRequires: rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-cliff
BuildRequires: python3-module-html5lib
BuildRequires: python3-module-pbr

BuildArch:        noarch

%description
The cliff framework is meant to be used to create multi-level commands
such as subversion and git, where the main program handles some basic
argument parsing and then invokes a sub-command to do the work. This
package adds JSON, YAML, and HTML output formatters to those commands.

%prep
%setup -n %modname-%version

# Remove bundled egg info
rm -rf *.egg-info

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Fri Oct 25 2019 Grigory Ustinov <grenka@altlinux.org> 2.0-alt1
- Updated to 2.0.
- Build without python2.

* Fri May 18 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.1-alt3
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1-alt2.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt2
- enable python3 package

* Wed Aug 26 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt1
- Initial release for Sisyphus
