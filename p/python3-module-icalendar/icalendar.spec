%define oname icalendar

Name: python3-module-%oname
Version: 4.0.3
Release: alt2

Summary: iCalendar parser/generator
License: GPLv2.1
Group: Development/Python3
Url: https://pypi.org/project/icalendar/

BuildArch: noarch

Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

%description
iCalendar is a parser/generator of iCalendar files
(RFC 2445) for use with Python.

%prep
%setup -n %oname-%version

%build
%python3_build -b build3
PYTHONPATH=../src %make -C docs html BUILDDIR=build3 SPHINXBUILD=py3_sphinx-build

%install
rm -f build && ln -sf build3 build
%python3_install

%files
%doc docs/build3/html *.rst
%_bindir/*
%python3_sitelibdir_noarch/%oname
%python3_sitelibdir_noarch/%oname-*

%changelog
* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.0.3-alt2
- Build for python2 disabled.

* Mon Apr 29 2019 Fr. Br. George <george@altlinux.ru> 4.0.3-alt1
- Autobuild version bump to 4.0.3

* Thu Mar 22 2018 Fr. Br. George <george@altlinux.ru> 4.0.1-alt1
- Autobuild version bump to 4.0.1
- Python3 module introdice

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 3.10-alt1
- Autobuild version bump to 3.10

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 3.9.1-alt1
- Autobuild version bump to 3.9.1

* Wed Apr 22 2015 Fr. Br. George <george@altlinux.ru> 3.9.0-alt1
- Autobuild version bump to 3.9.0
- Fix documentation build

* Mon Feb 02 2015 Fr. Br. George <george@altlinux.ru> 3.8.4-alt1
- Autobuild version bump to 3.8.4

* Sat Sep 27 2014 Fr. Br. George <george@altlinux.ru> 3.8.3-alt1
- Autobuild version bump to 3.8.3

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 3.8.2-alt1
- Autobuild version bump to 3.8.2

* Mon Jun 09 2014 Fr. Br. George <george@altlinux.ru> 3.7-alt1
- Autobuild version bump to 3.7

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 3.6.1-alt1
- Autobuild version bump to 3.6.1

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 3.5-alt1
- Autobuild version bump to 3.5

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 3.3-alt1
- Autobuild version bump to 3.3

* Tue Nov 08 2011 Fr. Br. George <george@altlinux.ru> 2.2-alt1
- Autobuild version bump to 2.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Fr. Br. George <george@altlinux.ru> 2.1-alt1
- Autobuild version bump to 2.1

