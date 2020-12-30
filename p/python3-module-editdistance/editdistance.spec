Name:       python3-module-editdistance
Version:    0.5.3
Release:    alt1
Group:      Development/Python3
License:    MIT
URL:        https://github.com/roy-ht/editdistance
Summary:    Fast implementation of the edit distance (Levenshtein distance).
Source:     editdistance-%version.tar.gz

# Automatically added by buildreq on Wed Dec 30 2020
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel libstdc++-devel python2-base python3 python3-base python3-dev python3-module-paste python3-module-pkg_resources python3-module-setuptools sh4
BuildRequires: gcc-c++ python3-module-setuptools
#_scm python3-module-sphinxcontrib

%description
Fast implementation of the edit distance (Levenshtein distance).

This library simply implements Levenshtein distance with C++ and Cython.

The algorithm used in this library is proposed by Heikki Hyyro,
"Explaining and extending the bit-parallel approximate string matching
algorithm of Myers", (2001).

%prep
%setup -n editdistance-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Wed Dec 30 2020 Fr. Br. George <george@altlinux.ru> 0.5.3-alt1
- Initial build forALT

