%define _unpackaged_files_terminate_build 1
%define oname imap_tools

Name: python3-module-%oname
Version: 0.11.0
Release: alt1
Summary: Work with IMAP protocol easy and effective
License: MIT
Group: Development/Python3
Url: https://github.com/ikvk/imap_tools
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Features:
- transparent work with letter attributes
- work with letters in directories (copy, delete, flag, move, seen)
- work with directories (list, set, get, create, exists, rename, delete, status)


%prep
%setup

%build
%python3_build

%install
%python3_install
mkdir -p %buildroot%python3_sitelibdir/%oname/tests
mkdir -p %buildroot%python3_sitelibdir/%oname/examples
install -m 0644 tests/* %buildroot%python3_sitelibdir/%oname/tests
install -m 0644 examples/* %buildroot%python3_sitelibdir/%oname/examples
rm -rf %buildroot%python3_sitelibdir/tests

%files
%python3_sitelibdir/*
%doc LICENSE README.*

%changelog
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

