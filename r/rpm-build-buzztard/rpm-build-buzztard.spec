%define rpm_macrosdir %_sysconfdir/rpm/macros.d

Name: rpm-build-buzztard
Url: http://sisyphus.ru/srpm/Sisyphus/rpm-build-buzztard
Version: 1.0
Release: alt3

Provides: buzztard-build
Summary: RPM macros for buzztard build
License: %lgpl2plus
Group: Development/Other

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# rpm macro definitions
Source1: buzztard-build.rpm-macros

BuildRequires(pre): rpm-build-licenses

BuildArch: noarch

%description
The package provide a set of macros for building buzztard packages.

%install

install -pD -m644 %SOURCE1 %buildroot%rpm_macrosdir/%name

%files
%rpm_macrosdir/%name

%changelog
* Thu Jan 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Restored Buzz Gear dir

* Tue Apr 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Change Buzz Gear dir

* Thu Apr 16 2009 Timur Batyrshin <erthad@altlinux.org> 1.0-alt1.2
- typo fixed

* Sat Feb 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Add Url for this package

* Sat Feb 07 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 1.0-alt1
- Initial build for Sisyphus

