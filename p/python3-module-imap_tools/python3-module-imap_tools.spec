%define _unpackaged_files_terminate_build 1
%define mname imap_tools

Name: python3-module-%mname
Version: 0.34.0
Release: alt1
Summary: Working with email and mailbox using IMAP protocol
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/ikvk/imap_tools
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Features:
- Parsed email message attributes
- Query builder for searching emails
- Work with emails in folders (copy, delete, flag, move, seen)
- Work with mailbox folders (list, set, get, create, exists, rename, delete, status)
- No dependencies

%package -n %name-tests
Summary: Tests for %name
Group: Development/Python3
BuildArch: noarch

%description -n %name-tests
This package contains tests for %name.

%prep
%setup

%build
%python3_build

%install
%python3_install
cp -pr tests %buildroot%python3_sitelibdir/%mname
rm -rf %buildroot%python3_sitelibdir/tests

%files
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/%mname/tests
%doc LICENSE README.rst

%files -n %name-tests
%python3_sitelibdir/%mname/tests

%changelog
* Sat Jan 09 2021 Alexander Makeenkov <amakeenk@altlinux.org> 0.34.0-alt1
- Updated to version 0.34.0

* Sat Jul 04 2020 Alexander Makeenkov <amakeenk@altlinux.org> 0.17.0-alt1
- Updated to version 0.17.0

* Wed Jun 10 2020 Alexander Makeenkov <amakeenk@altlinux.org> 0.16.0-alt1
- Updated to version 0.16.0

* Thu May 21 2020 Alexander Makeenkov <amakeenk@altlinux.org> 0.15.0-alt1
- Updated to version 0.15.0
- Don't build examples

* Sat Apr 25 2020 Alexander Makeenkov <amakeenk@altlinux.org> 0.14.2-alt1
- New version

* Mon Mar 02 2020 Alexander Makeenkov <amakeenk@altlinux.org> 0.13.1-alt1
- New version

* Sat Feb 29 2020 Alexander Makeenkov <amakeenk@altlinux.org> 0.13.0-alt1
- New version

* Tue Feb 04 2020 Alexander Makeenkov <amakeenk@altlinux.org> 0.12.0-alt1
- Updated to new version
- Moved tests and examples in separate packages

* Thu Dec 19 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.11.0-alt1
- New version

* Sun Dec 15 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.10.0-alt1
- New version

* Thu Nov 14 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.4-alt1
- New version

* Wed Oct 23 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.3-alt1
- New version

* Thu Oct 10 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.0-alt1
- New version

* Fri Aug 30 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.0-alt1
- New version

* Tue Aug 13 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.1-alt1
- New version

* Wed Jul 31 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.0-alt1
- New version

* Sun Jul 21 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.0-alt2
- Minor spec fix

* Sun Jun 23 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.0-alt1
- New version

* Sat Apr 20 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.1-alt1
- New version

* Tue Apr 09 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.5-alt1
- Initial build for ALT

