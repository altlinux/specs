Name:           python-module-tweepy
Version:        1.7.1
Release:        alt1.1
Summary:        Twitter library for python

License:        MIT
Group:          Development/Python
URL:            http://pypi.python.org/pypi/tweepy/

Packager:       Andrey Cherepanov <cas@altlinux.org>

Source0:        tweepy-%{version}.tar.gz
Source1:        MIT_LICENSE

BuildArch:      noarch
BuildRequires(pre): rpm-build-python
BuildRequires:  python-devel
BuildRequires:  python-module-distribute
BuildRequires:  python-module-simplejson
Provides:	tweepy = %version
Requires:       python-module-simplejson

%description
A library for accessing the Twitter.com API. Supports OAuth, covers the
entire API, and streaming API.

%prep
%setup -q -n tweepy-%version
cp -p %SOURCE1 ./LICENSE

%build
%python_build

%install
%python_install

%files
%doc README LICENSE
%dir %python_sitelibdir/tweepy 
%python_sitelibdir/tweepy
%python_sitelibdir/tweepy-*.egg-info

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.1-alt1.1
- Rebuild with Python-2.7

* Wed Aug 10 2011 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- Initial build in Sisyphus

* Mon Feb 21 2011 rtnpro <rtnpro@gmail.com> 1.7.1-3
- Added LICENSE, removed unnecessary macros

* Sat Feb 05 2011 rtnpro <rtnpro@gmail.com> 1.7.1-2
- Some fixes in the SPEC file

* Fri Feb 04 2011 rtnpro <rtnpro@gmail.com> 1.7.1-1
- Intial RPM package for tweepy
