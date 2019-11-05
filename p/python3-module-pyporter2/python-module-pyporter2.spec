%define oname pyporter2

Name: python3-module-%oname
Version: 0.9.9
Release: alt2

Summary: Implementation of the Porter2 (english) stemming algorithm
License: MIT/X11
Group: Development/Python3
Url: http://www.dirolf.com/project/pyporter2
# https://github.com/mdirolf/pyporter2.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


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
install -pD Stemmer.py %buildroot%python3_sitelibdir/Stemmer.py
install -pD voc.txt %buildroot%_datadir/%name/voc.txt
install -pD stemmedvoc.txt %buildroot%_datadir/%name/stemmedvoc.txt

%files
%doc README
%python3_sitelibdir/*
%_datadir/%name/*.txt


%changelog
* Tue Nov 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.9-alt2
- disable python2

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.9-alt1.git81d39.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.9-alt1.git81d39.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.git81d39
- New snapshot
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.0-alt1.git02b0c.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.0-alt1.git02b0c.1
- Rebuilt with python 2.6

* Mon Feb 02 2009 Denis Klimov <zver@altlinux.org> 0.0.0-alt1.git02b0c
- Initial build for ALT Linux


