%define oname gdata

%def_without python3

Name:           python-module-%oname
Version:        2.0.18
Release:        alt1.hg20140113
Summary:        A Python module for accessing online Google services
Group:          Development/Python
License:        Apache-2.0
URL:            http://code.google.com/p/gdata-python-client/
# hg clone https://code.google.com/p/gdata-python-client/
Source0:	%name-%version-%release.tar
Packager:	Mikhail A Pokidko <pma@altlinux.org>

BuildArch:      noarch
BuildRequires:  python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel python-tools-2to3
%endif

%description
This is a Python module for accessing online Google services, such as:
- Blogger
- Calendar
- Picasa Web Albums
- Spreadsheets
- YouTube
- Notebook
and other

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
This is a Python module for accessing online Google services, such as:
- Blogger
- Calendar
- Picasa Web Albums
- Spreadsheets
- YouTube
- Notebook
and other

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: A Python module for accessing online Google services
Group: Development/Python3

%description -n python3-module-%oname
This is a Python module for accessing online Google services, such as:
- Blogger
- Calendar
- Picasa Web Albums
- Spreadsheets
- YouTube
- Notebook
and other

%prep
%setup

%if_with python3
cp -fR . ../python3
rm -f ../python3/samples/apps/emailsettings_pop_settings.py
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build
chmod -x samples/*/*.py
rm -rf src/gdata/Crypto/test.py
rm -rf src/gdata/Crypto/Util/test.py

%if_with python3
pushd ../python3
%python3_build
chmod -x samples/*/*.py
rm -rf src/gdata/Crypto/test.py
rm -rf src/gdata/Crypto/Util/test.py
popd
%endif

%install
%python_install --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
chmod -x samples/*/*.py
rm -rf src/gdata/Crypto/test.py
rm -rf src/gdata/Crypto/Util/test.py
popd
%endif

%files -f INSTALLED_FILES
%doc *.txt

%files docs
%doc pydocs/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Thu Aug 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.18-alt1.hg20140113
- Version 2.0.18

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.10-alt1.svn.987.1
- Rebuild with Python-2.7

* Sat Jun 19 2010 Mikhail Pokidko <pma@altlinux.org> 2.0.10-alt1.svn.987
- 2.0.10. Closes: #20657

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.1
- Rebuilt with python 2.6

* Thu Jul 02 2009 Mikhail Pokidko <pma@altlinux.org> 2.0.0-alt1
- version up. closes: #20657

* Thu Aug 14 2008 Mikhail Pokidko <pma@altlinux.org> 1.1.1-alt1
- Version up

* Wed May 14 2008 Mikhail Pokidko <pma@altlinux.org> 1.0.13-alt1
- Initial ALT build

