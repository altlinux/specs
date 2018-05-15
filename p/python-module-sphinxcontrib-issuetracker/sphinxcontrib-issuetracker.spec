%define rname sphinxcontrib
%define oname %rname-issuetracker

Name: python-module-%oname
Version: 0.11
Release: alt2.git20130117.1
Summary: Sphinx integration with different issuetrackers
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/sphinxcontrib-issuetracker

# https://github.com/lunaryorn/sphinxcontrib-issuetracker.git
Source: %name-%version.tar

# https://github.com/ignatenkobrain/sphinxcontrib-issuetracker/pull/13
Patch1: %oname-%version-sphinx-support.patch

BuildPreReq: python-devel python-module-setuptools

%description
A Sphinx extension to reference issues in issue trackers, either
explicitly with an "issue" role or optionally implicitly by issue ids
like #10 in plaintext.

Currently the following issue trackers are supported:

* GitHub
* BitBucket
* Launchpad
* Google Code
* Debian BTS
* Jira

%prep
%setup
%patch1 -p1

%build
%python_build_debug

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.11-alt2.git20130117.1
- (NMU) rebuild with python3.6

* Thu Oct 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11-alt2.git20130117
- Applied fixes for sphinx-1.6.5 support.

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.git20130117
- Initial build for Sisyphus

