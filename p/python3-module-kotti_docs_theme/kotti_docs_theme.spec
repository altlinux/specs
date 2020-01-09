%define oname kotti_docs_theme

Name: python3-module-%oname
Version: 0.3
Release: alt2

Summary: Sphinx Theme for Kotti Documentation
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/kotti_docs_theme/
BuildArch: noarch

# https://github.com/Kotti/kotti_docs_theme.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
This theme is based on sphinx-bootstrap by Scotch Media and modified for
documentation of Kotti and Kotti add-ons.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

cp -fR %oname/themes %buildroot%python3_sitelibdir/%oname/

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Thu Jan 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt2
- porting on python3

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.dev.git20130511
- Initial build for Sisyphus

