%define _unpackaged_files_terminate_build 1
%define oname sphinx-kr-theme

Name: python3-module-%oname
Version: 0.2.1
Release: alt3

Summary: The third-part package of kennethreitz/kr-sphinx-themes
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/sphinx-kr-theme/

# https://github.com/tonyseek/sphinx-kr-theme.git
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(pygments)

%py3_provides sphinx_kr_theme


%description
This is the third-part package of Kenneth Reitz's krTheme. You will not
have to copy the theme files into VCS or register it as submodule
anymore.

%prep
%setup -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.1-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20140613.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20140613
- Initial build for Sisyphus

