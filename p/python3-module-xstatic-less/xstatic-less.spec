%define mname xstatic
%define oname %mname-less
%define pypi_name XStatic-less

Name: python3-module-%oname
Version: 1.3.0.1
Release: alt4

Summary: less (XStatic packaging standard)
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/%pypi_name/
Source: %pypi_name-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-%mname

%py3_provides %mname.pkg.less
%py3_requires %mname.pkg


%description
less packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these
files.

%prep
%setup -n %pypi_name-%version

%build
%python3_build_debug

%install
%python3_install

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%check
%__python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/%mname/pkg/*
%python3_sitelibdir/*.egg-info


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3.0.1-alt4
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0.1-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.0.1-alt3
- build as noarch

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0.1-alt2.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0.1-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.0.1-alt2.1
- NMU: Use buildreq for BR.

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0.1-alt2
- Applied python-module-xstatic-less-1.3.0.1-alt1.diff

* Mon Nov 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0.1-alt1
- Initial build for Sisyphus

