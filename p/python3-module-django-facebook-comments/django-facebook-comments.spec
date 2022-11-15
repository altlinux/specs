%define oname django-facebook-comments

%def_with bootstrap

Name: python3-module-%oname
Version: 0.1.5
Release: alt3.1

Summary: Drop-in facebook comments for django
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-facebook-comments/
BuildArch: noarch

# hg clone https://bitbucket.org/sirpengi/django-facebook-comments
Source: %name-%version.tar
Patch: porting-on-python3.patch

BuildRequires(pre): rpm-build-python3

%add_python3_self_prov_path %buildroot%python3_sitelibdir/facebook_comments

%description
django-facebook-comments is a reusable Django app to place facebook
comment boxes in your templates.

This app basically provides two templatetags to use in your templates,
one which just places in a facebook comment box, and one which caches
the facebook comment box (using their api) so that content will be in
the rendered html (some people like this for SEO purposes).

%prep
%setup
%patch0 -p1

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst dfc_test_app
%python3_sitelibdir/*


%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.1.5-alt3.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.5-alt3
- porting on python3

* Sat May 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.5-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.hg20120729.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.hg20120729
- Initial build for Sisyphus

