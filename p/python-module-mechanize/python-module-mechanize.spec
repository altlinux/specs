%define oname mechanize

%def_with python3

Name: python-module-%oname
Version: 0.2.5
Release: alt1.1.1

Summary: Stateful programmatic web browsing

License: BSD / ZPL
Group: Development/Other
Url: http://wwwsearch.sourceforge.net/mechanize/

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module %oname

Source: http://wwwsearch.sourceforge.net/mechanize/src/%oname-%version.tar
Patch: mechanize-0.2.5-alt-python3.patch

BuildArch: noarch

#BuildPreReq: rpm-build-compat >= 1.2

# manually removed: all
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3 time

#BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

%description
Stateful programmatic web browsing in Python,
after Andy Lester's Perl module WWW::Mechanize.

%package -n python3-module-%oname
Summary: Stateful programmatic web browsing
Group: Development/Python3

%description -n python3-module-%oname
Stateful programmatic web browsing in Python,
after Andy Lester's Perl module WWW::Mechanize.

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
pushd ../python3
%patch -p2
popd
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc docs/ examples/
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1.1.1
- NMU: Use buildreq for BR.

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.1
- Added module for Python 3

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.5-alt1
- new version 0.2.5 (with rpmrb script)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.11-alt1.1
- Rebuild with Python-2.7

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1.11-alt1
- new version 0.1.11 (with rpmrb script)

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.10-alt3
- Rebuilt with python 2.6

* Thu Feb 19 2009 Vitaly Lipatov <lav@altlinux.ru> 0.1.10-alt2
- build as noarch

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.10-alt1
- new version 0.1.10 (with rpmrb script)

* Wed Jul 16 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.7b-alt1
- initial build for ALT Linux Sisyphus

