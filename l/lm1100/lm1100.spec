Name: lm1100
Version: 1.0.2
Release: alt1.a
License: GPL
Group: System/Configuration/Printing

# Source: http://www.linuxprinting.org/download/printing/lm1100/%name-%version.tar.gz
Source: %name-%version.tar
Patch1: lm1100-1.0.2a-gcc32.patch
Patch2: lm1100.1.0.2a-fix-compile-gcc-3.4.patch
Patch3: lexmark2ppm.pl.patch
Patch4: lm1100.1.0.2a-LDFLAGS.patch
Patch5: lm1100-1.0.2a-fix-find-requires.patch
Url: http://www.linuxprinting.org/download/printing/lm1100/

BuildRequires: gcc-c++

Summary: Linux Lexmark 1000/1100 Printer Driver
%description
Linux Lexmark 1000/1020/1100 Printer Driver. This filter converts a ppm file
into the Lexmark 1000/1020/1100 internal format.

%prep
%setup
%patch1 -p1
%patch2
%patch3
%patch4
%patch5 -p2

# Remove extra qualifications '<class>::<member>' on class members, to make
# code compiling with gcc 4.1.1.
perl -p -i -e 's/\b[^\s:]+:://' *.h

%build
%make

%install
install -d %buildroot%_bindir

install -m 0755 lm1100 %buildroot%_bindir
install -m 0755 lexmark2ppm.pl %buildroot%_bindir
install -m 0755 byteutil.pl %buildroot%_bindir

# Executables (filter for usage with CUPS and printer emulator script for
# development and debugging (also debugging this RPM w/o Lexmark 1100).
# LPD support
install -d %buildroot%_libexecdir/rhs/rhs-printfilters
[ -e ps-to-lm1100.fpi ] || mv ps-to-printer.fpi ps-to-lm1100.fpi # file name conflict
install -m 0755 ps-to-lm1100.fpi %buildroot%_libexecdir/rhs/rhs-printfilters
ln -s %_bindir/lm1100 %buildroot%_libexecdir/rhs/rhs-printfilters

%files
%doc LICENSE README RELEASE.* cmy.txt
%_bindir/lm1100
%_bindir/lexmark2ppm.pl
%_bindir/byteutil.pl
%_libexecdir/rhs/rhs-printfilters/lm1100
%_libexecdir/rhs/rhs-printfilters/ps-to-lm1100.fpi

%changelog
* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 1.0.2-alt1.a
- Initial build for ALT

