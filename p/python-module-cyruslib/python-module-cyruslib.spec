%define module_name cyruslib

Name: python-module-%module_name
Version: 0.8.5
Release: alt1

Summary: manage cyrus-imap server from python
License: GPL2
Group: Development/Python
Url: http://python-cyrus.sourceforge.net

Source: python-module-%module_name-%version.tar

BuildArch: noarch

BuildRequires: python-module-setuptools

%setup_python_module %module_name

%description
Cyruslib is wrapped interface for imaplib.py, it adds support for cyrus
specific commands.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc AUTHORS README Changelog
%python_sitelibdir/cyruslib\.*
%python_sitelibdir/sievelib\.*
%python_sitelibdir/*.egg-info


%changelog
* Wed Jun 20 2012 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8.5-alt1
- Initial build.

