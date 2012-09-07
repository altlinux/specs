Summary: Tools for SSM (source-specific multicast) testing
Name: ssmping
Version: 0.9.1
Release: alt1
License: BSD-like
Group: Networking/Other
Packager: Evgenii Terechkov <evg@altlinux.org>
Source0: http://www.venaas.no/multicast/%name/%name-%version.tar.gz
Patch0: %name-0.9-build.patch
Patch1: %name-0.9-install.patch
Patch2: 02-link-manpages.diff
Patch3: %name-0.9-alt-norestrict.patch
Url: http://www.venaas.no/multicast/ssmping/

%description
Ssmping is a tool for checking whether one can receive SSM from a
given host. If a host runs ssmpingd, users on other hosts can use
the ssmping client tool to test whether they can receive SSM from
the host. Another tool called asmping is provided to check whether
can receive ASM. Finally, there is also a tool called mcfirst to
check whether one can receive any given multicast session.

%prep
%setup
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make %{?_smp_mflags} CFLAGS="%optflags"

%install
mkdir -p %buildroot%prefix
make DESTDIR=%buildroot PREFIX=%prefix install

%files
%_bindir/asmping
%_bindir/mcfirst
%_bindir/ssmping
%_sbindir/ssmpingd
%_man1dir/asmping.1*
%_man1dir/mcfirst.1*
%_man1dir/ssmping*.1*
%doc README

%changelog
* Sat Sep  8 2012 Terechkov Evgenii <evg@altlinux.org> 0.9.1-alt1
- Initial build for ALT Linux Sisyphus
