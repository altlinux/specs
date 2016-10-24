
%define modulename sshpt

Name: %modulename
Version: 1.3.11
Release: alt1

%setup_python_module %modulename

Summary: SSH Power Tool - Run commands and copy files to multiple servers simultaneously WITHOUT pre-shared keys
License: %gpl3plus
Group: Networking/Remote access

Url: http://code.google.com/p/sshpt
BuildArch: noarch

Source: %name-%version.tar

Requires: python-module-paramiko >= 1.16.0
Provides: python-module-%modulename = %version-%release

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
BuildPreReq: python-module-setuptools

%description
The SSH Power Tool (sshpt) enables you to execute commands and upload
files to many servers simultaneously via SSH without using pre-shared keys.
Uploaded files and commands can be executed directly or via sudo.
Connection and command execution results are output in standard CSV format
for easy importing into spreadsheets, databases, or data mining applications.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/%name
%doc README.txt
%python_sitelibdir/*


%changelog
* Tue Oct 25 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.11-alt1
- 1.3.11

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt1.1
- Rebuild with Python-2.7

* Thu Dec 02 2010 Aleksey Avdeev <solo@altlinux.ru> 1.1.3-alt1
- initial build for ALT Linux Sisyphus
