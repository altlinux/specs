%define _unpackaged_files_terminate_build 1
%define oname derpconf

%def_with check

Name: python3-module-%oname
Version: 0.8.1
Release: alt2

Summary: derpconf abstracts loading configuration files for your app
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/derpconf/
# https://github.com/globocom/derpconf.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/98/2d/4703d2f342faf2d66970f67d7664f24facca299b16983365f3c8ee20a0cd/%{oname}-%{version}.tar.gz


BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-gevent python3-module-coverage
BuildRequires: python3-module-colorama python3-module-tox
BuildRequires: python3-module-six
%endif

%py3_provides %oname


%description
derpconf abstracts loading configuration files for your app. derpconf
was extracted from thumbor.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%if_with check
%check
python3 setup.py test
%endif

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Wed Nov 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.8.1-alt2
- version updated to 0.8.1
- python2 -> python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1
- automated PyPI update

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20140930
- Initial build for Sisyphus

