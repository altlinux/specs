Name: lbzip2
Version: 2.1
Release: alt1

Summary: Parallel bzip2/bunzip2 filter
License: GPLv3+
Group: Archiving/Compression

URL: http://lacos.hu/
Source: https://github.com/downloads/kjn/lbzip2/lbzip2-%version.tar.gz

%description
Lbzip2 is a Pthreads-based parallel bzip2/bunzip2 filter, passable to GNU tar
with the --use-compress-program option.

It isn't restricted to regular files on input, nor output. Successful splitting
for decompression isn't guaranteed, just very likely (failure is detected).
Splitting in both modes and compression itself occur with an approximate 900k
block size.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*

%changelog
* Sun Nov 27 2011 Victor Forsiuk <force@altlinux.org> 2.1-alt1
- 2.1

* Fri May 21 2010 Victor Forsiuk <force@altlinux.org> 0.23-alt1
- 0.23

* Mon Dec 14 2009 Victor Forsyuk <force@altlinux.org> 0.19-alt1
- 0.19

* Mon Oct 26 2009 Victor Forsyuk <force@altlinux.org> 0.16-alt1
- Initial build.
