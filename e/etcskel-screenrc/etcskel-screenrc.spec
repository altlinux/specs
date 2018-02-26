%define skeldir %_sysconfdir/skel

Name: etcskel-screenrc
Version: 20100420
Release: alt1
BuildArch: noarch
BuildRequires: etcskel

Summary: default GNU screen(1) configuration for new users
Group: System/Configuration/Other
License: GPL

Source: %name.tar.gz

%description
This package contains initial content of newly created 
home directories. This content will be copied into 
users private files on new account creation.

%prep
%setup -q -n %name

%build

%install
%__install -d %buildroot%skeldir
cp -r . %buildroot%skeldir/
CPWD=`pwd`
cd %buildroot
find .%skeldir -name .\* | sed 's,^\.,%%config ,' > "$CPWD/etcskel.files"

%files -f etcskel.files

%changelog
* Tue Apr 20 2010 Mykola Grechukh <gns@altlinux.ru> 20100420-alt1
- first build
