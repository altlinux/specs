%define oname docker

Name: python3-module-%oname
Version: 6.0.1
Release: alt1

Summary: Python client for Docker.

License: %asl
Group: Development/Python3
Url: https://github.com/docker/docker-py

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute python3-module-pip
BuildRequires: python3-module-setuptools python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%description
An API client for docker written in Python

%prep
%setup -n %oname-%version

%build
%pyproject_build

%install
%pyproject_install

%filter_from_requires /python3[(]six.moves[)]/d

%files
%doc LICENSE README.md
# Exclude Windows specific stuff
%exclude %python3_sitelibdir/%oname/transport/npipesocket.py
%exclude %python3_sitelibdir/%oname/transport/npipeconn.py
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-*.dist-info

%changelog
* Tue Nov 29 2022 Vladimir Didenko <cow@altlinux.ru> 6.0.1-alt1
- 6.0.1

* Mon Sep 5 2022 Vladimir Didenko <cow@altlinux.ru> 6.0.0-alt1
- 6.0.0

* Mon Dec 6 2021 Vladimir Didenko <cow@altlinux.ru> 5.0.3-alt1
- 5.0.3

* Tue Sep 28 2021 Vladimir Didenko <cow@altlinux.ru> 5.0.2-alt1
- 5.0.2

* Mon Apr 12 2021 Vladimir Didenko <cow@altlinux.ru> 5.0.0-alt1
- 5.0.0

* Thu Mar 11 2021 Vladimir Didenko <cow@altlinux.ru> 4.4.4-alt1
- 4.4.4

* Fri Dec 4 2020 Vladimir Didenko <cow@altlinux.ru> 4.4.0-alt1
- 4.4.0

* Wed Sep 9 2020 Vladimir Didenko <cow@altlinux.ru> 4.3.1-alt1
- 4.3.1
- Build Python3 version as separate package

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.ru> 4.2.2-alt1
- 4.2.2

* Tue Jun 23 2020 Vladimir Didenko <cow@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Wed Mar 11 2020 Vladimir Didenko <cow@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Thu Oct 17 2019 Vladimir Didenko <cow@altlinux.ru> 4.1.0-alt1
- 4.1.0

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Wed Apr 10 2019 Vladimir Didenko <cow@altlinux.ru> 3.7.2-alt1
- 3.7.2

* Tue Jan 29 2019 Vladimir Didenko <cow@altlinux.ru> 3.7.0-alt1
- 3.7.0

* Thu Nov 22 2018 Vladimir Didenko <cow@altlinux.ru> 3.5.1-alt1
- 3.5.1

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.ru> 3.4.1-alt1
- 3.4.1

* Thu May 10 2018 Vladimir Didenko <cow@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Thu Mar 22 2018 Vladimir Didenko <cow@altlinux.ru> 3.1.4-alt1
- 3.1.4

* Wed Jan 17 2018 Vladimir Didenko <cow@altlinux.ru> 2.7.0-alt1
- 2.7.0

* Wed Jul 5 2017 Vladimir Didenko <cow@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Fri Apr 7 2017 Vladimir Didenko <cow@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Mon Mar 6 2017 Vladimir Didenko <cow@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Wed Jan 25 2017 Vladimir Didenko <cow@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Fri Dec 16 2016 Vladimir Didenko <cow@altlinux.ru> 1.10.6-alt1
- 1.10.6

* Wed Oct 12 2016 Vladimir Didenko <cow@altlinux.ru> 1.10.3-alt1
- 1.10.3

* Wed Aug 3 2016 Vladimir Didenko <cow@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Fri May 6 2016 Vladimir Didenko <cow@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Fri Mar 11 2016 Vladimir Didenko <cow@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Mon Nov 16 2015 Vladimir Didenko <cow@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Mon Sep 14 2015 Vladimir Didenko <cow@altlinux.ru> 1.4.0-alt1
- 1.4.0
