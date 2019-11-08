%define oname minify

Name: python3-module-%oname
Version: 0.1.4
Release: alt2

Summary: Minify provides distutils/setuptools commands for minifying CSS and JS resources
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/minify/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-yuicompressor

%py3_provides %oname
%py3_requires yuicompressor


%description
Minify provides distutils/setuptools commands for minifying CSS and JS
resources using the well-known YUI compressor from Yahoo! Inc. When you
install minify, two new commands are available:

* minify_js which minifies Javascript files
* minify_css which minifies CSS files

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc CHANGES README
%python3_sitelibdir/*


%changelog
* Fri Nov 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.4-alt2
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.4-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus

