Name: spdlog
Version: 0.13.0
Release: alt1

Summary: Super fast C++ logging library

Group: Development/Other
License: MIT
Url: https://github.com/gabime/spdlog

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/gabime/%name/archive/v%version.tar.gz
Source: %name-%version.tar

%description
This is a packaged version of the gabime/spdlog header-only C++
logging library available at Github.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/Other
#Requires: libstdc++-devel

%description -n lib%name-devel
The %name-devel package contains C++ header files for developing
applications that use %name.

%prep
%setup
%__subst "s|CHAR_WIDTH|SPDLOG_CHAR_WIDTH|g" include/spdlog/fmt/bundled/format.h

%install
find ./example -name '.gitignore' -exec rm {} \;
mkdir -p %buildroot%_includedir
cp -pvR include/spdlog %buildroot%_includedir/

%files -n lib%name-devel
%doc README.md example/
%doc LICENSE
%_includedir/spdlog/

%changelog
* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- initial build for ALT Sisyphus

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 04 2016 Daniel Kopecek <dkopecek@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Fri Jul 08 2016 Daniel Kopecek <dkopecek@redhat.com> - 0-8.20160703git34bb86b
- update to rev 34bb86b

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20151110gitcbc8ba7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-6.20151110gitcbc8ba7
- update to rev cbc8ba7

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-5.20150410git211ce99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-4.20150410git211ce99
- don't build the base package
- remove a dot from the release tag
- corrected -devel subpackage description

* Mon Apr 20 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-3.20150410git.211ce99
- use the -p option when copying the header files

* Tue Apr 14 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-2.20150410git.211ce99
- don't build the debuginfo subpackage
- require libstdc++-devel
- don't generate a distribution specific pkg-config file

* Fri Apr 10 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-1.20150410git.211ce99
- Initial package
