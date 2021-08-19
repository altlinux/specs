%define oname python-creole
%define modname creole

Name: python3-module-creole
Version: 1.4.10
Release: alt1

Summary: Markup converter in pure Python for: creole2html, html2creole, html2ReSt, html2textile

License: GPLv3+
Group: Development/Python3
Url: https://github.com/jedie/python-creole

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%description
Python lib for:
 - creole markup -> html
 - html -> creole markup
python-creole is pure python. No external libs needed.
The creole2html part based on the creole markup parser and emitter from
the MoinMoin project by Radomir Dopieralski and Thomas Waldmann.

%prep
%setup
# need only for developing and tests
rm creole/{publish.py,setup_utils.py}

%build
%python3_build

%install
%python3_install
%python3_prune

# don't pack internal tools
rm -v %buildroot%_bindir/{publish,update_rst_readme}

%files
%doc AUTHORS README.rst LICENSE
%_bindir/creole2html
%_bindir/html2creole
%_bindir/html2rest
%_bindir/html2textile
%python3_sitelibdir/%modname
%python3_sitelibdir/*.egg-info


%changelog
* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.4.10-alt1
- new version (1.4.10) with rpmgs script
- cleanup spec, switch to build from pypi tarball

* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Version 1.2.0
- Added module for Python 3

* Fri May 24 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Mon Jul 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.3-alt1.2
- exclude tests from package

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.3-alt1.1
- Rebuild with Python-2.7

* Mon Mar 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Mon Dec 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- first build for Sisyphus
