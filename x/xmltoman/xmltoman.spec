Name: xmltoman
Version: 0.6
Release: alt1

Summary: XML to manpages converting utilities
License: GPLv2
Group: Text tools
Url: https://github.com/atsb/xmltoman
 
Source: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: perl(XML/Parser.pm)

%description
xmltoman and xmlmantohtml are two very simple scripts for converting xml
to groff or html.

%prep
%setup

%build
make

%install
make install prefix=%buildroot%_prefix
install -pm0644 -D %name.1 %buildroot%_man1dir/%name.1
install -pm0644 xmlmantohtml.1 %buildroot%_man1dir

%files
%doc COPYING README
%_bindir/xmltoman
%_bindir/xmlmantohtml
%_datadir/%name
%_man1dir/*

%changelog
* Fri May 13 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6-alt1
- 0.6 released

* Thu Aug 18 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt1
- 0.4 released

* Tue Aug 21 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt1
- Initial build.
