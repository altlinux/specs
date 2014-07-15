Name:		bugsx
Version:	1.08
Source:		ftp://ftp.x.org/contrib/applications/bugsx108.tgz
Release:	alt1
Summary:	Program to evolve biomorphs using genetic algorithms
Group:		Games/Educational
License:	distributable

# Automatically added by buildreq on Tue Jul 15 2014
# optimized out: libX11-devel libcloog-isl4 xorg-xproto-devel
BuildRequires: gccmakedep imake libXext-devel xorg-cf-files

%description
BugsX is a program which draws biomorphs based on parametric plots of
Fourier sine and cosine series and let's you play with them using
genetic algorithms.

%prep
%setup -n %name
sed -i '/^SRCS/s/[.]o/.c/g' Imakefile

%build
xmkmf -a
%make_build

%install
%makeinstall_std install.man

%files
%doc README bugsx.ps.gz
%_man1dir/*
%_bindir/*

%changelog
* Tue Jul 15 2014 Fr. Br. George <george@altlinux.ru> 1.08-alt1
- Initial revival from antic ashes urn

