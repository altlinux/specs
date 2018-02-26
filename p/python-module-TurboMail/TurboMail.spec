%define oname TurboMail
Name: python-module-%oname
Version: 3.0.3
Release: alt2.1
Summary: Mail delivery subsystem and MIME message generation framework for Python
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/TurboMail/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
TurboMail 3 offers:

* Simplified creation of complex messages, including rich text,
  attachments, and more.
* Modular delivery managers including the blocking immediate manager and
  the threaded on demand manager.
* Modular back-ends ('transports') including SMTP and in-memory (debug)
* Easier debugging when using the debug back-end in concert with the
  immediate manager.
* A plugin architecture with a sample plugin for altered message
  encoding.
* Automatic integration into TurboGears 1.x.

%prep
%setup

%build
%python_build

%install
%python_install

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f


%files
%doc *.txt tests
%python_sitelibdir/*
%exclude %python_sitelibdir/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.3-alt2.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt2
- applied repocop fixes:
  + macos-resource-fork-file-in-package for python-module-TurboMail

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1
- Initial build for Sisyphus

