%define oname tweepy

Name:       python3-module-%oname
Version:    3.8.0
Release:    alt2

Summary:    Twitter library for python

License:    MIT
Group:      Development/Python3
URL:        https://github.com/tweepy/tweepy
Packager:   Andrey Cherepanov <cas@altlinux.org>
BuildArch:  noarch

Source0:    tweepy-%version.tar

BuildRequires(pre): rpm-build-python3
Provides: tweepy = %version


%description
A library for accessing the Twitter.com API. Supports OAuth, covers the
entire API, and streaming API.

%prep
%setup -q -n tweepy-%version

%build
%python3_build

%install
%python3_install

rm -rf %buildroot%python3_sitelibdir/examples

%files
%doc *.md
%python3_sitelibdir/tweepy
%python3_sitelibdir/tweepy-*.egg-info


%changelog
* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.8.0-alt2
- porting on python3

* Mon Jul 15 2019 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Mon Apr 08 2019 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version.

* Fri Jun 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.6.0-alt2
- Fixed build.

* Fri May 18 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version.

* Thu May 26 2016 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version
- Add python-module-pip to build requirements

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
