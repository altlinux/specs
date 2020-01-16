%define module_name cyruslib

Name: python3-module-%module_name
Version: 0.8.5
Release: alt2

Summary: manage cyrus-imap server from python
License: GPL2
Group: Development/Python3
Url: http://python-cyrus.sourceforge.net
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
Cyruslib is wrapped interface for imaplib.py, it adds support for cyrus
specific commands.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS README Changelog
%python3_sitelibdir/cyruslib\.*
%python3_sitelibdir/sievelib\.*
%python3_sitelibdir/__pycache__/
%python3_sitelibdir/*.egg-info


%changelog
* Thu Jan 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8.5-alt2
- porting on python3

* Wed Jun 20 2012 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8.5-alt1
- Initial build.

