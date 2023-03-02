%define  oname eradicate

Name:    python3-module-%oname
Version: 2.2.0
Release: alt1

Summary: Removes commented-out code from Python files

License: MIT
Group:   Development/Python3
URL:     https://github.com/myint/eradicate

Packager:  Grigory Ustinov <grenka@altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-python3

Conflicts: python-module-%oname

%description
With modern revision control available, there is no reason to save
commented-out code to your repository. "eradicate" helps cleans up
existing junk comments. It does this by detecting block comments that
contain valid Python syntax that are likely to be commented out code.
(It avoids false positives like the sentence "this is not good",
which is valid Python syntax, but is probably not code.)

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%_bindir/eradicate
%python3_sitelibdir/*

%changelog
* Thu Mar 02 2023 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt1
- Automatically updated to 2.2.0.

* Mon May 23 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1
- Automatically updated to 2.1.0.

* Thu Jan 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2
- Porting on Python3.

* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
