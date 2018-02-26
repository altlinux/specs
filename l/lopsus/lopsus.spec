
Name: lopsus
Version: 1.4.0.1
Release: alt1

URL: http://www.marigostra.ru/developments/lopsus.html
License: %gpl3plus
Group: Text tools
Summary: A small website generator
Packager: Michael Pozhidaev <msp@altlinux.ru>

# Automatically added by buildreq on Fri Jun 05 2009
BuildRequires: gcc-c++

BuildRequires: rpm-build-licenses

Source: %name-%version.tar.gz

%description
Lopsus is small, light website generator. It has special form to
specify pages content , which is a mix of latex and mediawiki syntax.
Pages content does not contain any style data. Considering
style data can be stored completely in CSS. There is a lack of
documentation in this distribution. It is a subject for further
developing. 

%package page
License: %gpl3plus
Group: Text tools
Summary: Utility to translate %name page content files

%description page
Lopsus is small, light website generator. It has special form to
specify pages content , which is a mix of latex and mediawiki syntax.
Pages content does not contain any style data. Considering
style data can be stored completely in CSS. There is a lack of
documentation in this distribution. It is a subject for further
developing. 

This package contains the utility to translate %name page content files.

%prep
%setup -q
%build

%configure
%make_build CXXFLAGS='%optflags -fpic'

%install
make DESTDIR=%buildroot install

%files
%doc README NEWS AUTHORS ChangeLog THANKS
%_bindir/%name
%_bindir/%name-init
%_bindir/%name-news
%_datadir/%name

%files page
%_bindir/%name-page

%changelog
* Wed Dec 30 2009 Michael Pozhidaev <msp@altlinux.ru> 1.4.0.1-alt1
- New version

* Wed Nov 25 2009 Michael Pozhidaev <msp@altlinux.ru> 1.4.0-alt1
- New version

* Sun Jun 07 2009 Michael Pozhidaev <msp@altlinux.ru> 1.0.0-alt2
- First stable release

* Thu May 28 2009 Michael Pozhidaev <msp@altlinux.ru> 1.0.0-alt1
- First release candidat

* Tue May 12 2009 Michael Pozhidaev <msp@altlinux.ru> 0.2.1-alt1
- INitial rpm
