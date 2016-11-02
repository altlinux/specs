Name: rs
Version: 11.0
Release: alt1
Source: rs-11.0.tar
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
* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 11.0-alt1
- Autobuild version bump to 11.0

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 10.3-alt1
- Autobuild version bump to 10.3

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 10.2-alt1
- Autobuild version bump to 10.2

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 10.1-alt1
- Autobuild version bump to 10.1

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 10.0-alt1
- Autobuild version bump to 10.0

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 9.2-alt1
- Autobuild version bump to 9.2
- Switch to RELENG regular update

* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 1.19-alt1
- Autobuild version bump to 1.19

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

