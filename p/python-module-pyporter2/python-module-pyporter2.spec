Name: python-module-pyporter2
Version: 0.0.0
Release: alt1.git02b0c.1.1

Summary: Implementation of the Porter2 (english) stemming algorithm

License: MIT/X11
Group: Development/Python
BuildArch: noarch
Url: http://www.dirolf.com/project/pyporter2
Packager: Denis Klimov <zver@altlinux.org>

Source: %name-%version.tar

%description
This is an implementation of the Porter2 (english) stemming algorithm
in Python. It was born out of some academic work I did on clustering
algorithms in the spring of 2008. The Porter Stemming Algorithm was
first published in this 1979 paper - it is now one of the most widely
known and used stemming algorithms. An implementation of the Porter
stemmer already existed in Python, but not of the updated Porter2
stemmer. I decided to implement a Python version of Porter2 as an
exercise.

%prep
%setup -n %name-%version

%install
install -pD Stemmer.py %buildroot%python_sitelibdir/Stemmer.py
install -pD voc.txt %buildroot%_datadir/%name/voc.txt
install -pD stemmedvoc.txt %buildroot%_datadir/%name/stemmedvoc.txt

%files
%doc README
%python_sitelibdir/Stemmer.py*
%_datadir/%name/*.txt

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.0-alt1.git02b0c.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.0-alt1.git02b0c.1
- Rebuilt with python 2.6

* Mon Feb 02 2009 Denis Klimov <zver@altlinux.org> 0.0.0-alt1.git02b0c
- Initial build for ALT Linux


