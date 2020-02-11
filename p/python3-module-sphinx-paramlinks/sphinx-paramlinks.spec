%define _unpackaged_files_terminate_build 1

%define oname sphinx-paramlinks

Name: python3-module-%oname
Version: 0.3.2
Release: alt2

Summary: Allows param links in Sphinx function/method descriptions to be linkable
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinx-paramlinks/
BuildArch: noarch

Source0: https://pypi.python.org/packages/68/66/35fd8994e7c380f0272af0fc4b729272fd61a5f209a5ca4b2ee38d92ca68/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-docutils python3-module-sphinx

%py3_provides sphinx_paramlinks


%description
A Sphinx extension which allows :param: directives within Python
documentation to be linkable.

This is an experimental, possibly-not-useful extension that's used by
the SQLAlchemy project and related projects.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.2-alt2
- Porting to python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- automated PyPI update

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus

