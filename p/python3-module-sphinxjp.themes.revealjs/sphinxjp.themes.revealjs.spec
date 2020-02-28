%define mname sphinxjp.themes
%define oname %mname.revealjs

%def_with check

Name: python3-module-%oname
Version: 0.3.0
Release: alt3

Summary: A sphinx theme for generate reveal.js presentation
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinxjp.themes.revealjs

BuildArch: noarch

# https://github.com/tell-k/sphinxjp.themes.revealjs.git
Source: %name-%version.tar
Patch: sphinxjp-0.3.0-Fix-Pytest4.x-compatibility-errors.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-mock python3-module-pytest
BuildRequires: python3-module-pytest-cov


%description
reveal.js style presentation theme for Sphinx.

%prep
%setup
%patch -p1

sed -i 's|sphinx.util.compat|docutils.parsers.rst|' \
                    $(find ./ -name 'directives.py')

%build
export LC_ALL=en_US.UTF-8
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v -a "--cov sphinxjp"

%files
%doc *.rst src/*.txt
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/sphinxjp/themes/*


%changelog
* Fri Feb 28 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.0-alt3
- Build for python2 disabled.

* Mon Jun 03 2019 Stanislav Levin <slev@altlinux.org> 0.3.0-alt2.git20150621
- Fixed Pytest4.x compatibility errors.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.git20150621.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20150621.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.git20150621.1
- NMU: Use buildreq for BR.

* Sun Aug 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150621
- Initial build for Sisyphus

