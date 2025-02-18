%define src_dir %_usrsrc/%name-%version

Name: universal-pidff
Version: 0.1.0
Release: alt1

Summary: Universal Force Feedback driver for Linux

License: GPL-2.0
Group: System/Configuration/Hardware
Url: https://github.com/JacKeTUs/universal-pidff

Source: %name-%version.tar
Source1: %name.sh

Requires: dkms-%name = %EVR

BuildArch: noarch

%description
Linux PIDFF driver with useful patches for initialization of FFB devices.
Primarily targeting Direct Drive wheelbases.

Usage:
%name <install | force-install | uninstall>.

%package -n dkms-%name
Summary: %name DKMS package
Group: System/Configuration/Hardware
Requires: dkms
BuildArch: noarch

%description -n dkms-%name
%summary

%prep
%setup

%__subst "s/version=/version=%version/" %SOURCE1

%build

%install
install -Dm 755 %SOURCE1 %buildroot%_sbindir/%name

mkdir -p %buildroot%_datadir/%name/
mv -v effect-test.ffb %buildroot%_datadir/%name/

mkdir -p %buildroot%src_dir
cp -v {*.h,*.c} %buildroot%src_dir
cp -v dkms.conf %buildroot%src_dir
cp -v Makefile %buildroot%src_dir
cp -v Kbuild %buildroot%src_dir

%files
%doc LICENSE *.md docs/*.md
%_sbindir/%name
%_datadir/%name/

%files -n dkms-%name
%src_dir/

%changelog
* Tue Feb 18 2025 Mikhail Tergoev <fidel@altlinux.org> 0.1.0-alt1
- Initial build for ALT Sisyphus
