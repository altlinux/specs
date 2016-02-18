Name: python-module-systemd
Epoch: 1
Version: 230
Release: alt1.1
Summary: Python module wrapping systemd functionality
Group: Development/Python

License: LGPLv2+
Url: https://github.com/systemd/python-systemd
Source: %name-%version.tar
Patch1: %name-snapshot.patch

#BuildPreReq: rpm-build-python rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils libgpg-error python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: libsystemd-devel python-devel python3-devel rpm-build-python3

#BuildRequires: python-devel python3-devel python-module-sphinx python-module-lxml python3-module-lxml
#BuildRequires: libsystemd-devel

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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:230-alt1.1
- NMU: Use buildreq for BR.

* Mon Aug 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1:230-alt1
- Initial packaging

