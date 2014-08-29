%define rname sphinxcontrib
%define oname %rname-issuetracker
Name: python-module-%oname
Version: 0.11
Release: alt1.git20130117
Summary: Sphinx integration with different issuetrackers
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-issuetracker
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lunaryorn/sphinxcontrib-issuetracker.git
Source: %name-%version.tar
BuildArch: noarch

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

%build
%python_build_debug

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.git20130117
- Initial build for Sisyphus

