Name: crystal-open
Version: 2.14
Release: alt3
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
* Fri Jun 26 2020 Kirill Maslinsky <kirill@altlinux.org> 2.14-alt3
- built with current node
- node_modules packaged

* Mon May 25 2020 Kirill Maslinsky <kirill@altlinux.org> 2.14-alt2
- Russian translation added

* Sun Mar 15 2020 Kirill Maslinsky <kirill@altlinux.org> 2.14-alt1
- Initial build for ALT



