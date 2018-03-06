Name: rpmfile2
Version: 0.2
Release: alt2

Summary: List files and their magic types in .rpm packages
License: MIT
Group: File tools

URL: https://github.com/svpv/rpmfile2
Source: %name-%version.tar

# Automatically added by buildreq on Wed Mar 07 2018
BuildRequires: libmagic-devel librpmcpio-devel

%description
The rpmfile2 program lists filenames, along with their magic types,
as determined by file(1), in .rpm packages.  This is a reimplementation
of the original rpmfile(1) script written many years ago.

%prep
%setup
%ifarch %e2k
sed -i '/^LTO/d' Makefile
%endif

%build
make

%install
install -pD -m755 rpmfile2 %buildroot%_bindir/rpmfile2

%files
%doc README.md
%_bindir/rpmfile2

%changelog
* Sat Apr 10 2021 Michael Shigorin <mike@altlinux.org> 0.2-alt2
- E2K: avoid lcc-unsupported option (done otherwise there)

* Wed Mar 07 2018 Alexey Tourbin <at@altlinux.ru> 0.2-alt1
- first beta release
- identifies hardlinks properly
