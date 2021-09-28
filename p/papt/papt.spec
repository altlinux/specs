Summary: Wrapper for apt-rpm utilities

Name: papt
Version: 0.1.0
Release: alt2

License: GPL-2.0-or-later
Group: System/Configuration/Packaging
URL: https://github.com/legionus/papt

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires: help2man
BuildRequires: perl-AptPkg
BuildRequires: perl-CryptX
BuildRequires: perl-JSON
BuildRequires: perl-Number-Format
BuildRequires: perl-ph

Requires: curl
Requires: apt

%description
This utility allows to simultaneously download the packages required for
updating the system. This utility is a wrapper for apt-get, apt-cache and
apt-mark.

%prep
%setup -q

%build
make

%install
install -D -m755 papt   %buildroot%_bindir/papt
install -D -m644 papt.1 %buildroot%_man1dir/papt.1

%files
%_bindir/papt
%_man1dir/papt.1*

%changelog
* Tue Sep 28 2021 Alexey Gladkov <legion@altlinux.ru> 0.1.0-alt2
- Fix requires.

* Tue Sep 28 2021 Alexey Gladkov <legion@altlinux.ru> 0.1.0-alt1
- First build.

