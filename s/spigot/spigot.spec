Name:		spigot
Version:	20200101
Release:	alt1
Group:		Sciences/Mathematics
License:	MIT
Summary:	A command-line streaming exact real calculator
URL:		https://www.chiark.greenend.org.uk/~sgtatham/spigot/
Source:		%name-%version.tar.gz

# Automatically added by buildreq on Wed May 13 2020
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libstdc++-devel libtinfo-devel python2-base sh4
BuildRequires: gcc-c++ halibut libgmp-devel libncurses-devel

%description
A normal calculating program, given a mathematical expression to
evaluate, will want to know in advance how many digits of output are
needed (if it even has that option), and if the expression includes
more than one successive operation, then rounding errors will build up
so that the last few digits are potentially wrong, or perhaps more in
some cases (e.g. if significance loss occurs).

spigot, by contrast, does not output any digit of the answer until it's
sure that the digit is right, and it will keep generating digits until
you tell it to stop.

Also, spigot is "streaming" in the sense that if you tell it to do
computations on a number you've previously stored in a file (perhaps to
very high precision) or a number it's reading from a pipe, then it will
begin producing output as soon as it's read enough of the input to know
how the output starts.

The downside is that spigot is very slow compared to the usual kind of
computer arithmetic. But it can be useful if you really need a lot of
digits for some reason (e.g. a large number of digits of mathematical
constants are sometimes incorporated into cryptographic algorithms), or
as a cross-check on other calculating systems.

%prep
%setup -n %name-%version

%build
%configure
%make_build

%install
%makeinstall_std

%check
make test

%files
%doc %_defaultdocdir/%name
%_bindir/*
%_man1dir/*


%changelog
* Wed May 13 2020 Fr. Br. George <george@altlinux.ru> 20200101-alt1
- Initial build for ALT

