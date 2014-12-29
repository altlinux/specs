Name: ipsumdump
Version: 1.84
Release: alt2
Packager: Andriy Stepanov <stanv@altlinux.ru>
Summary: Summarizes TCP/IP dump files into a self-describing ASCII format easily readable by humans and programs
License: %bsd
Url: http://www.read.seas.harvard.edu/~kohler/ipsumdump/
Source0: %name-%version.tar
Group: Networking/Other
BuildRequires: rpm-build-licenses
BuildRequires: perl-podlators
BuildRequires: gcc-c++

%description
Ipsumdump reads IP packets from tcpdump(1) files, or network interfaces,
and summarizes their contents in an ASCII file.
Ipsumdump can read packets from network interfaces, from tcpdump files, and
from existing ipsumdump files.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/ipsumdump
%_bindir/ipaggcreate
%_bindir/ipaggmanip
%_man1dir/ipsumdump.1.bz2
%_man1dir/ipaggcreate.1.bz2
%_man1dir/ipaggmanip.1.gz

%changelog
* Mon Dec 29 2014 Andriy Stepanov <stanv@altlinux.ru> 1.84-alt2
- Update BuildRequires

* Mon Dec 29 2014 Andriy Stepanov <stanv@altlinux.ru> 1.84-alt1
- ALTLinux build
