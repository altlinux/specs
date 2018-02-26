Name: python-module-musicbrainz2
Version: 0.7.0
Release: alt1.1.1

Summary: Python module for access to the MusicBrainz Database.
License: distributable
Group: Development/Python
Url: http://musicbrainz.org/doc/PythonMusicBrainz2

BuildArch: noarch
Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar

BuildPreReq: rpm-build-python
BuildRequires: python-devel >= 2.4 python-module-setuptools
BuildRequires: python-modules-ctypes libdiscid-devel

%description
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
%setup -q

%build
python setup.py build
python setup.py docs

%install
python setup.py install --root=$RPM_BUILD_ROOT --optimize=2 --record=INSTALLED_FILES
mkdir -p %{buildroot}%_defaultdocdir/%name-%version
cp -R html *.txt %{buildroot}%_defaultdocdir/%name-%version


%files
%doc *.txt
%_bindir/*
%python_sitelibdir/*

%files doc
%docdir html


%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.1
- Rebuilt with python 2.6

* Sat Oct  3 2009 Alexey Morsov <swi@altlinux.org> 0.7.0-alt1
- initial build

