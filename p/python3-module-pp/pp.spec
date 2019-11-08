%define _unpackaged_files_terminate_build 1
%define oname pp

Name: python3-module-%oname
Version: 1.6.5
Release: alt2

Summary: Parallel and distributed programming for Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/pp/
BuildArch: noarch

Source0: https://pypi.python.org/packages/14/e9/f69030681985226849becd36b04e2c0cb99babff23c8342bc4e30ded06b2/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
Parallel Python module (PP) provides an easy and efficient way to create
parallel-enabled applications for SMP computers and clusters. PP module
features cross-platform portability and dynamic load balancing. Thus
application written with PP will parallelize efficiently even on
heterogeneous and multi-platform clusters (including clusters running
other application with variable CPU loads).

%prep
%setup -q -n %{oname}-%{version}

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|import user|import types|' %oname.py

%build
%python3_build_debug

%install
%python3_install

%files
%doc AUTHORS CHANGELOG README doc/*.config doc/*.html
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Nov 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.6.5-alt2
- disable python2, enable python3

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt1
- automated PyPI update

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.4-alt1
- Initial build for Sisyphus

