Summary: Wrapper for apt-rpm utilities

Name: papt
Version: 0.5.1
Release: alt1

License: GPL-2.0-or-later
Group: System/Configuration/Packaging
URL: https://github.com/legionus/papt

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires: help2man
BuildRequires: perl(AptPkg/Config.pm)
BuildRequires: perl(Crypt/Digest.pm)
BuildRequires: perl(Crypt/Digest/BLAKE2b_512.pm)
BuildRequires: perl(Crypt/Digest/MD5.pm)
BuildRequires: perl(Crypt/Digest/SHA1.pm)
BuildRequires: perl(Crypt/Digest/SHA256.pm)
BuildRequires: perl(Crypt/Digest/SHA512.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Errno.pm)
BuildRequires: perl(Fcntl.pm)
BuildRequires: perl(Getopt/Long.pm)
BuildRequires: perl(Number/Format.pm)
BuildRequires: perl(RPM2.pm)
BuildRequires: perl(Term/ANSIColor.pm)
BuildRequires: perl(Text/Wrap.pm)
BuildRequires: perl(WWW/Curl/Easy.pm)
BuildRequires: perl(WWW/Curl/Multi.pm)
BuildRequires: perl(sys/ioctl.ph)

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

install -D -m755 papt-query   %buildroot%_bindir/papt-query
install -D -m644 papt-query.1 %buildroot%_man1dir/papt-query.1

%files
%_bindir/papt*
%_man1dir/papt*.1*

%changelog
* Tue Apr 04 2023 Alexey Gladkov <legion@altlinux.ru> 0.5.1-alt1
- Use curl utility by default.

* Tue Mar 22 2022 Alexey Gladkov <legion@altlinux.ru> 0.5.0-alt1
- papt:
  + Assume the answer is no if stdin is not available.
  + Add colors for different lists.

* Mon Nov 01 2021 Alexey Gladkov <legion@altlinux.ru> 0.4.0-alt1
- Fix regexp for print-uris.
- Add some debug information.
- Add BLAKE2b support.
- Show the number of received and remaining packages.

* Fri Oct 01 2021 Alexey Gladkov <legion@altlinux.ru> 0.3.0-alt1
- Add utility to search packages in the apt-cache.

* Thu Sep 30 2021 Alexey Gladkov <legion@altlinux.ru> 0.2.0-alt1
- Use WWW::Curl to download packages.

* Tue Sep 28 2021 Alexey Gladkov <legion@altlinux.ru> 0.1.0-alt2
- Fix requires.

* Tue Sep 28 2021 Alexey Gladkov <legion@altlinux.ru> 0.1.0-alt1
- First build.

