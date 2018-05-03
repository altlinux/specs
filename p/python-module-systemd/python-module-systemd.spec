Name: python-module-systemd
Epoch: 1
Version: 234
Release: alt1.1
Summary: Python module wrapping systemd functionality
Group: Development/Python

License: LGPLv2+
Url: https://github.com/systemd/python-systemd
Source: %name-%version.tar
Patch1: %name-snapshot.patch

BuildPreReq: rpm-build-python rpm-build-python3
BuildRequires: python-devel python3-devel python-module-lxml python3-module-lxml
BuildRequires: libsystemd-devel

%description
Python module for native access to the systemd facilities.
Functionality includes sending of structured messages to the journal
and reading journal files, querying machine and boot identifiers and a
lists of message identifiers provided by systemd. Other functionality
provided by libsystemd is also wrapped.

This is the version for Python 2.

%package -n python3-module-systemd
Summary: %summary
Group: Development/Python3

%description -n python3-module-systemd
Python module for native access to the systemd facilities.
Functionality includes sending of structured messages to the journal
and reading journal files, querying machine and boot identifiers and a
lists of message identifiers provided by systemd. Other functionality
provided by libsystemd is also wrapped.

This is the version for Python 3.

%prep
%setup -q
%patch1 -p1

%build
%make PYTHON=%__python build
%make PYTHON=%__python3 build

%install
%makeinstall_std PYTHON=%__python
%makeinstall_std PYTHON=%__python3

%files
%doc README.md LICENSE.txt
%python_sitelibdir/*

%files -n python3-module-systemd
%doc README.md LICENSE.txt
%python3_sitelibdir/*

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:234-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Aug 09 2017 Alexey Shabalin <shaba@altlinux.ru> 1:234-alt1
- 234

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:230-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:230-alt1.1
- NMU: Use buildreq for BR.

* Mon Aug 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1:230-alt1
- Initial packaging

