%define _name bsddb3
# sometime fail
%def_disable check

Name: python-module-%_name
Version: 6.0.1
Release: alt1.1

Summary: Python bindings for BerkleyDB
Group: Development/Python
License: BSD
Url: https://pypi.python.org/pypi/bsddb3/

Source: https://pypi.python.org/packages/source/b/%_name/%_name-%version.tar.gz

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils python-base python-modules python-modules-bsddb python-modules-compiler python-modules-email python3 python3-base
BuildRequires: libdb4-devel python-devel python3-devel rpm-build-python3

#BuildRequires: libdb4-devel
#BuildRequires: python-devel
#BuildRequires: python3-devel rpm-build-python3
#BuildRequires: /proc

%description
This package provides Python wrappers for Berkeley DB                                          .

%package -n python3-module-%name
Summary: Python3 bindings for BerkleyDB
Group: Development/Python3
License: BSD

%description -n python3-module-%name
This package provides Python3 wrappers for Berkeley DB.


%prep
%setup -n %_name-%version -a0
mv %_name-%version py3build

%build
%python_build

pushd py3build
%python3_build
popd

%install
%python_install

pushd py3build
%python3_install
popd

%if_enabled check
%check
%__python test.py

pushd py3build
%__python3 test.py
popd
%endif

%files
%python_sitelibdir/%_name/
%python_sitelibdir/%_name-%version-py*.egg-info
%doc ChangeLog *.txt

%exclude %python_sitelibdir/%_name/tests/

%files -n python3-module-%name
%python3_sitelibdir/%_name/
%python3_sitelibdir/%_name-%version-py*.egg-info

%exclude %python3_sitelibdir/%_name/tests/

%exclude %_includedir/python*/%_name/bsddb.h

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 6.0.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Jul 06 2014 Yuri N. Sedunov <aris@altlinux.org> 6.0.1-alt1
- first build for Sisyphus

