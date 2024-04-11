%define oname derpconf

%def_with check

Name: python3-module-%oname
Version: 0.8.4
Release: alt1

Summary: derpconf abstracts loading configuration files for your app

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/derpconf
VCS: https://github.com/globocom/derpconf

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%py3_provides %oname

%description
derpconf abstracts loading configuration files for your app. derpconf
was extracted from thumbor.

%prep
%setup

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu Apr 11 2024 Grigory Ustinov <grenka@altlinux.org> 0.8.4-alt1
- Build new version.

* Tue Jan 30 2024 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt2.1
- NMU: Added zombie-imp to BuildRequires.

* Wed Nov 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.8.1-alt2
- version updated to 0.8.1
- python2 -> python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1
- automated PyPI update

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20140930
- Initial build for Sisyphus

