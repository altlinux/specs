%define oname kitchen

%def_without docs

%def_with check

Name: python3-module-%oname
Version: 1.2.6
Release: alt3

Summary: Cornucopia of useful code
License: LGPLv2+
Group: Development/Python3
Url: https://pypi.python.org/pypi/kitchen/
Vcs: https://github.com/fedora-infra/kitchen.git

Source: %name-%version.tar
Patch: suse-remove-nose.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib
%if_with check
BuildRequires: python3-module-pytest
%endif
%if_with docs
BuildRequires: python3-module-sphinx
%endif

%py3_provides %oname


%description
Kitchen contains a cornucopia of useful code.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Kitchen contains a cornucopia of useful code.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Kitchen contains a cornucopia of useful code.

This package contains documentation for %oname.

%prep
%setup
%patch -p1

sed -i 's|#! /usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%if_with docs
pushd %{oname}3/docs
py3_sphinx-build -b pickle -d _build/doctrees . _build/pickle
py3_sphinx-build -b html -d _build/doctrees . _build/html
cp -fR _build/pickle %buildroot%python_sitelibdir/%oname/
popd
%endif

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -k "\
not test_internal_generate_combining_table \
and not test_easy_gettext_setup_non_unicode \
and not test_invalid_fallback_no_raise \
and not test_lgettext \
and not test_lngettext" kitchen3


%files
%doc *.rst
%python3_sitelibdir/*
%if_with docs
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc %{oname}/docs/_build/html/*
%endif


%changelog
* Mon Apr 03 2023 Anton Vyatkin <toni@altlinux.org> 1.2.6-alt3
- Fix BuildRequires

* Thu Jun 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.6-alt2
- drop excessive python3-module-jinja2-tests BR

* Thu Dec 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.6-alt1
- Version updated to 1.2.6
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1.git20141202.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.1-alt1.git20141202.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1.git20141202.1
- NMU: Use buildreq for BR.

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.git20141202
- Initial build for Sisyphus

