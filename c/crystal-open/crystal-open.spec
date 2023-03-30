Name: crystal-open
Version: 2.130.1
Release: alt4
Summary: Sketch Engine web interface
License: GPLv3
Group: Text tools
Url: http://nlp.fi.muni.cz/trac/noske/wiki/Downloads
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildRequires: npm node node-sass node-gyp
BuildArch: noarch

%description
Sketch Engine web interface, open source version.

%prep
%setup
%patch -p1

%build
%make_build

%install
%makeinstall_std VERSION=%version

%files
%_var/www/crystal
%config(noreplace) %_var/www/crystal/config.js

%changelog
* Thu Mar 30 2023 Kirill Maslinsky <kirill@altlinux.org> 2.130.1-alt4
- bugfix in layered display

* Thu Mar 30 2023 Kirill Maslinsky <kirill@altlinux.org> 2.130.1-alt3
- better layered attributes display

* Tue Feb 14 2023 Kirill Maslinsky <kirill@altlinux.org> 2.130.1-alt2
- implement layered display for token attributes

* Wed Jan 04 2023 Kirill Maslinsky <kirill@altlinux.org> 2.130.1-alt1
- 2.130.1

* Sun Nov 14 2021 Kirill Maslinsky <kirill@altlinux.org> 2.14-alt6
- fix build: repackage node_modules
- update dependency on sass-loader to ^11.1.0

* Mon Dec 21 2020 Kirill Maslinsky <kirill@altlinux.org> 2.14-alt5
- Russian translation edited

* Mon Nov 16 2020 Kirill Maslinsky <kirill@altlinux.org> 2.14-alt4
- Add tip in Russian, set default locale to ru

* Fri Jun 26 2020 Kirill Maslinsky <kirill@altlinux.org> 2.14-alt3
- built with current node
- node_modules packaged

* Mon May 25 2020 Kirill Maslinsky <kirill@altlinux.org> 2.14-alt2
- Russian translation added

* Sun Mar 15 2020 Kirill Maslinsky <kirill@altlinux.org> 2.14-alt1
- Initial build for ALT



