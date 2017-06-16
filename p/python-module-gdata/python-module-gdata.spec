%define oname gdata

%def_without python3

Name: python-module-gdata
Version: 2.0.18
Release: alt3.git20160102

Summary: A Python module for accessing online Google services

Group: Development/Python
License: Apache-2.0
Url: https://github.com/google/gdata-python-client

# Source0-git:	https://github.com/google/gdata-python-client.git
Source: %name-%version-%release.tar

BuildArch: noarch

BuildRequires: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python-tools-2to3
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
%python_install

%if_with python3
pushd ../python3
%python3_install
chmod -x samples/*/*.py
rm -rf src/gdata/Crypto/test.py
rm -rf src/gdata/Crypto/Util/test.py
popd
%endif

%files
%doc *.txt
%python_sitelibdir/atom/
%python_sitelibdir/gdata/
%python_sitelibdir/*.egg-info

%files docs
%doc pydocs/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/atom/
%python3_sitelibdir/gdata/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Jun 16 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.18-alt3.git20160102
- update to the latest commit
- cleanup spec, fix dir packing

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.18-alt2.git20150813
- New snapshot

* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.18-alt2.git20150316
- New snapshot

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.18-alt2.git20150214
- New snapshot

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

