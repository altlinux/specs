%define _unpackaged_files_terminate_build 1

Name: mackup
Version: 0.8.27
Release: alt1
Summary: Keep your application settings in sync
License: GNU GPL v3.0
Group: Other
Url: https://github.com/lra/mackup
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel
BuildRequires:  python3-module-setuptools

%description
What does it do:
- Back ups your application settings in a safe directory (e.g. Dropbox)
- Syncs your application settings among all your workstations
- Restores your configuration on any fresh install in one command line
By only tracking pure configuration files, it keeps the crap out of your
freshly new installed workstation (no cache, temporary and locally specificfiles
are transfered). Mackup makes setting up the environment easy and simple, saving
time for your family, great ideas, and all the cool stuff you like.


%prep
%setup

%build
%python3_build

%install
%python3_install
sed -i "/MACKUP_CONFIG_FILE/s/.mackup.cfg/\/usr\/lib\/python3\/site-packages\/mackup\/applications\/mackup.cfg/" %buildroot/%python3_sitelibdir/%name/constants.py

%files
%_bindir/%name
%python3_sitelibdir/%{name}*
%config(noreplace) %python3_sitelibdir/%name/applications/mackup.cfg

%changelog
* Mon Aug 26 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.27-alt1
- New version

* Wed Jul 31 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.26-alt1
- New version

* Sun Jul 21 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.25-alt3
- Minor spec fix

* Sun Jul 14 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.25-alt2
- Fixed replacing of mackup.cfg file

* Sun Jul 14 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.25-alt1
- New version

* Wed May 22 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.24-alt1
- New version

* Mon Mar 04 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.22-alt1
- Initial build for ALT

