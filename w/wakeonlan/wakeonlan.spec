Name:		wakeonlan
Version:	0.42
Release:	alt1

Summary:	A Perl script to wake up computers through Magic Packets

Group:		Networking/Other
License:	Artistic
URL:		http://github.com/jpoliv/wakeonlan/

BuildArch:	noarch

Source:		%name-%version.tar
# git://git.altlinux.org/gears/w/wakeonlan.git
Patch:		%name-%version-%release.patch

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Pod/Man.pm)

%ifdef __BTE
%def_without test
%endif

%description
With this package you can remotely wake up and power on machines which have
motherboards or network cards that support 'Wake-on-Lan' packets.

The tool allows you to wake up a single machine, or a group of machines.

You need the MAC addresses of machines to construct the WOL packets, but,
in contrast to 'etherwake', you do not need root privileges to use the
program itself as UDP packets are used.

%prep
%setup
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%check
make test

%files
%doc Changes README.md examples/
%_bindir/*
%_man1dir/*.1*


%changelog
* Sun Dec 04 2022 Arseny Maslennikov <arseny@altlinux.org> 0.42-alt1
- 0.41.0.19.git41b636c-alt1 -> 0.42.

* Thu Aug 31 2017 Arseny Maslennikov <arseny@altlinux.org> 0.41.0.19.git41b636c-alt1
- Initial build for ALT Sisyphus
