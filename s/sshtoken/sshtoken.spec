Name:           sshtoken
Version:        0.1
Release:        alt1
License:        MIT
Source:         %name-%version.tar.gz
URL:            https://git.sr.ht/~frbrgeorge/sshtoken
Summary:        Generate and apply secure token by signing an object with ssh
Group:          Text tools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: /usr/bin/rst2man
BuildArch: noarch

%description
Generate and apply secure token by signing an object with ssh-keygen.

%package -n python3-module-%name
Group:          Development/Python3
Summary:        Supplemental python module for %name

%description -n python3-module-%name
%summary

%package -n git-credential-ssh
Group:          Development/Other
Summary:        GIT addon to encrypt credentials via SSH

%description -n git-credential-ssh
%summary

%prep
%setup

%build
%pyproject_build
rst2man README.rst > %name.1

%install
%pyproject_install
install git-credential-ssh -D %buildroot%_bindir/git-credential-ssh
install git-credential-ssh.1 -D %buildroot%_man1dir/git-credential-ssh.1
install %name.1 -D %buildroot%_man1dir/%name.1

%files
%doc *.md *.rst
%_bindir/%name
%_man1dir/%{name}*

%files -n python3-module-%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}

%files -n git-credential-ssh
%_bindir/git-credential-ssh
%_man1dir/git-credential-ssh*

%changelog
* Sun Aug 17 2025 Fr. Br. George <george@altlinux.org> 0.1-alt1
- Initial build for ALT
