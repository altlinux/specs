Name: gengetopt
Version: 2.22.6
Release: alt1

Summary: Tool to write command line option parsing code for C programs
License: GPLv3+
Group: Development/C
Url: http://www.gnu.org/software/%name/

Source: ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.gz

BuildRequires: gcc-c++ bison flex help2man source-highlight

%description
Gengetopt is a tool to generate C code to parse the command line
arguments argc and argv that are part of every C or C++ program. The
generated code uses the C library function getopt_long to perform the
actual command line parsing.

%define pkgdocdir %_docdir/%name-%version

%prep
%setup

%build
%configure --docdir=%pkgdocdir
# SMP-incompatible build
%make

%install
%makeinstall_std

%check
%make check

%files
%_bindir/%name
%_datadir/%name/
%_infodir/%name.info*
%_man1dir/%name.1*
%doc %pkgdocdir/


%changelog
* Tue Feb 24 2015 Yuri N. Sedunov <aris@altlinux.org> 2.22.6-alt1
- first build for Sisyphus

