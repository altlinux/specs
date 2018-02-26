%define sname trackermusic

Name: %{sname}-mime-info
Version: 0.0.1
Release: alt1.qa1

Summary: mime types description of many tracker music formates

License: GPL
Group: Graphical desktop/Other

Packager: Yury Aliaev <mutabor@altlinux.ru>

Source: %{sname}.xml

Requires(post,postun): shared-mime-info >= 0.15-alt2

%description
This package contains mime types description of many tracker music formates
also known as "modules".

%prep

%build

%install
install -pD -m644 %SOURCE0  %buildroot%_datadir/mime/packages/%{sname}.xml

%files
%_datadir/mime/packages/*

%changelog
* Sat Nov 21 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.0.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * shared-mime-info for trackermusic-mime-info
  * postclean-05-filetriggers for spec file

* Tue Jul 22 2008 Yury Aliaev <mutabor@altlinux.ru> 0.0.1-alt1
- initial package created
