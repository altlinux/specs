Name:           metamath
Version:        0.198.127
Release:        alt1
Source:         %name-exe-master-%version.tar.gz
License:        GPLv2

Summary:        A language of rigorously verifying, archiving, and presenting mathematical proofs
VCS:            https://github.com/metamath/metamath-exe
URL:            https://us.metamath.org
Group:          Sciences/Mathematics

Patch:          0001-Patch-tests-for-32bit.patch
# Automatically added by buildreq on Tue Jan 27 2026
# optimized out: bash5 glibc-kernheaders-generic gnu-config libgpg-error perl python3 python3-base sh5
BuildRequires: doxygen

%description
Metamath is a simple and flexible computer-processable language that
supports rigorously verifying, archiving, and presenting mathematical
proofs. See the FAQ for more information.

%prep
%setup -n %name-exe-master
%ifarch %ix86
%patch -p1
%endif

%build
%autoreconf
%configure
%make_build
doxygen Doxyfile.diff

%install
%makeinstall_std

%check
( cd tests; METAMATH=../src/metamath sh run_test.sh *.in )

%files
%doc html *.md *.TXT
%_bindir/*
%_man1dir/*

%changelog
* Tue Jan 27 2026 Fr. Br. George <george@altlinux.org> 0.198.127-alt1
- Initial build for ALT
