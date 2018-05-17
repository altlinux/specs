%define _unpackaged_files_terminate_build 1

%define oname unicode_slugify

%def_with python3

Name: python-module-%oname
Version: 0.1.5
Release: alt1%ubt
Summary: A slugifier that works in unicode
License: BSD
BuildArch: noarch
Group: Development/Python
Url: https://pypi.org/project/unicode-slugify

# https://github.com/mozilla/unicode-slugify.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(six) python2.7(unidecode)
BuildRequires: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(six) python3(unidecode)
BuildRequires: python3-module-nose
%endif

%description
Unicode Slugify is a slugifier that generates unicode slugs.
It was originally used in the Firefox Add-ons web site
to generate slugs for add-ons and add-on collections.
Many of these add-ons and collections had
unicode characters and required more than simple transliteration.

%package tests
Summary: A slugifier that works in unicode
Group: Development/Python
Requires: %name = %EVR

%description tests
Unicode Slugify is a slugifier that generates unicode slugs.
It was originally used in the Firefox Add-ons web site
to generate slugs for add-ons and add-on collections.
Many of these add-ons and collections had
unicode characters and required more than simple transliteration.

This package contains tests.

%if_with python3
%package -n python3-module-%oname
Summary: A slugifier that works in unicode
Group: Development/Python3

%description -n python3-module-%oname
Unicode Slugify is a slugifier that generates unicode slugs.
It was originally used in the Firefox Add-ons web site
to generate slugs for add-ons and add-on collections.
Many of these add-ons and collections had
unicode characters and required more than simple transliteration.

%package -n python3-module-%oname-tests
Summary: A slugifier that works in unicode
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Unicode Slugify is a slugifier that generates unicode slugs.
It was originally used in the Firefox Add-ons web site
to generate slugs for add-ons and add-on collections.
Many of these add-ons and collections had
unicode characters and required more than simple transliteration.

This package contains tests.
%endif

%prep
%setup
%patch1 -p1

%if_with python3
cp -a . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%check
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README.md LICENSE
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests.*

%files tests
%python_sitelibdir/%oname/tests.*

%if_with python3
%files -n python3-module-%oname
%doc README.md LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests.*
%exclude %python3_sitelibdir/%oname/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests.*
%python3_sitelibdir/%oname/*/tests.*
%endif

%changelog
* Thu May 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.5-alt1%ubt
- Initial build for ALT.
