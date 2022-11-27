%define _unpackaged_files_terminate_build 1
%define module_name imap_tools

Name: python3-module-%module_name
Version: 1.0.0
Release: alt1
Summary: High level lib for work with email by IMAP
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/ikvk/imap_tools
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
High level lib for work with email by IMAP:
- Basic message operations: fetch, uids, numbers
- Parsed email message attributes
- Query builder for search criteria
- Actions with emails: copy, delete, flag, move, append
- Actions with folders: list, set, get, create, exists, rename, subscribe, delete, status
- IDLE commands: start, poll, stop, wait
- Exceptions on failed IMAP operations
- No external dependencies, tested

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%module_name-%version.dist-info
%doc LICENSE README.rst

%changelog
* Sat Nov 26 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.0.0-alt1
- Updated to version 1.0.0

* Thu Jun 02 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.55.0-alt1
- Updated to version 0.55.0

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

