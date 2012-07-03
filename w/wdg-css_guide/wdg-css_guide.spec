Name: wdg-css_guide
Version: 1.0
Release: alt1

Group: Books/Other
License: OPL
Summary: CSS Guide from Web Design Group (WDG)
BuildArch: noarch
Url: http://htmlhelp.com/reference/css/

Packager: Sergey Kurakin <kurakin@altlinux.org>

Source: http://htmlhelp.com/distribution/wdgcss.tar.gz

%description
Change the appearance of hundreds of Web pages by changing
just one file... Influence presentation without losing
visitors... All with the power and flexibility
of Web style sheets.

%prep
%setup -q -c

%install
%__mkdir_p %buildroot/%_defaultdocdir/%name
%__cp -r wdgcss/* %buildroot/%_defaultdocdir/%name

%files
%_defaultdocdir/%name

%changelog
* Sun May 31 2009 Sergey Kurakin <kurakin@altlinux.org> 1.0-alt1
- first buld for AltLinux Sisyphus
