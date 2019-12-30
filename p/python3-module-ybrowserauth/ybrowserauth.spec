%define oname ybrowserauth

Name: python3-module-%oname
Version: 1.2
Release: alt2

Summary: A class for accessing Yahoo! Mail and Photos using BBauth
License: BSD
Group: Development/Python3
Url: https://code.google.com/p/django-hotclub/
BuildArch: noarch

# http://django-hotclub.googlecode.com/svn/trunk/external_libs/ybrowserauth/
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
Lets you add Yahoo! Browser-Based authentication to your applications.

%prep
%setup

sed -i 's|import md5|from hashlib import md5|' ybrowserauth.py

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/*


%changelog
* Mon Dec 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2-alt2
- porting on python3

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20080919
- Initial build for Sisyphus

