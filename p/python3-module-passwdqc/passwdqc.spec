Name:       python3-module-passwdqc
Version:    0.0.1
Release:    alt1
License:    BSD
URL:        https://git.sr.ht/~frbrgeorge/PasswdqcPython
Source:     passwdqc-%version.tar.gz
Group:      Development/Python3
Summary:    PasswdQC python wrapper
BuildRequires:  gcc libpasswdqc-devel

%description
PasswdQC is a simple password strength checking PAM module, and this
Python module provides high-level bindings for libpasswdqc.

%prep
%setup -n passwdqc-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*passwdqc*

%changelog
* Sat May 15 2021 Fr. Br. George <george@altlinux.ru> 0.0.1-alt1
- Initial build for ALT
