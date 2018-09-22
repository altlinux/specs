Name: httperf
Version: 0.9.0
Release: alt4.git3209c7f9

Summary: Tool for measuring web server performance
License: GPLv2+ with exceptions
Group: Networking/WWW

URL:  https://github.com/httperf/httperf
#URL: http://www.hpl.hp.com/research/linux/httperf
Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch
Source1: %name-paper-html.tar
Source2: ftp://ftp.hpl.hp.com/pub/httperf/httperf-paper.ps

# Automatically added by buildreq on Sat Sep 22 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 perl python-base python-modules python3 python3-base python3-dev ruby ruby-stdlibs sh3
BuildRequires: glibc-devel-static libssl-devel

%define pkgdocdir %_docdir/%name-%version

%description
httperf is a tool to measure web server performance. It speaks the HTTP protocol
both in its HTTP/1.0 and HTTP/1.1 flavors and offers a variety of workload
generators. While running, it keeps track of a number of performance metrics
that are summarized in the form of statistics that are printed at the end of a
test run.  The most basic operation of httperf is to generate a fixed number of
HTTP GET requests and to measure how many replies (responses) came back from the
server and at what rate the responses arrived.

%package docs
Summary: Documentation of a Tool for Measuring Web Server Performance
Group: Documentation
BuildArch: noarch

%description docs
httperf is a tool to measure web server performance. This package contains
HTML and PostScript documentation for it.

%prep
%setup
%patch0 -p1
tar xf %SOURCE1
mv %name html
install -m 0644 %SOURCE2 httperf-paper.ps

%build
%autoreconf
%configure
%make

%install
%makeinstall_std
# now docs...
install -d -m755 %buildroot%pkgdocdir
# by hand to avoid using %%doc purging the above
gzip httperf-paper.ps
install -p -m644 README.md httperf-paper.ps.gz %buildroot%pkgdocdir
cp -a html icons %buildroot%pkgdocdir

%files
%_bindir/*
%_man1dir/*
%dir %pkgdocdir
%pkgdocdir/README.md

%files docs
%dir %pkgdocdir
%pkgdocdir/html/
%pkgdocdir/icons/
%pkgdocdir/httperf-paper.ps.gz

%changelog
* Thu Sep 20 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.9.0-alt4.git3209c7f9
- Fix build with OpenSSL 1.1.0i

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9.0-alt3.qa1
- NMU: rebuilt for debuginfo.

* Tue Dec 07 2010 Victor Forsiuk <force@altlinux.org> 0.9.0-alt3
- Rebuilt with libssl10.

* Sat Jan 10 2009 Victor Forsyuk <force@altlinux.org> 0.9.0-alt2
- Package docs as noarch.

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.0-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Fri Dec 28 2007 Victor Forsyuk <force@altlinux.org> 0.9.0-alt1
- 0.9.0

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.8-alt3.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sun Dec 10 2006 Michael Shigorin <mike@altlinux.org> 0.8-alt3
- updated Url:
- added docs subpackage just in case

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.8-alt2.1
- Rebuilt with openssl-0.9.7d.

* Mon Oct 28 2002 Michael Shigorin <mike@altlinux.ru> 0.8-alt2
- rebuilt with gcc-3.2

* Tue Jun 11 2002  Michael Shigorin <mike@altlinux.ru> 0.8-alt1
- built for ALT Linux
- (inger)NO SMP
