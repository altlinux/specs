%define version 2.0
%define release alt2.beta7

%setup_python_module nltk

Summary: Python modules for Natural Language Processing (NLP)
Name: python-module-nltk
Version: %version
Release: %release.1


Packager: Kirill Maslinsky <kirill@altlinux.org>
License: Apache
Group: Development/Python
Url: http://www.nltk.org
BuildRequires(pre): rpm-build-python
BuildArch: noarch

Source: %name-%version.tar
Source1: nltk_contrib-%version.tar

Patch0: alt-setup.patch

# Automatically added by buildreq on Mon Mar 02 2009
BuildRequires: elinks python-devel python-module-numpy python-module-yaml python-modules-email python-modules-encodings python-modules-logging python-modules-sqlite3 python-modules-tkinter python-modules-xml

%description
Description: The Natural Language Toolkit (NLTK) is a Python package for
processing natural language text.  NLTK requires Python 2.4 or higher.

Keywords: NLP,CL,natural language processing,computational
linguistics,parsing,tagging,tokenizing,syntax,linguistics,language,natural
language

%prep
%setup
rm -rvf nltk/yaml/
# still hope to remove copy of ElementTree later, when it won't be used by any modules
#rm -rvf nltk/etree

tar xf %SOURCE1

%patch0 -p2

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/nltk/
%python_sitelibdir/nltk_contrib/
%python_sitelibdir/*.egg-info
%doc README.txt LICENSE.txt

%changelog
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

