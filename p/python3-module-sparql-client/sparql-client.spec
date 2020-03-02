%define _unpackaged_files_terminate_build 1
%define oname sparql-client

%def_disable check

Name: python3-module-%oname
Version: 3.0
Release: alt2

Summary: Python API to query a SPARQL endpoint
License: MPLv1.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/sparql-client/
BuildArch: noarch

# https://github.com/eea/sparql-client.git
Source: %name-%version.tar
Patch0: port-to-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-dateutil python3-module-eventlet
BuildRequires: python3-module-mock

%py3_requires dateutil


%description
sparql-client is a library to query a SPARQL endpoint. It will
automatically convert literals to the coresponding Python types.

%prep
%setup
%patch0 -p1

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
pushd tests
export PYTHONPATH=%buildroot%python3_sitelibdir
for i in *.py; do
    %__python3 $i
done
popd

%files
%doc *.rst docs/*.txt docs/*.rst
%python3_sitelibdir/*


%changelog
* Mon Mar 02 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.0-alt2
- Version updated to 3.0
- porting to python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0-alt1
- Updated to upstream version 3.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1
- automated PyPI update

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt2.dev.git20140915
- Fixed build

* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.dev.git20140915
- Initial build for Sisyphus

