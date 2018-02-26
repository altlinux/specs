Name: potrace
Version: 1.10
Release: alt1

Summary: Potrace is a utility for transform bitmaps into vector graphics
License: GPLv2+
Group: Office

Url: http://potrace.sourceforge.net
Source: http://potrace.sourceforge.net/download/potrace-%version.tar.gz

# Automatically added by buildreq on Tue Aug 23 2011
BuildRequires: zlib-devel

# for check
BuildRequires: ghostscript

%description
Potrace is a utility for tracing a bitmap, which means, transforming a bitmap
into a smooth, scalable image. The input is a portable bitmap (PBM), and the
default output is an encapsulated PostScript file (EPS). A typical use is to
create EPS files from scanned data, such as company or university logos,
handwritten notes, etc. The resulting image is not "jaggy" like a bitmap, but
smooth. It can then be rendered at any resolution.

%prep
%setup

%build
%configure --enable-a4 --enable-metric
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_bindir/*
%_man1dir/*
%doc NEWS README ChangeLog doc/placement.pdf

%changelog
* Tue Aug 23 2011 Yuri N. Sedunov <aris@altlinux.org> 1.10-alt1
- 1.10
- %%check section

* Fri Dec 24 2010 Victor Forsiuk <force@altlinux.org> 1.9-alt1
- 1.9

* Mon Oct 29 2007 Victor Forsyuk <force@altlinux.org> 1.8-alt1
- 1.8
- Use A4 as the default papersize.

* Mon Mar 07 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.7-alt1
- 1.7

* Mon Feb 28 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.6-alt1
- 1.6

* Thu Jul 15 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.5-alt2
- rebuild

* Mon Jul 12 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.5-alt1
- new version

* Sun Mar 7 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.4-alt1
- 1.4
- further optimized the speed of the function path.c:pathlist_to_tree
- fixed compression bug where garbage was added after the end of stream
- removed potrace.{ps,pdf} from	distribution

* Sat Jan 17 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.3-alt1
- 1.3
- the bounding box in the xfig backend was fixed
- the postscript output now has better page encapsulation
- bitmaps of dimension 0 are now tolerated better.

* Wed Dec 24 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.2-alt1
- 1.2

* Fri Aug 29 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.1-alt1
- 1.1

* Thu Aug 28 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.0-alt1
- First version of RPM package.
