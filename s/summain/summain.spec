Name: summain
Version: 0.20
Release: alt1

Summary: File manifest generator

License: GPLv3+
Group: File tools
Url: http://liw.fi/%name/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://code.liw.fi/debian/pool/main/s/%name/%{name}_%version.orig.tar.gz

# build-time
#BuildRequires: python-coverage-test-runner
BuildRequires: libattr-devel
BuildRequires: python-devel
# build- and run-time
BuildRequires: python-module-cliapp
BuildRequires: python-module-json
#Requires: python-cliapp

%description
Summain generates file manifests, which contain metadata about the
files, and a checksum of their content for regular files. The manifest
can be generated for a directory tree at different points in time and
compared (with diff) to see if something has changed.

%prep
%setup

%build
%python_build
# Generate manpages
make summain.1

%install
%python_install
# fix permission
chmod 755 %buildroot%python_sitelibdir/_summain.so

%check
exit 0
# TODO: add and use python_check
%__python setup.py check

%files
%doc COPYING NEWS README
%_man1dir/summain.1*
%_bindir/summain
%python_sitelibdir/*

%changelog
* Thu Jul 28 2016 Vitaly Lipatov <lav@altlinux.ru> 0.20-alt1
- new version 0.20 (with rpmrb script)

* Thu Aug 13 2015 Vitaly Lipatov <lav@altlinux.ru> 0.19-alt1
- initial build for ALT Linux Sisyphus

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 20 2014 Kevin Fenzi <kevin@scrye.com> - 0.19-4
- Rebuild for rpm bug 1131892

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Michel Salim <salimma@fedoraproject.org> - 0.19-1
- Update to 0.19

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 17 2013 Michel Salim <salimma@fedoraproject.org> - 0.18-1
- Update to 0.18

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 0.17-1
- Update to 0.17

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 19 2012 Michel Salim <salimma@fedoraproject.org> - 0.14-2.1
- When building for EL6, skip unavailable package checks

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Michel Salim <salimma@fedoraproject.org> - 0.14-1
- Update to 0.14

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 0.13-1
- Initial package
