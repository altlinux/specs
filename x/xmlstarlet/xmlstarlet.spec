%define _unpackaged_files_terminate_build 1

Name: xmlstarlet
Summary: Command Line XML Toolkit
Version: 1.6.1
Release: alt1
License: MIT
Group: Text tools
URL: http://xmlstar.sourceforge.net/

# http://xmlstar.sourceforge.net/downloads/xmlstarlet-%{version}.tar.gz
Source: %name-%version.tar

Patch1: xmlstarlet-1.6.1-nogit.patch

BuildRequires: xmlto
BuildRequires: libxml2-devel libxslt-devel zlib-devel
BuildRequires: docbook5-schemas

%description
XMLStarlet is a set of command line utilities which can be used
to transform, query, validate, and edit XML documents and files
using simple set of shell commands in similar way it is done for
plain text files using UNIX grep, sed, awk, diff, patch, join, etc
commands.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure \
	--disable-static-libs \
	--with-libxml-include-prefix=%_includedir/libxml2 \
	%nil

%make_build

%install
%makeinstall_std
mv %buildroot%_bindir/xml %buildroot%_bindir/%name

# remove duplicate documentation
rm -rf %buildroot%_defaultdocdir/%name

%files
%doc AUTHORS ChangeLog NEWS README Copyright TODO
%doc doc/xmlstarlet.txt doc/xmlstarlet-ug.html doc/html.css
%_bindir/%name
%_man1dir/%{name}.1*

%changelog
* Wed Jan 13 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.1-alt1
- Updated to upstream version 1.6.1.

* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt3
- fix build

* Mon Dec 10 2007 Alexey Sidorov <alexsid@altlinux.ru> 1.0.1-alt2
- x86_64 build fixed
- html and txt documentation fixed
- remove pdf variant of user's guide

* Fri Dec 07 2007 Alexey Sidorov <alexsid@altlinux.ru> 1.0.1-alt1
- Initial build for ALT (adopted package from fc6)
