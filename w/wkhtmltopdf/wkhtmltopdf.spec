Name: wkhtmltopdf
Version: 0.9.9
Release: alt1

Summary: Command line utility to convert html to pdf using WebKit
License: %gpl3plus
Group: Publishing
URL: http://code.google.com/p/wkhtmltopdf/
Packager: Artem Zolochevskiy <azol@altlinux.ru>

# git://github.com/antialize/wkhtmltopdf.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Fri Mar 26 2010
BuildRequires: gcc-c++ libqt4-devel

%description
wkhtmltopdf is a command line program which permits to create a pdf from
an url, a local html file or stdin. It produces a pdf like rendred with
the WebKit engine.

This program requires an X11 server to run.

%prep
%setup

%build
PATH=$PATH:%_qt4dir/bin qmake
%make_build
%make wkhtmltopdf.1.gz

%install
%make_install INSTALL_ROOT=%buildroot%prefix install
install -D -m 644 wkhtmltopdf.1.gz %buildroot%_man1dir/wkhtmltopdf.1.gz

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
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
