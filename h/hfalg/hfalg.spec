Name: hfalg
Version: 1.20
Release: alt1

Summary: Hacker Factor Image Forensics Algorithms
# Neither source file nor referring page does contain specific license.
# At the same time source file is published and we see no restrictions
# on distribution. So at least distribution is allowed:
License: Freely distributable
Group: Graphics

URL: https://infohost.nmt.edu/~schlake/ela/
Source: https://infohost.nmt.edu/~schlake/ela/src/hfalg.c

# Automatically added by buildreq on Fri Mar 11 2011
BuildRequires: libjpeg-devel

%description
hfalg is a tool for digital image analysis and forensics. See
http://www.hackerfactor.com/papers/bh-usa-07-krawetz-wp.pdf for
background information.

%prep
%setup -c -T
cp %_sourcedir/hfalg.c .

%build
gcc %optflags hfalg.c -o hfalg -ljpeg -lm

%install
install -Dpm 755 hfalg %buildroot/%_bindir/hfalg

%files
%_bindir/*

%changelog
* Tue Mar 15 2011 Victor Forsiuk <force@altlinux.org> 1.20-alt1
- Initial build.
