%define oname babel

%def_with python3

Name: python-module-%oname
Version: 0.9.5
Release: alt1.2

Summary: a collection of tools for internationalizing Python applications
License: BSD
Group: Development/Python

Url: http://babel.edgewall.org

Source: %name-%version.tar
Source1: CLDR.tar
Patch: %name-%version-%release.patch

Packager: Andrey Rahmatullin <wrar@altlinux.org>

BuildArch: noarch
BuildPreReq: python-module-setuptools 
%{?!_without_check:%{?!_disable_check:BuildRequires: %py_dependencies setuptools.command.test pytz}}

%setup_python_module babel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python3-module-pytz python-tools-2to3
%endif
%py_requires pytz

%description
Babel is an integrated collection of utilities that assist in
internationalizing and localizing Python applications, with an emphasis
on web-based applications.
The functionality Babel provides for internationalization (I18n) and
localization (L10N) can be separated into two different aspects:
  * tools to build and work with gettext message catalogs, and
  * a Python interface to the CLDR (Common Locale Data Repository),
    providing access to various locale display names, localized number
    and date formatting, etc.

%if_with python3
%package -n python3-module-%oname
Summary: a collection of tools for internationalizing Python 3 applications
Group: Development/Python3
%py3_requires pytz

%description -n python3-module-%oname
Babel is an integrated collection of utilities that assist in
internationalizing and localizing Python applications, with an emphasis
on web-based applications.
The functionality Babel provides for internationalization (I18n) and
localization (L10N) can be separated into two different aspects:
  * tools to build and work with gettext message catalogs, and
  * a Python interface to the CLDR (Common Locale Data Repository),
    providing access to various locale display names, localized number
    and date formatting, etc.
%endif

%prep
%setup -a1
%patch -p1
mkdir babel/localedata
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
python scripts/import_cldr.py CLDR/
%python_build
%if_with python3
pushd ../python3
python scripts/import_cldr.py CLDR/
for i in $(find ./ -name '*.py'); do
	sed -i 's|%_bindir/env python|%_bindir/env python3|' $i
	2to3 -w -n $i
done
sed -i \
	's|from UserDict import DictMixin|from collections import MutableMapping as DictMixin|' \
	babel/localedata.py
%python3_build build_ext
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/pybabel %buildroot%_bindir/pybabel3
%endif
%python_install

%check
python setup.py test

%files
%_bindir/pybabel
%python_sitelibdir/babel/
%python_sitelibdir/*.egg-info
%doc ChangeLog doc

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog doc
%_bindir/pybabel3
%python3_sitelibdir/babel/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.5-alt1.1
- Rebuild with Python-2.7

* Sat Aug 28 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.9.5-alt1
- 0.9.5
- build from SVN
- run tests
- add pytz to Requires according to the upstream recommendation

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1.1
- Rebuilt with python 2.6

* Sun Oct 18 2009 Vladimir Lettiev <crux@altlinux.ru> 0.9.4-alt1
- initial build
