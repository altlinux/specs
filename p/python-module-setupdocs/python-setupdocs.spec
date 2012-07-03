%define oname setupdocs

%def_with python3

Name:           python-module-%oname
Version:        1.0.6
Release:        alt2.svn20101016
Summary:        Setuptools plugin

Group:          Development/Python
License:        BSD
URL:            http://pypi.python.org/pypi/SetupDocs/
Source:        http://pypi.python.org/packages/source/s/setupdocs/SetupDocs-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildArch:      noarch
BuildRequires:  python-devel, python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif
Requires:       python-module-distribute

%description
Python setuptools plugin that automates building of docs from ReST
source.

%if_with python3
%package -n python3-module-%oname
Summary: Setuptools plugin (Python 3)
Group: Development/Python
Requires: python3-module-distribute

%description -n python3-module-%oname
Python setuptools plugin that automates building of docs from ReST
source.
%endif

%prep
%setup -n SetupDocs-%version
sed -i 's/\#\!.*$//' setupdocs/setupdocs.py
rm -rf setupdocs.egg-info
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build
popd
%endif

%install
%python_install -O1
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt2.svn20101016
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.6-alt1.svn20101016.1.1
- Rebuild with Python-2.7

* Wed May 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.svn20101016.1
- Requires python-module-distribute instead of python-module-setuptools

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.svn20101016
- Version 1.0.6

* Fri Mar 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.svn20100225
- Version 1.0.5

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.svn20090716.1
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.svn20090716
- Version 1.0.4

* Thu Oct 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus (thnx Valery Pipin)

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.1-3
- Removed already existing eggs so that new eggs info files are build
- from source.

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.1-2
- Improved description and cleaned some futile information
- Corrected URL

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.1-1
- Initial package
