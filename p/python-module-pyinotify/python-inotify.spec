%def_with python3

Summary:       Monitor filesystem events with Python under Linux
Name:          python-module-pyinotify
Version:       0.9.2
Release:       alt4
License:       MIT
Group:         Development/Python
URL:           https://github.com/seb-m/pyinotify
Source0:       %name-%version.tar
Source1:       pyinotify
Source2:       py3inotify

BuildRequires: python-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

Provides: python-module-inotify = %version-%release
Obsoletes: python-module-inotify < %version-%release

Provides: pyinotify = %version-%release
Obsoletes: pyinotify < %version-%release

BuildArch:     noarch

%description
This is a Python module for watching filesystems changes. pyinotify
can be used for various kind of fs monitoring. pyinotify relies on a
recent Linux Kernel feature (merged in kernel 2.6.13) called
inotify. inotify is an event-driven notifier, its notifications are
exported from kernel space to user space.

%package       examples
Summary:       Examples for Python inotify module
Group:         Development/Python
Requires:      python-module-inotify = %version-%release

%description   examples
This package includes some examples usage of the Python inotify module.

%if_with python3
%package -n    python3-module-pyinotify
Summary:       Monitor filesystem events with Python under Linux
Group:         Development/Python3
Provides:      python3-module-inotify = %version-%release

%description -n    python3-module-pyinotify
This is a Python3 module for watching filesystems changes. pyinotify
can be used for various kind of fs monitoring. pyinotify relies on a
recent Linux Kernel feature (merged in kernel 2.6.13) called
inotify. inotify is an event-driven notifier, its notifications are
exported from kernel space to user space.

%endif


%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
install -D -m 0755 -p %SOURCE1 %buildroot%_bindir/pyinotify

%if_with python3
pushd ../python3
%python3_install
install -D -m 0755 -p %SOURCE2 %buildroot%_bindir/py3inotify
popd
%endif

# examples
install -d -m 0755 %buildroot%_datadir/pyinotify
cp -a python2/examples/* %buildroot%_datadir/pyinotify

%files
%doc ACKS COPYING README.md
%_bindir/pyinotify
%python_sitelibdir_noarch/pyinotify*

%if_with python3
%files -n python3-module-pyinotify
%_bindir/py3inotify
%python3_sitelibdir_noarch/pyinotify*
%python3_sitelibdir_noarch/__pycache__/pyinotify*
%endif

%files examples
%_datadir/pyinotify

%changelog
* Thu Jan 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt4
- add python3 module build

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt3
- Rebuild with Python-2.7

* Thu Sep 29 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt2
- merge python-module-inotify and python-module-pyinotify packages

* Wed Sep 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt1
- 0.9.2 build on Fedora spec

* Mon Sep 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt1
- 0.9.0 (ALT #23991)

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt1head.1
- Rebuilt with python 2.6

* Fri May 22 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.6-alt1head
- new version from HEAD (fix bug #20123)

* Sat Feb 21 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt2
- build as noarch

* Sun Jan 25 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version 0.8.1 (with rpmrb script)

* Sun May 11 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.0q-alt1
- initial build for ALT Linux Sisyphus
