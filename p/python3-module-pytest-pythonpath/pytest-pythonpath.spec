%define _unpackaged_files_terminate_build 1
%define oname pytest-pythonpath

Name: python3-module-%oname
Version: 0.7.1
Release: alt3

Summary: pytest plugin for adding to the PYTHONPATH from command line or configs
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-pythonpath/
BuildArch: noarch

# https://github.com/bigsassy/pytest-pythonpath.git
Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
%py3_provides pytest_pythonpath


%description
This is a py.test plugin for adding to the PYTHONPATH from the
pytests.ini file before tests run.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%files
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7.1-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.1-alt2
- Fixed build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.git20140208.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20140208
- Initial build for Sisyphus

