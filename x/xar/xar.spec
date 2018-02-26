Name: xar
Version: 1.5.3
Release: alt1

Summary: The XAR project aims to provide an easily extensible archive format
License: BSD
Group: Archiving/Compression
Url: http://code.google.com/p/%name/
# http://xar.googlecode.com/svn/tags/xar-1.5.3
Source: %name-%version.tar
Patch: xar-1.5.3-alt-config.patch
Requires: lib%name = %version-%release

# Automatically added by buildreq on Sat Dec 17 2011
BuildRequires: bzlib-devel libacl-devel libe2fs-devel libssl-devel libxml2-devel xsltproc zlib-devel

%description
The XAR project aims to provide an easily extensible archive format.
Important design decisions include an easily extensible XML table of
contents for random access to archived files, storing the toc at the
beginning of the archive to allow for efficient handling of streamed
archives, the ability to handle files of arbitrarily large sizes,
the ability to choose independent encodings for individual files in
the archive, the ability to store checksums for individual files in
both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

Please note that the code quality of this project is quite poor.
Do not expect that error conditions would be handled properly.

%package -n lib%name
Summary: The eXtensible ARchiver runtime library
Group: System/Libraries

%description -n lib%name
The XAR project aims to provide an easily extensible archive format.
This package contains the eXtensible ARchiver runtime library.

Please note that the code quality of this project is quite poor.
Do not expect that error conditions would be handled properly.

%package -n lib%name-devel
Summary: Development files for the eXtensible ARchiver library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The XAR project aims to provide an easily extensible archive format.

This package contains headers and other development files required to
build XAR-based software.

%prep
%setup
%patch -p1
# get rid of RPATH.
sed -ri 's/(RPATH=)".*/\1/' configure.ac

%build
autoconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%check
cd test
export "PATH=%buildroot%_bindir:$PATH"
export LD_LIBRARY_PATH="%buildroot%_libdir"
./checksums
./compression
./data
./hardlink
./heap

%files
%_bindir/*
%_man1dir/*
%doc LICENSE

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Sat Dec 17 2011 Dmitry V. Levin <ldv@altlinux.org> 1.5.3-alt1
- Updated to 1.5.3.
- Made it actually work on x86.
- Fixed RPATH issue.
- Enabled test suite.
- Enabled ACL support.
- Relocated headers back to /usr/include/xar/.
- Updated package descriptions, added a warning about poor code quality.

* Mon Apr 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.2-alt3
- repair build

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Fri Mar 13 2009 Eugene Ostapets <eostapets@altlinux.ru> 1.5.2-alt2
- Move headers from %_includedir/%name to %_includedir

* Fri Mar 06 2009 Eugene Ostapets <eostapets@altlinux.ru> 1.5.2-alt1
- First build for ALTLinux

