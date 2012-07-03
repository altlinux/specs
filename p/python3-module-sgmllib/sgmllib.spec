%define oname sgmllib
Name: python3-module-%oname
Version: 1.0.0
Release: alt1.hg20100824
Summary: Py3k port of the old stdlib module
License: BSD
Group: Development/Python3
Url: http://hg.hardcoded.net/sgmllib
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/hsoft/sgmllib
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-distribute

%description
sgmllib was dropped in Python 3. For those depending on it, that's
somewhat unfortunate. This is a quick and dirty port of this old module.
I just ran 2to3 on it and published it. I don't intend to maintain it,
so it might be a good idea to eventually think about finding another
module to use.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc CHANGES README
%python3_sitelibdir/*

%changelog
* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20100824
- Initial build for Sisyphus

