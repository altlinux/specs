%define oname sshpt

Name:       %oname
Version:    1.3.15
Release:    alt1

Summary:    SSH Power Tool - Run commands and copy files to multiple servers simultaneously WITHOUT pre-shared keys
License:    %gpl3plus
Group:      Networking/Remote access
Url:        http://code.google.com/p/sshpt
BuildArch:  noarch

Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-build-licenses

Provides: python3-module-%oname = %version-%release
Requires: python3-module-paramiko


%description
The SSH Power Tool (sshpt) enables you to execute commands and upload
files to many servers simultaneously via SSH without using pre-shared keys.
Uploaded files and commands can be executed directly or via sudo.
Connection and command execution results are output in standard CSV format
for easy importing into spreadsheets, databases, or data mining applications.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/%name
%python3_sitelibdir/*


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3.15-alt1
- Version updated to 1.3.15
- porting on python3.

* Tue Oct 25 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.11-alt1
- 1.3.11

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt1.1
- Rebuild with Python-2.7

* Thu Dec 02 2010 Aleksey Avdeev <solo@altlinux.ru> 1.1.3-alt1
- initial build for ALT Linux Sisyphus
