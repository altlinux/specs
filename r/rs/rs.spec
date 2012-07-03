Name: rs
Version: 1.18
Release: alt1
Source: rs-1.18.tar
Url: http://www.freebsd.org/cgi/cvsweb.cgi/src/usr.bin/%name
Packager: Fr. Br. George <george@altlinux.ru>
Summary: Reshape a data array
License: BSD
Group: Text tools
# svn checkout svn://svn.freebsd.org/base/head/usr.bin/rs

%description
The rs utility reads the standard input, interpreting each line as a row
of blank-separated entries in an array, transforms the array according
to the options, and writes it on the standard output.  With no arguments
it transforms stream input into a columnar format convenient for
terminal viewing.

%prep
%setup
# getline double definition
sed -i 's/getline/get_line/g' %name.c

%build
cc -D'__FBSDID(x)=' -O2 %name.c -o %name

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
install -s -m755 %name %buildroot%_bindir/
install %name.1 %buildroot%_man1dir/

%files
%_bindir/%name
%_man1dir/%name.*

%changelog
* Fri Jan 13 2012 Fr. Br. George <george@altlinux.ru> 1.18-alt1
- Autobuild version bump to 1.18

* Wed Jul 27 2011 Fr. Br. George <george@altlinux.ru> 1.17-alt1
- Autobuild version bump to 1.17

* Mon May 25 2009 Fr. Br. George <george@altlinux.ru> 1.14-alt2
- New toolchain build fixup

* Sat Apr 11 2009 Fr. Br. George <george@altlinux.ru> 1.14-alt1
- Version up

* Thu Nov 08 2007 Fr. Br. George <george@altlinux.ru> 1.13-alt1
- Initial build for ALT

