Name: xmlstarlet
Summary: Command Line XML Toolkit
Version: 1.0.1
Release: alt3
License: MIT
Group: Text tools
URL: http://xmlstar.sourceforge.net/
Packager: Alexey Sidorov <alexsid@altlinux.ru>

Source0: http://xmlstar.sourceforge.net/downloads/xmlstarlet-%{version}.tar.gz
Patch0: xmlstarlet-1.0.1-nostatic.patch
Patch1: xmlstarlet-1.0.1-cmdname.patch
Patch2: xmlstarlet-1.0.1-docs.patch
Patch3: xmlstarlet-1.0.1-html.patch
Patch4: xmlstarlet-1.0.1-txt.patch

BuildRequires: libxml2-devel libxslt-devel zlib-devel

%description
XMLStarlet is a set of command line utilities which can be used
to transform, query, validate, and edit XML documents and files
using simple set of shell commands in similar way it is done for
plain text files using UNIX grep, sed, awk, diff, patch, join, etc
commands.

%prep
%setup -q
#patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%__subst "s|.a |.so |g" configure.in
%__subst "s|.a |.so |g" configure

%build
%configure	--with-libxml-libs-prefix=%_libdir \
			--with-libxslt-libs-prefix=%_libdir
# --program-transform-name=%name
%make_build

%install
%make install DESTDIR=%buildroot
mv %buildroot%_bindir/xml %buildroot%_bindir/%name

%files

%doc AUTHORS ChangeLog NEWS README Copyright TODO doc/xmlstarlet.txt doc/xmlstarlet-ug.html
#doc examples
%doc %{_mandir}/man1/xmlstarlet.1*
%_bindir/%name

%changelog
* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt3
- fix build

* Mon Dec 10 2007 Alexey Sidorov <alexsid@altlinux.ru> 1.0.1-alt2
- x86_64 build fixed
- html and txt documentation fixed
- remove pdf variant of user's guide

* Fri Dec 07 2007 Alexey Sidorov <alexsid@altlinux.ru> 1.0.1-alt1
- Initial build for ALT (adopted package from fc6)
