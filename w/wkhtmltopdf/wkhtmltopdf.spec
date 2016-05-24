# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev.git20141216.1
Name: wkhtmltopdf
Version: 0.12.2
#Release: alt1.dev.git20141216

Summary: Command line utility to convert html to pdf using WebKit
License: %gpl3plus
Group: Publishing
URL: http://wkhtmltopdf.org/
Packager: Artem Zolochevskiy <azol@altlinux.ru>

# https://github.com/wkhtmltopdf/wkhtmltopdf.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Fri Mar 26 2010
BuildRequires: gcc-c++ libqt4-devel

Requires: libwkhtmltox = %EVR

%description
wkhtmltopdf is a command line program which permits to create a pdf from
an url, a local html file or stdin. It produces a pdf like rendred with
the WebKit engine.

This program requires an X11 server to run.

%package -n libwkhtmltox
Summary: Shared libraries of libwkhtmltox
Group: System/Libraries

%description -n libwkhtmltox
wkhtmltopdf is a command line program which permits to create a pdf from
an url, a local html file or stdin. It produces a pdf like rendred with
the WebKit engine.

This package contains development files of libwkhtmltox.

%package -n libwkhtmltox-devel
Summary: Development files of libwkhtmltox
Group: Development/C++
Requires: %name = %EVR
Requires: libwkhtmltox = %EVR

%description -n libwkhtmltox-devel
wkhtmltopdf is a command line program which permits to create a pdf from
an url, a local html file or stdin. It produces a pdf like rendred with
the WebKit engine.

This package contains development files of libwkhtmltox.

%prep
%setup

%build
PATH=$PATH:%_qt4dir/bin qmake
%make_build

%install
%make_install INSTALL_ROOT=%buildroot%prefix install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%files
%doc *.md AUTHORS
%_bindir/*
%_man1dir/*

%files -n libwkhtmltox
%_libdir/*.so.*

%files -n libwkhtmltox-devel
%_includedir/*
%_libdir/*.so

%changelog
* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.12.2-alt1.dev.git20141216.1
- (AUTO) subst_x86_64.

* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2-alt1.dev.git20141216
- Version 0.12.2-dev

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9.9-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Jul 25 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.9.9-alt1
- update to 0.9.9
- add Debian patch to fix some typos

* Fri Mar 26 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.9.5-alt1
- update to 0.9.5
- don't package COPYING file (according to Docs Policy)

* Tue Nov 24 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.8.3-alt2
- fix build with new %%cmake macro

* Sun Oct 18 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.8.3-alt1
- initial build for Sisyphus
