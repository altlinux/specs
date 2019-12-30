%define oname gdata

Name: python3-module-gdata
Version: 2.0.18
Release: alt4

Summary: A Python module for accessing online Google services
Group: Development/Python3
License: Apache-2.0
Url: https://github.com/google/gdata-python-client
BuildArch: noarch

# Source0-git:	https://github.com/google/gdata-python-client.git
Source: %name-%version-%release.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%add_python3_req_skip google.appengine.api google.appengine.ext


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

%prep
%setup
%patch0 -p1

rm -f samples/apps/emailsettings_pop_settings.py
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

chmod -x samples/*/*.py

rm -rf src/gdata/Crypto/test.py
rm -rf src/gdata/Crypto/Util/test.py

%install
%python3_install

chmod -x samples/*/*.py

rm -rf src/gdata/Crypto/test.py
rm -rf src/gdata/Crypto/Util/test.py

install -d %buildroot%python3_sitelibdir/%oname/finance
install -d %buildroot%python3_sitelibdir/%oname/finance/__pycache__

for i in $(find src/%oname/finance -name '*.py')
do
    install -p -m644 $i %buildroot%python3_sitelibdir/%oname/finance/
done
for i in $(find src/%oname/finance/__pycache__ -name '*.pyc')
do
    install -p -m644 $i %buildroot%python3_sitelibdir/%oname/finance/__pycahce__
done

%files
%doc *.txt
%python3_sitelibdir/atom/
%python3_sitelibdir/gdata/
%python3_sitelibdir/*.egg-info

%files docs
%doc pydocs/*


%changelog
* Mon Dec 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.18-alt4
- porting on python3

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

