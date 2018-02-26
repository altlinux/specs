Name: wdg-html4_reference
Version: 1.0.7
Release: alt1

Group: Books/Other
License: OPL
Summary: HTML4 Reference from Web Design Group (WDG)
BuildArch: noarch
Url: http://htmlhelp.com/reference/html40/

Packager: Sergey Kurakin <kurakin@altlinux.org>

Source: http://htmlhelp.com/distribution/wdghtml40.tar.gz

%description
HTML 4.0 became a W3C Recommendation in December of 1997. This HTML
standard provided a number of significant improvements over previous
versions of the language while emphasizing the concepts of accessibility
and structural markup. In December of 1999, HTML 4.01 replaced HTML 4.0
as a minor update.

%prep
%setup -q -c

%install
%__mkdir_p %buildroot/%_defaultdocdir/%name
%__cp -r wdghtml40/* %buildroot/%_defaultdocdir/%name

%files
%_defaultdocdir/%name

%changelog
* Sun May 31 2009 Sergey Kurakin <kurakin@altlinux.org> 1.0.7-alt1
- first buld for AltLinux Sisyphus
