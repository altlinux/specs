%define oname musicbrainz2

%def_without python3

Name: python-module-%oname
Version: 0.7.4
Release: alt1

Summary: Python module for access to the MusicBrainz Database.
License: distributable
Group: Development/Python
Url: http://musicbrainz.org/doc/PythonMusicBrainz2

BuildArch: noarch
Source: %name-%version.tar

BuildPreReq: rpm-build-python
BuildRequires: python-devel >= 2.4 python-module-setuptools
BuildRequires: python-modules-ctypes libdiscid-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
The package python-musicbrainz2 is a client library
written in python, which provides easy object oriented
access to the MusicBrainz Database using the XMLWebService.
It has been written from scratch and uses a different
model than PythonMusicbrainz, the first generation
python bindings.

%package -n python3-module-%oname
Summary: Python module for access to the MusicBrainz Database
Group: Development/Python3

%description -n python3-module-%oname
The package python-musicbrainz2 is a client library
written in python, which provides easy object oriented
access to the MusicBrainz Database using the XMLWebService.
It has been written from scratch and uses a different
model than PythonMusicbrainz, the first generation
python bindings.

%package doc
Summary: API documentation for %name
Group: Development/Python
BuildRequires:  python-module-epydoc

%description doc
API documentation for %name

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

python setup.py docs

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	2to3 -w -n $i
	mv $i $i.py3
done
popd
%endif

%python_install
mkdir -p %{buildroot}%_defaultdocdir/%name-%version
cp -R html *.txt %{buildroot}%_defaultdocdir/%name-%version

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%files doc
%docdir html

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1
- Version 0.7.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.1
- Rebuilt with python 2.6

* Sat Oct  3 2009 Alexey Morsov <swi@altlinux.org> 0.7.0-alt1
- initial build

