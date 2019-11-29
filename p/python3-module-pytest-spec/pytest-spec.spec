%define _unpackaged_files_terminate_build 1
%define oname pytest-spec

%def_disable check

Name: python3-module-%oname
Version: 1.1.0
Release: alt2

Summary: pytest plugin to display test execution output like a SPECIFICATION
License: GPLv2+
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-spec/
BuildArch: noarch

# https://github.com/pchomik/pytest-spec.git
Source0: https://pypi.python.org/packages/96/d1/68ced04b24b93203db875e0123c288b5993732fda2be5f3859907e4a40a4/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-pbr
BuildRequires: python3-module-pytest python3-module-unittest2

%py3_provides pytest_spec


%description
pytest plugin to display test execution output like a SPECIFICATION.

Available features:

* Format output to look like specification.
* Group tests by classes.
* Failed, passed and skipped are marked and colored.
* Remove test_ and underscores for every test.
* Method under test may be highlighted (method) like in example.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version -vv

%files
%doc *.rst PKG-INFO
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt2
- python2 disabled

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.24-alt2.git20150202.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.2.24-alt2.git20150202
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.24-alt1.git20150202
- Initial build for Sisyphus

