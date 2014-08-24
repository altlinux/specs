%define oname nltk
%define version 3.0.0
%define release alt1.b2

Summary: Python modules for Natural Language Processing (NLP)
Name: python3-module-%oname
Version: %version
Release: %release

License: Apache
Group: Development/Python3
Url: http://www.nltk.org
BuildArch: noarch

Source: %name-%version.tar
# https://github.com/nltk/nltk_contrib.git
Source1: nltk_contrib-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-numpy
BuildPreReq: python3-module-yaml
BuildPreReq: python3-module-setuptools python-tools-2to3

%description
Description: The Natural Language Toolkit (NLTK) is a Python package for
processing natural language text.  NLTK requires Python 2.4 or higher.

Keywords: NLP,CL,natural language processing,computational
linguistics,parsing,tagging,tokenizing,syntax,linguistics,language,natural
language.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Description: The Natural Language Toolkit (NLTK) is a Python package for
processing natural language text.  NLTK requires Python 2.4 or higher.

Keywords: NLP,CL,natural language processing,computational
linguistics,parsing,tagging,tokenizing,syntax,linguistics,language,natural
language.

%prep
%setup
rm -rvf nltk/yaml/
find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/nltk/
%python3_sitelibdir/*.egg-info
%doc README.* LICENSE.txt ChangeLog examples
%exclude %python3_sitelibdir/*/test
%exclude %python3_sitelibdir/*/*/*/*/test*

%files tests
%python3_sitelibdir/*/test
%python3_sitelibdir/*/*/*/*/test*

%changelog
* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.b2
- Initial build for Sisyphus

