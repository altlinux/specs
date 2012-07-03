%define cvsdate 20031027

Name: texitheque
Version: 0.3
%define release alt0.1

%ifdef cvsdate
Release: alt0.1cvs20031027.1
%else
Release: %release
%endif

Summary: Texitheque is a set of small documentation utilities
License: GPL
Group: Publishing
Url: http://freedesktop.org

%ifndef cvsdate
Source: %url/files/%name-%version.tar.gz
%else
Source: %name-%version-%cvsdate.tar.bz2
%endif

Provides: perl(Texitheque/CGI/StockMessages.pm)

BuildPreReq: automake_1.4

# Automatically added by buildreq on Mon Oct 27 2003
BuildRequires: glib2-devel groff-base pkgconfig xsltproc

%description
Texitheque is a small documentation utility packages based on
texinfo. It contains utilities to extract/construct
texinfo source from files such as ChangeLogs or C source
function comments and it contains utilities to produce
various target formats.

Here is a rough feature set overview:
- supports inlined function docs (C comments starting with /**)
- supports real documents (texinfo)
- supports website news input (texinfo)
- supports ChangeLogs as input
- supports website navigation input (xml)
- supports generic cross references
- generates man pages
- generates a full website with html pages
- generates tag-span marked up xml (used by beast's doc browser)
- generates postscript (and pdf from postscript files)

%define _perl_req_method relaxed
#%%add_findprov_lib_path %_libdir/%name

%prep
%ifndef cvsdate
%setup -q
%else
%setup -q -n %name
%endif

%build
%set_automake_version 1.4

%ifdef cvsdate
%__rm -f missing
%__libtoolize --copy --force
%__aclocal
%__automake -a -c
%__autoconf

#./autogen.sh
%endif

%configure
%make_build

%install
%makeinstall

%__install -m644 modules/Texitheque/CGI/{StockMessages,FileUploader}.pm \
	%buildroot%_libdir/%name/modules/Texitheque/CGI/

%files
%_bindir/*
%_libdir/%name
%_libdir/pkgconfig/*
%doc AUTHORS ChangeLog NEWS README

%changelog
* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3-alt0.1cvs20031027.1
- rebuilt with perl 5.12

* Mon Oct 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3-alt0.1cvs20031027
- First build for Sisyphus. 

