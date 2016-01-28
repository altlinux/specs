%define version 3.0.1
%define release alt1
%define oname nltk

%def_with python3

%setup_python_module %oname

Name: python-module-%oname
Summary: Python modules for Natural Language Processing (NLP)
Group: Development/Python
Version: %version
Release: %release.1
License: Apache
Url: http://www.nltk.org
BuildRequires(pre): rpm-build-python
BuildArch: noarch

Source: %name-%version.tar
# https://github.com/nltk/nltk_contrib.git
Source1: nltk_contrib-%version.tar

Patch0: alt-setup.patch

# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: fontconfig python-base python-devel python-module-numpy python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-numpy
BuildRequires: python-module-numpy-testing python-module-setuptools python-module-yaml python-modules-json python-modules-tkinter python3-module-numpy-testing python3-module-setuptools python3-module-yaml rpm-build-python3 time

#BuildPreReq: python-module-setuptools python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-numpy
#BuildPreReq: python3-module-yaml
#BuildPreReq: python3-module-setuptools python-tools-2to3
%endif

%add_python_req_skip MinEditDist Unitran Utils snow

%description
Description: The Natural Language Toolkit (NLTK) is a Python package for
processing natural language text.  NLTK requires Python 2.4 or higher.

Keywords: NLP,CL,natural language processing,computational
linguistics,parsing,tagging,tokenizing,syntax,linguistics,language,natural
language

%package -n python3-module-%oname
Summary: Python modules for Natural Language Processing (NLP)
Group: Development/Python3
%add_python3_req_skip MinEditDist Unitran UserDict Utils md5 qt qtcanvas
%add_python3_req_skip qttable snow

%description -n python3-module-%oname
Description: The Natural Language Toolkit (NLTK) is a Python package for
processing natural language text.  NLTK requires Python 2.4 or higher.

Keywords: NLP,CL,natural language processing,computational
linguistics,parsing,tagging,tokenizing,syntax,linguistics,language,natural
language

%package tests
Summary: Tests for NLTK
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip featurechart treeview align_util distance_measures

%description tests
Description: The Natural Language Toolkit (NLTK) is a Python package for
processing natural language text.  NLTK requires Python 2.4 or higher.

Keywords: NLP,CL,natural language processing,computational
linguistics,parsing,tagging,tokenizing,syntax,linguistics,language,natural
language

This package contains teets for NLTK.

%package -n python3-module-%oname-tests
Summary: Tests for NLTK
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip featurechart treeview

%description -n python3-module-%oname-tests
Description: The Natural Language Toolkit (NLTK) is a Python package for
processing natural language text.  NLTK requires Python 2.4 or higher.

Keywords: NLP,CL,natural language processing,computational
linguistics,parsing,tagging,tokenizing,syntax,linguistics,language,natural
language

This package contains teets for NLTK.

%prep
%setup
rm -rvf nltk/yaml/
# still hope to remove copy of ElementTree later, when it won't be used by any modules
#rm -rvf nltk/etree

tar xf %SOURCE1

#patch0 -p2

%if_with python3
cp -fR . ../python3
sed -i "s|u'||" \
	../python3/nltk_contrib/nltk_contrib/scripttranscriber/Unitran/Tables.py
#find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
for i in $(find ../python3 -type f -name '*.py' |grep -v 'Tables\.py')
do
	2to3 -w -n $i
done
%endif

%build
%python_build
export PYTHONPATH=$PWD
pushd nltk_contrib
%python_build
popd

%if_with python3
pushd ../python3
%python3_build
export PYTHONPATH=$PWD
pushd nltk_contrib
%python3_build
popd
popd
%endif

%install
%python_install
export PYTHONPATH=$PWD
pushd nltk_contrib
%python_install
popd

%if_with python3
pushd ../python3
%python3_install
export PYTHONPATH=$PWD
pushd nltk_contrib
%python3_install
popd
popd
%endif

echo 'from Tkinter import *' >%buildroot%python_sitelibdir/tkinter.py
mv nltk_contrib/doc nltk_contrib.doc

%files
%python_sitelibdir/tkinter.py*
%python_sitelibdir/nltk/
%python_sitelibdir/nltk_contrib/
%python_sitelibdir/*.egg-info
%doc README.txt LICENSE.txt nltk_contrib.doc
%exclude %python_sitelibdir/*/test
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/test*

%files tests
%python_sitelibdir/*/test
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/nltk
%python3_sitelibdir/nltk_contrib
%python3_sitelibdir/*.egg-info
%doc README.txt LICENSE.txt nltk_contrib.doc
%exclude %python3_sitelibdir/*/test
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%python3_sitelibdir/*/*/*/*/*/test*
%endif

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 3.0.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1
- Version 3.0.1

* Thu May 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt3
- Moved tests into tests subpackage

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt2
- Fixed build

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1
- Version 2.0.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt2.beta7.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.beta7
- Rebuilt with python 2.6

* Thu Nov 12 2009 Kirill Maslinsky <kirill@altlinux.org> 2.0-alt1.beta7
- 2.0 beta7
- nltk and nltk_contrib packaged together

* Tue Sep 15 2009 Kirill Maslinsky <kirill@altlinux.org> 2.0-alt1.beta5
- 2.0 beta5
- nltk and nltk_contrib now are separate packages
- correct License tag: Apache license
- do not build java interface
- spec cleanup (use proper macros for python build and install)

* Sun May 24 2009 Kirill Maslinsky <kirill@altlinux.org> 0.9.9-alt1
- 0.9.9

* Mon Mar 02 2009 Kirill Maslinsky <kirill@altlinux.org> 0.9.8-alt1.1
- fixed packaging
    - build as noarch
    - fix pythonic pseudo-unmets
    - do not package copy of PyYAML
    - use description from PKG-INFO

* Mon Mar 02 2009 Kirill Maslinsky <kirill@altlinux.org> 0.9.8-alt1
- Initial build for Sisyphus

