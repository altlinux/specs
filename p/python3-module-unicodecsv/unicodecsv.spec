%define sname unicodecsv

Name: python3-module-%sname
Version: 0.14.1
Release: alt2
Summary: Drop-in replacement for Python csv module which supports unicode strings
Group: Development/Python3
License: BSD
URL: https://github.com/jdunck/python-unicodecsv
Source: %sname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-unittest2

BuildArch: noarch

%description
The unicodecsv is a drop-in replacement for Python 2.7's csv module which supports unicode strings without a hassle.

%prep
%setup -n %sname-%version

# Remove bundled egg-info
rm -rf %sname.egg-info

%build
%python3_build

%install
%python3_install

# Delete tests
rm -fr %buildroot%python3_sitelibdir/*/test*

%files
%python3_sitelibdir/*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.14.1-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.14.1-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.14.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.14.1-alt1
- Initial release

