%define oname keepnote-extensions
Name: python-module-%oname
Version: 20110905
Release: alt1
Summary: Extensions for KeepNote - note-taking and organization
License: GPLv2
Group: Office
Url: http://keepnote.org/extensions.shtml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mdrasmus/keepnote-extensions.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel zip keepnote

Requires: keepnote
Provides: %oname = %EVR

%description
This package contains a collection of stable extensions for the
KeepNote note-taking application (http://rasm.ods.org/keepnote).

%package testing
Summary: Testing extensions for KeepNote - note-taking and organization
Group: Office
Requires: keepnote
%add_findreq_skiplist %python_sitelibdir/keepnote/extensions/pasteboard/__init__.py
Provides: %oname-testing = %EVR

%description testing
This package contains a collection of testing extensions for the
KeepNote note-taking application (http://rasm.ods.org/keepnote).

%prep
%setup

%build
./make.py

%install
install -d %buildroot%python_sitelibdir/keepnote/extensions

pushd stable
for i in $(find ./* -type d); do
	../install.sh $i.kne
	cp -fR ~/.config/keepnote/extensions/$i \
		%buildroot%python_sitelibdir/keepnote/extensions/
	echo %python_sitelibdir/keepnote/extensions/$i >>../STABLE
done
popd

pushd testing
for i in $(find ./* -type d); do
	../install.sh $i.kne
	cp -fR ~/.config/keepnote/extensions/$i \
		%buildroot%python_sitelibdir/keepnote/extensions/
	echo %python_sitelibdir/keepnote/extensions/$i >>../TESTING
done
popd

%files -f STABLE
%doc README

%files testing -f TESTING
%doc README

%changelog
* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110905-alt1
- Initial build for Sisyphus

