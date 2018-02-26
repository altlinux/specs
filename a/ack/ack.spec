Name:		ack
Version:	6.0pre4
Release:	alt1
Summary:	The Amsterdam Compiler Kit
Group:		Development/Other
URL:		http://tack.sourceforge.net/
License:	BSD
Source:		%name-%version.tar.bz2
# http://sourceforge.net/projects/tack/files/ACK/6.0pre4/ack-6.0pre4.tar.bz2/download
ExclusiveArch: %ix86

# Automatically added by buildreq on Tue Mar 01 2011
BuildRequires: flex

%description

The Amsterdam Compiler Kit is a complete compiler toolchain consisting of
front end compilers for a number of different languages, code generators,
support libraries, and all the tools necessary to go from source code to
executable on any of the platforms it supports.

This is an early prerelease of the apocryphal version 6.0 release. Not a
lot is supported, the build mechanism needs work, and a lot of things are
probably broken. However, what's there should be sufficient to get things
done and to evaluate how the full 6.0 release should work. 

Support:
ANSI C, Pascal, Modula 2. K&R is supported via the ANSI C compiler.

%prep
%setup
sed -i '/^DEFAULT_PLATFORM = "/s@.*@DEFAULT_PLATFORM = "linux386"@
/^PREFIX = "/s@.*@PREFIX = "/usr"@' config.pm
echo 'PREFIX = "%buildroot%_prefix"' > buildroot.pm
rm -rf /tmp/%name-temp
for f in `fgrep -rl lib.bin .`; do
sed -i 's/lib[.]bin/libexec/g' $f
done

%build
./pm configure
./pm

%install
./pm -fpmfile -f buildroot.pm install
strip %buildroot%_bindir/* `find %buildroot%_prefix/libexec -type f` || :
mkdir -p %buildroot%_datadir
mv %buildroot%_prefix/man %buildroot%_datadir/

%files
%_bindir/*
%_libdir/*
%_mandir/*/*
%_prefix/libexec/*
%_includedir/*

%changelog
* Wed Mar 02 2011 Fr. Br. George <george@altlinux.ru> 6.0pre4-alt1
- Initial build from scratch

