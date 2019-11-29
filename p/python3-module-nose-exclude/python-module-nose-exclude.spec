%global pypi_name nose-exclude

Name:           python3-module-%pypi_name
Version:        0.5.0
Release:        alt2
Summary:        Exclude specific directories from nosetests runs
Group:          Development/Python3

License:        LGPLv2
URL:            http://pypi.python.org/pypi/nose-exclude/%version
BuildArch:      noarch

# https://github.com/kgrandis/nose-exclude
Source0:        %name-%version.tar

BuildRequires(pre):  rpm-build-python3


%description
nose-exclude is a `Nose`_ plugin that allows you to easily
specify directories to be excluded from testing.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/nose_exclude.py*
%python3_sitelibdir/nose_exclude-%version-py?.?.egg-info
%python3_sitelibdir/__pycache__/nose_exclude*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5.0-alt2
- python2 disabled

* Wed Jul 10 2019 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt1
- Build new version.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.0-alt1.2
- Rebuild with python3.7.

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.2.0-alt1
- First build for ALT (based on Fedora 0.2.0-3.fc21.src)

