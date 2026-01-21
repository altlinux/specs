Name:     stegopy
Version:  0.0.4.0.14.823a
Release:  alt1

Summary:  Steganography with Python3 LSB algorithm
License:  GPLv3
Group:    Development/Python3
Url:      https://github.com/securityhigh/StegoPy
VCS:      https://github.com/securityhigh/StegoPy

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-colorama
BuildRequires: python3-module-cryptography

BuildArch: noarch

%description
StegoPy - Steganography with Python3 LSB algorithm
with some improvements.
The cryptography algorithm can choose the balance itself.

%prep
%setup -q

%install
install -pDm0755 stegopy.py %buildroot%_usr/bin/stegopy

%files
%doc *.md LICENSE
%_bindir/stegopy

%changelog
* Mon Dec 02 2024 Danila Skachedubov <skachedubov@altlinux.org> 0.0.4.0.14.823a-alt1
- Initial build for ALT.
